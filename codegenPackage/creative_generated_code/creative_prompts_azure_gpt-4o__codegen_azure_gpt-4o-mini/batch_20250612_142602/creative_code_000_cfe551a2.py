"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-llama.github.io
Prompt: Write a Python script using the DeFiLlama API to fetch and display real-time Total Value Locked (TVL) data for a specific DeFi protocol.
Generated: DETERMINISTIC_cfe551a2419fecf9
Batch ID: 20250612_142602
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

class DeFiProtocolTVL:
    """
    A class to fetch and display Total Value Locked (TVL)
    data for a specific DeFi protocol using the DeFiLlama API.
    """

    def __init__(self, protocol_name):
        """
        Initialize the DeFiProtocolTVL class with the protocol name.

        :param protocol_name: The name of the DeFi protocol to fetch TVL data for.
        """
        self.protocol_name = protocol_name
        self.api_url = "https://api.llama.fi/protocols"

    def fetch_tvl_data(self):
        """
        Fetch the TVL data for the specified DeFi protocol.

        :return: TVL data as a dictionary if successful, None otherwise.
        """
        try:
            # Send GET request to the DeFiLlama API
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            protocols_data = response.json()

            # Find the protocol data
            for protocol in protocols_data:
                if protocol['name'].lower() == self.protocol_name.lower():
                    return {
                        'name': protocol['name'],
                        'tvl': protocol['tvl'],
                        'chain': protocol['chain'],
                        'url': protocol['url']
                    }

            print(f"No TVL data found for protocol: {self.protocol_name}")
            return None

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from DeFiLlama API: {e}")
            return None

    def display_tvl(self):
        """
        Fetch and display the TVL data for the protocol.
        """
        tvl_data = self.fetch_tvl_data()
        if tvl_data is not None:
            print(f"DeFi Protocol: {tvl_data['name']}")
            print(f"Total Value Locked (TVL): ${tvl_data['tvl']:,}")
            print(f"Chain: {tvl_data['chain']}")
            print(f"More Info: {tvl_data['url']}")
        else:
            print("Failed to retrieve TVL data.")

if __name__ == "__main__":
    # Specify the DeFi protocol you want to fetch data for
    protocol_name = "Aave"  # Change this to the desired protocol name
    tvl_fetcher = DeFiProtocolTVL(protocol_name)
    tvl_fetcher.display_tvl()
```
