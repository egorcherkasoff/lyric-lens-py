import streamlit as st
from modules.api import API
from modules.lyrics import get_lyrics


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

    if open_card:
        # st.write(f"card opened!!! {song['id']}")
        pass
    st.divider()


api = API()

# app intro
st.title("Lyric Lens")

st.write("Lyric Lens is a tool for searching lyrics which uses Genius API.")

user_query = st.text_input(label="Search", placeholder="Search for any song or artist")

if user_query:
    songs = api.search(user_query)

    for song in songs:
        render_card(song)
