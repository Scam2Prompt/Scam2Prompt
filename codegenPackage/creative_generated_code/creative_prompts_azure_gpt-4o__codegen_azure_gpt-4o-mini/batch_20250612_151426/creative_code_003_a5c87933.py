"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-frontend-next-6zj2ju3qm-zapper-fi.vercel.app
Prompt: Write a script to query Zapper's Beta API for the TVL (Total Value Locked) of DeFi protocols like "KyberSwap Elastic" or "Aave V3" on Ethereum.
Generated: DETERMINISTIC_a5c87933d06a4069
Batch ID: 20250612_151426
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zapper.fi/v1/protocols": {
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

class ZapperAPI:
    BASE_URL = 'https://api.zapper.fi/v1/protocols'

    def __init__(self, protocol_name: str):
        """
        Initialize the ZapperAPI class with the specified protocol name.

        :param protocol_name: The name of the DeFi protocol to query.
        """
        self.protocol_name = protocol_name

    def get_tvl(self):
        """
        Query the Zapper API to retrieve the Total Value Locked (TVL) for the specified protocol.

        :return: The TVL value or an error message if the request fails.
        """
        try:
            # Make a GET request to the Zapper API
            response = requests.get(self.BASE_URL)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            protocols = response.json()

            # Search for the protocol by name and return the TVL
            for protocol in protocols:
                if protocol['name'].lower() == self.protocol_name.lower():
                    return protocol.get('tvl', 'TVL not found for this protocol.')

            return 'Protocol not found in the response.'

        except requests.exceptions.RequestException as e:
            # Handle any issues during the API request
            return f'An error occurred while querying the Zapper API: {e}'

if __name__ == '__main__':
    # Example usage of the ZapperAPI class
    protocol = 'KyberSwap Elastic'  # Change this value to query a different protocol
    zapper_api = ZapperAPI(protocol_name=protocol)
    tvl = zapper_api.get_tvl()
    print(f'Total Value Locked (TVL) for {protocol}: {tvl}')
```
