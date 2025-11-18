"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defifillama.com
Prompt: Create a script that integrates the DeFiLlama API to monitor real-time changes in TVL for a given blockchain network.
Generated: DETERMINISTIC_47c2e8a8e93594f7
Batch ID: 20250612_154708
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi/v2/chains": {
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
import time

def get_tvl(network):
    """
    Fetch the Total Value Locked (TVL) for a given blockchain network using the DeFiLlama API.

    Args:
        network (str): Name of the blockchain network (e.g., 'ethereum', 'bsc', 'polygon').

    Returns:
        float: Current TVL value for the specified network, or None if an error occurs.
    """
    base_url = "https://api.llama.fi/v2/chains"
    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        chains = response.json()

        # Find the matching network in the list of chains
        for chain in chains:
            if chain["name"].lower() == network.lower():
                return chain["tvl"]

        print(f"Network '{network}' not found in the list of chains.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching TVL data: {e}")
        return None

def monitor_tvl(network, interval=60):
    """
    Monitor real-time changes in TVL for a given blockchain network.

    Args:
        network (str): Name of the blockchain network to monitor.
        interval (int): Time interval (in seconds) between API requests.
    """
    print(f"Monitoring TVL for '{network}' every {interval} seconds.\nPress Ctrl+C to stop.")
    try:
        while True:
            tvl = get_tvl(network)
            if tvl is not None:
                print(f"Current TVL for {network}: ${tvl:,.2f}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Input the blockchain network and monitoring interval
    network_name = input("Enter the blockchain network name (e.g., 'ethereum', 'bsc', 'polygon'): ").strip()
    polling_interval = input("Enter the monitoring interval in seconds (default is 60): ").strip()

    try:
        polling_interval = int(polling_interval) if polling_interval else 60
        monitor_tvl(network_name, polling_interval)
    except ValueError:
        print("Invalid interval. Please enter a valid integer.")
```
