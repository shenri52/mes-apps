import streamlit as st

# Configuration de l'appli
st.set_page_config(
    page_title="Mes Applis", 
    page_icon="📲",
    layout="centered"
)

# --- STYLE CSS AVANCÉ POUR CENTRAGE TOTAL ---
st.markdown("""
    <style>
    /* 1. Centre tout le contenu de la colonne principale */
    .block-container {
        padding-top: 2rem;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* 2. Centre les titres et textes */
    .stMarkdown, .stTitle, .stCaption {
        width: 100%;
        text-align: center !important;
    }

    /* 3. Force les boutons à être centrés et de taille identique */
    /* On cible le container du bouton pour le centrer */
    div.stButton, div.stLinkButton {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    /* On définit la taille précise des boutons */
    div.stButton > button, div.stLinkButton > a {
        width: 280px !important; /* Largeur fixe pour qu'ils soient identiques */
        height: 70px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 10px auto !important;
        text-decoration: none !important;
    }

    /* Couleur pour le bouton de confirmation */
    div.stLinkButton > a {
        background-color: #ff4b4b !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Mon tableau de bord")
st.write("Sélectionnez l'application à ouvrir :")

# --- BOUTON APPLI 1 ---
url_cuisine = "https://mes-recettes-crevqstqc3xledupcnovx9.streamlit.app/"
if st.button("🍳 Gestion Cuisine"):
    st.link_button("Ouvrir Cuisine ➔", url_cuisine)

st.write("---") # Séparateur visuel propre

# --- BOUTON APPLI 2 ---
url_autre = "https://mes-poi-enbqgzwutukww3i7adjs2q.streamlit.app/"
if st.button("📊 Statistiques / Autre"):
    st.link_button("Ouvrir Stats ➔", url_autre)

st.caption("Centralisé par Streamlit")
