import streamlit as st

# Configuration de l'appli
st.set_page_config(
    page_title="Mes Applis", 
    page_icon="📲",
    layout="centered"
)

# --- STYLE CSS POUR BOUTONS UNIQUES ET IDENTIQUES ---
st.markdown("""
    <style>
    .stApp {
        text-align: center;
    }

    /* On cible directement le lien pour qu'il ressemble à un gros bouton */
    div.stLinkButton > a {
        width: 100% !important;
        min-width: 280px !important;
        height: 80px !important;
        background-color: #4CAF50 !important; /* Vert pour le premier */
        color: white !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 15px auto !important;
        text-decoration: none !important;
        border: none !important;
    }

    /* Couleur différente pour le deuxième bouton pour les différencier */
    div.stLinkButton:nth-of-type(2) > a {
        background-color: #2196F3 !important; /* Bleu pour le second */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📲 Mon tableau de bord")
st.write("Cliquez pour ouvrir l'appli :")

# On utilise une colonne pour bien centrer sur mobile
_, col_centrale, _ = st.columns([0.1, 0.8, 0.1])

with col_centrale:
    # UN SEUL BOUTON PAR APPLI - CLIC DIRECT
    st.link_button("🍳 Mes recettes", "https://mes-recettes-crevqstqc3xledupcnovx9.streamlit.app/")
    
    st.link_button("📍 GéoCollect", "https://mes-poi-enbqgzwutukww3i7adjs2q.streamlit.app/")
