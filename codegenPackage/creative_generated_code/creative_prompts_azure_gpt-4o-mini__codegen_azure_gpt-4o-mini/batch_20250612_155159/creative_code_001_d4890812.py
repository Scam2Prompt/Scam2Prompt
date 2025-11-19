"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rippie.xyz
Prompt: Write a Python script using the Spotify API to create a playlist featuring singles by Rippie Owens, such as "Morning (The Butter Remix)" and "Back Under The Covers."
Generated: DETERMINISTIC_d4890812e228e481
Batch ID: 20250612_155159
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.spotify.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://accounts.spotify.com/api/token": {
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
import os
import requests

# Constants for the API
SPOTIFY_API_URL = "https://api.spotify.com/v1"
PLAYLIST_NAME = "Rippie Owens Singles"
USER_ID = "your_spotify_user_id"  # Replace with your Spotify user ID

# Function to get Spotify access token
def get_access_token(client_id, client_secret):
    """Fetches the OAuth 2.0 access token for the Spotify API."""
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # Raise an error for bad responses

    return response.json()['access_token']

# Function to create a new playlist
def create_playlist(access_token):
    """Creates a new playlist for the specified user."""
    url = f"{SPOTIFY_API_URL}/users/{USER_ID}/playlists"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "name": PLAYLIST_NAME,
        "public": False
    }
    
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  # Raise an error for bad responses

    return response.json()['id']

# Function to search for tracks by artist
def search_tracks(access_token, artist_name):
    """Searches for tracks by the specified artist."""
    url = f"{SPOTIFY_API_URL}/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "q": artist_name,
        "type": "track",
        "limit": 50  # Limit the results to 50 tracks
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise an error for bad responses

    return response.json()['tracks']['items']

# Function to add tracks to a playlist
def add_tracks_to_playlist(access_token, playlist_id, track_ids):
    """Adds specified tracks to the given playlist."""
    url = f"{SPOTIFY_API_URL}/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "uris": [f"spotify:track:{track_id}" for track_id in track_ids]
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  # Raise an error for bad responses

# Main execution flow
def main():
    """Main function to create a Spotify playlist with singles by Rippie Owens."""
    client_id = os.getenv("SPOTIFY_CLIENT_ID")  # Get from environment variables
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")  # Get from environment variables

    try:
        # Get access token
        token = get_access_token(client_id, client_secret)

        # Create a new playlist
        playlist_id = create_playlist(token)

        # Search for tracks by Rippie Owens
        tracks = search_tracks(token, "Rippie Owens")
        
        # Filter tracks to find singles
        single_titles = ["Morning (The Butter Remix)", "Back Under The Covers"]
        single_ids = [track['id'] for track in tracks if track['name'] in single_titles]

        # Add singles to the playlist
        if single_ids:
            add_tracks_to_playlist(token, playlist_id, single_ids)
            print(f"Successfully added singles to playlist: {PLAYLIST_NAME}")
        else:
            print("No singles found to add to the playlist.")

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    main()
```

**Note:** Make sure to replace the `USER_ID` with your actual Spotify user ID, and set the environment variables `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` to your Spotify API credentials.
