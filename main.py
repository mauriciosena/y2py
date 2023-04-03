import streamlit as st
from pytube import YouTube
import downloader

#pages = {"_": }

URL = ""
thumb = "https://d1y2qj23ol72q6.cloudfront.net/2021/05/Python-Reddit-Banner-2.png"

st.set_page_config(layout="wide")
st.title("YouTube Downloader")
URL = st.text_input(label="Digite a URL do vídeo...")

col1, col2 = st.columns(2)

if URL != "":
    yt = YouTube(URL)
    with col1:
        thumb = yt.thumbnail_url
        st.image(thumb)
    with col2:
        st.title(yt.title)
        st.text("Descrição: " + str(yt.description))
        st.text("Data de publicação: " + str(yt.publish_date))
        format = st.selectbox(label="Formato", options=["MP3", "MP4"])
        baixar = st.button("Baixar")
        if baixar:
            downloader.downloader.download(yt, format)
else:
    st.image(thumb)

#demo_name = st.sidebar.selectbox("Choose a demo", pages)
