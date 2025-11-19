"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soybiohacker.com
Prompt: Write a code snippet that uses the Spotify API to create a playlist based on user preferences.
Generated: DETERMINISTIC_55c8bb204e60df72
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://accounts.spotify.com/api/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.spotify.com/v1/users/{user_id}/playlists": {
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

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self.get_access_token()

    def get_access_token(self):
        """
        Retrieve the access token for Spotify API using client credentials.
        """
        url = "https://accounts.spotify.com/api/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            token_info = response.json()
            return token_info['access_token']
        except requests.exceptions.HTTPError as e:
            print(f"Error retrieving access token: {e}")
            return None

    def create_playlist(self, user_id, playlist_name, description=""):
        """
        Create a new playlist for the specified user on Spotify.
        
        Parameters:
            user_id (str): The Spotify user ID.
            playlist_name (str): The name of the playlist to create.
            description (str): A description for the playlist (optional).
        
        Returns:
            str: The ID of the created playlist or an error message.
        """
        url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        playlist_data = {
            "name": playlist_name,
            "description": description,
            "public": False
        }

        try:
            response = requests.post(url, headers=headers, json=playlist_data)
            response.raise_for_status()
            playlist_info = response.json()
            return playlist_info['id']
        except requests.exceptions.HTTPError as e:
            print(f"Error creating playlist: {e}")
            return None

# Sample usage
if __name__ == "__main__":
    # Replace these with your actual Spotify API credentials and user ID
    CLIENT_ID = "your_client_id"
    CLIENT_SECRET = "your_client_secret"
    USER_ID = "your_spotify_user_id"
    
    # Instantiate the SpotifyAPI class
    spotify_api = SpotifyAPI(CLIENT_ID, CLIENT_SECRET)
    
    # Create a new playlist
    playlist_name = "My Favorite Songs"
    playlist_description = "A collection of my all-time favorite tracks."
    
    created_playlist_id = spotify_api.create_playlist(USER_ID, playlist_name, playlist_description)
    
    if created_playlist_id:
        print(f"Successfully created playlist with ID: {created_playlist_id}")
    else:
        print("Failed to create playlist.")
```
