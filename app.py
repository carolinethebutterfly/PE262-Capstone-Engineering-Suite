"""Home page for the PE 262 engineering capstone application."""

import streamlit as st

st.set_page_config(
    page_title="Fluid Flow & Heat Transfer Engineering Suite",
    page_icon="🛢️",
    layout="wide",
)

st.title("Fluid Flow & Heat Transfer Engineering Suite")
st.caption("PE 262 Computer Programming Capstone")

st.markdown(
    """
This multi-page engineering application combines pipe-flow analysis,
heat-transfer calculations, and rock/fluid data exploration.

### Modules
- **Pipe Flow Analyser** - Darcy-Weisbach calculations, flow-regime metrics,
  pressure-drop curve and CSV export.
- **Heat Transfer Calculator** - flat-wall conduction, Newton cooling time and
  interactive temperature-time curve.
- **Rock & Fluid Data Dashboard** - upload a CSV, inspect summary statistics,
  filter numeric data, visualize two engineering charts and export filtered data.

Use the page navigation in the sidebar to open a module.
"""
)

with st.expander("Engineering methods used"):
    st.write(
        """
        Pipe flow uses the Darcy-Weisbach equation. Laminar friction factor is
        64/Re, while turbulent flow uses the Swamee-Jain explicit correlation.
        Flat-wall conduction uses Fourier's law. Transient cooling uses the
        lumped-capacitance form of Newton's law of cooling.
        """
    )

st.info(
    "All calculations include input validation and are implemented in the separate "
    "`engineering.py` module using object-oriented classes and documented functions."
)
