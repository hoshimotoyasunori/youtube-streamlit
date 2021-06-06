import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit.proto.Video_pb2 import Video


# タイトル
st.sidebar.title('Streamlit 入門')

st.sidebar.write('Interactive Widgets')


# チェックボックス
if st.sidebar.checkbox('show Image'):
    img = Image.open('data/tehon1.jpg')
    st.image(img,caption='tehon',use_column_width=True)

# テキストボックス
text = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味：',text

# スライダー
condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'コンディション：',condition


# video_file = open('12345678.mp4','rb')
# video_bytes = video_file.read()

# st.video(video_bytes)

