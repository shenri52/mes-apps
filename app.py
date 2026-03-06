import streamlit as st

# Configuration de l'appli
st.set_page_config(
    page_title="Mes Applis", 
    page_icon="📲",
    layout="centered"
)

# --- STYLE CSS : FOND TRANSPARENT + BORDURE ROUGE ---
st.markdown("""
    <style>
    .stApp {
        text-align: center;
    }

    /* Style pour les boutons de lien transparents avec bordure */
    div.stLinkButton > a {
        width: 100% !important;
        min-width: 280px !important;
        height: 70px !important;
        
        /* Fond transparent */
        background-color: transparent !important; 
        
        /* Texte */
        color: #2AD624 !important;
        
        /* Bordure */
        border: 2px solid #2AD624 !important;
        
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 15px auto !important;
        text-decoration: none !important;
        transition: 0.3s !important;
    }
    /* Effet au survol (hover) et au clic (active) */
    div.stLinkButton > a:hover, div.stLinkButton > a:active {
        background-color: rgba(255, 75, 75, 0.2) !important;
        border-color: #ff4b4b !important;
        color: #2AD624 !important;
        transform: scale(1.02); /* Petit effet de zoom pour le retour tactile */
    }yle>
    """, unsafe_allow_html=True)

st.title("📲 Accès direct aux applications ")

# Centrage via colonne centrale
_, col_centrale, _ = st.columns([0.1, 0.8, 0.1])

with col_centrale:
    # LIENS DIRECTS (Un seul clic)
    st.link_button("🍳 Mes recettes", "https://mes-recettes-crevqstqc3xledupcnovx9.streamlit.app/")
    
    st.link_button("📍 GéoCollect", "https://mes-poi-enbqgzwutukww3i7adjs2q.streamlit.app/")
