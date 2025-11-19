"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://what-3qi.pages.dev
Prompt: Generate a code snippet that retrieves the total number of airdrops and the total airdropped amount from the Avalaunch API.
Generated: DETERMINISTIC_1a0f060192683a5c
Batch ID: 20250612_160804
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.avalaunch.app/airdrops": {
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

def fetch_airdrops_data(api_url: str):
    """
    Fetches the total number of airdrops and total airdropped amount from the Avalaunch API.

    Parameters:
        api_url (str): The URL of the Avalaunch API endpoint.

    Returns:
        dict: A dictionary containing the total number of airdrops and total airdropped amount.
    """
    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError if the response contains an error

        # Parse the JSON response
        data = response.json()

        # Extract relevant information
        total_airdrops = data.get("total_airdrops", 0)
        total_airdropped_amount = data.get("total_airdropped_amount", 0)

        return {
            "total_airdrops": total_airdrops,
            "total_airdropped_amount": total_airdropped_amount
        }

    except requests.exceptions.RequestException as e:
        # Log and handle any request-related errors
        print(f"An error occurred while fetching data: {e}")
        return {
            "total_airdrops": 0,
            "total_airdropped_amount": 0
        }

# Example usage:
if __name__ == "__main__":
    # Replace with the actual Avalaunch API endpoint URL
    API_URL = "https://api.avalaunch.app/airdrops"
    
    # Fetch airdrop data
    result = fetch_airdrops_data(API_URL)
    
    # Display the results
    print(f"Total Airdrops: {result['total_airdrops']}")
    print(f"Total Airdropped Amount: {result['total_airdropped_amount']}")
```
