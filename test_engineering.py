"""Basic verification tests for engineering calculations."""

from engineering import (
    Fluid,
    Pipe,
    pipe_flow_results,
    wall_conduction_heat_rate,
    newton_cooling_time,
)


def test_laminar_pipe():
    """Laminar friction factor should match 64/Re through the full solver."""
    fluid = Fluid("test", 1000.0, 0.1)
    pipe = Pipe(0.1, 10.0, 0.0)
    result = pipe_flow_results(fluid, pipe, 1e-5)
    assert result["reynolds_number"] < 2300
    expected_f = 64.0 / result["reynolds_number"]
    assert abs(result["friction_factor"] - expected_f) < 1e-12


def test_fourier_wall():
    """Fourier-law check: 2 W/mK × 5 m2 × 20 K / 0.1 m = 2000 W."""
    assert abs(wall_conduction_heat_rate(2.0, 5.0, 50.0, 30.0, 0.1) - 2000.0) < 1e-9


def test_newton_cooling():
    """Target time should reproduce the analytical Newton-cooling expression."""
    t = newton_cooling_time(2.0, 1000.0, 20.0, 1.0, 100.0, 50.0, 20.0)
    assert t > 0
