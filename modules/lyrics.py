from bs4 import BeautifulSoup
import requests


# get lyrics from genius site page
def get_lyrics(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    # get all elements with lyrics
    lyrics_html = soup.select("div[data-lyrics-container='true']")
    lyrics = ""
    for l in lyrics_html:
        lyrics += l.text
    return lyrics


if __name__ == "__main__":
    lyrics = get_lyrics("https://genius.com/Mikhail-krug-vladimir-central-lyrics")
    print(lyrics)
