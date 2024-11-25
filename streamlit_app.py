import streamlit as st
import time
import google.generativeai as genai
api_key=st.secrets["api_key"]

#Need to switch to an older version of python (3.10) to make the Google generativeai library work. 
#https://github.com/google-gemini/generative-ai-python/issues/156
#Managed in streamlit settings


#************** Main Function *****************
def get_code_from_video(raw_video,api_key):
  genai.configure(api_key=api_key)

  # ******** Helper Functions ******************
  def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini.

    See https://ai.google.dev/gemini-api/docs/prompting_with_media
    """
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

  def wait_for_files_active(files):
    """Waits for the given files to be active.

    Some files uploaded to the Gemini API need to be processed before they can be
    used as prompt inputs. The status can be seen by querying the file's "state"
    field.

    This implementation uses a simple blocking polling loop. Production code
    should probably employ a more sophisticated approach.
    """
    print("Waiting for file processing...")
    for name in (file.name for file in files):
      file = genai.get_file(name)
      while file.state.name == "PROCESSING":
        print(".", end="", flush=True)
        time.sleep(10)
        file = genai.get_file(name)
      if file.state.name != "ACTIVE":
        raise Exception(f"File {file.name} failed to process")
    print("...all files ready")
    print()


  # Create the model
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
  )


  #Start the chat
  files = [upload_to_gemini(raw_video, mime_type="video/mp4"),]
  wait_for_files_active(files)
  #st.write(f"Files: {files}")
  chat_session = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          files[0],
        ],
      }
    ]
  )

  response = chat_session.send_message("Please output the code that is shown in this video")
  return response.text




#********************* UI ***************************
st.title("Video to Code")

st.header("Stop pausing video to copy code!")

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
  #************ Call Main Function ***********
  st.write("Please wait, video is being processed by Gemini")
  code_output=get_code_from_video(uploaded_video,api_key)
  st.write(code_output)
        
st.divider() 
st.markdown("Written by [Ward Greunke](https://www.linkedin.com/in/wgreunke/)", unsafe_allow_html=True) 
st.markdown("Based on the starter notebook by [Paul Mooney](https://www.kaggle.com/code/paultimothymooney/how-to-upload-large-files-to-gemini-1-5)", unsafe_allow_html=True)








  
