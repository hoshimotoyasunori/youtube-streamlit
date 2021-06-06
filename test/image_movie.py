import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit.proto.Video_pb2 import Video


# タイトル
st.title('Streamlit 入門')

st.write('Display Image')

img = Image.open('data/tehon1.jpg')

st.image(img,caption='tehon',use_column_width=True)


video_file = open('data/12345678.mp4','rb')
video_bytes = video_file.read()

st.video(video_bytes)

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )

# グラフ
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0),width=200,height=200)
# st.table(df.style.highlight_max(axis=0))
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )
# マップ
# st.map(df)