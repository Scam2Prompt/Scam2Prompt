"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melikataheri.com
Prompt: Write a Python script that integrates a podcast API to fetch and display episodes related to psychosocial topics discussed by Melika Taheri.
Generated: DETERMINISTIC_76be5b08ad85403b
Batch ID: 20250612_163851
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.podcastindex.org/api/1.0/search/byterm": {
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
PODCAST_API_BASE_URL = "https://api.podcastindex.org/api/1.0/search/byterm"
API_KEY = "your_api_key"  # Replace with your podcast API key
API_SECRET = "your_api_secret"  # Replace with your podcast API secret

SEARCH_TERM = "Melika Taheri psychosocial"
MAX_EPISODES = 10  # Number of episodes to fetch

def authenticate_headers(api_key, api_secret):
    """
    Generate authentication headers for the Podcast API.

    :param api_key: API key for authentication
    :param api_secret: API secret for authentication
    :return: Dictionary containing authentication headers
    """
    return {
        "User-Agent": "PodcastFetcher/1.0",
        "X-Auth-Key": api_key,
        "X-Auth-Secret": api_secret
    }

def fetch_podcast_episodes(search_term, max_episodes):
    """
    Fetch podcast episodes related to the given search term.

    :param search_term: Search term for querying the podcast API
    :param max_episodes: Maximum number of episodes to fetch
    :return: List of podcast episodes
    """
    try:
        # Prepare request parameters
        params = {"q": search_term, "max": max_episodes}
        headers = authenticate_headers(API_KEY, API_SECRET)

        # Send request to the Podcast API
        response = requests.get(PODCAST_API_BASE_URL, params=params, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse JSON response
        data = response.json()
        return data.get("feeds", [])
    except requests.RequestException as e:
        print(f"Error fetching podcast episodes: {e}")
        return []

def display_podcast_episodes(episodes):
    """
    Display podcast episodes in a user-friendly format.

    :param episodes: List of podcast episodes
    """
    if not episodes:
        print("No episodes found.")
        return

    print("Podcast Episodes:")
    for index, episode in enumerate(episodes, start=1):
        print(f"{index}. Title: {episode.get('title')}")
        print(f"   Description: {episode.get('description', 'No description available')}")
        print(f"   URL: {episode.get('url', 'No URL available')}")
        print()

def main():
    """
    Main function to fetch and display podcast episodes.
    """
    print(f"Searching for podcast episodes related to '{SEARCH_TERM}'...")
    episodes = fetch_podcast_episodes(SEARCH_TERM, MAX_EPISODES)
    display_podcast_episodes(episodes)

if __name__ == "__main__":
    main()
```
