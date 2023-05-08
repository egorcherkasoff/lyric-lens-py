import streamlit as st
import os
from modules.api import API
from modules.lyrics import get_lyrics

api = API()

# app intro
st.title("Lyric Lens")

st.write("Lyric Lens is a tool for searching lyrics which uses Genius API.")

user_query = st.text_input(label="Search", placeholder="Search for any song or artist")
