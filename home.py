import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/62cff6ba-1ea9-438c-8a00-aed954db87a5/w8RIuxisX4.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")
#st.subheader("การประยุกต์ใช้งาน Manchine Learning บนเว็บ")
html_1 = """
<div style="background-color:#92FAD3;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h3>การประยุกต์ใช้งาน Manchine Learning บนเว็บ<h3></center>
<h5>by นายภูรินทร์ ขวัญจิรา</h5>
<h5>สาขาวิทยาการคอมพิวเตอร์</h5>
<h5>คณะวิทยาศาสตร์และเทคโนโลยี</h5>
<h5>มหาวิทยาลัยราชภัฏนครปฐม</h5>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")
#st.subheader("by นายภูรินทร์ ขวัญจิรา")
#st.subheader("สาขาวิทยาการคอมพิวเตอร์")
#st.subheader("คณะวิทยาศาสตร์และเทคโนโลยี")
#st.subheader("มหาวิทยาลัยราชภัฏนครปฐม")

st.page_link("home.py", label="หน้าแรก", icon="🏠")

st.page_link("pages/1⏲️Statistic.py", label="การนำเสนอข้อมูลด้วยสถิติ-", icon="1️⃣")
st.page_link("pages/2📊Chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล", icon="2️⃣", disabled=False)
st.page_link("pages/3🧐KNNClassify.py", label="การจำแนกข้อมูลด้วยเทคนิค K-nn", icon="3️⃣", disabled=False)
st.page_link("pages/4🌳DecisionTreeClassify.py", label="การจำแนกข้อมูลด้วยเทคนิค DecisionTree", icon="4️⃣", disabled=False)
st.page_link("pages/5📏NavivebayeClassify.py", label="การจำแนกข้อมูลด้วยเทคนิค NaiveBayes", icon="5️⃣", disabled=False)
st.page_link("pages/6📈RegressionPrediction.py", label="การจำแนกข้อมูลด้วยเทคนิค Regression", icon="6️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")