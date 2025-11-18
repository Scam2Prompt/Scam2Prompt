"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-9e9.pages.dev
Prompt: Develop a script to display $BONK token statistics, including exchange listings and integration counts, using data from the Bonk Coin website.
Generated: DETERMINISTIC_4fe8883e023623ba
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bonkcoin.com/statistics": {
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

# Constants
BONK_API_URL = "https://api.bonkcoin.com/statistics"  # Replace with the actual Bonk Coin API endpoint

def fetch_bonk_statistics():
    """
    Fetches BONK token statistics from the Bonk Coin API.

    Returns:
        dict: Parsed statistics data or None in case of an error.
    """
    try:
        response = requests.get(BONK_API_URL, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Parse the JSON response
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching BONK statistics: {e}")
        return None

def display_bonk_statistics(stats):
    """
    Displays BONK token statistics in a user-friendly format.

    Args:
        stats (dict): Dictionary containing BONK statistics.
    """
    if not stats:
        print("No statistics available to display.")
        return

    # Extract and display relevant statistics
    print("BONK Token Statistics:")
    print("-----------------------")
    print(f"Exchange Listings: {stats.get('exchange_listings', 'N/A')}")
    print(f"Integration Counts: {stats.get('integration_counts', 'N/A')}")
    print("-----------------------")

def main():
    """
    Main function to fetch and display BONK token statistics.
    """
    print("Fetching BONK token statistics...")
    bonk_stats = fetch_bonk_statistics()  # Fetch statistics
    display_bonk_statistics(bonk_stats)   # Display statistics

if __name__ == "__main__":
    main()
```

This script should be run in a Python environment with the `requests` library installed. Replace the `BONK_API_URL` with the actual API endpoint provided by the Bonk Coin website.
