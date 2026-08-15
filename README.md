# PE 262 Capstone - Fluid Flow & Heat Transfer Engineering Suite

A professional multi-page Streamlit engineering application developed for the
PE 262 Computer Programming capstone.

## Modules

### Module A - Pipe Flow Analyser
- Fluid selection: water, air, crude oil, user-defined
- Pipe diameter, length, roughness and flow-rate inputs
- Velocity, Reynolds number, Darcy friction factor and pressure drop
- Interactive pressure-drop vs flow-rate plot
- CSV export

### Module B - Heat Transfer Calculator
- Steady-state single-layer flat-wall conduction using Fourier's law
- Newton's law of cooling/heating time calculation
- Interactive temperature-time cooling curve
- Physical descriptions and units for all inputs

### Module C - Rock & Fluid Data Dashboard
- CSV upload and display
- Summary statistics
- Numeric filtering
- Histogram and crossplot
- Filtered CSV download

### Module D - Code Quality & Deployment
- OOP: `Fluid` and `Pipe` classes live in `engineering.py`
- Functions include docstrings and input validation
- Error handling prevents user-input crashes
- `AI_USAGE.md` documents three AI prompts and verification/corrections

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Verification examples

- Pipe flow uses Darcy-Weisbach:
  `ΔP = f (L/D) (ρV²/2)`
- Laminar friction factor: `f = 64/Re`
- Turbulent friction factor: Swamee-Jain explicit correlation
- Flat-wall conduction: `Qdot = kA(T1-T2)/L`
- Newton cooling:
  `T(t)=T∞+(T0-T∞)exp[-hAt/(mcp)]`

## Deployment

The app is designed for Streamlit Community Cloud.

**Live app URL:** add after deployment.

## Submission items

1. GitHub repository URL
2. Live Streamlit app URL
3. One-page PDF developer report (`developer_report.pdf`)
