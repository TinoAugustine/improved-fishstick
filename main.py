import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/tino.png")

with col2:
    st.title("Tino Augustine")
    content = """
        Hi, I am Tino Augustine an experienced Hotel Software Analyst with over 15 years in software and property management sectors. Currently based in Melbourne, Australia, he focuses on business analysis, Agile methodologies, and system functionalities for hotel, residential property management, and student housing software.
        
        In addition to his robust career, Tino is actively learning Python to enhance his technical skill set. This new proficiency will augment his capabilities in developing XML-based modules, creating custom reports, and conducting root cause assessments. His commitment to continuous learning exemplifies his dedication to staying at the forefront of technological advancements in his field.
        """
    st.info(content)

content2 = """
Below you can find some of the apps I have build using Python. Please feel free to contact me!

"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

