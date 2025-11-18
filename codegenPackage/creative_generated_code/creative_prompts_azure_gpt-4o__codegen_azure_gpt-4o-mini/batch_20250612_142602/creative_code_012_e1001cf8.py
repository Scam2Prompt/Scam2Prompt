"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama-app.github.io
Prompt: Write a script to fetch and display data from the DefiLlama API for non-EVM chains like Solana and Cardano.
Generated: DETERMINISTIC_e1001cf828e68a5b
Batch ID: 20250612_142602
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi": {
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

class DefiLlamaAPI:
    BASE_URL = "https://api.llama.fi"

    def __init__(self):
        """
        Initializes the DefiLlamaAPI class.
        """
        self.non_evm_chains = ["solana", "cardano"]

    def fetch_data(self):
        """
        Fetches data for non-EVM chains from the DefiLlama API.

        Returns:
            dict: A dictionary containing the fetched data.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/v1/protocols")
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()
            # Filter data for non-EVM chains
            non_evm_data = [protocol for protocol in data if protocol['chain'] in self.non_evm_chains]

            return non_evm_data

        except requests.RequestException as e:
            print(f"Error fetching data from DefiLlama API: {e}")
            return []

    def display_data(self, data):
        """
        Displays the fetched data in a readable format.

        Args:
            data (list): A list of dictionaries containing protocol data.
        """
        if not data:
            print("No data available to display.")
            return

        for protocol in data:
            print(f"Name: {protocol['name']}")
            print(f"Chain: {protocol['chain']}")
            print(f"TVL: ${protocol['tvL']:.2f}")
            print(f"Category: {protocol['category']}")
            print("=" * 40)

def main():
    """
    Main function to execute the script.
    """
    api = DefiLlamaAPI()
    data = api.fetch_data()
    api.display_data(data)

if __name__ == "__main__":
    main()
```
