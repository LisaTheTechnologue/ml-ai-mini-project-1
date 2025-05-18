import streamlit as st
import pandas as pd
import numpy as np

st.title("Ứng dụng Streamlit đầu tiên của tôi")

st.write("Chào mừng đến với ứng dụng Streamlit đơn giản này!")

if st.button("Tạo dữ liệu ngẫu nhiên"):
    data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=['x', 'y', 'z']
    )
    st.line_chart(data)
