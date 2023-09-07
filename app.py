import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Website", page_icon="👾", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return  None
    return r.json()
lottie_c="https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"



with st.container():
    st.subheader("Hi, Iam Praneeth")
    st.title("A Data Science Enthusiast")
    st.write("[Checkout My Github>](https://github.com/Praneeth1981)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """
            - I am interested in persuing career in data science.
            - I have a solid foundation in Python, as well as experience with data visualization tools like Power BI, Excel, and Tableau.
            - Familiar with numpy
            """

        )
    with right_column:
        st_lottie(lottie_c, height=300, key="coding")
