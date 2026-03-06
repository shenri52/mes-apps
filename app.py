import streamlit as st

# Configuration de l'appli qui sert de menu
st.set_page_config(
    page_title="Mes Applis", 
    page_icon="📲",
    layout="centered"
)

# Style personnalisé pour avoir de gros boutons bien visibles sur mobile
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 100px;
        font-size: 24px !important;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Mon Tableau de Bord")
st.write("Sélectionnez l'application à ouvrir :")

# --- BOUTON APPLI 1 ---
# Remplace le lien par ton URL réelle
url_cuisine = "https://mes-recettes-crevqstqc3xledupcnovx9.streamlit.app/"
if st.button("🍳 Gestion Cuisine"):
    st.link_button("Confirmer l'ouverture", url_cuisine)
    st.info("Cliquez sur le bouton de confirmation ci-dessus.")

# --- BOUTON APPLI 2 ---
# Remplace le lien par ton URL réelle
url_autre = "https://mes-poi-enbqgzwutukww3i7adjs2q.streamlit.app/"
if st.button("📊 Statistiques / Autre"):
    st.link_button("Confirmer l'ouverture", url_autre)
    st.info("Cliquez sur le bouton de confirmation ci-dessus.")

st.caption("Centralisé par Streamlit")a
