import streamlit as st

# Configuration de l'appli
st.set_page_config(
    page_title="Mes Applis", 
    page_icon="📲",
    layout="centered"
)

# --- STYLE CSS AJUSTÉ ---
st.markdown("""
    <style>
    /* Centre le texte global */
    .stApp {
        text-align: center;
    }
    
    /* Force les boutons à prendre toute la largeur de leur colonne */
    div.stButton > button, div.stLinkButton > a {
        width: 100% !important;
        height: 70px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
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

# --- UTILISATION DE COLONNES POUR CENTRER ---
# On crée 3 colonnes : vide (15%), bouton (70%), vide (15%)
# Cela force le contenu au milieu exact de l'écran
col_vide1, col_centrale, col_vide2 = st.columns([0.15, 0.7, 0.15])

with col_centrale:
    # --- BOUTON APPLI 1 ---
    url_cuisine = "https://mes-recettes-crevqstqc3xledupcnovx9.streamlit.app/"
    if st.button("🍳 Mes recettes"):
        st.link_button("Ouvrir Mes recettes ➔", url_cuisine)

    st.write("---") 

    # --- BOUTON APPLI 2 ---
    url_autre = "https://mes-poi-enbqgzwutukww3i7adjs2q.streamlit.app/"
    if st.button("📍  GéoCollect"):
        st.link_button("Ouvrir GéoCollect ➔", url_autre)
