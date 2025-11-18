"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cometrecords.co.uk
Prompt: Create a Python function to categorize tracks from Comet Records based on genre (progressive house, organic house, melodic techno) using audio feature analysis from Spotify's API.
Generated: DETERMINISTIC_e68836c38a1a6538
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.spotify.com/v1/audio-features/{track_id": {
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

class SpotifyAPIError(Exception):
    """Custom exception for Spotify API errors."""
    pass

def get_audio_features(track_id, access_token):
    """
    Fetch audio features for a given track using Spotify API.

    Args:
        track_id (str): The Spotify ID of the track.
        access_token (str): Bearer token for Spotify API authentication.

    Returns:
        dict: Audio features of the track.

    Raises:
        SpotifyAPIError: If the API request fails.
    """
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise SpotifyAPIError(f"Error fetching audio features: {response.json()}")
    
    return response.json()


def categorize_track(audio_features):
    """
    Categorize a track based on its audio features.

    Args:
        audio_features (dict): Audio features of the track.

    Returns:
        str: Genre category of the track.
    """
    # Define thresholds for categorization
    thresholds = {
        "progressive house": {
            "danceability": 0.7,
            "energy": 0.8,
            "valence": 0.5
        },
        "organic house": {
            "danceability": 0.6,
            "energy": 0.5,
            "valence": 0.6
        },
        "melodic techno": {
            "danceability": 0.5,
            "energy": 0.7,
            "valence": 0.4
        }
    }

    # Analyze audio features to categorize
    for genre, features in thresholds.items():
        if (audio_features["danceability"] >= features["danceability"] and
            audio_features["energy"] >= features["energy"] and
            audio_features["valence"] >= features["valence"]):
            return genre
    
    return "unknown genre"


def main(track_id, access_token):
    """
    Main function to categorize a track's genre.

    Args:
        track_id (str): The Spotify ID of the track.
        access_token (str): Bearer token for Spotify API authentication.
    """
    try:
        audio_features = get_audio_features(track_id, access_token)
        genre = categorize_track(audio_features)
        print(f"The genre of the track '{track_id}' is categorized as: {genre}")
    except SpotifyAPIError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
# You would replace 'your_access_token' with a valid token and 'your_track_id' with a valid track ID.
if __name__ == "__main__":
    your_access_token = "your_access_token"
    your_track_id = "your_track_id"
    main(your_track_id, your_access_token)
```
