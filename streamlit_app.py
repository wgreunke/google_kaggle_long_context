import streamlit as st
import pandas as pd

#This is the function that calls the llm and generates the code.
def generate_code_from_video(video_file):
    llm_response="test"
    return llm_response



#********************* UI ***************************
st.title("Video to Code")

st.header("Stop pressing pause to copy code from video!")

st.markdown("This project was part of the Google Gemini Long Context [Kaggle Competition](https://www.kaggle.com/competitions/gemini-long-context/overview)", unsafe_allow_html=True)

left_co,middle_co, cent_co,last_co = st.columns(4)
with middle_co:
    st.image("vtc.png",width=300)

st.markdown("Upload an mp4 tutorial video then press generate code.  Google long-context will do the rest!" )

#*********** Video File upload **************
uploaded_file=None
uploaded_video=st.file_uploader("Choose a video",type=["mp4"])
if uploaded_video is not None:
    st.write("Video is uploaded")
    #st.video(uploaded_video)


#Use columns to control the size of the video
col1,col2,col3=st.columns([3,3,3])

with col2:
    
    #Show the video player
    if uploaded_video is not None:
        st.video(uploaded_video)

        if st.button("Generate Code"):
            st.write(generate_code_from_video(uploaded_video))
        





st.markdown("Written by [Ward Greunke](https://www.linkedin.com/in/wgreunke/)", unsafe_allow_html=True) 
st.markdown("Thanks to ?????? for the starter notebook. [Kaggle Competition](https://www.kaggle.com/competitions/gemini-long-context/overview)", unsafe_allow_html=True)


