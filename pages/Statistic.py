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

st.subheader("การนำเสนอข้อมูลด้วยสถิติ")
st.write(dt.head(50))
st.write('ผลรวม')
cl1,cl2,cl3,cl4.cl5,cl6,cl7=st.columns(7)
cl1.write(dt['Size'].sum())
cl2.write(dt['Weight'].sum())
cl3.write(dt['Sweetness'].sum())
cl4.write(dt['Crunchiness'].sum())
cl5.write(dt['Juiciness'].sum())
cl6.write(dt['Ripeness'].sum())
cl7.write(dt['Acidity'].sum())