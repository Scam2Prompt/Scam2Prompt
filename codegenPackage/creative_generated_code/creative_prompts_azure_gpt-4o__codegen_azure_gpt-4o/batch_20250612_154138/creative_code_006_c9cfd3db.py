"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://statenislandbitcoin.com
Prompt: Provide code to track presale activity for altcoins like NuggetRush (NUGX) and analyze its novelty in P2E, GameFi, and NFT markets, as discussed on StatenIslandBitcoin.com.
Generated: DETERMINISTIC_c9cfd3db4e9f4217
Batch ID: 20250612_154138
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/": {
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
from datetime import datetime

# Constants
COIN_API_URL = "https://api.coingecko.com/api/v3/coins/"
TRACKED_COINS = ["nuggetrush"]  # Altcoins to track (e.g., NuggetRush)
MARKETS_TO_ANALYZE = ["P2E", "GameFi", "NFT"]  # Relevant markets
STATS_FILE = "altcoin_presale_stats.json"  # File to save presale activity stats

def fetch_coin_data(coin_id):
    """
    Fetches coin data from the CoinGecko API.
    
    Parameters:
        coin_id (str): The ID of the coin to fetch data for.
    
    Returns:
        dict: Coin data if successful, None otherwise.
    """
    try:
        response = requests.get(f"{COIN_API_URL}{coin_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for coin '{coin_id}': {e}")
        return None

def analyze_market_novelty(coin_data, markets):
    """
    Analyzes the novelty of a coin in specified markets.
    
    Parameters:
        coin_data (dict): The coin data to analyze.
        markets (list): List of markets to evaluate (e.g., P2E, GameFi, NFT).
    
    Returns:
        dict: Analysis results indicating novelty in each market.
    """
    analysis_results = {}
    description = coin_data.get("description", {}).get("en", "").lower()
    
    for market in markets:
        if market.lower() in description:
            analysis_results[market] = "High Novelty"
        else:
            analysis_results[market] = "Low Novelty"
    
    return analysis_results

def save_presale_stats(stats):
    """
    Saves presale stats to a JSON file.
    
    Parameters:
        stats (list): List of presale stats to save.
    """
    try:
        with open(STATS_FILE, "w") as file:
            json.dump(stats, file, indent=4)
        print(f"Presale stats successfully saved to {STATS_FILE}.")
    except IOError as e:
        print(f"Error saving presale stats: {e}")

def track_and_analyze_presale_activity():
    """
    Tracks presale activity for altcoins and analyzes their novelty in specific markets.
    """
    presale_stats = []

    for coin_id in TRACKED_COINS:
        print(f"Tracking presale activity for: {coin_id}")
        
        coin_data = fetch_coin_data(coin_id)
        if not coin_data:
            continue
        
        # Extract relevant presale information
        coin_name = coin_data.get("name", "Unknown")
        symbol = coin_data.get("symbol", "Unknown")
        presale_start = coin_data.get("ico_data", {}).get("start_date", "Unknown")
        presale_end = coin_data.get("ico_data", {}).get("end_date", "Unknown")
        
        # Analyze novelty in specified markets
        market_analysis = analyze_market_novelty(coin_data, MARKETS_TO_ANALYZE)
        
        # Compile stats
        presale_stats.append({
            "coin_name": coin_name,
            "symbol": symbol,
            "presale_start": presale_start,
            "presale_end": presale_end,
            "market_analysis": market_analysis,
            "last_updated": datetime.now().isoformat()
        })
    
    # Save stats to a file
    save_presale_stats(presale_stats)
    print("Tracking and analysis complete.")

if __name__ == "__main__":
    track_and_analyze_presale_activity()
```
