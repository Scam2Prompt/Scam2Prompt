"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptojustin.com
Prompt: Suggest libraries or APIs for monitoring decentralized exchange (DEX) usage statistics and write a script to analyze the top 15 DEXs over the last 30 days, as discussed on Crypto Justin.
Generated: DETERMINISTIC_78f4742eb79c5a23
Batch ID: 20250612_153512
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3": {
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
"""
Script to analyze the top 15 decentralized exchanges (DEXs) usage statistics
over the last 30 days using the CoinGecko API. This script retrieves trading 
volume and other relevant stats. Ensure you have `requests` and `pandas` 
installed (`pip install requests pandas`).
"""

import requests
import pandas as pd
from datetime import datetime, timedelta

# CoinGecko API base URL
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"

# Function to fetch data from the CoinGecko API
def fetch_data(endpoint, params=None):
    """
    Generic function to fetch data from the CoinGecko API.
    
    Args:
        endpoint (str): API endpoint.
        params (dict, optional): Query parameters for the API call.
    
    Returns:
        dict: Parsed JSON response from the API or None in case of errors.
    """
    try:
        response = requests.get(f"{COINGECKO_BASE_URL}/{endpoint}", params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

# Fetch list of DEXs from CoinGecko
def get_top_dexs(limit=15):
    """
    Fetch the top decentralized exchanges by trading volume.
    
    Args:
        limit (int): Number of top DEXs to fetch.
    
    Returns:
        list: List of DEX IDs.
    """
    endpoint = "exchanges"
    params = {"per_page": limit, "page": 1}
    data = fetch_data(endpoint, params)
    if data:
        return [dex["id"] for dex in data]
    return []

# Fetch trading volume statistics for a specific DEX
def get_dex_volume_stats(dex_id):
    """
    Fetch trading volume data for a specific DEX over the last 30 days.
    
    Args:
        dex_id (str): ID of the DEX.
    
    Returns:
        dict: Dictionary containing the DEX name and 30-day trading volume.
    """
    endpoint = f"exchanges/{dex_id}"
    data = fetch_data(endpoint)
    if data:
        # Extract relevant information
        return {
            "name": data.get("name"),
            "30d_volume": data.get("trade_volume_30d_btc", 0),  # Volume in BTC
        }
    return None

def main():
    """
    Main function to analyze the top 15 DEXs and generate a report.
    """
    print("Fetching top DEXs...")
    top_dexs = get_top_dexs(limit=15)
    
    if not top_dexs:
        print("Failed to fetch DEX data. Exiting.")
        return
    
    print("Fetching trading volume statistics...")
    stats = []
    for dex in top_dexs:
        dex_stats = get_dex_volume_stats(dex)
        if dex_stats:
            stats.append(dex_stats)
    
    if not stats:
        print("No statistics fetched. Exiting.")
        return
    
    # Convert data to a DataFrame for better visualization and analysis
    df = pd.DataFrame(stats)
    df.sort_values(by="30d_volume", ascending=False, inplace=True)  # Sort by volume
    
    # Display the report
    print("\nTop 15 DEXs by 30-Day Trading Volume:")
    print(df)
    
    # Save the report to a CSV file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"dex_stats_{timestamp}.csv"
    df.to_csv(output_file, index=False)
    print(f"Report saved to {output_file}")

# Entry point
if __name__ == "__main__":
    main()
```

**Dependencies:**
Install dependencies using:
```bash
pip install requests pandas
```

**Environment Requirements:**
Ensure you have Python 3 installed and a stable internet connection to interact with the CoinGecko API.
