"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifck3tvl2afu34735yd3ul2g5ifecjinp2c7na6kdjx3q2no76q5i.ipfs.dweb.link
Prompt: Create a Python script to query the Joe exchange API for token price data, focusing on $JOE, AVAX, and BTC.b, and visualize the price changes over the last 24 hours.
Generated: DETERMINISTIC_0bcd9c3b3e3ced69
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.joe.xyz/v1/tokens": {
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
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Constants for the Joe exchange API
JOE_API_URL = "https://api.joe.xyz/v1/tokens"
TOKENS = ["JOE", "AVAX", "BTC.b"]

def fetch_token_price_data():
    """
    Fetch price data for specified tokens from the Joe exchange API.

    Returns:
        dict: A dictionary containing token price data.
    """
    try:
        response = requests.get(JOE_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Filter data for the tokens of interest
        token_data = {token: data.get(token, None) for token in TOKENS}
        return token_data
    except requests.RequestException as e:
        print(f"Error fetching data from Joe exchange API: {e}")
        return {}
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return {}

def process_price_data(token_data):
    """
    Process the fetched token data into a DataFrame for visualization.

    Args:
        token_data (dict): A dictionary of token data.

    Returns:
        pd.DataFrame: A DataFrame containing the processed price data.
    """
    # Prepare a DataFrame to store price data for each token
    processed_data = []
    
    for token, data in token_data.items():
        if data:
            # Assume data contains 'price' and 'timestamp' keys
            price = data.get('price', None)
            timestamp = data.get('timestamp', None)
            processed_data.append({
                'token': token,
                'price': price,
                'timestamp': datetime.fromtimestamp(timestamp) if timestamp else None
            })

    return pd.DataFrame(processed_data)

def plot_price_changes(df):
    """
    Plot the price changes of the tokens over the last 24 hours.

    Args:
        df (pd.DataFrame): DataFrame containing the token price data.
    """
    # Ensure the DataFrame is valid and has data
    if df.empty:
        print("No data available for plotting.")
        return

    plt.figure(figsize=(12, 6))
    for token in df['token'].unique():
        token_df = df[df['token'] == token]
        plt.plot(token_df['timestamp'], token_df['price'], label=token)
    
    plt.title("Token Price Changes Over Last 24 Hours")
    plt.xlabel("Time")
    plt.ylabel("Price (in USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the script logic.
    """
    token_data = fetch_token_price_data()
    price_df = process_price_data(token_data)
    plot_price_changes(price_df)

if __name__ == "__main__":
    main()
```
