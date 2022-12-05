#https://davidsiltroy-python-ai-project-strawberry-flowers-r-main-0pg6aq.streamlit.app/
import streamlit as st

st.header('Thomas More - Artificial Intelligence Project: Object detection')

st.write("Here is going to be an Epic/Awesome Object Detection program!")

body = st.container()
body.write("Coming soon.... (in Winter)")


# Include PIL, load_image before main()
from PIL import Image

def load_image(image_file):
	img = Image.open(image_file)
	return img

...

if choice == "Image":
		st.subheader("Image")
		image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

		if image_file is not None:

			  # To See details
			  file_details = {"filename":image_file.name, "filetype":image_file.type,
                              "filesize":image_file.size}
			#   st.write(file_details)

            #   # To View Uploaded Image
			#   st.image(load_image(image_file),width=250)