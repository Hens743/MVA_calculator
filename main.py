import streamlit as st

def calculate_vat_exclusive(price_inclusive, vat_rate):
    return price_inclusive / (1 + vat_rate / 100)

def calculate_vat_inclusive(price_exclusive, vat_rate):
    return price_exclusive * (1 + vat_rate / 100)

st.title("MVA Kalkulator")
st.write("Beregn priser med og uten merverdiavgift (MVA).")

# User input
price_type = st.radio("Velg pris type", ("Inkludert MVA", "Ekskludert MVA"))
price = st.number_input("Pris", min_value=0.0, step=0.01)
vat_rate = st.number_input("MVA-sats (%)", min_value=0.0, step=0.1, value=25.0)

# Calculate and display the results
if price_type == "Inkludert MVA":
    price_exclusive = calculate_vat_exclusive(price, vat_rate)
    st.write(f"Pris ekskludert MVA: {price_exclusive:.2f} NOK")
else:
    price_inclusive = calculate_vat_inclusive(price, vat_rate)
    st.write(f"Pris inkludert MVA: {price_inclusive:.2f} NOK")

# Sidebar for additional information
st.sidebar.title("Om MVA")
st.sidebar.info(
    """
    Merverdiavgift (MVA) er en avgift som betales på de fleste varer og tjenester som
    selges i Norge. Standard MVA-sats er 25%, men det finnes også reduserte satser for
    visse varer og tjenester.
    """
)

# Optional: Add custom styling
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #e0e2e6;
    }
    </style>
    """, unsafe_allow_html=True)
