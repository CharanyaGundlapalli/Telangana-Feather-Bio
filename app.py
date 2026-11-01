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
st.markdown("---")
st.subheader("📈 Summary Metrics from Literature Review (50 Papers)")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Avg Degradation", "80.9%", "Keratin Efficiency")
m2.metric("Seed Germination", "77.2%", "Biofertilizer Effect")
m3.metric("Growth Improvement", "72.3%", "Crop Yield")
m4.metric("Bacillus Dominance", "90.5%", "Isolate Efficiency")
st.markdown("---")
st.subheader("🧬 Circular Bio-Economy & Microbial Valorization Pathway")
st.info(
    "**Step-by-Step Microbiological Process Framework:**\n\n"
    "1. **Waste Generation:** Accumulation of recalcitrant $\\beta$-keratin-rich poultry feather waste in Telangana (~33,760 tonnes/year), causing severe environmental pollution and pathogen risks.\n\n"
    "2. **Microbial Degradation:** Inoculation with specialized *Bacillus* strains (e.g., *Bacillus subtilis*, *Bacillus licheniformis*) that secrete extracellular **keratinase enzymes** to cleave rigid disulfide bonds ($-S-S-$) in keratin.\n\n"
    "3. **Amino Acid / Biofertilizer Conversion:** Enzymatic breakdown of insoluble feather keratin into soluble oligopeptides, free amino acids, and ammonia, formulating nutrient-rich PGPB biofertilizers.\n\n"
    "4. **Sustainable Agriculture:** Application of the biofertilizer to regional crops, significantly enhancing root elongation, soil microbial health, and boosting overall crop growth by ~72.3%."
)
st.markdown("---")
st.subheader("🔮 AI & Bio-Valorization Predictive Impact Simulator")
st.markdown("Simulate the projected outcomes based on Telangana's poultry waste input and *Bacillus* strain efficiency:")

# Interactive Slider for Waste Input
waste_input = st.slider("Select Poultry Feather Waste Input (Tonnes):", min_value=1000, max_value=40000, value=15000, step=1000)

# Predictive calculation logic
est_keratin = waste_input * 0.90
est_amino_acids = est_keratin * 0.809  # based on 80.9% degradation efficiency
projected_crop_boost = min(75.0, 50.0 + (waste_input / 2000))

# Display Predictions in columns
col_p1, col_p2, col_p3 = st.columns(3)
col_p1.metric("Predicted Keratin Yield", f"{est_keratin:,.0f} Tonnes", "90% Purity")
col_p2.metric("Soluble Bio-Amino Acids", f"{est_amino_acids:,.0f} Tonnes", "Enzymatic Conversion")
col_p3.metric("Projected Crop Growth Boost", f"{projected_crop_boost:.1f}%", "PGPB Enhanced")



