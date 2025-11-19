"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-llama.github.io
Prompt: Provide an example of how to use DeFiLlama for protocol discovery and research on new DeFi projects.
Generated: DETERMINISTIC_90e81f327282659f
Batch ID: 20250612_155650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi/protocols": {
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

class DeFiProtocolDiscovery:
    """
    A class to interact with DeFiLlama API for discovering DeFi protocols and their metrics.
    """

    BASE_URL = "https://api.llama.fi/protocols"

    def __init__(self):
        """
        Initializes the DeFiProtocolDiscovery instance.
        """
        self.protocols = []

    def fetch_protocols(self):
        """
        Fetches the list of DeFi protocols from DeFiLlama.
        Sends a GET request to the DeFiLlama API and populates the protocols list.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            self.protocols = response.json()  # Convert response to JSON format
            print(f"Fetched {len(self.protocols)} protocols successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching protocols: {e}")

    def display_protocols(self):
        """
        Displays the fetched protocols in a user-friendly format.
        """
        if not self.protocols:
            print("No protocols available. Please fetch protocols first.")
            return
        
        print("Available DeFi Protocols:")
        for protocol in self.protocols:
            name = protocol.get("name", "N/A")
            chain = protocol.get("chain", "N/A")
            tvl = protocol.get("tvl", "N/A")  # Total Value Locked
            url = protocol.get("url", "N/A")
            print(f"- Name: {name}, Chain: {chain}, TVL: {tvl}, URL: {url}")

def main():
    """
    Main function to execute protocol discovery and display results.
    """
    defi_discovery = DeFiProtocolDiscovery()
    defi_discovery.fetch_protocols()  # Fetch protocols from DeFiLlama
    defi_discovery.display_protocols()  # Display the fetched protocols

if __name__ == "__main__":
    main()
```
