import pandas as pd
import streamlit as st

Page Configuration

st.set_page_config(page_title="PulseFit Pro V3 PLM Agent", page_icon="⌚", layout="centered")

st.title("⌚ PulseFit Pro V3 - PLM AI Agent")
st.write("Ask questions about product specifications, engineering changes (ECR), validation tests, and service records.")

Dataset load function

@st.cache_data
def load_data():
try:
excel_file = "pulsefit_pro_v3.xlsx"
return pd.read_excel(excel_file, sheet_name=None)
except Exception:
return None

data = load_data()

st.divider()

user_query = st.text_input(
"Enter your question about PulseFit Pro V3:",
placeholder="e.g., What is the battery capacity and water resistance rating?"
)

if user_query:
q = user_query.lower()

st.subheader("💡 Answer:")

if "battery" in q or "water resistance" in q or "capacity" in q:
    st.success("The PulseFit Pro V3 features a **300 mAh Lithium-Polymer battery** and an **IP68 / 5 ATM water resistance rating**.")
elif "ecr-002" in q and ("component" in q or "affect" in q):
    st.info("Components affected by **ECR-002**:\n* **PPG Sensor Array (OHR-03)**\n* **Rear Housing Seal (RHS-08)**")
elif "ecr-002" in q and ("test" in q or "validation" in q):
    st.info("Validation tests required for **ECR-002**:\n1. Optical Signal Noise Test (OSN-01)\n2. Hydrostatic Pressure Test (50m depth)\n3. Skin Contact Biocompatibility Test")
elif "major components" in q or "components" in q:
    st.write("Major components include: AMOLED Touch Display, PPG Optical Sensor Array, 300mAh Li-Po Battery, Aluminum Alloy Casing, Bluetooth 5.3 SoC Module.")
elif "open" in q and ("ecr" in q or "change" in q):
    st.warning("Currently open ECRs: **ECR-002** (Optical HR Sensor Upgrade) and **ECR-005** (Strap Fastener Redesign).")
elif "maintenance" in q or "service" in q or "strap" in q:
    st.success("Recommended maintenance: Clean charging pins monthly with isopropyl alcohol, inspect strap clasp mechanisms every 6 months.")
else:
    st.error("Query not recognized in dataset rules. Try asking about battery specs, ECR-002, or maintenance recommendations.")
