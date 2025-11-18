"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hawksight-fi.pages.dev
Prompt: Provide a list of Solana DeFi protocols supported by Hawksight, and write a script to fetch yield APYs from these protocols using Hawksight's API.
Generated: DETERMINISTIC_8762ebc23f47f32b
Batch ID: 20250612_153424
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hawksight.xyz": {
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

class HawksightAPI:
    BASE_URL = "https://api.hawksight.xyz"

    @staticmethod
    def fetch_defi_protocols():
        """
        Fetch the list of Solana DeFi protocols supported by Hawksight.

        Returns:
            list: A list of supported DeFi protocols.
        """
        response = requests.get(f"{HawksightAPI.BASE_URL}/solana/protocols")
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()

    @staticmethod
    def fetch_yield_apys(protocol_name):
        """
        Fetch the yield APYs for a specific DeFi protocol.

        Args:
            protocol_name (str): The name of the DeFi protocol.

        Returns:
            dict: A dictionary containing the yield APYs for the specified protocol.
        """
        url = f"{HawksightAPI.BASE_URL}/solana/protocols/{protocol_name}/apys"
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()

def main():
    """
    Main function to execute the fetching of DeFi protocols and their associated yield APYs.
    """
    try:
        # Fetch supported DeFi protocols
        protocols = HawksightAPI.fetch_defi_protocols()
        print("Supported DeFi Protocols:")
        for protocol in protocols:
            print(f"- {protocol['name']}")

        # Fetch and display APYs for each protocol
        for protocol in protocols:
            protocol_name = protocol['name']
            yield_data = HawksightAPI.fetch_yield_apys(protocol_name)
            print(f"Yield APYs for {protocol_name}: {yield_data}")

    except requests.exceptions.RequestException as e:
        # Handle request errors
        print(f"An error occurred while fetching data: {e}")

if __name__ == "__main__":
    main()
```
