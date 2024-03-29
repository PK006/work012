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

lottie_url_hello = "https://lottie.host/7a795140-5518-4922-9812-40fb19b8b5cf/0gvLlGun9I.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")

st.subheader("การนำเสนอข้อมูลด้วยสถิติ")
st.write(dt.head(50))
