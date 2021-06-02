import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit.proto.Video_pb2 import Video


# タイトル
st.title('Streamlit 入門')

st.write('Interactive Widgets')


# チェックボックス
if st.checkbox('show Image'):
    img = Image.open('data/tehon1.jpg')
    st.image(img,caption='tehon',use_column_width=True)

# セレクトボックス
# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option,'です。'

# テキストボックス
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：',text

# スライダー
condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション：',condition


# video_file = open('12345678.mp4','rb')
# video_bytes = video_file.read()

# st.video(video_bytes)

