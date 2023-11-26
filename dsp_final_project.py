import streamlit as st
import numpy as np
from skimage import io, img_as_float
from skimage.filters import unsharp_mask, gaussian

def main():
    st.title("Unsharp Masking with Streamlit")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Read the image
        img = img_as_float(io.imread(uploaded_file))

        # Apply Gaussian blur
        gaussian_img = gaussian(img, sigma=2, mode='constant', cval=0.0)

        # Calculate unsharp mask
        img2 = (img - gaussian_img) * 2.

        # Combine original and unsharp mask
        img3 = img + img2

        # Clip the image values to be within [0.0, 1.0]
        img = np.clip(img, 0.0, 1.0)
        gaussian_img = np.clip(gaussian_img, 0.0, 1.0)
        img3 = np.clip(img3, 0.0, 1.0)

        # Display the images with a specified color map (you can adjust 'cmap' as needed)
        st.image([img, gaussian_img, img3], caption=['Original', 'Blurred', 'Original - Blurred'],
                 width=300, use_column_width=True, cmap='viridis')

if __name__ == "__main__":
    main()
