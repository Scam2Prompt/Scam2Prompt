"""
Generated Code Metadata:
========================
Original URL: https://convexfinance.io
Prompt: Write a script to calculate emissions controlled by locked CVX tokens for CRV, FXN, PRISMA, and FXS tokens over a 14-day period using Convex Finance's data.
Generated: DETERMINISTIC_51c547d8557d4af0
Batch ID: 20250612_145153
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.convexfinance.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from datetime import datetime, timedelta

# Define constants
CONVEX_FINANCE_API_URL = "https://api.convexfinance.com"
TOKENS = ["CRV", "FXN", "PRISMA", "FXS"]
TIME_PERIOD_DAYS = 14

def get_locked_cvx_data(token, days):
    """
    Retrieves locked CVX data for a given token over a specified period.

    Args:
    token (str): The token to retrieve data for (e.g. CRV, FXN, etc.)
    days (int): The number of days to retrieve data for

    Returns:
    list: A list of dictionaries containing the date and emissions data
    """
    try:
        # Calculate start and end timestamps
        end_timestamp = int(datetime.now().timestamp())
        start_timestamp = int((datetime.now() - timedelta(days=days)).timestamp())

        # Construct API request
        url = f"{CONVEX_FINANCE_API_URL}/emissions/cvx/locked"
        params = {
            "token": token,
            "start": start_timestamp,
            "end": end_timestamp
        }

        # Send GET request
        response = requests.get(url, params=params)

        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve data for {token}: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error retrieving data for {token}: {str(e)}")
        return []

def calculate_emissions(data):
    """
    Calculates the total emissions from the provided data.

    Args:
    data (list): A list of dictionaries containing the date and emissions data

    Returns:
    float: The total emissions
    """
    try:
        total_emissions = sum([d["emissions"] for d in data])
        return total_emissions
    except Exception as e:
        print(f"Error calculating emissions: {str(e)}")
        return 0.0

def main():
    # Initialize results dictionary
    results = {token: 0.0 for token in TOKENS}

    # Iterate over tokens and calculate emissions
    for token in TOKENS:
        data = get_locked_cvx_data(token, TIME_PERIOD_DAYS)
        emissions = calculate_emissions(data)
        results[token] = emissions

    # Print results
    print("Emissions over {} days:".format(TIME_PERIOD_DAYS))
    for token, emissions in results.items():
        print("{}: {:.2f}".format(token, emissions))

if __name__ == "__main__":
    main()
```
