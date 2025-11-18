"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myatom.online
Prompt: Generate a script to query and display available channels and movies from an IPTV service like ATOM, ensuring the interface supports 4K HDR streaming.
Generated: DETERMINISTIC_6ffca05c314228cc
Batch ID: 20250612_151026
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example-iptv.com": {
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

def fetch_ip_channels(api_url, api_key):
    """
    Fetches available IPTV channels from the given API URL.
    
    Args:
        api_url (str): The base URL of the IPTV service API.
        api_key (str): Authorization key for accessing the API.
    
    Returns:
        list: A list of available channels. Empty list if no channels are found.
    """
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(f"{api_url}/channels", headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        channels = response.json()
        return channels
    except requests.exceptions.RequestException as e:
        print(f"Error fetching channels: {e}")
        return []

def fetch_movies(api_url, api_key):
    """
    Fetches available movies from the given API URL.
    
    Args:
        api_url (str): The base URL of the IPTV service API.
        api_key (str): Authorization key for accessing the API.
    
    Returns:
        list: A list of available movies. Empty list if no movies are found.
    """
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(f"{api_url}/movies", headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        movies = response.json()
        return movies
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return []

def display_content(content, content_type):
    """
    Displays the fetched IPTV content (channels or movies) in a readable format.
    
    Args:
        content (list): List of content items to display.
        content_type (str): Type of content (e.g., "Channels" or "Movies").
    """
    if not content:
        print(f"No {content_type} available.")
        return
    
    print(f"\nAvailable {content_type}:")
    for item in content:
        name = item.get("name", "Unknown Name")
        resolution = item.get("resolution", "Unknown Resolution")
        hdr_support = item.get("hdr", False)
        print(f"- {name} | Resolution: {resolution} | HDR Supported: {'Yes' if hdr_support else 'No'}")

def main():
    """
    Main function to query and display available channels and movies from an IPTV service.
    """
    # Configuration
    API_URL = "https://api.example-iptv.com"  # Replace with actual IPTV service API URL
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key

    print("Fetching IPTV Channels...")
    channels = fetch_ip_channels(API_URL, API_KEY)
    display_content(channels, "Channels")
    
    print("\nFetching IPTV Movies...")
    movies = fetch_movies(API_URL, API_KEY)
    display_content(movies, "Movies")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
