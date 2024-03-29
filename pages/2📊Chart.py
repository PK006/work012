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

lottie_url_hello = "https://lottie.host/e9730a83-d346-4087-b0d7-98b8bf0b467a/qBSW3J4U2g.json"
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

cl1,cl2, cl3 ,cl4 =st.columns(4)
cl1.write(dt['Size'].sum())
cl2.write(dt['Weight'].sum())
cl3.write(dt['Sweetness'].sum())
cl4.write(dt['Crunchiness'].sum())


st.write("กราฟแท่ง")
a=dt['Size'].sum()
b=dt['Weight'].sum()
c=dt['Sweetness'].sum()
d=dt['Crunchiness'].sum()

dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["Size", "Weight", "Sweetness","Crunchiness",])
st.bar_chart(cx)

st.write('ค่าเฉลี่ย')
cl11,cl12,cl13,cl14=st.columns(4)
cl11.write(dt['Size'].mean())
cl12.write(dt['Weight'].mean())
cl13.write(dt['Sweetness'].mean())
cl14.write(dt['Crunchiness'].mean())

st.write("Area_Chart")
a=dt['Size'].mean()
b=dt['Weight'].mean()
c=dt['Sweetness'].mean()
d=dt['Crunchiness'].mean()
dxt=[a,b,c,d]
cxx=pd.DataFrame(dxt,index=["Size", "Weight", "Sweetness","Crunchiness"])
st.area_chart(cxx)

st.write('ค่าน้อยที่สุด')
cl31,cl32,cl33,cl34=st.columns(4)
cl31.write(dt['Size'].min())
cl32.write(dt['Weight'].min())
cl33.write(dt['Sweetness'].min())
cl34.write(dt['Crunchiness'].min())

st.write("Line_Chart")
cc=[3,8,1,10]
st.line_chart(cc)