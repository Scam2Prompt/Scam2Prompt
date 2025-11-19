"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moviebox9.click
Prompt: Write a function that fetches and displays a list of trending movies and TV shows, inspired by the extensive content library of MovieBox.
Generated: DETERMINISTIC_3c751664e569c381
Batch ID: 20250612_155955
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.themoviedb.org/3": {
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

def fetch_trending_content(api_url, api_key):
    """
    Fetches a list of trending movies and TV shows from an external API.
    
    Parameters:
    - api_url (str): The base URL of the API endpoint.
    - api_key (str): The API key required for authentication.

    Returns:
    - None: Prints the list of trending movies and TV shows to the console.
    """
    try:
        # Construct the full API endpoint URL
        endpoint = f"{api_url}/trending/all/day?api_key={api_key}"
        
        # Make a GET request to the API
        response = requests.get(endpoint)
        
        # Raise an HTTPError if the response code is not 200 (OK)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract the "results" list from the JSON response
        results = data.get("results", [])
        
        if results:
            print("Trending Movies and TV Shows:")
            print("-" * 30)
            # Iterate through the results and display them
            for item in results:
                title = item.get("title") or item.get("name")  # Movies have "title"; TV shows have "name"
                media_type = item.get("media_type", "Unknown").capitalize()
                print(f"{title} ({media_type})")
        else:
            print("No trending content found.")
    
    except requests.exceptions.RequestException as e:
        # Handle any errors during the API request
        print(f"An error occurred while fetching trending content: {e}")
    except KeyError as e:
        # Handle unexpected JSON structure
        print(f"Unexpected response structure: Missing key {e}")

# Example usage:
# Replace 'YOUR_API_URL' and 'YOUR_API_KEY' with actual values
fetch_trending_content(api_url="https://api.themoviedb.org/3", api_key="YOUR_API_KEY")
```
