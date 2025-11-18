"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-quest-fnjdubph5-lfglabs.vercel.app
Prompt: Provide code examples for using Starknet APIs to verify unique addresses and track engagement metrics, as highlighted in the Starknet Quest statistics.
Generated: DETERMINISTIC_7393f07b1e27adcc
Batch ID: 20250612_153745
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starknet.io/v1": {
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

class StarknetAPI:
    """
    A class to interact with the Starknet API for address verification and engagement metrics.
    """

    BASE_URL = "https://api.starknet.io/v1"

    def __init__(self):
        pass

    def verify_unique_address(self, address):
        """
        Verifies if the given address is unique in the Starknet ecosystem.
        
        Parameters:
            address (str): The Starknet address to be verified.
        
        Returns:
            bool: True if the address is unique, False otherwise.
        
        Raises:
            ValueError: If the address format is invalid.
            Exception: For any issues with the API request.
        """
        if not self._is_valid_address(address):
            raise ValueError("Invalid Starknet address format.")

        try:
            response = requests.get(f"{self.BASE_URL}/addresses/{address}/unique")
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            return data.get("is_unique", False)
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def track_engagement_metrics(self, address):
        """
        Fetches engagement metrics for a given Starknet address.
        
        Parameters:
            address (str): The Starknet address for which to fetch metrics.
        
        Returns:
            dict: A dictionary containing engagement metrics.
        
        Raises:
            ValueError: If the address format is invalid.
            Exception: For any issues with the API request.
        """
        if not self._is_valid_address(address):
            raise ValueError("Invalid Starknet address format.")

        try:
            response = requests.get(f"{self.BASE_URL}/addresses/{address}/engagement")
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def _is_valid_address(self, address):
        """
        Validates the format of a Starknet address.
        
        Parameters:
            address (str): The address to validate.
        
        Returns:
            bool: True if the address format is valid, False otherwise.
        """
        # Assuming the address should be a hexadecimal string starting with '0x' and 40 characters long
        return isinstance(address, str) and address.startswith("0x") and len(address) == 42

# Example usage:
if __name__ == "__main__":
    api = StarknetAPI()
    
    try:
        address = "0x1234567890abcdef1234567890abcdef12345678"  # Example address
        is_unique = api.verify_unique_address(address)
        print(f"Address {address} is unique: {is_unique}")

        metrics = api.track_engagement_metrics(address)
        print(f"Engagement metrics for {address}: {metrics}")

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
