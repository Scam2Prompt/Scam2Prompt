"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica18.vercel.app
Prompt: Generate a script to fetch and display stats for blockchain networks like Solana, Ethereum, and Polygon, inspired by the functionality described on Matrica.
Generated: DETERMINISTIC_2a57071d07b92d4a
Batch ID: 20250612_153401
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.solana.com/v1/stats": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.polygon.io/v1/stats": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.etherscan.io/api": {
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

def fetch_blockchain_stats(network_name):
    """
    Fetch stats for a given blockchain network.
    
    Args:
        network_name (str): Name of the blockchain network (e.g., 'Solana', 'Ethereum', 'Polygon').
    
    Returns:
        dict: A dictionary containing the fetched stats if successful, otherwise None.
    """
    # Define the base URLs for each blockchain network
    API_ENDPOINTS = {
        "Solana": "https://api.solana.com/v1/stats",  # Placeholder endpoint for Solana stats
        "Ethereum": "https://api.etherscan.io/api",   # Placeholder endpoint for Ethereum stats
        "Polygon": "https://api.polygon.io/v1/stats"  # Placeholder endpoint for Polygon stats
    }

    # Validate the network name
    if network_name not in API_ENDPOINTS:
        raise ValueError(f"Unsupported network: {network_name}. Supported networks are: {', '.join(API_ENDPOINTS.keys())}")

    # Prepare the API URL
    url = API_ENDPOINTS[network_name]

    try:
        # Make the HTTP request to fetch stats
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        # Handle network errors
        print(f"Error fetching data for {network_name}: {e}")
        return None
    except ValueError as e:
        # Handle JSON parsing errors
        print(f"Error parsing response for {network_name}: {e}")
        return None


def display_blockchain_stats(network_name, stats):
    """
    Display blockchain stats in a user-friendly format.
    
    Args:
        network_name (str): Name of the blockchain network.
        stats (dict): Dictionary containing the stats to display.
    """
    if stats:
        print(f"Stats for {network_name}:")
        for key, value in stats.items():
            print(f"- {key}: {value}")
    else:
        print(f"No stats available for {network_name}.")


def main():
    """
    Main function to fetch and display stats for multiple blockchain networks.
    """
    # List of blockchain networks to retrieve stats for
    networks = ["Solana", "Ethereum", "Polygon"]

    for network in networks:
        print(f"\nFetching stats for {network}...")
        stats = fetch_blockchain_stats(network)
        display_blockchain_stats(network, stats)


if __name__ == "__main__":
    main()
```
