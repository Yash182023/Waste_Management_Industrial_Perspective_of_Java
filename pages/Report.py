import streamlit as st
import os

style = """
<style>
    .main{
        background: rgb(233,195,2);
        background: linear-gradient(148deg, rgba(233,195,2,1) 0%, rgba(250,255,0,1) 37%, rgba(254,255,0,1) 64%, rgba(233,195,2,1) 100%);

    h1{
        color:#000000;
    }
    p{
        color:#000000;
    }
</style>

"""


st.markdown(style,unsafe_allow_html=True)

uploads = "C:/Users/sharm/OneDrive/Desktop/Waste_Management/uploads/"
# Function to save uploaded images
def save_uploaded_image(uploaded_image):
    with open(os.path.join("uploads", uploaded_image.name), "wb") as f:
        f.write(uploaded_image.getbuffer())
    return st.success("Image saved successfully!")

# Main content
st.title("Report Unmaintained Locations")

# Allow user to upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# If an image is uploaded, display it and save it to local machine
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    save_uploaded_image(uploaded_image)
