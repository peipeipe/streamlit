import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


st.title('Streamlit 超入門')

st.write('Display Image')

if st.checkbox('Show Image'):
    img =Image.open('photo.png')
    st.image(img,caption='kaeru',use_column_width=True)

expander =st.expander('問い合わせ')
expander.write('aaaaaa')