"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-ey3dlgbqo-offchain-labs.vercel.app
Prompt: Provide a code example for querying ecosystem charts and stats from the Arbitrum platform using its API.
Generated: DETERMINISTIC_3c76a62f944e6fc9
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.arbiscan.io/api": {
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

# Constants for the Arbitrum API
BASE_URL = "https://api.arbiscan.io/api"
API_KEY = "your_arbitrum_api_key_here"  # Replace with your actual API key

def fetch_ecosystem_stats():
    """
    Fetch ecosystem statistics and charts from the Arbitrum platform using its API.
    
    Returns:
        dict: Parsed JSON response containing ecosystem stats.
    Raises:
        Exception: For any errors during the API request or response processing.
    """
    try:
        # Define API parameters for querying ecosystem stats
        params = {
            "module": "stats",  # API module for stats
            "action": "ecosystemcharts",  # Specific API action
            "apikey": API_KEY  # API key for authentication
        }

        # Send GET request to the Arbitrum API
        response = requests.get(BASE_URL, params=params)

        # Raise an HTTPError if the status code is not 200
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check for success in the API response
        if data.get("status") != "1":
            raise Exception(f"API Error: {data.get('message', 'Unknown error')}")

        return data.get("result", {})
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"HTTP Request failed: {e}")
    except ValueError:
        raise Exception("Failed to parse JSON response.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Fetch and print ecosystem stats
        stats = fetch_ecosystem_stats()
        print("Arbitrum Ecosystem Stats:")
        print(stats)
    except Exception as e:
        # Handle and display any errors
        print(f"Error: {e}")
```

> **Note**: Replace `"your_arbitrum_api_key_here"` with your actual Arbitrum API key. Always keep your API key secure and avoid exposing it in public repositories.
