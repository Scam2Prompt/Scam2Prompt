"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stader.pages.dev
Prompt: Create a script to fetch and display the current TVL and total rewards paid by Stader Labs across all blockchains using their API or platform data.
Generated: DETERMINISTIC_1ba2a7c81267aaa2
Batch ID: 20250612_151158
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.staderlabs.com/v1/global-stats": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is the Python script that fulfills your request:

```python
import requests

def fetch_stader_data():
    """
    Fetch the current TVL (Total Value Locked) and total rewards paid 
    by Stader Labs across all blockchains using their API.

    Returns:
        dict: A dictionary containing TVL and total rewards paid.
    """
    # Base URL for Stader Labs API (replace with the actual endpoint if known)
    API_URL = "https://api.staderlabs.com/v1/global-stats"

    try:
        # Send GET request to fetch data
        response = requests.get(API_URL)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract relevant fields (assuming 'tvl' and 'total_rewards_paid' are in the response)
        tvl = data.get("tvl", "Data unavailable")
        total_rewards_paid = data.get("total_rewards_paid", "Data unavailable")

        return {"tvl": tvl, "total_rewards_paid": total_rewards_paid}

    except requests.exceptions.RequestException as e:
        # Handle any error during the API request
        print(f"Error fetching data from Stader Labs API: {e}")
        return {"tvl": "Error", "total_rewards_paid": "Error"}

def display_stader_data():
    """
    Fetch and display the TVL and total rewards paid by Stader Labs.
    """
    # Fetch data
    stader_data = fetch_stader_data()

    # Display the results
    print("Stader Labs Data:")
    print(f"Total Value Locked (TVL): {stader_data['tvl']}")
    print(f"Total Rewards Paid: {stader_data['total_rewards_paid']}")

if __name__ == "__main__":
    # Main entry point for the script
    display_stader_data()
```

### Notes:
- Replace the `API_URL` with the correct endpoint if the Stader Labs API documentation provides it.
- This script assumes the API has `tvl` and `total_rewards_paid` keys in its JSON response; adjust field names based on the actual API schema.
- Proper error handling is in place, and fallback values are provided if data is unavailable.
