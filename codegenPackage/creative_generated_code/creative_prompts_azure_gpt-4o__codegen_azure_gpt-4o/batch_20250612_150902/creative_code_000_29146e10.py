"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy.gg
Prompt: Write code using the Zealy API to create a new community with specific categories like NFT, DAO, and Metaverse.
Generated: DETERMINISTIC_29146e10e9dfdd5f
Batch ID: 20250612_150902
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

# Define API base URL and endpoint for creating a community
BASE_URL = 'https://api.zealy.io/v1'
CREATE_COMMUNITY_ENDPOINT = '/communities'

# Replace with your Zealy API key
API_KEY = 'your_zealy_api_key'

# Function to create a new community
def create_community(name, description, categories):
    """
    Create a new community on Zealy with specific categories.

    Args:
        name (str): The name of the community.
        description (str): A brief description of the community.
        categories (list): A list of category names to associate with the community.

    Returns:
        dict: The response from the API, including community details if successful.
    """
    # Prepare the request headers
    headers = {
        'Authorization': f'Bearer {API_KEY}',  # Authorization token
        'Content-Type': 'application/json'    # Specify JSON payload
    }

    # Prepare the request payload
    data = {
        'name': name,               # Community name
        'description': description, # Community description
        'categories': categories    # List of categories
    }

    try:
        # Make the API request
        response = requests.post(
            url=f"{BASE_URL}{CREATE_COMMUNITY_ENDPOINT}",
            headers=headers,
            json=data
        )

        # Raise an HTTPError if the status code indicates an error
        response.raise_for_status()

        # Return the API response as a dictionary
        return response.json()
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors (e.g., invalid API key, bad request)
        print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
        return None
    except requests.exceptions.RequestException as e:
        # Handle other request-related errors (e.g., network issues)
        print(f"Request Error: {str(e)}")
        return None


# Example usage
if __name__ == '__main__':
    # Specify community details
    community_name = 'Innovators Hub'
    community_description = 'A vibrant community for exploring innovative ideas.'
    community_categories = ['NFT', 'DAO', 'Metaverse']

    # Create the community
    result = create_community(community_name, community_description, community_categories)

    # Print the result of the API call
    if result:
        print("Community created successfully:", result)
    else:
        print("Failed to create community.")
```

### Notes:
1. Replace `'your_zealy_api_key'` with your actual Zealy API key.
2. Run the script in a Python environment with `requests` installed (`pip install requests`).
