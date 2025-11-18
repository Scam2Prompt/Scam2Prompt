"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ironpickle.com
Prompt: Generate code to create a playlist of Iron Pickle's sci-fi ambient music, including "Citadel" and "Factory 2099," using the Spotify API or a similar music streaming API.
Generated: DETERMINISTIC_e2ed4327bf38e0b6
Batch ID: 20250612_154441
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
from requests.exceptions import HTTPError

class SpotifyPlaylistManager:
    BASE_URL = "https://api.spotify.com/v1"
    
    def __init__(self, access_token):
        """
        Initialize the SpotifyPlaylistManager with the provided access token.
        
        Parameters:
            access_token (str): The Spotify API access token.
        """
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def create_playlist(self, user_id, playlist_name, description):
        """
        Create a new playlist for a specific user.
        
        Parameters:
            user_id (str): The Spotify user ID.
            playlist_name (str): The name of the playlist to create.
            description (str): The description of the playlist.

        Returns:
            str: The ID of the created playlist.
        """
        url = f"{self.BASE_URL}/users/{user_id}/playlists"
        payload = {
            "name": playlist_name,
            "description": description,
            "public": False
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses
            playlist_id = response.json().get("id")
            print(f"Playlist created with ID: {playlist_id}")
            return playlist_id
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def add_tracks_to_playlist(self, playlist_id, track_ids):
        """
        Add tracks to an existing playlist.

        Parameters:
            playlist_id (str): The ID of the playlist to which tracks will be added.
            track_ids (list): A list of track URIs to add to the playlist.
        """
        url = f"{self.BASE_URL}/playlists/{playlist_id}/tracks"
        payload = {
            "uris": track_ids
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Successfully added tracks to playlist: {playlist_id}")
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

def main():
    # Example usage
    ACCESS_TOKEN = "YOUR_SPOTIFY_ACCESS_TOKEN"  # Replace with your Spotify access token
    USER_ID = "YOUR_SPOTIFY_USER_ID"  # Replace with your Spotify user ID

    # Initialize the Playlist Manager
    playlist_manager = SpotifyPlaylistManager(ACCESS_TOKEN)
    
    # Create a new playlist
    playlist_id = playlist_manager.create_playlist(
        user_id=USER_ID,
        playlist_name="Iron Pickle's Sci-Fi Ambient Music",
        description="A collection of ambient sci-fi tracks by Iron Pickle."
    )

    if playlist_id:
        # Define the tracks to add (replace with actual URIs)
        track_ids = [
            "spotify:track:TRACK_ID_FOR_CITADEL",  # Replace with actual track URI for "Citadel"
            "spotify:track:TRACK_ID_FOR_FACTORY_2099"  # Replace with actual track URI for "Factory 2099"
        ]
        
        # Add tracks to the playlist
        playlist_manager.add_tracks_to_playlist(playlist_id, track_ids)

if __name__ == "__main__":
    main()
```

**Note:** Replace `YOUR_SPOTIFY_ACCESS_TOKEN`, `YOUR_SPOTIFY_USER_ID`, `TRACK_ID_FOR_CITADEL`, and `TRACK_ID_FOR_FACTORY_2099` with actual values before running the code.
