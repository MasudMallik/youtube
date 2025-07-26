import streamlit as st
audio=st.Page(
    page="functions/audio_download.py",
    icon="🎵",
    title="download audio",
    default=True
)
vid=st.Page(
    page="functions/video_download.py",
    icon="🎵",
    title="download video",
)
pg=st.navigation([audio,vid])
pg.run()