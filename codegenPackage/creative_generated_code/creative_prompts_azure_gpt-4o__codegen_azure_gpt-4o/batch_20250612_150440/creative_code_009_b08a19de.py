"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-ivbwkx2fp-offchain-labs.vercel.app
Prompt: Write a script to query and display charts or stats related to the Arbitrum ecosystem using publicly available APIs or documentation.
Generated: DETERMINISTIC_b08a19def18ef796
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi/chains": {
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
import matplotlib.pyplot as plt
import sys

# Constants
ARBITRUM_STATS_API = "https://api.llama.fi/chains"  # Example API endpoint for blockchain stats
ARBITRUM_CHAIN_NAME = "Arbitrum"  # The chain we are querying stats about

def fetch_arbitrum_data():
    """
    Fetches Arbitrum-related statistics from the public API.
    
    Returns:
        dict: Data related to Arbitrum ecosystem.
    Raises:
        Exception: If the API request fails or data is unavailable.
    """
    try:
        response = requests.get(ARBITRUM_STATS_API, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        chains_data = response.json()
        
        # Filter Arbitrum-specific data
        arbitrum_data = next((chain for chain in chains_data if chain["name"] == ARBITRUM_CHAIN_NAME), None)
        if not arbitrum_data:
            raise ValueError("Arbitrum data not found in the response.")
        
        return arbitrum_data
    except requests.exceptions.RequestException as req_err:
        print(f"Error fetching data from API: {req_err}")
        sys.exit(1)
    except ValueError as val_err:
        print(f"Error processing data: {val_err}")
        sys.exit(1)

def plot_arbitrum_stats(arbitrum_data):
    """
    Plots statistics related to Arbitrum.
    
    Args:
        arbitrum_data (dict): Data containing Arbitrum stats.
    """
    try:
        # Extract relevant stats for plotting
        labels = ["TVL", "24h Volume", "24h Change (%)"]
        values = [
            arbitrum_data.get("tvl", 0),
            arbitrum_data.get("volume_24h", 0),
            arbitrum_data.get("change_1d", 0)
        ]

        # Plot the stats
        fig, ax = plt.subplots()
        ax.bar(labels, values, color=["blue", "green", "orange"])
        ax.set_title("Arbitrum Ecosystem Stats")
        ax.set_ylabel("Value")
        ax.set_xlabel("Metrics")

        # Display the values on top of each bar
        for i, v in enumerate(values):
            ax.text(i, v + (max(values) * 0.02), f"{v:.2f}", ha='center')
        
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error while plotting data: {e}")
        sys.exit(1)

def main():
    """
    Main entry point of the script.
    Fetches Arbitrum data and displays a chart of key statistics.
    """
    print("Fetching Arbitrum ecosystem stats...")
    arbitrum_data = fetch_arbitrum_data()
    
    print(f"Data retrieved successfully: {arbitrum_data}")
    print("Plotting stats...")
    
    plot_arbitrum_stats(arbitrum_data)

if __name__ == "__main__":
    main()
```
