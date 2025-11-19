"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy.gg
Prompt: How can I use the Zealy API to create a community for gaming or DeFi projects?
Generated: DETERMINISTIC_9c10c881527f8ae9
Batch ID: 20250612_163156
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zealy.io/v1": {
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

# Zealy API Base URL
BASE_URL = "https://api.zealy.io/v1"

# Replace with your API Key from the Zealy API dashboard
API_KEY = "YOUR_ZEALY_API_KEY"

# Headers for authentication and content type
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def create_community(name, description, category, tags):
    """
    Creates a community in Zealy for gaming or DeFi projects.

    Parameters:
        name (str): Name of the community.
        description (str): Short description of the community.
        category (str): Category of the community (e.g., "Gaming" or "DeFi").
        tags (list): List of tags to associate with the community.

    Returns:
        dict: Response from the Zealy API, including community details if successful.
    """
    url = f"{BASE_URL}/communities"

    # Payload data for community creation
    payload = {
        "name": name,
        "description": description,
        "category": category,
        "tags": tags
    }

    try:
        # Make the POST request to create the community
        response = requests.post(url, json=payload, headers=HEADERS)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return the response JSON content if the request was successful
        return response.json()

    except requests.exceptions.RequestException as e:
        # Handle exceptions such as network errors or invalid API usage
        print(f"Error occurred while creating community: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Set community details
    community_name = "Awesome Gaming Community"
    community_description = "A community hub for gamers to connect, share, and collaborate."
    community_category = "Gaming"
    community_tags = ["gaming", "e-sports", "fun"]

    # Create the community and output the response
    result = create_community(community_name, community_description, community_category, community_tags)

    if result:
        print("Community created successfully:")
        print(result)
    else:
        print("Failed to create community. Please check the error above.")
```
