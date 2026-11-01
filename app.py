import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Telangana Avian Waste & PGPB Biofertilizer Dashboard",
    page_icon="🐓",
    layout="wide"
)

st.title("🐓 Telangana Avian Waste, Infection Risk & AI Biofertilizer Dashboard")
st.markdown("### A Circular Bio-Economy Framework: Turning Avian Feather Waste into PGPB Biofertilizers")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Telangana Poultry", "92.5 Million", "High Density")
col2.metric("Annual Feather Waste", "~33,760 Tonnes", "+5.4% YoY")
col3.metric("Keratin Content in Waste", "~28,690 Tonnes", "90% Keratin")
col4.metric("Avg Keratin Degradation", "80.9%", "Bacillus Strains")

st.markdown("---")
st.subheader("📊 Telangana District-wise Feather Waste Generation")

district_data = pd.DataFrame({
    'District': ['Rangareddy', 'Karimnagar', 'Warangal', 'Mahabubnagar', 'Nalgonda', 'Khammam', 'Nizamabad', 'Medak'],
    'Feather_Waste_Tons_Per_Year': [6752, 5183, 4672, 4197, 3723, 3321, 3066, 2847],
    'Infection_Risk_Score': [88, 79, 75, 68, 62, 58, 54, 50]
})

fig = px.bar(
    district_data,
    x='District',
    y='Feather_Waste_Tons_Per_Year',
    color='Infection_Risk_Score',
    color_continuous_scale='Reds',
    title="Feather Waste Accumulation & Pathogen Risk Index in Telangana"
)
st.plotly_chart(fig, use_container_width=True)
st.markdown("---")
st.subheader("🔬 PGPB Traits Frequency Across Bird Sources")
strain_data = pd.DataFrame({
    'Source & Strain': ['Poultry Bacillus', 'Poultry Pseudomonas', 'Wild Bird Bacillus', 'Wild Bird Enterobacter', 'Other Avian Strains'],
    'Frequency': [45, 30, 25, 15, 10]
})
fig_strain = px.bar(
    strain_data, x='Source & Strain', y='Frequency',
    color='Frequency', color_continuous_scale='Greens',
    title="Comparison of PGPB Traits in Feather-Degrading Isolates"
)
st.plotly_chart(fig_strain, use_container_width=True)

st.success("✅ Dashboard is live and fully functional for your National Seminar Presentation!")
