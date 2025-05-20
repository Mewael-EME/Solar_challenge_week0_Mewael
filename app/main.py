# app/main.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from app.utils import load_data, plot_boxplot, get_summary_table, get_avg_ghi_ranking

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# Title
st.title("☀️ Cross-Country Solar Potential Dashboard")

# Country selector
countries = ['Benin', 'Sierra Leone', 'Togo']
selected_countries = st.multiselect("Select countries to compare:", countries, default=countries)

# Load data
dataframes = load_data(selected_countries)

# Metric selection
metric = st.selectbox("Select metric to plot:", ['GHI', 'DNI', 'DHI'])

# Show Boxplot
st.subheader(f"{metric} Distribution by Country")
fig = plot_boxplot(dataframes, metric)
st.pyplot(fig)

# Show summary table
st.subheader("📊 Summary Statistics")
summary_df = get_summary_table(dataframes)
st.dataframe(summary_df)

# Show average GHI bar chart
st.subheader("📈 Average GHI Ranking")
ghi_ranking = get_avg_ghi_ranking(dataframes)
st.bar_chart(ghi_ranking.set_index("Country")["GHI"])

# Footer
st.markdown("---")
st.markdown("Made for Solar Challenge • Developed by Mewael Mizan Tesfay")
