"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkscan-sepolia.netlify.app
Prompt: Write code to interact with the Starkscan API and fetch the number of blocks, transactions, contracts, and events currently recorded on Starknet.
Generated: DETERMINISTIC_09988c4f2263ea13
Batch ID: 20250612_151347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starkscan.co/api/v0/": {
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
    A class to interact with the Starkscan API to fetch blockchain data from Starknet.
    """

    BASE_URL = "https://api.starkscan.co/api/v0/"  # Base URL for Starkscan API

    def __init__(self):
        """
        Initializes the StarknetAPI class.
        """
        self.session = requests.Session()  # Create a persistent session

    def fetch_data(self):
        """
        Fetches the number of blocks, transactions, contracts, and events from Starknet.

        Returns:
            dict: A dictionary containing the count of blocks, transactions, contracts, and events.
        """
        endpoint = "stats"  # API endpoint for fetching stats
        url = f"{self.BASE_URL}{endpoint}"
        
        try:
            response = self.session.get(url)  # Make a GET request to the API
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()  # Parse the JSON response
            return {
                "blocks": data.get("blocks"),
                "transactions": data.get("transactions"),
                "contracts": data.get("contracts"),
                "events": data.get("events"),
            }
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching data: {e}")
            return None
        except ValueError:
            print("Error parsing JSON response.")
            return None

if __name__ == "__main__":
    """
    Main execution point of the script.
    Fetches the blockchain data and prints it to the console.
    """
    api = StarknetAPI()  # Instantiate the StarknetAPI class
    data = api.fetch_data()  # Fetch the blockchain data
    
    if data:  # Check if data was successfully retrieved
        print("Starknet Statistics:")
        print(f"Blocks: {data['blocks']}")
        print(f"Transactions: {data['transactions']}")
        print(f"Contracts: {data['contracts']}")
        print(f"Events: {data['events']}")
```
