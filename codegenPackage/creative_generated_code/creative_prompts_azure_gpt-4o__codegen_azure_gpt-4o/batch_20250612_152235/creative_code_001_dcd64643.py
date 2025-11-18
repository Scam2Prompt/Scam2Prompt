"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinknotyellowsale.pages.dev
Prompt: Generate a script to retrieve and display the total ETH staked, node operator count, and regional distribution statistics from Rocket Pool as described in the content.
Generated: DETERMINISTIC_dcd646434303bf10
Batch ID: 20250612_152235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.rocketpool.net/v1": {
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
# Import necessary modules
import requests
import json

# Define constants
ROCKET_POOL_API_URL = "https://api.rocketpool.net/v1"
ENDPOINTS = {
    "total_eth_staked": "/network/eth2/staked",
    "node_operators": "/node/operator/count",
    "regional_distribution": "/network/node/regional-distribution"
}

# Define function to fetch data from Rocket Pool API
def fetch_data(endpoint):
    """
    Fetch data from the Rocket Pool API.
    
    Parameters:
    endpoint (str): The API endpoint to fetch data from.

    Returns:
    dict: The response data in JSON format.
    """
    try:
        response = requests.get(ROCKET_POOL_API_URL + endpoint)
        response.raise_for_status()  # Ensure status code is 200
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Rocket Pool API: {e}")
        return None

# Define function to display retrieved statistics
def display_statistics():
    """
    Retrieve and display statistics for total ETH staked, 
    node operator count, and regional distribution from Rocket Pool.
    """
    # Fetch total ETH staked
    total_eth_data = fetch_data(ENDPOINTS["total_eth_staked"])
    if total_eth_data:
        total_eth_staked = total_eth_data.get("total_eth_staked", "Unknown")
        print(f"Total ETH Staked: {total_eth_staked} ETH")

    # Fetch node operator count
    node_operator_data = fetch_data(ENDPOINTS["node_operators"])
    if node_operator_data:
        node_operator_count = node_operator_data.get("count", "Unknown")
        print(f"Node Operator Count: {node_operator_count}")

    # Fetch regional distribution statistics
    regional_distribution_data = fetch_data(ENDPOINTS["regional_distribution"])
    if regional_distribution_data:
        print("Regional Distribution Statistics:")
        regions = regional_distribution_data.get("regions", [])
        for region in regions:
            region_name = region.get("region", "Unknown")
            node_count = region.get("node_count", "Unknown")
            print(f"  Region: {region_name}, Node Count: {node_count}")

# Main entry point
if __name__ == "__main__":
    print("Retrieving Rocket Pool statistics...")
    display_statistics()
```
