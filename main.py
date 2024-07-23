# import streamlit as st

# # Translation dictionary
# translations = {
#     'title': {
#         'en': "VAT Calculator",
#         'no': "MVA Kalkulator",
#         'es': "Calculadora de IVA",
#         'fr': "Calculateur de TVA"
#     },
#     'description': {
#         'en': "Calculate prices with and without VAT.",
#         'no': "Beregn priser med og uten merverdiavgift (MVA).",
#         'es': "Calcula precios con y sin IVA.",
#         'fr': "Calculez les prix avec et sans TVA."
#     },
#     'price_type_label': {
#         'en': "Select price type",
#         'no': "Velg pris type",
#         'es': "Seleccione tipo de precio",
#         'fr': "Sélectionnez le type de prix"
#     },
#     'price_label': {
#         'en': "Price",
#         'no': "Pris",
#         'es': "Precio",
#         'fr': "Prix"
#     },
#     'vat_rate_label': {
#         'en': "Select VAT rate",
#         'no': "Velg MVA-sats",
#         'es': "Seleccione tasa de IVA",
#         'fr': "Sélectionnez le taux de TVA"
#     },
#     'calculate_button': {
#         'en': "Calculate",
#         'no': "Beregn",
#         'es': "Calcular",
#         'fr': "Calculer"
#     },
#     'price_exclusive_label': {
#         'en': "Price excluding VAT:",
#         'no': "Pris ekskludert MVA:",
#         'es': "Precio sin IVA:",
#         'fr': "Prix hors TVA :"
#     },
#     'price_inclusive_label': {
#         'en': "Price including VAT:",
#         'no': "Pris inkludert MVA:",
#         'es': "Precio con IVA:",
#         'fr': "Prix incluant TVA :"
#     },
#     'sidebar_title': {
#         'en': "About VAT",
#         'no': "Om MVA",
#         'es': "Sobre el IVA",
#         'fr': "À propos de la TVA"
#     },
#     'sidebar_info': {
#         'en': """
#             Value Added Tax (VAT) is a tax paid on most goods and services sold in Norway.
#             The standard VAT rate is 25%, but there are also reduced rates for certain goods and services.
#         """,
#         'no': """
#             Merverdiavgift (MVA) er en avgift som betales på de fleste varer og tjenester som
#             selges i Norge. Standard MVA-sats er 25%, men det finnes også reduserte satser for
#             visse varer og tjenester.
#         """,
#         'es': """
#             El Impuesto al Valor Agregado (IVA) es un impuesto que se paga sobre la mayoría de los bienes y servicios vendidos en Noruega.
#             La tasa de IVA estándar es del 25%, pero también hay tasas reducidas para ciertos bienes y servicios.
#         """,
#         'fr': """
#             La Taxe sur la Valeur Ajoutée (TVA) est une taxe payée sur la plupart des biens et services vendus en Norvège.
#             Le taux de TVA standard est de 25%, mais il existe également des taux réduits pour certains biens et services.
#         """
#     }
# }

# # Language selection
# lang = st.sidebar.selectbox("Select language", ("English", "Norsk", "Español", "Français"))
# lang_code = {'English': 'en', 'Norsk': 'no', 'Español': 'es', 'Français': 'fr'}[lang]

# def translate(text_id):
#     return translations[text_id][lang_code]

# def calculate_vat_exclusive(price_inclusive, vat_rate):
#     return price_inclusive / (1 + vat_rate / 100)

# def calculate_vat_inclusive(price_exclusive, vat_rate):
#     return price_exclusive * (1 + vat_rate / 100)

# st.title(translate('title'))
# st.write(translate('description'))

# # Input form
# with st.form(key='mva_calculator'):
#     price_type = st.radio(translate('price_type_label'), (translate('price_inclusive_label'), translate('price_exclusive_label')))
#     price = st.number_input(translate('price_label'), min_value=0.0, step=0.01, format="%.2f")

#     vat_rates = {
#         "Generell (25%)": 25.0,
#         "Redusert (15%)": 15.0,
#         "Redusert (12%)": 12.0,
#         "Redusert (11.11%)": 11.11,
#         "Redusert (6%)": 6.0
#     }

#     vat_rate_label = st.selectbox(translate('vat_rate_label'), list(vat_rates.keys()))
#     vat_rate = vat_rates[vat_rate_label]

#     submit_button = st.form_submit_button(label=translate('calculate_button'))

# if submit_button:
#     if price_type == translate('price_inclusive_label'):
#         price_exclusive = calculate_vat_exclusive(price, vat_rate)
#         st.success(f"{translate('price_exclusive_label')} {price_exclusive:.2f} NOK")
#     else:
#         price_inclusive = calculate_vat_inclusive(price, vat_rate)
#         st.success(f"{translate('price_inclusive_label')} {price_inclusive:.2f} NOK")

# st.sidebar.title(translate('sidebar_title'))
# st.sidebar.info(translate('sidebar_info'))

# st.markdown("""
#     <style>
#     .reportview-container {
#         background: #f0f2f6;
#     }
#     .sidebar .sidebar-content {
#         background: #e0e2e6;
#     }
#     </style>
#     """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate VAT exclusive and inclusive
def calculate_vat(price, vat_rate, inclusive=True):
    if inclusive:
        return price / (1 + vat_rate / 100)
    else:
        return price * (1 + vat_rate / 100)

