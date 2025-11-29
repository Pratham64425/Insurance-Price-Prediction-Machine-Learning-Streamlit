import streamlit as st

st.set_page_config(
    page_title="ICICI Bank Portal",
    layout="wide",
    # initial_sidebar_state="expanded"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header Logo
st.image("pages/icici-header-logo.png", width=350)
st.markdown("<br>", unsafe_allow_html=True)

# About Page Banner
st.image("pages/Icici-about.jpg", use_container_width=True)
st.markdown("<br>", unsafe_allow_html=True)

# ------------------- INTRODUCTION -------------------
st.markdown("""
## 📌 Introduction  

The Industrial Credit and Investment Corporation of India (ICICI) was established on **5 January 1955**.  
Sir Arcot Ramasamy Mudaliar was the first Chairman of ICICI Ltd.  

It was formed as a joint venture between:  
- The World Bank  
- Public sector banks  
- Public sector insurance companies  

The goal was to support and finance Indian industry.

ICICI Bank was later created in **1994** as a 100% subsidiary of ICICI Ltd.

In **2001**, ICICI, ICICI Bank, ICICI Personal Financial Services, and ICICI Capital Services merged.  
This merger led to the **privatization of ICICI Bank**.

ICICI Bank started **Internet Banking in 1998**, becoming one of India’s early adopters.

ICICI became the **first non-Japan Asian company** to list on the NYSE in **1999**.
""")

# ------------------- GLOBAL PRESENCE -------------------
st.markdown("""
---

## 🌍 Global Presence  

- **7,246+ branches**  
- **10,610+ ATMs**  
- Presence in **11 countries**  

### 🌐 International Branches  
USA • Singapore • Bahrain • Hong Kong • Qatar  
Oman • Dubai IFSC • China • South Africa  

### 🇬🇧 European Offices  
Belgium • Germany  
""")

# ------------------- IMPORTANT BANK INFO -------------------
st.markdown("""
---

## 🏦 Systemically Important Bank  

ICICI Bank is rated as a **D-SIB (Domestic Systemically Important Bank)** by RBI.  
This means it is considered *“Too Big To Fail”* and is vital to India’s financial system.

---
""")

# ------------------- PRODUCTS -------------------
st.markdown("""
## 🧾 Products  

ICICI Bank offers many services including:  
- Savings and current accounts  
- Fixed and recurring deposits  
- Home, personal, auto and gold loans  
- NRI services and remittances  
- Card services  
- Trade and forex services  
- Lockers  
- Agri and rural services  

### 💻 Digital Platforms  
- iMobile Pay  
- InstaBiz  
- Digital Rupee App  
- Retail Internet Banking  
- Corporate Internet Banking  
- Money2India / Money2World  
- Pockets wallet  
- ICICI Stack (digital suite)
""")

# ------------------- SUBSIDIARIES -------------------
st.markdown("""
---

## 🏢 Subsidiaries  

### ICICI Prudential Life Insurance  
### ICICI Lombard General Insurance  
### ICICI Prudential Mutual Fund  
### ICICI Securities  

ICICI Securities provides:  
- Equity & derivatives trading  
- Stock and commodity market research  
- ICICI Direct platform for financial products  
""")

st.markdown("<br>", unsafe_allow_html=True)

# Back Button
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")
