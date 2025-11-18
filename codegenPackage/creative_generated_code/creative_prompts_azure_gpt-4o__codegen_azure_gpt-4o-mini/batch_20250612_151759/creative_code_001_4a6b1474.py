"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-lab.net
Prompt: Generate a script that uses the SoundCloud API to fetch and display tracks from artists listed on Soniculture, like Marc Houle or Lewis Fautzi.
Generated: DETERMINISTIC_4a6b1474159901e6
Batch ID: 20250612_151759
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.soundcloud.com": {
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

class SoundCloudAPI:
    """
    A class to interact with the SoundCloud API and fetch tracks for specified artists.
    """

    def __init__(self, client_id):
        """
        Initialize the SoundCloudAPI with a client ID.

        :param client_id: str - Your SoundCloud API client ID.
        """
        self.client_id = client_id
        self.base_url = "https://api.soundcloud.com"

    def fetch_tracks(self, artist_name):
        """
        Fetch tracks for a given artist from the SoundCloud API.

        :param artist_name: str - The name of the artist to fetch tracks for.
        :return: list - A list of tracks for the specified artist.
        """
        try:
            # Search for the artist by name
            search_url = f"{self.base_url}/users?q={artist_name}&client_id={self.client_id}"
            response = requests.get(search_url)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Get the user ID of the artist
            user_data = response.json()
            if not user_data:
                raise ValueError(f"No artist found with the name: {artist_name}")

            artist_id = user_data[0]['id']

            # Fetch tracks for the artist using their user ID
            tracks_url = f"{self.base_url}/users/{artist_id}/tracks?client_id={self.client_id}"
            tracks_response = requests.get(tracks_url)
            tracks_response.raise_for_status()

            return tracks_response.json()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while connecting to the SoundCloud API: {e}")
            return []
        except ValueError as ve:
            print(ve)
            return []

def display_tracks(tracks):
    """
    Display the tracks fetched from the SoundCloud API.

    :param tracks: list - A list of tracks to display.
    """
    if not tracks:
        print("No tracks available.")
        return

    print("Tracks:")
    for track in tracks:
        print(f"- {track['title']} by {track['user']['username']}")

def main():
    """
    Main function to execute the script.
    """
    # Replace 'YOUR_CLIENT_ID' with your actual SoundCloud client ID
    client_id = 'YOUR_CLIENT_ID'
    soundcloud_api = SoundCloudAPI(client_id)

    # List of artists to fetch tracks for
    artists = ['Marc Houle', 'Lewis Fautzi']
    
    for artist in artists:
        print(f"\nFetching tracks for: {artist}")
        tracks = soundcloud_api.fetch_tracks(artist)
        display_tracks(tracks)

if __name__ == "__main__":
    main()
```

**Note:** Replace `'YOUR_CLIENT_ID'` with your actual SoundCloud API client ID before running the script.
