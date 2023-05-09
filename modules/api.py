import requests
from modules.api_key import API_KEY


class API:
    BASE_URL = "https://api.genius.com/"
    API_KEY = API_KEY

    # search with genius api
    def search(self, query):
        # create query url
        query_url = f"{self.BASE_URL}search?q={query.replace(' ', '%20')}&access_token={self.API_KEY}"
        # request to api
        response = requests.get(query_url)
        response = response.json()
        # if no songs found, return message
        try:
            raw_songs = response["response"]["hits"]
        except KeyError:
            return f"HTTP: {response['meta']['status']}, Message: {response['meta']['message']}. Hint: You may forgot about creating .env file with API KEY provided"
        if raw_songs == []:
            return f"No results on your query"
        songs = []
        for song in raw_songs:
            id = song["result"]["id"]
            title = song["result"]["title"]
            song_image_url = song["result"]["song_art_image_thumbnail_url"]
            song_url = song["result"]["url"]
            primary_artist_name = song["result"]["primary_artist"]["name"]
            primary_artist_url = song["result"]["primary_artist"]["url"]
            # artist_image_url = song["result"]["primary_artist"]["image_url"]
            songs.append(
                {
                    "id": id,
                    "title": title,
                    "song_url": song_url,
                    "song_image": song_image_url,
                    "primary_artist_name": primary_artist_name,
                    "primary_artist_url": primary_artist_url,
                    # "artist_image": artist_image_url,
                }
            )
        return songs

    # maybe add this feature
    def get_artist(self):
        pass


if __name__ == "__main__":
    api = API()
    songs = api.search("Drake")
    print(songs)
