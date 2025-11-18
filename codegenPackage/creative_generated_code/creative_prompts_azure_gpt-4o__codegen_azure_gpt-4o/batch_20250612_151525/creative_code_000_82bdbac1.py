"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsc-info.mdex.com
Prompt: Write a Python script using the Mdex API to fetch real-time trading pair data and display the current prices.
Generated: DETERMINISTIC_82bdbac17e3ccf45
Batch ID: 20250612_151525
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mdex.com": {
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

# Mdex API base URL
MDEX_API_BASE_URL = "https://api.mdex.com"

def fetch_trading_pair_data(pair: str):
    """
    Fetches real-time trading data for a given trading pair from the Mdex API.
    
    Args:
        pair (str): The trading pair to fetch data for (e.g., "BTC_USDT").
    
    Returns:
        dict: A dictionary containing trading data if successful.
    """
    try:
        # Construct the API endpoint URL
        endpoint = f"{MDEX_API_BASE_URL}/market/real?symbol={pair}"
        
        # Make the request to the Mdex API
        response = requests.get(endpoint, timeout=10)  # Set a timeout for reliability
        
        # Check if the response status code indicates success
        response.raise_for_status()

        # Parse the JSON data returned by the API
        data = response.json()

        # Check if the API returned the expected data
        if data.get("success"):
            return data.get("data", {})
        else:
            print(f"Error: API returned an unsuccessful response for pair {pair}")
            return None

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while making the request - {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def display_trading_data(pair_data: dict):
    """
    Displays trading pair data in a readable format.
    
    Args:
        pair_data (dict): Trading data returned by the Mdex API.
    """
    if not pair_data:
        print("No data available to display.")
        return
    
    # Extract relevant information from the trading data
    symbol = pair_data.get("symbol", "Unknown Pair")
    price = pair_data.get("close", "Unknown Price")
    high = pair_data.get("high", "Unknown High")
    low = pair_data.get("low", "Unknown Low")

    # Display the data
    print(f"Trading Pair: {symbol}")
    print(f"Current Price: {price}")
    print(f"24h High: {high}")
    print(f"24h Low: {low}")

def main():
    """
    Main function to fetch and display trading pair data using the Mdex API.
    """
    # Prompt the user to enter the trading pair they want to check
    trading_pair = input("Enter the trading pair (e.g., BTC_USDT): ").strip()

    # Fetch trading pair data
    pair_data = fetch_trading_pair_data(trading_pair)

    # Display the fetched trading pair data
    display_trading_data(pair_data)

if __name__ == "__main__":
    # Entry point of the script
    main()
```

Before running this script, ensure you have network connectivity and that the Mdex API is accessible at the provided URL. You may also need to verify the trading pair format supported by Mdex. Install the required Python library (`requests`) using `pip install requests`.
