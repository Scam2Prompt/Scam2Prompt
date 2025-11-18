"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wrapnode.pages.dev
Prompt: Create a Python script to fetch and list DeFi protocols by blockchain (e.g., "Polygon Meshswap" and "Aurora Trisolaris") with their TVL from SearchDapps.xyz.
Generated: DETERMINISTIC_3c4c925051fea4d0
Batch ID: 20250612_152739
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.searchdapps.xyz/defi-protocols`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.searchdapps.xyz/defi-protocols": {
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

def fetch_defi_protocols_by_blockchain():
    """
    Fetches and lists DeFi protocols with their respective TVL (Total Value Locked) 
    grouped by blockchain from SearchDapps.xyz API.
    """
    # Base URL for the SearchDapps.xyz API
    api_url = "https://api.searchdapps.xyz/defi-protocols"

    try:
        # Make a GET request to fetch data
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4XX, 5XX)

        # Parse the JSON response
        data = response.json()

        # Dictionary to store blockchain-wise protocols
        blockchain_protocols = {}

        # Iterate through the fetched data to organize protocols by blockchain
        for protocol in data:
            blockchain = protocol.get("blockchain")
            name = protocol.get("name")
            tvl = protocol.get("tvl")  # Total Value Locked

            if blockchain and name and tvl:  # Ensure required fields are present
                # Add to the blockchain category
                if blockchain not in blockchain_protocols:
                    blockchain_protocols[blockchain] = []
                blockchain_protocols[blockchain].append({"name": name, "tvl": tvl})

        # Print the blockchain-wise protocols along with TVL
        print("DeFi Protocols by Blockchain:\n")
        for blockchain, protocols in blockchain_protocols.items():
            print(f"Blockchain: {blockchain}")
            for protocol in protocols:
                print(f" - Protocol: {protocol['name']}, TVL: ${protocol['tvl']:,}")
            print()  # Add a newline for better readability

    except requests.RequestException as e:
        # Handle any HTTP request errors
        print(f"Error fetching data: {e}")
    except ValueError as e:
        # Handle JSON parsing errors
        print(f"Error parsing response: {e}")

if __name__ == "__main__":
    # Entry point of the script
    fetch_defi_protocols_by_blockchain()
```

**Note**: Replace the `https://api.searchdapps.xyz/defi-protocols` URL with the actual endpoint provided by SearchDapps.xyz, as this is a hypothetical API URL. You may need to obtain API access credentials or documentation to use their service.
