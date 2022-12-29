import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Charanvir Singh")
    content = """Hi, my name is Charanvir Singh. I am a full stack developer who loves to learn new languages and 
    frameworks and create and work on projects. This portfolio is to showcase the Python projects that I have 
    created. I will be adding new projects regularly as I work on new projects and learn additional frameworks and 
    libraries associated with Python. My passion lies with artificial intelligence and machine learning and how they 
    relate to the medical field. I hope to start building models and programs that can relate these two fields that I 
    enjoy."""
    st.info(content)
