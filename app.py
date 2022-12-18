from pathlib import Path
import streamlit as st
from PIL import Image
import base64

# ----- path settings -----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "JohnsonPaku-Resume.pdf"
profile_pic = current_dir / "assets" / "profile_pic.jpg"

# ------ general settings ------
PAGE_TITLE = "Digital CV | Johnson Paku"
PAGE_ICON = ":computer:"
NAME = "Johnson Paku"
JOB_TITLE = "Data Analyst and AI Engineer"
EMAIL = "j.r.paku@hotmail.co.nz"
PHONE = "+64 22 587 3767"
ADDRESS = "Auckland, New Zealand"
SOCIAL_MEDIA = {
    'LINKEDIN': "https://www.linkedin.com/in/johnson-paku-22bb54232/",
    "GIT_HUB": "https://github.com/Jpaku93?tab=repositories"
}

PROJECTS = {
    "DASHBOARD FOR COVID-19",
    "PREDICTING THE PRICE OF A HOUSE",
    "PREDICTING THE PRICE OF A STOCK",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide" )

# ------ LOAD CSS, PDF & PROFILE PIC ------
with open(css_file, "r") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
with open(resume_file, "rb") as f:
    resume = f.read()
    
profile_pic = Image.open(profile_pic)

# ------ HEROSECTION------
col1, col2 =  st.beta_columns([1, 3])
with col1:
    st.image(profile_pic, width = 250)

with col2:
    st.title(NAME)
    st.markdown(f"**{JOB_TITLE}**")
    if st.button(label = "📝Download Resume"):
        # download bytes file
        b64 = base64.b64encode(resume).decode()
        # download link
        href = f'<a href="data:file/pdf;base64,{b64}" download="JohnsonPaku-Resume.pdf">Download Resume</a>'
        # download
        st.markdown(href, unsafe_allow_html=True)
    

    # ------ Details ------
    st.markdown(f"📧**{EMAIL}**")
    st.markdown(f"📱**{PHONE}**")
    st.markdown(f"📫**{ADDRESS}**")
    
    st.markdown(f"[LinkedIn]({SOCIAL_MEDIA['LINKEDIN']}) | [GitHub]({SOCIAL_MEDIA['GIT_HUB']})")

            
# ------ EXPERIENCE & QUALIFICATIONS ------
st.write("---")
st.subheader("Experience & Qualifications")
st.write("""
    - ✔️** (2020 - 2022) Bachelor of Software Engineering, AI** - Media Design School, Auckland, New Zealand
    - ✔️Experience with data analysis and machine learning
    - ✔️Experience with data visualization and dashboarding
    - ✔️Experience with data engineering and data pipelines
    - ✔️Excellent communication skills and team player
""")

# ------ TECHNICAL SKILLS ------
st.write("---")
st.subheader("Technical Skills")
st.write("""   
    - 👩‍💻 **Programming:** Python(Scikit-learn, Tensorflow, Keras, Pandas), C++(UnrealEngine, OpenGL), C#, SQL 
    - 📊 **Visualization:** Streamlit, Power BI, Seaborn, Plotly
    - 📚 **Modeling:** Linear Regression, Logistic Regression, KNN, Decision Trees, Random Forest, SVM, Naive Bayes, K-Means, PCA, NLP, Deep Learning 
    - 🗃️ **Data engineering:** Azure, SSMS, MySQL
    - 🗨️󠁄󠁄 **Languages:** Fluent in English 
""")
            