import streamlit as st

# Configuration de l'appli
st.set_page_config(
    page_title="Mes Applis", 
    page_icon="📲",
    layout="centered"
)

# --- STYLE CSS FINAL ---
st.markdown("""
    <style>
    /* Centre le texte global de la page */
    .stApp {
        text-align: center;
    }

    /* Supprime les paddings des colonnes pour un alignement parfait */
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 auto !important;
    }

    /* Force TOUS les boutons (normaux et liens) à être identiques */
    div.stButton > button, div.stLinkButton > a {
        width: 100% !important;  /* Utilise toute la largeur de la colonne centrale */
        min-width: 250px !important; /* Taille minimum pour le confort */
        height: 70px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 10px 0px !important;
        text-decoration: none !important;
        transition: 0.3s;
    }

    /* Couleur rouge spécifique pour le bouton de confirmation */
    div.stLinkButton > a {
        background-color: #ff4b4b !important;
        color: white !important;
        border: none !important;
    }
    
    /* Effet au survol/clic */
    div.stButton > button:active, div.stLinkButton > a:active {
        transform: scale(0.98);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📲 Mon tableau de bord")
st.write("Sélectionnez l'application à ouvrir :")

# --- CENTRAGE VIA COLONNES ---
# On utilise une colonne centrale assez large pour le mobile
_, col_centrale, _ = st.columns([0.1, 0.8, 0.1])

with col_centrale:
    # --- BOUTON APPLI 1 ---
    url_cuisine = "https://mes-recettes-crevqstqc3xledupcnovx9.streamlit.app/"
    if st.button("🍳 Mes recettes"):
        st.link_button("Ouvrir Mes recettes ➔", url_cuisine)

    # Petit espace entre les deux blocs
    st.write("")

    # --- BOUTON APPLI 2 ---
    url_autre = "https://mes-poi-enbqgzwutukww3i7adjs2q.streamlit.app/"
    if st.button("📍 GéoCollect"):
        st.link_button("Ouvrir GéoCollect ➔", url_autre)

st.write("---")
st.caption("Centralisé par Streamlit")
