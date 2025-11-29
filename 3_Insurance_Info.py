import streamlit as st
import base64

st.set_page_config(page_title="Insurance Info", layout="wide")

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown("""
<div class='info-box'>
    <h2>About Insurance</h2>
    <p>
        Insurance helps protect you from sudden financial loss during health issues, accidents,
        travel problems, or other emergencies. By paying a small premium, you ensure safety and
        financial support when life becomes unpredictable.
    </p>

     Why Insurance Matters
     
         Helps during medical emergencies
         Protects your car or bike from accidents and damage
         Covers travel risks like missed flights, baggage loss, or passport issues
         Provides financial security for your family
         Gives peace of mind and long-term protection
         

     What We Offer
        We provide personalized Car, Bike, Health, and Travel insurance policies with
        low premiums, fast claim support, and cashless benefits.

</div>
""", unsafe_allow_html=True)


# ----- FUNCTION TO DISPLAY SVG ICON -----
def load_svg(svg_file):
    with open(svg_file, "r") as f:
        svg = f.read()
    b64 = base64.b64encode(svg.encode()).decode()
    return f"<img src='data:image/svg+xml;base64,{b64}' class='product-icon'>"


# SVG Paths
car_icon = load_svg("pages/car.svg")
bike_icon = load_svg("pages/bike.svg")
health_icon = load_svg("pages/health.svg")
travel_icon = load_svg("pages/travel.svg")


# -------------------- PAGE TITLE --------------------
st.markdown("<h1 class='main-title'>Our Products</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# -------------------- PRODUCT GRID --------------------
col1, col2, col3, col4 = st.columns(4)

# -------------------- CARD 1 — CAR --------------------
with col1:
    st.markdown(f"""
    <div class='product-card'>
        {car_icon}
        <h3 class='product-title'>Car</h3>
        <ul class='product-text'>
            Doorstep cashless repair
            Low mileage plans
            AI-based claim process
        </ul>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Check price →", key="car_price"):
        st.switch_page("pages/2_Insurance_Premium_Predictor.py")


# -------------------- CARD 2 — BIKE --------------------
with col2:
    st.markdown(f"""
    <div class='product-card'>
        {bike_icon}
        <h3 class='product-title'>Bike</h3>
        <ul class='product-text'>
            Cashless garage network
            Long-term policies
            Repair guarantee
        </ul>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Check price →", key="bike_price"):
        st.switch_page("pages/2_Insurance_Premium_Predictor.py")


# -------------------- CARD 3 — HEALTH --------------------
with col3:
    st.markdown(f"""
    <div class='product-card'>
        {health_icon}
        <h3 class='product-title'>Health</h3>
        <ul class='product-text'>
        Personalised policies
        Cashless hospitals
        Coverage for all budgets
        </ul>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Check price →", key="health_price"):
        st.switch_page("pages/2_Insurance_Premium_Predictor.py")


# -------------------- CARD 4 — TRAVEL --------------------
with col4:
    st.markdown(f"""
    <div class='product-card'>
        {travel_icon}
        <h3 class='product-title'>Travel</h3>
        <ul class='product-text'>
            Worldwide hospitalisation
            Coverage for flight issues
            Instant online policy
        </ul>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Check price →", key="travel_price"):
        st.switch_page("pages/2_Insurance_Premium_Predictor.py")
