"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epsys.ro
Prompt: Develop a Python script to compare transparency metrics (e.g., live draw availability, legal oversight) across Hondatoto's lottery markets, as described on the website.
Generated: DETERMINISTIC_e1d9760578c64c5a
Batch ID: 20250612_153725
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.hondatoto.com/api/": {
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
import pandas as pd
from typing import List, Dict

# Constants
API_BASE_URL = "https://www.hondatoto.com/api/"  # Replace with actual API endpoint
MARKETS_ENDPOINT = "markets"  # Example API endpoint for lottery markets
TRANSPARENCY_METRICS = ["live_draw_availability", "legal_oversight"]  # Metrics to compare

def fetch_market_data(api_url: str) -> List[Dict]:
    """
    Fetch lottery market data from Hondatoto API.

    Args:
        api_url (str): The URL of the Hondatoto API to fetch market data.

    Returns:
        List[Dict]: A list of dictionaries containing market data.
    """
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching market data: {e}")
        return []

def extract_transparency_metrics(market_data: List[Dict], metrics: List[str]) -> pd.DataFrame:
    """
    Extract transparency metrics from market data into a pandas DataFrame.

    Args:
        market_data (List[Dict]): The raw market data.
        metrics (List[str]): List of transparency metrics to extract.

    Returns:
        pd.DataFrame: A DataFrame containing the selected transparency metrics.
    """
    extracted_data = []
    
    for market in market_data:
        # Extract relevant metrics if available
        market_metrics = {metric: market.get(metric, None) for metric in metrics}
        market_metrics["market_name"] = market.get("market_name", "Unknown")
        extracted_data.append(market_metrics)

    return pd.DataFrame(extracted_data)

def main():
    """
    Main function to compare transparency metrics across Hondatoto's lottery markets.
    """
    # Step 1: Fetch market data from Hondatoto API
    api_url = f"{API_BASE_URL}{MARKETS_ENDPOINT}"
    market_data = fetch_market_data(api_url)

    if not market_data:
        print("No market data available. Exiting program.")
        return

    # Step 2: Extract transparency metrics into a pandas DataFrame
    metrics_df = extract_transparency_metrics(market_data, TRANSPARENCY_METRICS)

    # Step 3: Display and analyze the data
    print("Transparency Metrics Across Lottery Markets:")
    print(metrics_df)

    # Optional: Save the data to a CSV file for further analysis
    output_file = "transparency_metrics.csv"
    metrics_df.to_csv(output_file, index=False)
    print(f"Transparency metrics saved to {output_file}")

if __name__ == "__main__":
    main()
```
