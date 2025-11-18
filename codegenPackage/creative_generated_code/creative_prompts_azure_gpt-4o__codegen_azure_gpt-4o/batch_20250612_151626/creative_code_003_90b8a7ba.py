"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-paperhands.pages.dev
Prompt: Create a program that visualizes trading history data for tokens and NFTs using the Paperhands API.
Generated: DETERMINISTIC_90b8a7ba4b433cca
Batch ID: 20250612_151626
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paperhands.xyz/v1": {
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

# Constants
API_BASE_URL = "https://api.paperhands.xyz/v1"
TOKEN_ENDPOINT = "/tokens/"
NFT_ENDPOINT = "/nfts/"
TIMEOUT = 10  # API request timeout in seconds

def fetch_trading_data(endpoint: str, identifier: str):
    """
    Fetch trading history data from the Paperhands API.
    
    Args:
        endpoint (str): The API endpoint to query (tokens or nfts).
        identifier (str): The token or NFT identifier.
        
    Returns:
        dict: Trading history data.
    
    Raises:
        requests.exceptions.RequestException: If an API request error occurs.
    """
    url = f"{API_BASE_URL}{endpoint}{identifier}/history"
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def parse_trading_data(data: dict):
    """
    Parse trading history data into time and price lists for visualization.
    
    Args:
        data (dict): Trading history data.
        
    Returns:
        tuple: Lists of timestamps and prices.
    """
    if not data or "history" not in data:
        print("Invalid data format")
        return [], []
    
    timestamps = []
    prices = []
    for record in data["history"]:
        timestamps.append(record["timestamp"])
        prices.append(record["price"])
    
    return timestamps, prices

def visualize_trading_data(timestamps: list, prices: list, title: str):
    """
    Visualize trading history data using matplotlib.
    
    Args:
        timestamps (list): List of timestamps.
        prices (list): List of prices.
        title (str): Title for the plot.
    """
    if not timestamps or not prices:
        print("No data available to visualize")
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, prices, marker="o", linestyle="-", color="blue")
    plt.title(title)
    plt.xlabel("Timestamp")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to fetch and visualize trading history data for tokens and NFTs.
    """
    # Example inputs
    token_id = "example-token-id"
    nft_id = "example-nft-id"
    
    # Fetch and visualize token trading history
    token_data = fetch_trading_data(TOKEN_ENDPOINT, token_id)
    token_timestamps, token_prices = parse_trading_data(token_data)
    visualize_trading_data(token_timestamps, token_prices, f"Token: {token_id} Trading History")
    
    # Fetch and visualize NFT trading history
    nft_data = fetch_trading_data(NFT_ENDPOINT, nft_id)
    nft_timestamps, nft_prices = parse_trading_data(nft_data)
    visualize_trading_data(nft_timestamps, nft_prices, f"NFT: {nft_id} Trading History")

if __name__ == "__main__":
    main()
```
