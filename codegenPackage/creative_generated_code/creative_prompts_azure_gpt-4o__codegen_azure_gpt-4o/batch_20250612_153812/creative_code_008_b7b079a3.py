"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celaroopl.xyz
Prompt: Generate a script to analyze the borrowing trends on Clearpool by calculating the total loans originated and total value locked.
Generated: DETERMINISTIC_b7b079a311129d43
Batch ID: 20250612_153812
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
import json

def fetch_clearpool_data(api_url):
    """
    Fetch data from Clearpool API.
    
    :param api_url: str, The endpoint URL for Clearpool data.
    :return: dict, The JSON response from the API.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Clearpool API: {e}")
        return None

def calculate_borrowing_trends(data):
    """
    Calculate borrowing trends including total loans originated and total value locked.
    
    :param data: dict, The JSON data from Clearpool API.
    :return: tuple, (total_loans_originated, total_value_locked).
    """
    total_loans_originated = 0
    total_value_locked = 0

    try:
        # Iterate through each pool in the data to calculate totals
        for pool in data.get("pools", []):
            total_loans_originated += float(pool.get("loansOriginated", 0))
            total_value_locked += float(pool.get("valueLocked", 0))
    except (TypeError, ValueError) as e:
        print(f"Error processing pool data: {e}")

    return total_loans_originated, total_value_locked

def main():
    """
    Main function to analyze borrowing trends on Clearpool.
    """
    # Define the Clearpool API endpoint
    api_url = "https://api.clearpool.finance/v1/pools"
    
    # Fetch data from Clearpool API
    data = fetch_clearpool_data(api_url)
    if not data:
        print("Failed to retrieve data. Exiting.")
        return

    # Calculate borrowing trends
    total_loans_originated, total_value_locked = calculate_borrowing_trends(data)

    # Display results
    print("Clearpool Borrowing Trends:")
    print(f"Total Loans Originated: {total_loans_originated}")
    print(f"Total Value Locked: {total_value_locked}")

if __name__ == "__main__":
    main()
```
