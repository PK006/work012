import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import pandas as pd

dt=pd.read_csv('./data/apple.csv')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/71e6e18c-2bab-40bd-9121-bd755b60a778/Ib8ewkFcIq.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

st.subheader("การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล")

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>กราฟแสดงข้อมูลแอปเปิ้ล</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

st.write('ผลรวม')
cl1,cl2,cl3,cl4.cl5,cl6,cl7=st.columns(7)
cl1.write(dt['Size'].sum())
cl2.write(dt['Weight'].sum())
cl3.write(dt['Sweetness'].sum())
cl4.write(dt['Crunchiness'].sum())
cl5.write(dt['Juiciness'].sum())
cl6.write(dt['Ripeness'].sum())
cl7.write(dt['Acidity'].sum())

st.write("กราฟแท่ง")
a=dt['Size'].sum()
b=dt['Weight'].sum()
c=dt['Sweetness'].sum()
d=dt['Crunchiness'].sum()
e=dt['Juiciness'].sum()
f=dt['Ripeness'].sum()
g=dt['Acidity'].sum()
dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["Size", "Weight", "Sweetness","Crunchiness","Juiciness","Ripeness","Acidity",])
st.bar_chart(cx)