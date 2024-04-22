from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import requests
import os
import dotenv

dotenv.load_dotenv()
CLIENT_ID = os.getenv("CILENT_ID")
SECRET = os.getenv("SECRET")
USER_ID = os.getenv('USER')
scope = "playlist-modify-private"
BILLBOARD_URL_BASE = "https://www.billboard.com/charts/hot-100/"
ITEMS_TO_REMOVE = ['Songwriter(s):', 'Producer(s):', 'Imprint/Promotion Label:',
                   "Lizard Eliminated After 'Sink or Swim' Experience on 'The Masked Singer': 'I'm Not Used to Losing'",
                   "Gains in Weekly Performance", 'Additional Awards']


def search_for_track(track_name, year):
    results = sp.search(q=f'track:{track_name} year:{year}', limit=1, type='track')
    try:
        uri = results['tracks']['items'][0]['uri']
    except IndexError:
        print(f"Cannot find {track_name} in Spotify. Skipping...")
        return 'N/A'
    return uri


def remove_items(item_list, keyword):
    c = item_list.count(keyword)
    for i in range(c):
        item_list.remove(keyword)
    return item_list


# Set up connection to Spotify Client
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
oauth = spotipy.oauth2.SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=SECRET,
    redirect_uri="http://example.com",
    scope=scope,
)

# Prompt User
user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = user_input.split("-")[0]

# Web scrape Billboard's Top 100 for that specified year
url = f"{BILLBOARD_URL_BASE}{user_input}/"
response = requests.get(url=url)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
song_names_spans = soup.find_all("h3", id='title-of-a-story', class_="c-title")
song_title_list = [song.getText().strip() for song in song_names_spans]

# # Get rid of the repeated title text from the html
for item in ITEMS_TO_REMOVE:
    song_title_list = remove_items(song_title_list, item)

# Only get the top 100 songs, remove all extraneous entries.
song_title_list = song_title_list[:100]
song_uris = []
for song in song_title_list:
    song_uri = search_for_track(song, year)
    if song_uri == 'N/A':
        continue
    else:
        song_uris.append(song_uri)

# Create a new playlist based on the user's tokens. Then add songs to that playlist.
token = oauth.get_cached_token()
user_id = sp.current_user()['id']
playlist_name = f"{user_input} Billboard 100"
desc = f"A blast from the {user_input}, a spotify playlist created by a Bot based on Billboard's Top 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=desc)
playlist_id = playlist['id']
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
