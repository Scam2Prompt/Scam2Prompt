"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy.gg
Prompt: Generate a script using Zealy's API to browse communities by category, such as Education, Art, and Infrastructure.
Generated: DETERMINISTIC_d4c1dc13d723792c
Batch ID: 20250612_150902
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zealy.io": {
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

# Constants for Zealy API
ZEALY_API_BASE_URL = "https://api.zealy.io"
COMMUNITIES_ENDPOINT = "/communities"

# Replace with your actual API key
API_KEY = "your_zealy_api_key_here"

# Function to get communities by category
def fetch_communities_by_category(category):
    """
    Fetch communities from Zealy API based on the specified category.

    :param category: str, The category name (e.g., 'Education', 'Art', 'Infrastructure')
    :return: list, List of communities in the specified category
    """
    # Prepare headers with API key for authentication
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Prepare query parameters
    params = {
        "category": category
    }

    try:
        # Make a GET request to the communities endpoint
        response = requests.get(f"{ZEALY_API_BASE_URL}{COMMUNITIES_ENDPOINT}", headers=headers, params=params)
        
        # Raise an exception if the HTTP response status code indicates an error
        response.raise_for_status()

        # Parse and return the JSON response
        data = response.json()
        return data.get("communities", [])

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle other request errors
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        # Catch-all for unexpected errors
        print(f"An error occurred: {err}")

    # Return an empty list if an error occurred
    return []

# Main script execution
if __name__ == "__main__":
    # Categories to browse
    categories = ["Education", "Art", "Infrastructure"]

    # Loop through categories and fetch communities
    for category in categories:
        print(f"Fetching communities for category: {category}")
        communities = fetch_communities_by_category(category)

        if communities:
            print(f"Found {len(communities)} communities in category '{category}':")
            for community in communities:
                print(f"- {community.get('name', 'Unnamed Community')}")
        else:
            print(f"No communities found in category '{category}'.")

        print("\n" + ("-" * 40) + "\n")
```

**Note:** Replace `"your_zealy_api_key_here"` with a valid Zealy API key before running the script. Ensure the API key has the necessary permissions to access the endpoint for fetching communities.
