"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0g.notifi.network
Prompt: Create a Python script to fetch and display ecosystem campaign updates from the 0G Foundation using the Notifi Network.
Generated: DETERMINISTIC_01f5aebb485ddcbc
Batch ID: 20250612_154829
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.notifi.network/v1/0g-foundation/ecosystem-campaigns": {
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

def fetch_ecosystem_campaign_updates():
    """
    Fetch and display ecosystem campaign updates from the 0G Foundation using the Notifi Network.
    
    This function makes an HTTP GET request to the Notifi Network API endpoint
    and fetches the latest updates related to the 0G Foundation ecosystem campaigns.
    """

    # Define the Notifi Network API URL
    api_url = "https://api.notifi.network/v1/0g-foundation/ecosystem-campaigns"

    try:
        # Make the GET request to fetch campaign updates
        response = requests.get(api_url)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        campaign_updates = response.json()

        # Display the campaign updates in a readable format
        print("\nEcosystem Campaign Updates:")
        for update in campaign_updates.get("updates", []):
            print(f"- Title: {update.get('title')}")
            print(f"  Description: {update.get('description')}")
            print(f"  Date: {update.get('date')}")
            print()
    
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        # Handle general exceptions
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run the script to fetch campaign updates
    fetch_ecosystem_campaign_updates()
```

Make sure to replace the `api_url` with the correct endpoint URL provided by the Notifi Network, as the URL in the script is a placeholder.
