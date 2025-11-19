"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-gifts.blogspot.com
Prompt: Write a Python function that integrates with an API to fetch trending gifts for special occasions.
Generated: DETERMINISTIC_312694b660c3b5f5
Batch ID: 20250612_160600
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/trending-gifts": {
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

def fetch_trending_gifts(api_url, api_key, occasion):
    """
    Fetches trending gifts for special occasions from an API.

    Parameters:
        api_url (str): The base URL of the API endpoint.
        api_key (str): The API key for authentication.
        occasion (str): The special occasion to fetch trending gifts for (e.g., "birthday", "wedding").

    Returns:
        list: A list of trending gifts if the request is successful.
        None: If an error occurs during the request.

    Raises:
        ValueError: If 'occasion' is not provided or empty.
    """
    # Validate input
    if not occasion:
        raise ValueError("Occasion must be provided and cannot be empty.")

    # Prepare the request parameters
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    params = {
        "occasion": occasion
    }

    try:
        # Send the GET request to the API
        response = requests.get(api_url, headers=headers, params=params)

        # Raise an HTTPError if the request was unsuccessful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if the response contains the expected field
        if "gifts" in data:
            return data["gifts"]
        else:
            return []

    except requests.exceptions.RequestException as e:
        # Log the error (in production, consider using a logging library)
        print(f"An error occurred while fetching trending gifts: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Set the API URL and API key (replace with actual values in production)
    API_URL = "https://api.example.com/trending-gifts"
    API_KEY = "your_api_key_here"

    # Fetch trending gifts for a given occasion
    occasion = "birthday"
    trending_gifts = fetch_trending_gifts(API_URL, API_KEY, occasion)

    if trending_gifts is not None:
        print(f"Trending gifts for {occasion}: {trending_gifts}")
    else:
        print("Failed to fetch trending gifts.")
```
