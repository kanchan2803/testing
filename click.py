import cv2
import numpy as np
import streamlit as st
import main
import cap
from PIL import Image

#ui
st.title("Text Recognition from Image")

#for camera input
start_camera = st.button("Start Camera", key="start_camera")
cam_placeholder = st.empty()

if start_camera:
    img_loc = cap.capture_image()
    processed_image, text = main.extract_text(img_loc)
    cam_placeholder.image(processed_image, caption='Processed Image')
    st.write("Extracted Text: ", text)


#add to upload img from user
uploaded_file = st.file_uploader("Upload image:",type=["jpg","png","jpeg"]) 

frame_placeholder = st.empty()

if st.button("Clear Selection"):
    st.rerun
    # st.experimental_rerun()


if uploaded_file is not None:
    # Use PIL to open the uploaded image
    bytes_data = uploaded_file.read()

    # Convert bytes to a NumPy array
    np_array = np.frombuffer(bytes_data, np.uint8)

    # Decode the NumPy array as a OpenCV image (BGR color space)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Save the image to a specified location
    temp_image_path="captured_image.jpg"
    cv2.imwrite(temp_image_path,image)
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Image')
    st.write("Image saved successfully.")
    processed_image, text = main.extract_text(temp_image_path)
    frame_placeholder.image(processed_image, caption='Processed Image')
    st.write("Extracted Text:", text)

