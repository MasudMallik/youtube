import streamlit as st
from pytubefix import YouTube
st.title("Download high quelity audio from any youtube link")
def download_audio(link="",file_name=""):
    if link=="":
        st.warning("please paste the link")
    else:
      with st.status("please wait...it is processing...."):
        try:
            yt=YouTube(link)
            audio=yt.streams.filter(only_audio=True).first()
            if file_name=="":
                st.warning("please enter the file name")
            else:
                down=audio.download(f"{file_name}.mp3")
                st.success("audio succesfully downloaded....")
        except Exception as e:
            st.warning(e)
    st.audio(down,format="audio/mpeg")

url=st.text_input("enter your url here")
file_name=st.text_input("please enter the audio name")
if st.button("submit",type="primary"):
    download_audio(url,file_name)