# Multilingual support
translations = {
    'title': {'en': "MVA Calculator", 'no': "MVA Kalkulator", 'es': "Calculadora de IVA", 'fr': "Calculateur de TVA"},
    'description': {'en': "Calculate prices with and without VAT.", 'no': "Beregn priser med og uten merverdiavgift (MVA).", 'es': "Calcula precios con y sin IVA.", 'fr': "Calculez les prix avec et sans TVA."},
    'price_type_label': {'en': "Select price type", 'no': "Velg pris type", 'es': "Seleccione tipo de precio", 'fr': "Sélectionnez le type de prix"},
    'price_label': {'en': "Price", 'no': "Pris", 'es': "Precio", 'fr': "Prix"},
    'vat_rate_label': {'en': "Select VAT rate", 'no': "Velg MVA-sats", 'es': "Seleccione tasa de IVA", 'fr': "Sélectionnez le taux de TVA"},
    'calculate_button': {'en': "Calculate", 'no': "Beregn", 'es': "Calcular", 'fr': "Calculer"},
    'price_exclusive_label': {'en': "Price excluding VAT:", 'no': "Pris ekskludert MVA:", 'es': "Precio sin IVA:", 'fr': "Prix hors TVA :"},
    'price_inclusive_label': {'en': "Price including VAT:", 'no': "Pris inkludert MVA:", 'es': "Precio con IVA:", 'fr': "Prix incluant TVA :"},
    'sidebar_title': {'en': "About VAT", 'no': "Om MVA", 'es': "Sobre el IVA", 'fr': "À propos de la TVA"},
    'sidebar_info': {
        'en': """
            Value Added Tax (VAT) is a tax paid on most goods and services sold in Norway.
            The standard VAT rate is 25%, but there are also reduced rates for certain goods and services.
        """,
        'no': """
            Merverdiavgift (MVA) er en avgift som betales på de fleste varer og tjenester som
            selges i Norge. Standard MVA-sats er 25%, men det finnes også reduserte satser for
            visse varer og tjenester.
        """,
        'es': """
            El Impuesto al Valor Agregado (IVA) es un impuesto que se paga sobre la mayoría de los bienes y servicios vendidos en Noruega.
            La tasa de IVA estándar es del 25%, pero también hay tasas reducidas para ciertos bienes y servicios.
        """,
        'fr': """
            La Taxe sur la Valeur Ajoutée (TVA) est une taxe payée sur la plupart des biens et services vendus en Norvège.
            Le taux de TVA standard est de 25%, mais il existe également des taux réduits pour certains biens et services.
        """
    }
}

# Language selection
lang = st.sidebar.selectbox("Select language", ("English", "Norsk", "Español", "Français"))
lang_code = {'English': 'en', 'Norsk': 'no', 'Español': 'es', 'Français': 'fr'}[lang]

def translate(text_id):
    try:
        return translations[text_id][lang_code]
    except KeyError:
        return translations[text_id]['en']  # Fallback to English if translation is missing

st.title(translate('title'))
st.write(translate('description'))

# Input form
with st.form(key='mva_calculator'):
    price_type = st.radio(translate('price_type_label'), (translate('price_inclusive_label'), translate('price_exclusive_label')))
    price = st.number_input(translate('price_label'), min_value=0.0, step=0.01, format="%.2f")

    vat_rates = {
        "Generell (25%)": 25.0,
        "Redusert (15%)": 15.0,
        "Redusert (12%)": 12.0,
        "Redusert (11.11%)": 11.11,
        "Redusert (6%)": 6.0
    }

    vat_rate_label = st.selectbox(translate('vat_rate_label'), list(vat_rates.keys()))
    vat_rate = vat_rates[vat_rate_label]

    submit_button = st.form_submit_button(label=translate('calculate_button'))

if submit_button:
    if price_type == translate('price_inclusive_label'):
        result = calculate_vat(price, vat_rate, inclusive=True)
        st.success(f"{translate('price_exclusive_label')} {result:.2f} NOK")
    else:
        result = calculate_vat(price, vat_rate, inclusive=False)
        st.success(f"{translate('price_inclusive_label')} {result:.2f} NOK")

# Batch Upload and Processing
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df['Price Exclusive'] = df['Price'].apply(lambda x: calculate_vat(x, vat_rate, inclusive=True))
    df['Price Inclusive'] = df['Price'].apply(lambda x: calculate_vat(x, vat_rate, inclusive=False))
    st.write(df)
    df.to_excel("VAT_Calculations.xlsx", index=False)
    st.download_button("Download Results", data="VAT_Calculations.xlsx", file_name="VAT_Calculations.xlsx")

# Data Visualization
if submit_button:
    st.write("## VAT Calculation Breakdown")
    fig, ax = plt.subplots()
    ax.bar(['Original Price', 'Price Exclusive', 'Price Inclusive'], [price, result, calculate_vat(price, vat_rate, inclusive=False) if price_type == translate('price_exclusive_label') else calculate_vat(price, vat_rate, inclusive=True)])
    st.pyplot(fig)

# Sidebar Information
st.sidebar.title(translate('sidebar_title'))
st.sidebar.info(translate('sidebar_info'))

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



