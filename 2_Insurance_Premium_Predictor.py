import streamlit as st
import pickle
import pandas as pd

# ---------------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------------
st.set_page_config(
    page_title="ICICI Bank Portal",
    layout="wide",
    # initial_sidebar_state="expanded"
)

# ---------------------------------------------------------------
# Load CSS
# ---------------------------------------------------------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# ICICI LOGO (replaces the extra button)
# ---------------------------------------------------------------
st.image("pages/icici-header-logo.png", width=300)


# ---------------------------------------------------------------
# Load PKL Files
# ---------------------------------------------------------------
with open("Model/EDA.pkl", "rb") as f:
    eda_df = pickle.load(f)

with open("Model/pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

try:
    with open("Model/Model_Analysis.pkl", "rb") as f:
        base_model = pickle.load(f)
except:
    base_model = None

# ---------------------------------------------------------------
# TOP NAVIGATION BUTTONS
# ---------------------------------------------------------------
top_col1, top_col2, top_col3 = st.columns(3)

with top_col1:
    if st.button("🏦 Home"):
        st.switch_page("app.py")

with top_col2:
    if st.button("About Bank"):
        st.switch_page("pages/1_About_Us.py")

with top_col3:
    if st.button("About Insurance"):
        st.switch_page("pages/3_Insurance_Info.py")


# ---------------------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------------------
st.markdown("<h1 class='main-title'>Insurance Premium Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Enter the details below and get premium prediction instantly</p>",
            unsafe_allow_html=True)


# ---------------------------------------------------------------
# FORM INPUTS
# ---------------------------------------------------------------

# Row Styling
st.markdown("""
<style>
.input-row {
    display: flex;
    justify-content: space-between;
    gap: 25px;
    margin-bottom: 20px;
}
.row-col { width: 48%; }
</style>
""", unsafe_allow_html=True)


# ----------------------- ROW 1 -----------------------
st.markdown("<div class='input-row'>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<label class='input-label'>Upper Age</label>", unsafe_allow_html=True)
        upper_age = st.number_input(" ", min_value=18, max_value=100, key="upper_age")
    with col2:
        st.markdown("<label class='input-label'>City Code</label>", unsafe_allow_html=True)
        city = st.selectbox("  ", eda_df["City_Code"].unique(), key="city")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------- ROW 2 -----------------------
st.markdown("<div class='input-row'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label class='input-label'>Lower Age</label>", unsafe_allow_html=True)
    lower_age = st.number_input(" ", min_value=18, max_value=100, key="lower_age")
with col2:
    st.markdown("<label class='input-label'>Accommodation Type</label>", unsafe_allow_html=True)
    acc_type = st.selectbox(" ", eda_df["Accomodation_Type"].unique(), key="acc_type")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------- ROW 3 -----------------------
st.markdown("<div class='input-row'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label class='input-label'>Holding Policy Type</label>", unsafe_allow_html=True)
    policy_type = st.number_input(" ", min_value=1, max_value=10, key="policy_type")
with col2:
    st.markdown("<label class='input-label'>Insurance Type</label>", unsafe_allow_html=True)
    insurance_type = st.selectbox(" ", eda_df["Insurance_Type"].unique(), key="insurance_type")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------- ROW 4 -----------------------
st.markdown("<div class='input-row'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label class='input-label'>Health Indicator</label>", unsafe_allow_html=True)
    health = st.selectbox(" ", eda_df["Health_Indicator"].unique(), key="health")
with col2:
    st.markdown("<label class='input-label'>Holding Policy Duration</label>", unsafe_allow_html=True)
    duration = st.selectbox(" ", eda_df["Holding_Policy_Duration"].unique(), key="duration")
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------- ROW 5 -----------------------
st.markdown("<div class='input-row'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<label class='input-label'>Is Spouse</label>", unsafe_allow_html=True)
    spouse = st.selectbox(" ", eda_df["Is_Spouse"].unique(), key="spouse")
with col2:
    st.markdown("<label class='input-label'>City Code (Optional)</label>", unsafe_allow_html=True)
    city2 = st.selectbox(" ", eda_df["City_Code"].unique(), key="city2")
st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------------
if st.button("Predict Premium"):

    input_data = pd.DataFrame({
        "Upper_Age": [upper_age],
        "Lower_Age": [lower_age],
        "City_Code": [city],
        "Accomodation_Type": [acc_type],
        "Insurance_Type": [insurance_type],
        "Is_Spouse": [spouse],
        "Health_Indicator": [health],
        "Holding_Policy_Duration": [duration],
        "Holding_Policy_Type": [policy_type]
    })

    prediction = pipeline.predict(input_data)[0]

    st.markdown(
        f"<div class='premium-box'>Predicted Premium: ₹ {prediction:,.2f}</div>",
        unsafe_allow_html=True
    )

# Footer
st.markdown("<p class='footer'>Built using Machine Learning</p>", unsafe_allow_html=True)
