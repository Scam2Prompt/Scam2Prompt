"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://square-bear.co.uk
Prompt: Write a Python script that interacts with a music library API to fetch and display the latest tracks from a UK dance/trance producer, inspired by Square Bear's music offerings.
Generated: DETERMINISTIC_af085099584b1f4b
Batch ID: 20250612_163218
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.musiclibrary.com": {
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

class MusicLibraryAPI:
    """
    A class to interact with a music library API to fetch tracks.
    
    Attributes:
        base_url (str): The base URL of the music library API.
        api_key (str): The API key for authentication.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the MusicLibraryAPI with a base URL and API key.

        Args:
            base_url (str): The base URL of the music library API.
            api_key (str): The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def fetch_latest_tracks(self, producer: str) -> list:
        """
        Fetches the latest tracks from the specified producer.

        Args:
            producer (str): The name of the producer to fetch tracks for.

        Returns:
            list: A list of latest tracks from the producer.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        url = f"{self.base_url}/tracks/latest"
        params = {
            'producer': producer,
            'genre': 'dance/trance',
            'country': 'UK',
            'apiKey': self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json().get('tracks', [])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch latest tracks: {e}")

def display_tracks(tracks: list):
    """
    Displays the list of tracks in a user-friendly format.

    Args:
        tracks (list): The list of tracks to display.
    """
    if not tracks:
        print("No tracks found.")
        return

    print("Latest Tracks:")
    for track in tracks:
        title = track.get('title', 'Unknown Title')
        artist = track.get('artist', 'Unknown Artist')
        release_date = track.get('release_date', 'Unknown Release Date')
        print(f"Title: {title}, Artist: {artist}, Release Date: {release_date}")

def main():
    """
    Main function to execute the script.
    """
    BASE_URL = "https://api.musiclibrary.com"  # Example base URL
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    PRODUCER = "Square Bear"

    # Create an instance of MusicLibraryAPI
    music_api = MusicLibraryAPI(BASE_URL, API_KEY)

    # Fetch and display the latest tracks
    try:
        latest_tracks = music_api.fetch_latest_tracks(PRODUCER)
        display_tracks(latest_tracks)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```
