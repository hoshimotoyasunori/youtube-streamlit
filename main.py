import streamlit as st
from PIL import Image
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!'
# カラム分け
left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ内容1をかく')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容2をかく')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容3をかく')

# チェックボックス
if st.checkbox('show Image'):
    img = Image.open('data/tehon1.jpg')
    st.image(img,caption='tehon',use_column_width=True)

# テキストボックス
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：',text

# スライダー
condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション：',condition


# video_file = open('12345678.mp4','rb')
# video_bytes = video_file.read()

# st.video(video_bytes)

