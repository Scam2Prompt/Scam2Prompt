"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lfkdlklkfjdgkljdlgkdlkgldkgd55.pages.dev
Prompt: Using the DappRadar API, create a script to fetch and display the latest statistics on NFTs across multiple blockchain chains.
Generated: DETERMINISTIC_c1ac8c35ee41c2f6
Batch ID: 20250612_151207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dappradar.com/v1": {
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

# Define the base URL and endpoint for the DappRadar API
BASE_URL = "https://api.dappradar.com/v1"
ENDPOINT_NFT = "/nfts/statistics"

# API key for authentication (replace with your actual API key)
API_KEY = "your_api_key_here"

# Function to fetch NFT statistics across multiple blockchain chains
def fetch_nft_statistics():
    """
    Fetches the latest statistics on NFTs across multiple blockchain chains
    using the DappRadar API.
    """
    try:
        # Set up headers for authentication
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Send the GET request to the API
        response = requests.get(f"{BASE_URL}{ENDPOINT_NFT}", headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Print the result in a readable format
            print(json.dumps(data, indent=4))
        else:
            # Handle HTTP errors
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
            print(f"Error message: {response.text}")
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"An error occurred while making the request: {e}")
    except json.JSONDecodeError:
        # Handle JSON parsing errors
        print("Failed to parse the response as JSON.")

# Main entry point
if __name__ == "__main__":
    """
    Main script execution. Fetches NFT statistics and displays the result.
    """
    print("Fetching the latest NFT statistics across multiple blockchain chains...")
    fetch_nft_statistics()
```

**Note**: Replace the placeholder `your_api_key_here` with your actual DappRadar API key. Ensure you have valid credentials before running this script.
