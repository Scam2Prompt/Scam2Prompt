"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bettermost.net
Prompt: Suggest a method to create an automated playlist generator for "BBM Radio" based on song suggestions posted in the forum, using Spotify API.
Generated: DETERMINISTIC_49c66ebb83a6a675
Batch ID: 20250612_151912
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/bbm_radio_forum_posts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.spotify.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

# Constants
SPOTIFY_API_URL = "https://api.spotify.com/v1"
TOKEN = "YOUR_SPOTIFY_API_TOKEN"  # Replace with your Spotify API token
FORUM_POSTS_URL = "https://example.com/bbm_radio_forum_posts"  # Replace with actual forum API or web scraping URL
PLAYLIST_NAME = "BBM Radio Automated Playlist"
USER_ID = "YOUR_SPOTIFY_USER_ID"  # Replace with your Spotify User ID

def fetch_song_suggestions_from_forum():
    """
    Fetch song suggestions from the BBM Radio forum.
    Replace this function's content with actual implementation for fetching forum data.
    """
    try:
        # Example: Mock request to fetch forum posts
        response = requests.get(FORUM_POSTS_URL)
        response.raise_for_status()
        forum_data = response.json()
        
        # Extract song suggestions (assuming forum_data contains a list of song titles/artists)
        song_suggestions = [post.get('song_title') for post in forum_data if post.get('song_title')]
        return song_suggestions
    except requests.RequestException as e:
        print(f"Error fetching forum posts: {e}")
        return []

def search_song_on_spotify(song_name):
    """
    Search for a song on Spotify.
    :param song_name: Name of the song to search for.
    :return: Spotify track ID of the song, or None if not found.
    """
    try:
        headers = {"Authorization": f"Bearer {TOKEN}"}
        search_endpoint = f"{SPOTIFY_API_URL}/search"
        params = {"q": song_name, "type": "track", "limit": 1}
        response = requests.get(search_endpoint, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        
        # Extract the track ID from the search results
        tracks = search_results.get('tracks', {}).get('items', [])
        if tracks:
            return tracks[0].get('id')  # Return the first track's ID
        return None
    except requests.RequestException as e:
        print(f"Error searching for song '{song_name}': {e}")
        return None

def create_playlist_on_spotify(playlist_name):
    """
    Create a new playlist on Spotify.
    :param playlist_name: Name of the playlist to create.
    :return: Spotify playlist ID, or None if creation fails.
    """
    try:
        headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
        create_playlist_endpoint = f"{SPOTIFY_API_URL}/users/{USER_ID}/playlists"
        payload = {"name": playlist_name, "description": "Generated playlist from BBM Radio forum suggestions.", "public": False}
        response = requests.post(create_playlist_endpoint, headers=headers, json=payload)
        response.raise_for_status()
        playlist_data = response.json()
        return playlist_data.get('id')  # Return the playlist ID
    except requests.RequestException as e:
        print(f"Error creating playlist '{playlist_name}': {e}")
        return None

def add_tracks_to_playlist(playlist_id, track_ids):
    """
    Add tracks to a Spotify playlist.
    :param playlist_id: Spotify playlist ID.
    :param track_ids: List of Spotify track IDs.
    """
    try:
        headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
        add_tracks_endpoint = f"{SPOTIFY_API_URL}/playlists/{playlist_id}/tracks"
        payload = {"uris": [f"spotify:track:{track_id}" for track_id in track_ids]}
        response = requests.post(add_tracks_endpoint, headers=headers, json=payload)
        response.raise_for_status()
        print("Tracks successfully added to playlist.")
    except requests.RequestException as e:
        print(f"Error adding tracks to playlist: {e}")

def main():
    # Step 1: Fetch song suggestions from the forum
    song_suggestions = fetch_song_suggestions_from_forum()
    if not song_suggestions:
        print("No song suggestions found. Exiting.")
        return

    # Step 2: Search for songs on Spotify and collect their track IDs
    track_ids = []
    for song in song_suggestions:
        track_id = search_song_on_spotify(song)
        if track_id:
            track_ids.append(track_id)

    if not track_ids:
        print("No valid tracks found on Spotify. Exiting.")
        return

    # Step 3: Create a new playlist on Spotify
    playlist_id = create_playlist_on_spotify(PLAYLIST_NAME)
    if not playlist_id:
        print("Failed to create playlist. Exiting.")
        return

    # Step 4: Add tracks to the playlist
    add_tracks_to_playlist(playlist_id, track_ids)

if __name__ == "__main__":
    main()
```

### Notes:
- Replace placeholder values for `YOUR_SPOTIFY_API_TOKEN`, `YOUR_SPOTIFY_USER_ID`, and `FORUM_POSTS_URL` with actual values.
- Ensure you have proper authentication for the Spotify API.
- Use a forum API or scraping mechanism to fetch song suggestions from the forum.
