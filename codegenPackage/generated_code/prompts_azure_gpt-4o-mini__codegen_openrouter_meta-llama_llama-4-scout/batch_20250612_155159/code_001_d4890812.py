"""
Generated Code Metadata:
========================
Original URL: https://rippie.xyz
Prompt: Write a Python script using the Spotify API to create a playlist featuring singles by Rippie Owens, such as "Morning (The Butter Remix)" and "Back Under The Covers."
Generated: DETERMINISTIC_d4890812e228e481
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
SPOTIPY_CLIENT_ID = 'your-spotify-client-id'
SPOTIPY_CLIENT_SECRET = 'your-spotify-client-secret'
SPOTIPY_REDIRECT_URI = 'your-spotify-redirect-uri'

# Set up Spotify API connection
scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

def get_artist_id(artist_name):
    """Get the ID of an artist"""
    try:
        results = sp.search(q=artist_name, type='artist')
        if results['artists']['items']:
            return results['artists']['items'][0]['id']
        else:
            return None
    except Exception as e:
        print(f"Error getting artist ID: {e}")
        return None

def get_track_id(artist_id, track_name):
    """Get the ID of a track by an artist"""
    try:
        results = sp.artist_related_artists(artist_id)
        for artist in results['artists']:
            if artist['name'] == artist_id:
                tracks = sp.artist_top_tracks(artist['id'])
                for track in tracks['tracks']:
                    if track['name'] == track_name:
                        return track['id']
        return None
    except Exception as e:
        print(f"Error getting track ID: {e}")
        return None

def create_playlist(playlist_name, tracks):
    """Create a playlist with the given tracks"""
    try:
        user_id = sp.me()['id']
        playlist = sp.user_playlist_create(user_id, playlist_name, public=True)
        sp.user_playlist_add_tracks(user_id, playlist['id'], tracks)
        print(f"Playlist '{playlist_name}' created with tracks: {tracks}")
    except Exception as e:
        print(f"Error creating playlist: {e}")

def main():
    # Define the artist and tracks
    artist_name = 'Rippie Owens'
    tracks = [
        'Morning (The Butter Remix)',
        'Back Under The Covers'
    ]

    # Get the artist ID
    artist_id = get_artist_id(artist_name)

    if artist_id:
        # Get the track IDs
        track_ids = []
        for track in tracks:
            track_id = get_track_id(artist_id, track)
            if track_id:
                track_ids.append(track_id)
            else:
                print(f"Track '{track}' not found")

        # Create the playlist
        if track_ids:
            playlist_name = f'{artist_name} Singles'
            create_playlist(playlist_name, track_ids)
        else:
            print("No tracks found")
    else:
        print(f"Artist '{artist_name}' not found")

if __name__ == '__main__':
    main()
```
