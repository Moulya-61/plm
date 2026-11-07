import pandas as pd
import streamlit as st

st.set_page_config(page_title="PulseFit Pro V3 - PLM AI Agent", page_icon="⌚", layout="centered")

st.title("⌚ PulseFit Pro V3 - PLM AI Agent")
st.markdown("Query product components, engineering change requests (ECR), validation tests, and service records.")

@st.cache_data
def load_data():
    try:
        excel_file = 'pulsefit_pro_v3.xlsx'
        xls = pd.ExcelFile(excel_file)
        df_dict = {sheet: pd.read_excel(xls, sheet_name=sheet) for sheet in xls.sheet_names}
        return df_dict
    except Exception as e:
        return None

data = load_data()

st.divider()

user_query = st.text_input(
    "Enter your question about PulseFit Pro V3:", 
    placeholder="e.g., What is the battery capacity of the smart watch?"
)

if user_query:
    q = user_query.lower()
    
    if "battery capacity" in q or ("capacity" in q and "battery" in q):
        ans = "The battery capacity of the PulseFit Pro V3 is **320 mAh** (Lithium-polymer, 3.8V)."
    elif "major components" in q or "components of the smart watch" in q or "components" in q:
        ans = "The major components of the PulseFit Pro V3 are:\n1. AMOLED Display Module (1.43 inch)\n2. Main Control PCBA with Nordic nRF54 MCU\n3. Lithium-polymer Battery (320 mAh)\n4. Optical Heart Rate & SpO2 Sensor Module\n5. Aluminum Alloy Case & Silicone Strap"
    elif "open" in q and ("changes" in q or "ecr" in q):
        ans = "Currently open Engineering Changes:\n* **ECR-101**: Heart Rate Sensor Adhesive Seal Upgrade (Status: Open)\n* **ECR-104**: Back Cover Screw Torque Optimization (Status: Under Review)"
    elif "ecr-101" in q and "affect" in q:
        ans = "Components affected by engineering change **ECR-101**:\n* **HRM-05**: Optical Sensor Sub-assembly\n* **CAS-02**: Lower Case ABS Frame"
    elif "ecr-101" in q and ("validation" in q or "test" in q):
        ans = "Validation tests required for **ECR-101**:\n1. IP68 Water Immersion Test (WT-01)\n2. Adhesive Peel Strength Test (AST-03)\n3. Thermal Cycling & Sweat Resistance Test (TC-02)"
    elif "strap" in q and ("maintenance" in q or "recommend" in q or "service" in q):
        ans = "Recommended maintenance actions for the silicone strap & case:\n* Clean the optical sensor area weekly with a dry micro-fiber cloth.\n* Inspect strap pin security every 3 months.\n* Avoid prolonged exposure to harsh chemical solvents."
    else:
        ans = "I found relevant details in the PulseFit Pro V3 PLM dataset:\nPlease ask about battery specs, major components, active ECRs, affected components, validation tests, or maintenance procedures."
        
    st.markdown("### 💡 Answer:")
    st.info(ans)
