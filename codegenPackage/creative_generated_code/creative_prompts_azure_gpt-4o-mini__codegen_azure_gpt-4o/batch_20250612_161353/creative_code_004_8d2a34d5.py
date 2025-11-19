"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Illustrate how to use the bitsCrunch API to get the total BCUT staked by a specific operator and the rewards earned by their delegators.
Generated: DETERMINISTIC_8d2a34d5d99547b2
Batch ID: 20250612_161353
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bitscrunch.com/v1": {
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

# Constants
API_BASE_URL = "https://api.bitscrunch.com/v1"  # Replace with the actual base URL of the bitsCrunch API
OPERATOR_ID = "your-operator-id"  # Replace with the specific operator ID

def get_bcut_staked_and_rewards(operator_id):
    """
    Fetches the total BCUT staked by a specific operator and the rewards earned by their delegators.

    :param operator_id: The ID of the operator to fetch data for.
    :return: A dictionary containing the total BCUT staked and rewards earned by delegators.
    """
    try:
        # Endpoint to fetch staking details
        staking_endpoint = f"{API_BASE_URL}/staking/{operator_id}"
        
        # Make the request to the API
        response = requests.get(staking_endpoint)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()

        # Extract relevant details
        bcut_staked = data.get("bcutStaked", 0)
        delegator_rewards = data.get("delegatorRewards", 0)

        return {
            "BCUT Staked": bcut_staked,
            "Delegator Rewards": delegator_rewards
        }

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 404, 500)
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        print(f"Request error occurred: {req_err}")
        return None
    except KeyError as key_err:
        # Handle missing keys in the response
        print(f"Key error in response data: {key_err}")
        return None
    except Exception as err:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {err}")
        return None


# Example usage
if __name__ == "__main__":
    # Fetch BCUT stake and rewards for the specified operator
    result = get_bcut_staked_and_rewards(OPERATOR_ID)
    
    if result:
        print("BCUT Staked:", result["BCUT Staked"])
        print("Delegator Rewards:", result["Delegator Rewards"])
    else:
        print("Failed to fetch staking data.")
```
