import streamlit as st
import pandas as pd


# Add custom CSS
st.markdown(
    """
    <style>
    .button {
        display: inline-block;
        margin: 2px; /* Reduce spacing between buttons */
        background-color: transparent; /* Remove button background */
        border: none; /* Remove border */
        color: blue; /* Set text color to blue */
        font-size: 16px; /* Adjust text size if needed */
        cursor: pointer; /* Make it look clickable */
    }
    .button:hover {
        text-decoration: underline; /* Add hover effect */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Code from Video")

st.write("Stop pressing pause to copy code from video!")


url="www.yahoo.com"
st.markdown("This project was part of the Google Gemini Long Context [Kaggle Competition](https://www.kaggle.com/competitions/gemini-long-context/overview)", unsafe_allow_html=True)

videos_list=[
    {"Title":"First Video","URL":"https://www.youtube.com/shorts/N6p3c-CH8ZI","ID":1},
    {"Title":"Second Video","URL":"https://www.youtube.com/shorts/lUBPD2bWodA","ID":2}
]

video_df=pd.DataFrame(videos_list)

current_id=""

st.write("Choose a video to extract code code:")
#Show a list of videos
for video in videos_list:
    if st.button(video["Title"],):
        current_id=video["ID"]
    #st.write(video["Title"])
    #st.write(video["URL"])

#Given the id grab the row for the video that has the data
video_row=video_df[video_df["ID"]==current_id]
st.write(current_id)

# ************* File Uploader ****************

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

#*********** Text File upload **************
uploaded_file=None
uploaded_video=st.file_uploader("Choose a video",type=["mp4"])
if uploaded_video is not None:
    st.write("Video is uploaded")
    #st.video(uploaded_video)






col1,col2,col3=st.columns([3,3,3])



with col2:
    
    #Show the video player
    if uploaded_video is not None:
        st.video(uploaded_video)

        st.button("Generate Code")




