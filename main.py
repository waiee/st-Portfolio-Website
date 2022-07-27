import streamlit as st

# Text title
st.title("Testing Streamlit")

#Header/subHeader
st.header("This is header")
st.subheader("This is a subheader")

#Text
st.text("Hello world")

#Markdown
st.markdown("### This is a markdown")

#Error/colourful text
st.success("Successful!")
#information
st.info("Information")
#warning
st.warning("This is a warning.")
#error
st.error("This is a n error!")
#exception
st.exception("NameError(name three not defined)")

#Get help info about python
st.help(range)

#writing text
st.write("Text with write")
st.write(range(10))

#Images
from PIL import Image
img = Image.open("IMG_4825.jpeg")
st.image(img, width=300, caption="Inilah muka saya")

#Videos
vid_file = open("video.mp4","rb").read()
# vid_bytes = vid_file.read()
st.video(vid_file)

# Audio
# audio_file = open("","rb").read()
# st.audio(audio_file,format='audio/mp3')

#Widget
#Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

#Radio Buttons
status = st.radio("What is your status",("Active", "Inactive"))

if status == 'Active':
    st.success("You are Active!")
else:
    st.warning("You are inactive.")

#selectBox
occupation = st.selectbox("Your Occupation", ["Programmer", "Doctor", "Pilot"])
st.write("You selected this option: ", occupation)
#Multiselect
location = st.multiselect("Where do you work?",("London", "New York", "Kelantan", "Keyel"))
