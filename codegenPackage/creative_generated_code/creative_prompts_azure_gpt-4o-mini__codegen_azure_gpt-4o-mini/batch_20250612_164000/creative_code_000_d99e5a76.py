"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Write a Python script to connect to the Arweave network and retrieve the current block height from the API.
Generated: DETERMINISTIC_d99e5a76fcd3eb4d
Batch ID: 20250612_164000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net": {
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

class ArweaveAPI:
    """Class to interact with the Arweave API."""

    BASE_URL = "https://arweave.net"

    def __init__(self):
        """Initialize the ArweaveAPI class."""
        pass

    def get_block_height(self):
        """Retrieve the current block height from the Arweave network.

        Returns:
            int: The current block height.

        Raises:
            ConnectionError: If there is an issue connecting to the Arweave API.
            ValueError: If the response from the API is not valid.
        """
        try:
            # Send a GET request to the Arweave API
            response = requests.get(f"{self.BASE_URL}/block_height")

            # Check if the request was successful
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Validate the response
            if not isinstance(data, int):
                raise ValueError("Invalid response format: Expected an integer.")

            return data

        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error connecting to the Arweave API: {e}")
        except ValueError as ve:
            raise ValueError(f"Error processing the response: {ve}")

if __name__ == "__main__":
    # Create an instance of the ArweaveAPI class
    arweave_api = ArweaveAPI()

    try:
        # Retrieve and print the current block height
        block_height = arweave_api.get_block_height()
        print(f"Current Arweave block height: {block_height}")

    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"An error occurred: {e}")
```
