import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Telangana Avian Waste & PGPB Biofertilizer Dashboard",
    layout="wide"
)

# Header
st.title("🐓 Telangana Avian Waste, Infection Risk & AI Biofertilizer Dashboard")
st.markdown("### A Circular Bio-Economy Framework: Turning Avian Feather Waste into PGPB Biofertilizers")

# 1. Telangana Poultry Overview Metrics
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric("Total Telangana Poultry", "92.5 Million", "High Density")
col_m2.metric("Annual Feather Waste", "~33,760 Tonnes", "+5.4% YoY")
col_m3.metric("Keratin Content in Waste", "~28,690 Tonnes", "90% Keratin")
col_m4.metric("Avg Keratin Degradation", "80.9%", "Bacillus Strains")

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

# 2. Summary Metrics from Literature Review 
st.subheader("📈 Summary Metrics from Literature Review, AI MODEL & BIOFERTILIZER EFFICACY")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Avg Degradation", "80.9%", "Keratin Efficiency")
m2.metric("Seed Germination", "77.2%", "Biofertilizer Effect")
m3.metric("Growth Improvement", "72.3%", "Crop Yield")
m4.metric("Bacillus Dominance", "90.5%", "Isolate Efficiency")

st.markdown("---")

# 3. PGPB Strains Frequency Bar Chart
st.subheader("🔬 PGPB Strains Frequency Across Bird Sources")
strain_data = pd.DataFrame({
    'Source & Strain': ['Poultry Bacillus', 'Poultry Pseudomonas', 'Wild Bird Bacillus', 'Wild Bird Enterobacter', 'Other Avian Strains'],
    'Frequency': [45, 30, 25, 15, 10]
})
fig_strain = px.bar(
    strain_data, x='Source & Strain', y='Frequency',
    color='Frequency', color_continuous_scale='Greens',
    title="Comparison of PGPB Traits in Feather-Degrading Isolates"
)
st.plotly_chart(fig_strain, use_container_width=True, key="strain_chart_unique")

st.markdown("---")

# 4. Target Crops & Plants Benefited
st.subheader("🌱 Target Crops & Plants Benefited by Feather Biofertilizers")

plant_data = pd.DataFrame({
    'Crop / Plant': ['Maize (Zea mays)', 'Rice (Oryza sativa)', 'Tomato (Solanum lycopersicum)', 'Wheat (Triticum aestivum)', 'Leafy Vegetables'],
    'Growth Response Score (%)': [88, 85, 82, 78, 75]
})

fig_plant = px.bar(
    plant_data, x='Crop / Plant', y='Growth Response Score (%)',
    color='Growth Response Score (%)', color_continuous_scale='Tealgrn',
    title="Relative Growth Enhancement Across Agricultural Crops"
)
st.plotly_chart(fig_plant, use_container_width=True, key="plant_chart_unique")

st.markdown("---")

# 5. Poultry Feather Pathogens & Infection Risks (Pie Chart)
st.subheader("🦠 Poultry Feather Pathogens & Biosecurity Risk Distribution")
pathogen_data = pd.DataFrame({
    'Pathogen & Infection': [
        'Salmonella enterica (Salmonellosis)', 
        'Campylobacter jejuni (Enteritis)', 
        'Aspergillus fumigatus (Respiratory Mycoses)', 
        'Avian Influenza Virus'
    ],
    'Risk Weight': [35, 25, 25, 15]
})

fig_pathogen = px.pie(
    pathogen_data, 
    names='Pathogen & Infection', 
    values='Risk Weight',
    title="Distribution of Associated Poultry Pathogens & Infection Risks",
    hole=0.4,
    color_discrete_sequence=px.colors.sequential.Reds_r
)
st.plotly_chart(fig_pathogen, use_container_width=True, key="pathogen_chart_unique")

st.markdown("---")

# 6. Kg to Keratin & Fertilizer Predictor Calculator
st.subheader("⚖️ Feather Weight (kg) to Keratin & Fertilizer Calculator")
st.markdown("Enter the weight of poultry feathers to calculate pure keratin yield, soluble amino acid conversion, and soil nutrient contribution:")

kg_input = st.number_input("Enter Feather Waste Weight (in kg):", min_value=10, max_value=100000, value=500, step=10)

keratin_yield_kg = kg_input * 0.90       
amino_acids_kg = keratin_yield_kg * 0.809  
npk_estimate = amino_acids_kg * 0.12     

col_c1, col_c2, col_c3 = st.columns(3)
col_c1.metric("Pure Keratin Mass", f"{keratin_yield_kg:,.1f} kg", "90% Protein Content")
col_c2.metric("Soluble Amino Acids", f"{amino_acids_kg:,.1f} kg", "Enzymatic Hydrolysate")
col_c3.metric("Est. Organic Nitrogen (N)", f"{npk_estimate:,.1f} kg", "Soil Enricher")

st.info(
    "**🌾 How it Helps as a Biofertilizer:**\n"
    "Microbial enzymatic degradation converts insoluble recalcitrant feather keratin into soluble oligopeptides and free amino acids. "
    "When applied to agricultural soils, it functions as a slow-release organic nitrogen fertilizer, activates native plant growth-promoting rhizosphere microflora, "
    "improves soil moisture retention, and boosts overall crop growth by ~72.3%."
)
