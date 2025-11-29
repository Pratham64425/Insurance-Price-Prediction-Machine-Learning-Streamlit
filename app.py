import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="ICICI Bank Portal",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ICICI Header Logo
st.image("pages/icici-header-logo.png", width=350)

# ----------- MAIN HERO SECTION -----------
left, right = st.columns([1.2, 1])

with left:
    st.markdown("<h1 class='hero-title'>Truth, Trust, Transparency</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Welcome to ICICI Bank – your safe and smart financial partner.</p>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # MAIN BUTTONS
    btn1, btn2 = st.columns([1, 1])

    with btn1:
        if st.button("🏦 About Bank"):
            st.switch_page("pages/1_About_Us.py")

    with btn2:
        if st.button("💰 Insurance Services"):
            st.switch_page("pages/2_Insurance_Premium_Predictor.py")

with right:
    st.image("pages/icici.jpg", use_container_width=True)

# ------------ AUTO SLIDE CARDS ------------
st.markdown("<h2 class='section-title'>Our Key Services</h2>", unsafe_allow_html=True)

# Auto refresh every 3 seconds
count = st_autorefresh(interval=3000, limit=None, key="carousel_key")

# List of card content with your image paths
cards = [
    {
        "img": "pages/App-banner.jpg",
        "title": "Life Insurance App",
        "text": "Buy, track and renew all your life insurance plans in one place."
    },
    {
        "img": "pages/car_insurance.jpg",
        "title": "Car Insurance",
        "text": "Protect your vehicle with trusted ICICI motor insurance."
    },
    {
        "img": "pages/cashless.jpg",
        "title": "Cashless Treatment",
        "text": "Get medical help at any hospital without paying upfront."
    },
    {
        "img": "pages/life_insurance.jpg",
        "title": "Life Insurance Benefits",
        "text": "Secure your future with planning, protection and tax benefits."
    },
]

# Select which card to show
index = count % len(cards)
card = cards[index]

center_col = st.columns([1, 2, 1])[1]

with center_col:
    st.image(card["img"], use_container_width=True)
    st.markdown(f"<h4 class='card-title'>{card['title']}</h4>", unsafe_allow_html=True)
    st.markdown(f"<p class='card-text'>{card['text']}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<p class='footer'>ICICI Bank • Demo Portal</p>", unsafe_allow_html=True)
