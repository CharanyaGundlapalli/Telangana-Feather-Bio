import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Telangana Avian Waste & PGPB Biofertilizer Dashboard",
    layout="wide"
)

st.title("🔬 Telangana Avian Waste & PGPB Biofertilizer Dashboard")
st.write("AI-Driven Bio-Valorization of Poultry Feather Waste in Telangana")

# 1. Summary Metrics from Literature
st.markdown("---")
st.subheader("📈 Summary Metrics from Literature Review")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Avg Degradation", "80.9%", "Keratin Efficiency")
m2.metric("Seed Germination", "77.2%", "Biofertilizer Effect")
m3.metric("Growth Improvement", "72.3%", "Crop Yield")
m4.metric("Bacillus Dominance", "90.5%", "Isolate Efficiency")

# 2. PGPB Traits Bar Chart
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

# 3. Pathogens & Infection Risks
st.markdown("---")
st.subheader("🦠 Poultry Pathogen Risks & Effective Bacterial Strains")
st.warning(
    "**⚠️ Associated Pathogens & Infection Hazards:**\n"
    "Untreated poultry feather waste in dump yards harbors severe biosecurity risks:\n"
    "* **Pathogens:** *Salmonella enterica* (Salmonellosis), *Campylobacter jejuni* (Avian Enteritis), *Aspergillus fumigatus* (Fungal Spore Respiratory Mycoses), and *Avian Influenza Virus*.\n"
    "* **Effective Degrading Isolates:** Keratinolytic *Bacillus subtilis*, *Bacillus licheniformis*, *Pseudomonas aeruginosa*, and *Streptomyces* strains degrade keratin while suppressing disease-causing microbes."
)

# 4. Kg to Keratin & Fertilizer Predictor Calculator
st.markdown("---")
st.subheader("⚖️ Feather Weight (kg) to Keratin & Fertilizer Calculator")

kg_input = st.number_input("Enter Feather Waste Weight (in kg):", min_value=10, max_value=100000, value=500, step=50)

keratin_yield_kg = kg_input * 0.90       
amino_acids_kg = keratin_yield_kg * 0.809  
npk_estimate = amino_acids_kg * 0.12     

col_c1, col_c2, col_c3 = st.columns(3)
col_c1.metric("Pure Keratin Mass", f"{keratin_yield_kg:,.1f} kg", "90% Protein Content")
col_c2.metric("Soluble Amino Acids", f"{amino_acids_kg:,.1f} kg", "Enzymatic Hydrolysate")
col_c3.metric("Est. Organic Nitrogen (N)", f"{npk_estimate:,.1f} kg", "Soil Enricher")

st.info(
    "**🌾 How it Helps as a Biofertilizer:**\n"
    "Microbial enzymatic degradation turns insoluble keratin into soluble amino acids and peptides. "
    "Applied to agricultural fields, it provides slow-release organic nitrogen, activates native soil rhizosphere microflora, "
    "improves soil water retention, and boosts overall crop growth by ~72.3%."
)
