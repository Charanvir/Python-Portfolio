import math

import streamlit as st
import pandas
project_data = pandas.read_csv("pythonportfoliodata.csv")
index_projects = math.ceil(len(project_data)/2)

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
    relate to the medical field. I hope to start building models and programs that can relate these two fields.
    """
    st.info(content)

content = """
Below are some projects that I have built in Python. Each project has a link to the GitHub repository in which the 
source code is located. Feel free to contact me to discuss some of my projects, or potential future projects you would 
like to work on together.
"""

projects_subheading = st.write(content)

col3, empty, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in project_data[:index_projects].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        image = row["image"]
        st.image(f"images/{image}", width=250)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in project_data[index_projects:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        image = row["image"]
        st.image(f"images/{image}", width=250)
        st.write(f"[Source Code]({row['url']})")
