
import streamlit as st
import pandas as pd

df1 = pd.read_excel(
    "Travel_in_Nagpur.xlsx"
)

df2 = pd.read_excel(
    "Travel_in_Nagpur_Version2_220_Places.xlsx"
)

df = pd.concat(
    [df1, df2],
    ignore_index=True
)

st.title("Hidden James Travel Guide")

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
