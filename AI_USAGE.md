# AI Usage Documentation

The capstone permits AI assistance provided the code is understood, verified and documented.

## Prompt 1
**Prompt:** "Build the engineering equations for a pipe-flow calculator using Darcy-Weisbach, Reynolds number and a robust friction-factor method."

**Verified:** Dimensional consistency of velocity, Reynolds number and pressure drop; laminar branch `64/Re`; turbulent branch checked against the Swamee-Jain equation.

**Corrected:** Added explicit input validation for zero/negative diameter, viscosity and density to prevent divide-by-zero failures.

## Prompt 2
**Prompt:** "Create a Newton's-law-of-cooling calculator that returns cooling time and a temperature-time curve."

**Verified:** Rearranged the analytical exponential solution by hand and confirmed that the target temperature must lie between the initial and ambient temperatures.

**Corrected:** Added protection against requesting exactly the ambient temperature, which would require infinite time in the ideal lumped model.

## Prompt 3
**Prompt:** "Design a Streamlit dashboard that uploads rock/fluid CSV data, filters it, makes two plots and downloads filtered data."

**Verified:** Tested the workflow using the included sample rock dataset and confirmed that uploaded numeric columns populate the filter and charts.

**Corrected:** Added graceful handling for empty files, non-numeric datasets and CSV parsing errors.
