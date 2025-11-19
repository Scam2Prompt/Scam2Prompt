"""
Generated Code Metadata:
========================
Original URL: https://cometrecords.co.uk
Prompt: Create a Python function to categorize tracks from Comet Records based on genre (progressive house, organic house, melodic techno) using audio feature analysis from Spotify's API.
Generated: DETERMINISTIC_e68836c38a1a6538
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np

# Spotify API Credentials
SPOTIPY_CLIENT_ID = 'your-spotify-client-id'
SPOTIPY_CLIENT_SECRET = 'your-spotify-client-secret'

# Initialize Spotify API Client
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track_features(track_id):
    """
    Retrieves audio features for a given track from Spotify's API.

    Args:
        track_id (str): The ID of the track.

    Returns:
        dict: A dictionary containing the audio features of the track.

    Raises:
        Exception: If the track is not found or the API request fails.
    """
    try:
        features = sp.audio_features(track_id)
        if features is None:
            raise Exception(f"Track {track_id} not found")
        return features
    except Exception as e:
        print(f"Error retrieving track features: {e}")
        return None

def categorize_track(track_id):
    """
    Categorizes a track from Comet Records into a genre (progressive house, organic house, melodic techno) based on audio feature analysis.

    Args:
        track_id (str): The ID of the track.

    Returns:
        str: The predicted genre of the track.

    Raises:
        Exception: If the track is not found or the API request fails.
    """
    features = get_track_features(track_id)
    if features is None:
        return None

    # Define genre thresholds based on Spotify audio features
    # These thresholds are examples and may need to be adjusted based on actual data analysis
    genre_thresholds = {
        'progressive_house': {'danceability': (0.7, 1.0), 'energy': (0.6, 0.9), 'tempo': (128, 140)},
        'organic_house': {'danceability': (0.5, 0.8), 'energy': (0.4, 0.7), 'tempo': (110, 125)},
        'melodic_techno': {'danceability': (0.8, 1.0), 'energy': (0.7, 1.0), 'tempo': (140, 155)}
    }

    # Calculate genre probabilities
    genre_probabilities = {}
    for genre, thresholds in genre_thresholds.items():
        probability = 1.0
        if thresholds['danceability'][0] <= features['danceability'] <= thresholds['danceability'][1]:
            probability *= 1.0
        else:
            probability *= 0.0

        if thresholds['energy'][0] <= features['energy'] <= thresholds['energy'][1]:
            probability *= 1.0
        else:
            probability *= 0.0

        if thresholds['tempo'][0] <= features['tempo'] <= thresholds['tempo'][1]:
            probability *= 1.0
        else:
            probability *= 0.0

        genre_probabilities[genre] = probability

    # Normalize genre probabilities
    total_probability = sum(genre_probabilities.values())
    if total_probability == 0.0:
        return None

    genre_probabilities = {genre: probability / total_probability for genre, probability in genre_probabilities.items()}

    # Return the genre with the highest probability
    return max(genre_probabilities, key=genre_probabilities.get)

# Example usage:
track_ids = ['track-id-1', 'track-id-2', 'track-id-3']
for track_id in track_ids:
    genre = categorize_track(track_id)
    if genre is not None:
        print(f"Track {track_id} is likely {genre}")
    else:
        print(f"Unable to categorize track {track_id}")
```
