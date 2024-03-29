import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/2c6019aa-3c40-41b7-a0c6-28d0ca625af1/hdJuoEJmoc.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")
st.subheader("การประยุกต์ใช้งาน Manchine Learning บนเว็บ")
st.subheader("by นายภูรินทร์ ขวัญจิรา")
st.subheader("สาขาวิทยาการคอมพิวเตอร์")
st.subheader("คณะวิทยาศาสตร์และเทคโนโลยี")
st.subheader("มหาวิทยาลัยราชภัฏนครปฐม")

st.page_link("home.py", label="หน้าแรก", icon="🏠")

st.page_link("pages/1⏲️Statistic.py", label="การนำเสนอข้อมูลด้วยสถิติ-", icon="1︎⃣ ")
st.page_link("pages/2📊Chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล", icon="2︎⃣ ", disabled=False)
st.page_link("pages/3🧐KNNClassify.py", label="การจำแนกข้อมูลด้วยเทคนิค Knn", icon="3︎⃣ ", disabled=False)
st.page_link("pages/4🌳DecisionTreeClassify.py", label="การจำแนกข้อมูลด้วยเทคนิค DecisionTree", icon="4︎⃣ ", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")