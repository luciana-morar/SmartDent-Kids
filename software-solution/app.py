import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="SmartDent-Kids", layout="wide")

logo_col, title_col = st.columns([1, 10])
with logo_col:
    st.image("software-solution/tooth.png", width=70)


with title_col:
    st.title("SmartDent-Kids")
    st.markdown("> **Platformă AI pentru Analiza Radiografiilor Panoramice Pediatrice**")

st.divider()

uploaded_file = st.file_uploader("Încărcați o radiografie panoramică (OPT)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Radiografia încărcată")
        st.image(image, width="stretch")

    with col2:
        st.subheader("Rezultate analiză")
        if st.button(" Analizează cu AI (simulat)"):
            st.markdown("**Rezultate detecție**")
            detection_df = pd.DataFrame({
                "Dinte": ["75", "84", "36"],
                "Localizare": ["Ocluzală", "Mezială", "Ocluzală"],
                "Leziune": ["Carie (CAR)", "Carie (CAR)", "Obturație (OBT)"],
                "Profunzime": ["Dentină profundă", "Smalț", "—"],
                "Implicare furcație": ["Nu", "Nu", "Nu"],
                "Distrucție coronară >50%": ["Nu", "Nu", "Nu"]
            })
            st.dataframe(detection_df, use_container_width=True)

            st.markdown("**Predicție prognostic**")
            pred_col1, pred_col2 = st.columns(2)
            pred_col1.metric("Probabilitate afectare pulpară (Dinte 75)", "82%")
            pred_col2.metric("Supraviețuire estimată (24 luni)", "75%")

else:
    st.info("Vă rugăm să încărcați o radiografie panoramică pentru a începe.")