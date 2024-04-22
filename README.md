# Spotify-Top-100-Playlist-Generator

Given a specific date (YYYY-MM-DD Format), this application webscrapes from Billboard's Top 100 songs and creates a new playlist using the Spotify API.

## How to use
The application works from console, so after executing this program. You will be prompted with the following message:

![Image of the prompt shown in console](https://github.com/rinriukato/Spotify-Top-100-Playlist-Generator/blob/main/sample_images/Screenshot%202024-04-22%20153815.png)

The user will be prompted to input a date in the following format. **It will most likely crash if you do not input the correct format**

That inputted date will be used to webscrape from Billboard's Top 100 songs list, and the application will get every song name listed here.
In this example, I inputted *2023-11-04*, and this is the billboard website page that we will be scraping from.

![Billboard's Top 100](https://github.com/rinriukato/Spotify-Top-100-Playlist-Generator/blob/main/sample_images/Screenshot%202024-04-22%20153839.png)

Once the data is scraped and formatted, utilizing the Spotify API, get each song uri, then create a new playlist with each song in the list. If a song is not found in spotify, it will not be added. **NOTE: If it fails to find a song, it doesn't necessarily means that it's not on spotify, it could be that the song title was incorrectly formatted**.

![Example of the program finishing](https://github.com/rinriukato/Spotify-Top-100-Playlist-Generator/blob/main/sample_images/Screenshot%202024-04-22%20153853.png)

Once the application is finished, you can check out the playlist in your spotify account like so:
![Final Result of playlist](https://github.com/rinriukato/Spotify-Top-100-Playlist-Generator/blob/main/sample_images/Screenshot%202024-04-22%20153956.png)

## Important Notes
* Since this program utilizes important environmental variables, it won't work on your machine unless you set up authentication with spotify and go into the developer dashboard and get your own Cilent ID and Secret. [Once you've made an account, go here to the developer dashboard](https://developer.spotify.com/dashboard)
* OAuth2 is also required in order to access your account to create playlists and add songs to that playlist. 
