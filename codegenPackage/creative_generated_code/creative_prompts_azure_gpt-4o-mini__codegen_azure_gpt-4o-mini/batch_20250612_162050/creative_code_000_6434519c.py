"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farazhaidermusic.com
Prompt: Generate a Python script to fetch and play music from Faraz Haider's Spotify profile using the Spotify API.
Generated: DETERMINISTIC_6434519cd202b514
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import vlc

# Set up constants for Spotify API
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SCOPE = "user-library-read"

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE))

def fetch_tracks(artist_name):
    """
    Fetches the tracks from a specified artist's Spotify profile.

    Parameters:
    artist_name (str): The name of the artist to fetch tracks from.

    Returns:
    list: A list of track URIs if found, otherwise an empty list.
    """
    try:
        # Search for the artist
        results = sp.search(q=f'artist:{artist_name}', type='artist')
        artist = results['artists']['items']
        if not artist:
            print(f"No artist found with name: {artist_name}")
            return []

        # Get the artist's ID
        artist_id = artist[0]['id']

        # Fetch the artist's top tracks
        top_tracks = sp.artist_top_tracks(artist_id)['tracks']
        track_uris = [track['uri'] for track in top_tracks]

        if not track_uris:
            print(f"No tracks found for artist: {artist_name}")

        return track_uris

    except Exception as e:
        print(f"An error occurred while fetching tracks: {e}")
        return []

def play_music(track_uri):
    """
    Plays music for a given track URI using VLC.

    Parameters:
    track_uri (str): The URI of the track to play.
    """
    try:
        # Create a VLC media player instance
        player = vlc.MediaPlayer(track_uri)
        player.play()

        # Keep playing until the track is finished
        while player.is_playing():
            continue

    except Exception as e:
        print(f"An error occurred while trying to play the track: {e}")

def main():
    """
    Main function to execute the script.
    Fetches and plays music from Faraz Haider's Spotify profile.
    """
    artist_name = "Faraz Haider"

    # Fetch tracks from the artist
    track_uris = fetch_tracks(artist_name)

    if track_uris:
        print(f"Playing tracks for {artist_name}:")
        for track_uri in track_uris:
            play_music(track_uri)

if __name__ == "__main__":
    main()
```

Make sure to set the environment variables `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI` before running the script. This script requires the `spotipy` and `python-vlc` libraries, which can be installed via pip:

```bash
pip install spotipy python-vlc
```
