import streamlit as st
from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian
import matplotlib.pyplot as plt

# Streamlit app
st.title("Unsharp Masking Demo")

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    img = img_as_float(io.imread(uploaded_file))

    # Gaussian blur
    gaussian_img = gaussian(img, sigma=2, mode='constant', cval=0.0)

    # Unsharp mask
    img2 = (img - gaussian_img) * 2.

    # Sharpened image
    img3 = img + img2

    # Display original image
    st.subheader("Original Image")
    st.image(img, caption='Original Image', use_column_width=True)

    # Display blurred image
    st.subheader("Blurred Image")
    st.image(gaussian_img, caption='Blurred Image', use_column_width=True)

    # Display sharpened image
    st.subheader("Sharpened Image (Original - Blurred)")
    st.image(img3, caption='Original - Blurred', use_column_width=True)

    # Display matplotlib plot (optional)
    st.pyplot(plt)
