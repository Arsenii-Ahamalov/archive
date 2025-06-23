import streamlit as st
import nbformat
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="📊 Animal Shelter Dashboard")

st.title("📊 Animal Shelter Data Dashboard")

st.markdown(
    """
    🐶 **About the Data**  
    This dashboard visualizes data from an **animal shelter**.  
    The data includes:  
    - **`intakes.csv`** → Records of animals **admitted** (from 2013-10-01 to 2024-10-06).  
    - **`outcomes.csv`** → Records of animals **leaving the shelter** (e.g., adopted, returned to owner).  
    """
)

NOTEBOOK_PATH = "animal_shelter_analyze.ipynb"

def execute_notebook(notebook_path):
    """Executes a Jupyter Notebook and returns only plots (no tables)."""
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    exec_globals = {"st": st, "plt": plt, "pd": pd, "np": np}  
    plots = []  
    
    for cell in nb.cells:
        if cell.cell_type == "code":
            try:
                cell_code = cell.source

                cell_code = cell_code.replace("display(", "# Removed display(")

                exec(cell_code, exec_globals)

                fig = plt.gcf() 
                if fig and fig.get_axes():  
                    plots.append(fig)
                    plt.close(fig)

            except Exception as e:
                st.error(f"Error in cell execution: {e}")
    
    return plots 

extracted_plots = execute_notebook(NOTEBOOK_PATH)

st.subheader("📈 Shelter Data Visualizations")

if extracted_plots:
    cols = st.columns(2) 

    for i, fig in enumerate(extracted_plots):
        with cols[i % 2]:  
            st.pyplot(fig)
else:
    st.warning("No plots were found in the notebook.")

st.success("Dashboard loaded successfully! 🚀")

