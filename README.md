# Welcome to this repo!

## YouTube Playlist Length Calculator

- You just have to enter **playlist URL** or **URL of any video** in the playlist to calculate total length of playlist.

- This web app also shows the  playlist length in 1.25X,1.50X,1.75X & 2.00X settings.     

## This is a Flask app created to quickly check the total length of a YT playlist.
- This app uses YouTube Data API v3. 
- At first playlist ID is extracted from given URL.
- Then YouTube Data API is called with proper options stored in config.json.
- After getting individual video durations, all of them are added.
- Finally the total length is displayed using Jinja templating engine.

## Screenshots
<p float="left">
  <img src="https://github.com/omkarae/yt-playlist-length/blob/master/1.png" alt="UI" height=200px></img>
  <img src="https://github.com/omkarae/yt-playlist-length/blob/master/2.png" alt="Response" height=200px></img>
</p>


## Technologies/modules used - 
- Flask
- YouTube Data API v3
- Jinja
- isodate
- datetime
