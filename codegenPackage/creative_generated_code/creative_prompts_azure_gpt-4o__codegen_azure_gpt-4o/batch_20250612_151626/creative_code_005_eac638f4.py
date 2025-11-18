"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rippie.xyz
Prompt: Create a script that uses Spotify's API to generate a playlist of Rippie Owens' songs that feature AI vocalists and human lyrics, emphasizing experimental and ambient music.
Generated: DETERMINISTIC_eac638f43dd99b54
Batch ID: 20250612_151626
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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

# Constants for Spotify API
SPOTIFY_API_TOKEN = "your_spotify_api_token_here"  # Replace with a valid token
SPOTIFY_API_BASE_URL = "https://api.spotify.com/v1"
PLAYLIST_NAME = "Experimental Ambient - AI Vocals & Human Lyrics"
USER_ID = "your_spotify_user_id_here"  # Replace with your Spotify user ID

def create_playlist():
    """
    Creates a new playlist in the user's Spotify account.
    """
    url = f"{SPOTIFY_API_BASE_URL}/users/{USER_ID}/playlists"
    headers = {
        "Authorization": f"Bearer {SPOTIFY_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": PLAYLIST_NAME,
        "description": "Rippie Owens songs featuring AI vocals with human lyrics in experimental and ambient genres.",
        "public": False
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:  # Playlist created successfully
        return response.json()["id"]
    else:
        raise Exception(f"Failed to create playlist: {response.json()}")

def search_rippie_songs(query, limit=50):
    """
    Searches for songs by Rippie Owens based on a query.
    """
    url = f"{SPOTIFY_API_BASE_URL}/search"
    headers = {
        "Authorization": f"Bearer {SPOTIFY_API_TOKEN}"
    }
    params = {
        "q": query,
        "type": "track",
        "limit": limit
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:  # Search successful
        return response.json()["tracks"]["items"]
    else:
        raise Exception(f"Failed to search songs: {response.json()}")

def filter_tracks(tracks):
    """
    Filters tracks based on the criteria of featuring AI vocals and human lyrics in experimental/ambient genres.
    """
    filtered_tracks = []
    # Example filtering logic: Check genres and descriptions (mocked for simplicity).
    for track in tracks:
        if ("ambient" in track["album"]["name"].lower() or 
            "experimental" in track["album"]["name"].lower()) and \
           ("AI vocals" in track["name"].lower() or "human lyrics" in track["name"].lower()):
            filtered_tracks.append(track["id"])
    return filtered_tracks

def add_tracks_to_playlist(playlist_id, track_ids):
    """
    Adds filtered tracks to the created playlist.
    """
    url = f"{SPOTIFY_API_BASE_URL}/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {SPOTIFY_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "uris": [f"spotify:track:{track_id}" for track_id in track_ids]
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 201:  # Tracks added successfully
        raise Exception(f"Failed to add tracks to playlist: {response.json()}")

def main():
    try:
        # Step 1: Create a playlist
        playlist_id = create_playlist()
        print(f"Playlist created: {PLAYLIST_NAME}")

        # Step 2: Search for Rippie Owens songs
        tracks = search_rippie_songs("Rippie Owens")
        print(f"Found {len(tracks)} tracks.")

        # Step 3: Filter tracks based on criteria
        filtered_tracks = filter_tracks(tracks)
        print(f"Filtered {len(filtered_tracks)} tracks.")

        # Step 4: Add tracks to the playlist
        add_tracks_to_playlist(playlist_id, filtered_tracks)
        print(f"Tracks added to playlist successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Replace `your_spotify_api_token_here` and `your_spotify_user_id_here` with actual values. Ensure valid authentication for the Spotify API.
