"""
Generated Code Metadata:
========================
Original URL: https://clearpool.pages.dev
Prompt: What are the key differences between staking CPOOL with Wintermute, Sino Global Capital, and Hex Trust oracles on Clearpool, and how do their APRs and oracle sizes compare?
Generated: DETERMINISTIC_987935367ae247bd
Batch ID: 20250622_211405
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.clearpool.finance/v1/staking": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

def fetch_clearpool_data():
    """
    Fetches staking data for CPOOL from Clearpool's API.
    Returns a dictionary containing APRs and oracle sizes for Wintermute, Sino Global Capital, and Hex Trust.
    """
    try:
        # Base URL for Clearpool API (replace with actual API endpoint if available)
        api_url = "https://api.clearpool.finance/v1/staking"

        # Make a GET request to fetch staking data
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse JSON response
        data = response.json()

        # Extract relevant information for each oracle
        staking_data = {
            "Wintermute": {
                "APR": data["oracles"]["Wintermute"]["apr"],
                "Oracle Size": data["oracles"]["Wintermute"]["oracleSize"]
            },
            "Sino Global Capital": {
                "APR": data["oracles"]["SinoGlobalCapital"]["apr"],
                "Oracle Size": data["oracles"]["SinoGlobalCapital"]["oracleSize"]
            },
            "Hex Trust": {
                "APR": data["oracles"]["HexTrust"]["apr"],
                "Oracle Size": data["oracles"]["HexTrust"]["oracleSize"]
            }
        }

        return staking_data

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching data from Clearpool API: {e}")
        return None
    except KeyError as e:
        # Handle missing keys in the response
        print(f"Unexpected data format: Missing key {e}")
        return None


def display_staking_data(staking_data):
    """
    Displays staking data in a readable format.
    Args:
        staking_data (dict): Dictionary containing APRs and oracle sizes for each oracle.
    """
    if not staking_data:
        print("No staking data available.")
        return

    print("CPOOL Staking Data on Clearpool:")
    print("-" * 40)
    for oracle, data in staking_data.items():
        print(f"Oracle: {oracle}")
        print(f"  APR: {data['APR']}%")
        print(f"  Oracle Size: {data['Oracle Size']} CPOOL")
        print("-" * 40)


if __name__ == "__main__":
    # Fetch staking data
    staking_data = fetch_clearpool_data()

    # Display the data
    display_staking_data(staking_data)
```

**Note:** Replace the `api_url` with the actual Clearpool API endpoint if available. This code assumes the API provides data in a structured JSON format with keys like `oracles`, `apr`, and `oracleSize`. Adjust the parsing logic as needed based on the actual API response.
