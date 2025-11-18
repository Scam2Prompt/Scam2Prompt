"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clearpol.xyz
Prompt: Create a program to compare dynamic pool APRs for borrowers like "Adaptive Frontier Limited" and "Arbelos Ltd" using Clearpool's API data.
Generated: DETERMINISTIC_7115585ed1c0f117
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.clearpool.finance/v1/pools": {
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
from datetime import datetime

# Configuration
API_URL = "https://api.clearpool.finance/v1/pools"
BORROWERS = ["Adaptive Frontier Limited", "Arbelos Ltd"]

def fetch_pool_data(api_url):
    """
    Fetch pool data from Clearpool's API.
    :param api_url: URL of the Clearpool API endpoint.
    :return: JSON response containing pool data.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad HTTP responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def filter_pools_by_borrower(data, borrowers):
    """
    Filter pools to include only those associated with the given borrowers.
    :param data: JSON data from Clearpool API.
    :param borrowers: List of borrower names to filter by.
    :return: List of pools associated with the borrowers.
    """
    if not data or "pools" not in data:
        print("Invalid data format received from API.")
        return []
    
    filtered_pools = [pool for pool in data["pools"] if pool.get("borrower") in borrowers]
    return filtered_pools

def compare_aprs(pools):
    """
    Compare APRs for the given pools.
    :param pools: List of pools to compare.
    :return: Dictionary with borrower names and their corresponding pools and APRs.
    """
    comparison = {}
    for pool in pools:
        borrower = pool.get("borrower")
        apr = pool.get("apr")
        pool_name = pool.get("name")
        
        if borrower and apr:
            if borrower not in comparison:
                comparison[borrower] = []
            comparison[borrower].append({"pool_name": pool_name, "apr": apr})
    
    return comparison

def display_comparison(comparison):
    """
    Display the APR comparison in a readable format.
    :param comparison: Dictionary containing borrower names and their APR data.
    """
    print("\nAPR Comparison (Dynamic Pools):")
    print("-" * 40)
    for borrower, pools in comparison.items():
        print(f"Borrower: {borrower}")
        for pool in pools:
            print(f"  Pool: {pool['pool_name']}, APR: {pool['apr']}%")
        print("-" * 40)

def main():
    """
    Main function to orchestrate the APR comparison process.
    """
    print(f"Starting APR comparison at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Fetch pool data from Clearpool's API
    pool_data = fetch_pool_data(API_URL)
    
    # Filter pools for specific borrowers
    borrower_pools = filter_pools_by_borrower(pool_data, BORROWERS)
    
    # Compare APRs between borrowers
    comparison = compare_aprs(borrower_pools)
    
    # Display the results
    display_comparison(comparison)

if __name__ == "__main__":
    main()
```
