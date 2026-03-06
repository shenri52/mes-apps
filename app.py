import streamlit as st

# Configuration de l'appli
st.set_page_config(
    page_title="Mes Applis", 
    page_icon="📲",
    layout="centered"
)

# Style personnalisé pour centrer et égaliser les boutons
st.markdown("""
    <style>
    /* Centre le titre et le texte */
    .stApp {
        text-align: center;
    }
    
    /* Force TOUS les boutons à être identiques */
    div.stButton > button, div.stLinkButton > a {
        width: 100% !important;
        height: 80px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        margin-bottom: 10px !important;
        text-decoration: none !important;
    }
    
    /* Couleur spécifique pour le bouton de confirmation */
    div.stLinkButton > a {
        background-color: #ff4b4b !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Mon Tableau de Bord")
st.write("Sélectionnez l'application à ouvrir :")

# --- BOUTON APPLI 1 ---
url_cuisine = "https://mes-recettes-crevqstqc3xledupcnovx9.streamlit.app/"
if st.button("🍳 Gestion Cuisine"):
    st.link_button("Ouvrir Cuisine ➔", url_cuisine)

st.divider() # Petite ligne de séparation

# --- BOUTON APPLI 2 ---
url_autre = "https://mes-poi-enbqgzwutukww3i7adjs2q.streamlit.app/"
if st.button("📊 Statistiques / Autre"):
    st.link_button("Ouvrir Stats ➔", url_autre)

st.caption("Centralisé par Streamlit")
