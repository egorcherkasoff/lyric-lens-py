import streamlit as st
from modules.api import API
from modules.lyrics import get_lyrics
import re


# renders song card on this page
def render_card(song):
    img_col, info_col, btn_col = st.columns(3)
    with img_col:
        st.image(song["song_image"])
    with info_col:
        st.text(song["title"])
        st.write(f"[{song['primary_artist_name']}]({song['primary_artist_url']})")
    with btn_col:
        open_card = st.button("Open Lyrics", key={song["id"]})

    # if user clicked "Open Lyrics" btn
    if open_card:
        # get lyrics from genius website
        lyrics = get_lyrics(song["song_url"])
        # regex to get "tags" from lyrics, such as [verse], [chorus], etc
        pattern = re.compile("\[(.*?)\]")
        tags = re.findall(pattern, lyrics)
        # split lyrics text by tags
        lyric_parts = re.split(pattern, lyrics)
        # check if part is tag to make it bold
        for part in lyric_parts:
            if part in tags:
                st.markdown(f"**{part}**")
            else:
                st.write(part)
    st.divider()


api = API()

# app intro
st.title("Lyric Lens")

st.write("Lyric Lens is a tool for searching lyrics which uses Genius API.")

user_query = st.text_input(label="Search", placeholder="Search for any song or artist")

if user_query:
    songs = api.search(user_query)

    # check if message was returned
    if type(songs) == str:
        st.warning(songs)
    else:
        for song in songs:
            render_card(song)
