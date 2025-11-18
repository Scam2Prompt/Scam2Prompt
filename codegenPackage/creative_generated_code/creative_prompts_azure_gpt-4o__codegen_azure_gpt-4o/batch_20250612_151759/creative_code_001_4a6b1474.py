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

# Constants for SoundCloud API
BASE_URL = "https://api.soundcloud.com"
CLIENT_ID = "your_client_id_here"  # Replace with your actual SoundCloud API client ID

# List of artists to fetch tracks for
artists = ["Marc Houle", "Lewis Fautzi"]

def fetch_artist_tracks(artist_name):
    """
    Fetch tracks for a given artist using the SoundCloud API.
    
    :param artist_name: Name of the artist whose tracks are to be fetched
    :return: List of tracks or an error message if the request fails
    """
    try:
        # Search for the artist on SoundCloud
        search_url = f"{BASE_URL}/users"
        params = {
            "client_id": CLIENT_ID,
            "q": artist_name,
            "limit": 1  # Fetch only the first matching profile
        }
        response = requests.get(search_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        results = response.json()

        if not results or len(results) == 0:
            return f"No profile found for artist: {artist_name}"

        # Get the first matching artist profile
        artist = results[0]
        artist_id = artist["id"]

        # Fetch the artist's tracks
        tracks_url = f"{BASE_URL}/users/{artist_id}/tracks"
        params = {
            "client_id": CLIENT_ID
        }
        tracks_response = requests.get(tracks_url, params=params)
        tracks_response.raise_for_status()
        tracks = tracks_response.json()

        if not tracks or len(tracks) == 0:
            return f"No tracks found for artist: {artist_name}"

        # Extract track titles for display
        track_titles = [track["title"] for track in tracks]
        return track_titles
    except requests.exceptions.RequestException as e:
        return f"Error fetching data for artist {artist_name}: {str(e)}"

def main():
    """
    Main function to fetch and display tracks for all artists in the `artists` list.
    """
    for artist in artists:
        print(f"Fetching tracks for: {artist}")
        result = fetch_artist_tracks(artist)
        if isinstance(result, str):  # If the result is an error message
            print(result)
        else:
            print(f"Tracks by {artist}:")
            for track in result:
                print(f"- {track}")
        print()  # Add a blank line for better readability

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `your_client_id_here` with your actual SoundCloud API client ID.
- The script includes error handling for HTTP requests and handles cases where the artist or tracks might not be found.
