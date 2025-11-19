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
  "https://api.bitscrunch.io/v1": {
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

class BitsCrunchAPI:
    """
    A class to interact with the BitsCrunch API for retrieving staking information.
    """

    BASE_URL = "https://api.bitscrunch.io/v1"  # Base URL for the BitsCrunch API

    def __init__(self, api_key):
        """
        Initializes the BitsCrunchAPI instance with the given API key.

        :param api_key: The API key for authentication with the BitsCrunch API.
        """
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def get_staked_info(self, operator_address):
        """
        Fetches the total BCUT staked by a specific operator and the rewards earned by their delegators.

        :param operator_address: The address of the operator to query.
        :return: A dictionary containing total staked and rewards information.
        :raises ValueError: If the operator_address is not valid.
        :raises Exception: If an error occurs while making the API request.
        """
        if not operator_address:
            raise ValueError("Operator address must not be empty.")

        endpoint = f"{self.BASE_URL}/staking/operators/{operator_address}/info"
        
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()  # Parse the JSON response

            # Check if the response contains the expected keys
            if 'total_staked' in data and 'rewards' in data:
                return {
                    "total_staked": data['total_staked'],
                    "rewards": data['rewards']
                }
            else:
                raise Exception("Unexpected response format from API.")

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    OPERATOR_ADDRESS = "operator_address_here"

    bitscrunch_api = BitsCrunchAPI(API_KEY)

    try:
        staked_info = bitscrunch_api.get_staked_info(OPERATOR_ADDRESS)
        print(f"Total BCUT Staked: {staked_info['total_staked']}")
        print(f"Rewards Earned: {staked_info['rewards']}")
    except Exception as e:
        print(f"Error: {e}")
```

Make sure to replace `"your_api_key_here"` and `"operator_address_here"` with the actual API key and operator address when running the code.
