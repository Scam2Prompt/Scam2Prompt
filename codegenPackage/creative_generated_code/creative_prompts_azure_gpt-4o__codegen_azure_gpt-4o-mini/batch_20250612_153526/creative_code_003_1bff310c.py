"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythchain.pages.dev
Prompt: Write code to interact with DeFi protocols like "Aave V3" or "Curve" using their APIs, and calculate the Total Value Locked (TVL) for platforms listed on SearchDapps.
Generated: DETERMINISTIC_1bff310c169ada3a
Batch ID: 20250612_153526
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/aave/protocol-v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.thegraph.com/subgraphs/name/curvefi/curve": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.searchdapps.com/v1/platforms": {
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
import json

class DeFiAPI:
    """
    A class to interact with DeFi protocols like Aave V3 and Curve.
    """

    def __init__(self):
        self.aave_api_url = "https://api.thegraph.com/subgraphs/name/aave/protocol-v2"
        self.curve_api_url = "https://api.thegraph.com/subgraphs/name/curvefi/curve"
        self.search_dapps_url = "https://api.searchdapps.com/v1/platforms"

    def fetch_aave_tvl(self):
        """
        Fetches the Total Value Locked (TVL) for Aave V3 protocol.
        
        Returns:
            float: The Total Value Locked in Aave V3.
        """
        query = """
        {
            reserves {
                totalLiquidity
            }
        }
        """
        try:
            response = requests.post(self.aave_api_url, json={'query': query})
            response.raise_for_status()
            data = response.json()
            tvl = sum(float(reserve['totalLiquidity']) for reserve in data['data']['reserves'])
            return tvl
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Aave TVL: {e}")
            return 0.0

    def fetch_curve_tvl(self):
        """
        Fetches the Total Value Locked (TVL) for Curve protocol.
        
        Returns:
            float: The Total Value Locked in Curve.
        """
        query = """
        {
            pools {
                totalLiquidity
            }
        }
        """
        try:
            response = requests.post(self.curve_api_url, json={'query': query})
            response.raise_for_status()
            data = response.json()
            tvl = sum(float(pool['totalLiquidity']) for pool in data['data']['pools'])
            return tvl
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Curve TVL: {e}")
            return 0.0

    def fetch_all_platforms(self):
        """
        Fetches a list of DeFi platforms from SearchDapps.
        
        Returns:
            list: A list of platforms with their names and types.
        """
        try:
            response = requests.get(self.search_dapps_url)
            response.raise_for_status()
            platforms = response.json()
            return platforms
        except requests.exceptions.RequestException as e:
            print(f"Error fetching platforms: {e}")
            return []

    def calculate_total_tvl(self):
        """
        Calculates the total TVL for Aave and Curve protocols, and returns a summary.
        
        Returns:
            dict: A dictionary containing the total TVL for Aave and Curve.
        """
        total_tvl = {
            "Aave TVL": self.fetch_aave_tvl(),
            "Curve TVL": self.fetch_curve_tvl()
        }
        return total_tvl

if __name__ == "__main__":
    defi_api = DeFiAPI()
    
    # Fetch and display total TVL for Aave and Curve
    total_tvl = defi_api.calculate_total_tvl()
    print(json.dumps(total_tvl, indent=4))

    # Fetch and display platforms from SearchDapps
    platforms = defi_api.fetch_all_platforms()
    print("DeFi Platforms from SearchDapps:")
    for platform in platforms:
        print(f"- {platform['name']} ({platform['type']})")
```
