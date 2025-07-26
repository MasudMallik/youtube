import streamlit as st
from pytubefix import YouTube
from io import BytesIO

st.title("🎵 Download high quality audio from any YouTube link")

def download_audio(link="", file_name=""):
    if not link:
        st.warning("Please paste the YouTube link.")
        return

    if not file_name:
        st.warning("Please enter the file name.")
        return

    with st.status("Please wait... it is processing..."):
        try:
            yt = YouTube(link)
            audio = yt.streams.filter(only_audio=True).first()

            buffer = BytesIO()
            audio.stream_to_buffer(buffer)
            buffer.seek(0)

            st.success("Audio successfully accessed from YouTube!")

            # Play audio
            st.audio(buffer, format="audio/mpeg")

            # Download button
            st.download_button(
                label="Download Audio",
                data=buffer,
                file_name=f"{file_name}.mp3",
                mime="audio/mpeg"
            )

        except Exception as e:
            st.error(f"Error: {e}")

# UI
url = st.text_input("Enter your YouTube URL here")
file_name = st.text_input("Please enter the audio name")
if st.button("Submit", type="primary"):
    download_audio(url, file_name)
