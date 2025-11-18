"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium-frontend.pages.dev
Prompt: Write a function to interact with Raydium's API and retrieve the total value locked (TVL) across all pools.
Generated: DETERMINISTIC_6f6b2571bb7234ae
Batch ID: 20250612_150545
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.raydium.io/v2": {
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

class RaydiumAPI:
    BASE_URL = "https://api.raydium.io/v2"

    @staticmethod
    def get_total_value_locked():
        """
        Retrieve the total value locked (TVL) across all pools from Raydium's API.
        
        Returns:
            float: The total value locked in USD or raises an error if the request fails.
        """
        try:
            # Define the endpoint for fetching pool data
            endpoint = f"{RaydiumAPI.BASE_URL}/pools"
            response = requests.get(endpoint)

            # Raise an error for bad responses
            response.raise_for_status()

            # Parse the JSON response
            pools_data = response.json()

            # Calculate the total value locked
            total_value_locked = sum(pool['tvl'] for pool in pools_data if 'tvl' in pool)

            return total_value_locked

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise
        except KeyError as key_err:
            print(f"Key error: {key_err} - Check the API response structure.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise


if __name__ == "__main__":
    # Example usage of the RaydiumAPI to get the total value locked
    try:
        tvl = RaydiumAPI.get_total_value_locked()
        print(f"Total Value Locked (TVL) across all pools: ${tvl:.2f}")
    except Exception as e:
        print("Failed to retrieve total value locked.")
```
