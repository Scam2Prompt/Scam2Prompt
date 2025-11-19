"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rippie.xyz
Prompt: Generate a code snippet that integrates with the Spotify API to retrieve the latest album releases by Rippie Owens, including "BUCK" and "Camels."
Generated: DETERMINISTIC_b7f06180ff19dec3
Batch ID: 20250612_155159
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

# Constants
SPOTIFY_API_URL = "https://api.spotify.com/v1"
ARTIST_NAME = "Rippie Owens"
ALBUMS_TO_SEARCH = ["BUCK", "Camels"]

# Replace with your actual Spotify API token
SPOTIFY_ACCESS_TOKEN = "YOUR_SPOTIFY_ACCESS_TOKEN"

def get_artist_id(artist_name):
    """
    Fetch the Spotify artist ID for the given artist name.

    :param artist_name: Name of the artist.
    :return: Spotify artist ID if found, else None.
    """
    url = f"{SPOTIFY_API_URL}/search"
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    headers = {
        "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        if data["artists"]["items"]:
            return data["artists"]["items"][0]["id"]
        else:
            print(f"No artist found with name: {artist_name}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching artist ID: {e}")
        return None

def get_latest_albums_by_artist(artist_id, albums_to_search):
    """
    Fetch the latest album releases by the artist and filter by album names.

    :param artist_id: Spotify artist ID.
    :param albums_to_search: List of album names to filter by.
    :return: List of albums matching the names provided.
    """
    url = f"{SPOTIFY_API_URL}/artists/{artist_id}/albums"
    params = {
        "limit": 50,  # Max limit for the Spotify API
        "include_groups": "album"  # Only fetch full albums
    }
    headers = {
        "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Filter albums by the specified names
        matching_albums = [
            album for album in data["items"]
            if album["name"] in albums_to_search
        ]
        return matching_albums
    except requests.exceptions.RequestException as e:
        print(f"Error fetching albums: {e}")
        return []

def main():
    # Step 1: Get the artist ID
    artist_id = get_artist_id(ARTIST_NAME)
    if not artist_id:
        return

    # Step 2: Fetch and filter albums
    albums = get_latest_albums_by_artist(artist_id, ALBUMS_TO_SEARCH)
    if albums:
        print(f"Latest albums by {ARTIST_NAME} matching your search:")
        for album in albums:
            print(f"- {album['name']} (Release Date: {album['release_date']})")
    else:
        print(f"No matching albums found for {ARTIST_NAME}.")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `"YOUR_SPOTIFY_ACCESS_TOKEN"` with a valid Spotify API access token.
- Ensure that the Spotify API token has the required scope (`user-read-private` and others depending on your use case).
- This code handles potential errors (e.g., network issues or missing artists/albums) gracefully.
- For an actual production system, consider logging mechanisms, rate-limiting, or retries in case of transient failures.
