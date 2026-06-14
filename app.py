%%writefile app.py

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hidden James Travel Guide",
    page_icon="🌍",
    layout="wide"
)

# Load datasets
df1 = pd.read_excel("Travel_in_Nagpur.xlsx")
df2 = pd.read_excel("Travel_in_Nagpur_Version2_220_Places.xlsx")

df = pd.concat([df1, df2], ignore_index=True)

# Remove duplicates
df = df.drop_duplicates()

# Header
st.title("🌍 Hidden James Travel Guide")
st.write("Discover hidden places around Nagpur")

# Sidebar
st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].dropna().unique())
)

search = st.sidebar.text_input(
    "Search Place"
)

# Filtering
filtered = df.copy()

if category != "All":
    filtered = filtered[
        filtered["Category"] == category
    ]

if search:
    filtered = filtered[
        filtered["Place_Name"]
        .astype(str)
        .str.contains(search, case=False)
    ]

st.subheader(
    f"Found {len(filtered)} Places"
)

# Cards
for _, row in filtered.iterrows():

    with st.container():

        st.markdown("---")

        col1, col2 = st.columns([3,1])

        with col1:

            st.markdown(
                f"### {row['Place_Name']}"
            )

            if 'Category' in row:
                st.write(
                    f"📌 Category: {row['Category']}"
                )

            if 'Location' in row:
                st.write(
                    f"📍 Location: {row['Location']}"
                )

            if 'Description' in row:
                st.write(
                    row['Description']
                )

        with col2:

            st.metric(
                "Rating",
                row.get("Rating","N/A")
            )
