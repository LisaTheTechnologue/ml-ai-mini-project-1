import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

st.title("Phân đoạn ảnh với KMeans Clustering")

# Nhập URL ảnh
url = st.text_input("Nhập URL hình ảnh:")

# Slider chọn số cụm k
k = st.slider("Số cụm (k) cho KMeans:", min_value=2, max_value=10, value=4)

if url:
    try:
        # Tải hình từ URL
        response = requests.get(url)
        image = Image.open(BytesIO(response.content)).convert("RGB")

        st.image(image, caption="Ảnh gốc", use_container_width=True)


        # Chuẩn bị dữ liệu cho KMeans
        img_np = np.array(image)
        h, w, c = img_np.shape
        img_flat = img_np.reshape(-1, 3)

        # Phân đoạn ảnh
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(img_flat)
        centers = np.uint8(kmeans.cluster_centers_)

        segmented_img = centers[labels].reshape(h, w, 3)

        st.image(segmented_img, caption=f"Ảnh sau phân đoạn với k={k}", use_container_width=True)

    except Exception as e:
        st.error(f"Không thể tải hoặc xử lý ảnh: {e}")
