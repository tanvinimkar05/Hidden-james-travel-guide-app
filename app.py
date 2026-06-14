
import streamlit as st

st.title("Testing")

try:
    import openpyxl
    st.success(f"openpyxl loaded: {openpyxl.__version__}")
except Exception as e:
    st.error(f"openpyxl error: {e}")

st.stop()
category = st.selectbox(
    "Select Category",
    ["All"] +
    list(df["Category"].unique())
)

if category == "All":
    result = df
else:
    result = df[
        df["Category"] == category
    ]

st.dataframe(result)
