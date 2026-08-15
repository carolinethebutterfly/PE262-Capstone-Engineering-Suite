"""Engineering calculations used by the Streamlit application."""

from dataclasses import dataclass
import math
from typing import Dict, Iterable
import numpy as np


@dataclass
class Fluid:
    """Stores basic fluid properties used in pipe-flow calculations."""

    name: str
    density: float  # kg/m3
    dynamic_viscosity: float  # Pa.s

    @staticmethod
    def presets() -> Dict[str, "Fluid"]:
        """Return built-in engineering-fluid property presets."""
        return {
            "Water": Fluid("Water", 998.2, 1.002e-3),
            "Air": Fluid("Air", 1.204, 1.825e-5),
            "Crude oil": Fluid("Crude oil", 850.0, 0.020),
        }


@dataclass
class Pipe:
    """Represents a circular pipe for Darcy-Weisbach calculations."""

    diameter: float  # m
    length: float  # m
    roughness: float  # m

    def validate(self) -> None:
        """Validate that all pipe dimensions are physically meaningful."""
        if self.diameter <= 0:
            raise ValueError("Pipe diameter must be greater than zero.")
        if self.length <= 0:
            raise ValueError("Pipe length must be greater than zero.")
        if self.roughness < 0:
            raise ValueError("Pipe roughness cannot be negative.")


def reynolds_number(rho: float, velocity: float, diameter: float, mu: float) -> float:
    """Calculate Reynolds number for internal flow."""
    if rho <= 0 or diameter <= 0 or mu <= 0:
        raise ValueError("Density, diameter and viscosity must be positive.")
    if velocity < 0:
        raise ValueError("Velocity cannot be negative.")
    return rho * velocity * diameter / mu


def friction_factor(reynolds: float, roughness: float, diameter: float) -> float:
    """Return the Darcy friction factor.

    Laminar flow uses f = 64/Re. Turbulent flow uses the Swamee-Jain
    explicit approximation to the Colebrook equation.
    """
    if reynolds <= 0:
        return 0.0
    if diameter <= 0:
        raise ValueError("Diameter must be positive.")
    if roughness < 0:
        raise ValueError("Roughness cannot be negative.")
    if reynolds < 2300:
        return 64.0 / reynolds
    relative_roughness = roughness / diameter
    return 0.25 / (
        math.log10(relative_roughness / 3.7 + 5.74 / (reynolds ** 0.9)) ** 2
    )


def pipe_flow_results(
    fluid: Fluid,
    pipe: Pipe,
    volumetric_flow_rate: float,
) -> Dict[str, float]:
    """Calculate velocity, Reynolds number, friction factor and pressure drop.

    Parameters
    ----------
    fluid:
        Fluid object containing density and dynamic viscosity.
    pipe:
        Pipe object containing geometry and roughness.
    volumetric_flow_rate:
        Volumetric flow rate in m3/s.
    """
    pipe.validate()
    if fluid.density <= 0 or fluid.dynamic_viscosity <= 0:
        raise ValueError("Fluid density and viscosity must be positive.")
    if volumetric_flow_rate < 0:
        raise ValueError("Flow rate cannot be negative.")

    area = math.pi * pipe.diameter**2 / 4.0
    velocity = volumetric_flow_rate / area
    re = reynolds_number(
        fluid.density, velocity, pipe.diameter, fluid.dynamic_viscosity
    )
    f = friction_factor(re, pipe.roughness, pipe.diameter)
    dp = (
        f
        * (pipe.length / pipe.diameter)
        * 0.5
        * fluid.density
        * velocity**2
    )
    return {
        "area_m2": area,
        "velocity_m_s": velocity,
        "reynolds_number": re,
        "friction_factor": f,
        "pressure_drop_pa": dp,
    }


def pressure_drop_curve(
    fluid: Fluid,
    pipe: Pipe,
    flow_rates: Iterable[float],
) -> np.ndarray:
    """Calculate Darcy-Weisbach pressure drop for a sequence of flow rates."""
    return np.array(
        [pipe_flow_results(fluid, pipe, float(q))["pressure_drop_pa"] for q in flow_rates]
    )


def wall_conduction_heat_rate(
    thermal_conductivity: float,
    area: float,
    hot_temperature: float,
    cold_temperature: float,
    thickness: float,
) -> float:
    """Calculate steady one-dimensional heat conduction through a flat wall."""
    if thermal_conductivity <= 0 or area <= 0 or thickness <= 0:
        raise ValueError("Thermal conductivity, wall area and thickness must be positive.")
    return (
        thermal_conductivity
        * area
        * (hot_temperature - cold_temperature)
        / thickness
    )


def newton_cooling_time(
    mass: float,
    heat_capacity: float,
    convection_coefficient: float,
    area: float,
    initial_temperature: float,
    target_temperature: float,
    ambient_temperature: float,
) -> float:
    """Calculate cooling/heating time using the lumped Newton-cooling model."""
    if min(mass, heat_capacity, convection_coefficient, area) <= 0:
        raise ValueError("Mass, heat capacity, h and area must all be positive.")

    theta0 = initial_temperature - ambient_temperature
    thetat = target_temperature - ambient_temperature

    if theta0 == 0:
        raise ValueError("Initial temperature cannot equal ambient temperature.")
    if thetat == 0:
        raise ValueError("The ideal lumped model approaches ambient temperature asymptotically.")
    ratio = thetat / theta0
    if ratio <= 0 or ratio >= 1:
        raise ValueError(
            "Target temperature must lie between the initial and ambient temperatures."
        )

    tau = mass * heat_capacity / (convection_coefficient * area)
    return -tau * math.log(ratio)


def cooling_curve(
    mass: float,
    heat_capacity: float,
    convection_coefficient: float,
    area: float,
    initial_temperature: float,
    ambient_temperature: float,
    times: Iterable[float],
) -> np.ndarray:
    """Return temperature versus time for the lumped Newton-cooling model."""
    if min(mass, heat_capacity, convection_coefficient, area) <= 0:
        raise ValueError("Mass, heat capacity, h and area must all be positive.")
    times_arr = np.asarray(list(times), dtype=float)
    tau = mass * heat_capacity / (convection_coefficient * area)
    return ambient_temperature + (
        initial_temperature - ambient_temperature
    ) * np.exp(-times_arr / tau)
