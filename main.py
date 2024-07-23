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

# Ensure openpyxl is imported
try:
    import openpyxl
except ImportError:
    st.error("Please install the openpyxl library.")

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
    },
    'file_structure_info': {
        'en': """
            ### Excel File Structure
            The Excel file should have the following columns:
            - **Price**: The price values you want to process (required).
            - Any other columns can be present but won't affect calculations.
            Example:
            | Price | Product Name | Category  |
            |-------|--------------|-----------|
            | 100.00| Widget A     | Category 1|
            | 200.50| Widget B     | Category 2|
            | 150.75| Widget C     | Category 1|
        """,
        'no': """
            ### Excel-filstruktur
            Excel-filen skal ha følgende kolonner:
            - **Pris**: Prisverdiene du vil behandle (påkrevd).
            - Eventuelle andre kolonner kan være til stede, men påvirker ikke beregningene.
            Eksempel:
            | Pris   | Produktnavn  | Kategori   |
            |--------|--------------|------------|
            | 100.00 | Widget A     | Kategori 1 |
            | 200.50 | Widget B     | Kategori 2 |
            | 150.75 | Widget C     | Kategori 1 |
        """,
        'es': """
            ### Estructura del archivo Excel
            El archivo Excel debe tener las siguientes columnas:
            - **Precio**: Los valores de precio que desea procesar (requerido).
            - Cualquier otra columna puede estar presente pero no afectará los cálculos.
            Ejemplo:
            | Precio | Nombre del producto | Categoría  |
            |--------|---------------------|------------|
            | 100.00 | Widget A            | Categoría 1|
            | 200.50 | Widget B            | Categoría 2|
            | 150.75 | Widget C            | Categoría 1|
        """,
        'fr': """
            ### Structure du fichier Excel
            Le fichier Excel doit avoir les colonnes suivantes :
            - **Prix** : Les valeurs de prix que vous souhaitez traiter (requis).
            - Toutes les autres colonnes peuvent être présentes mais n'affecteront pas les calculs.
            Exemple :
            | Prix   | Nom du produit | Catégorie   |
            |--------|----------------|-------------|
            | 100.00 | Widget A       | Catégorie 1 |
            | 200.50 | Widget B       | Catégorie 2 |
            | 150.75 | Widget C       | Catégorie 1 |
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
    try:
        df = pd.read_excel(uploaded_file)
        if 'Price' not in df.columns:
            st.error("The uploaded file does not contain a 'Price' column.")
        else:
            df['Price Exclusive'] = df['Price'].apply(lambda x: calculate_vat(x, vat_rate, inclusive=True))
            df['Price Inclusive'] = df['Price'].apply(lambda x: calculate_vat(x, vat_rate, inclusive=False))
            
            # Editable DataFrame
            st.write("### Editable DataFrame")
            edited_df = st.data_editor(df, use_container_width=True)
            
            # Save the result to an Excel file
            result_file = "VAT_Calculations.xlsx"
            edited_df.to_excel(result_file, index=False)
            with open(result_file, "rb") as file:
                st.download_button(label="Download Updated Results", data=file, file_name=result_file)
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")

# Sidebar Information
st.sidebar.title(translate('sidebar_title'))
st.sidebar.info(translate('sidebar_info'))
st.sidebar.write(translate('file_structure_info'))

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

   





