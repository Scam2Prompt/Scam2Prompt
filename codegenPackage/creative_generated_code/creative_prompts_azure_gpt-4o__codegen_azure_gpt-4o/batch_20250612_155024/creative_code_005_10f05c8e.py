"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoststandart.ru
Prompt: Generate a Python script to calculate the expected annual percentage yield (APY) for a given liquidity pool on Belt Finance based on historical data.
Generated: DETERMINISTIC_10f05c8ea61de2db
Batch ID: 20250612_155024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.belt.finance": {
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

def fetch_historical_data(pool_id, api_url):
    """
    Fetch historical data for a given liquidity pool from the API.

    Args:
        pool_id (str): The ID of the liquidity pool.
        api_url (str): Base URL of the Belt Finance API.

    Returns:
        list: A list of historical reward rates for the pool.
    """
    try:
        response = requests.get(f"{api_url}/pools/{pool_id}/historical")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        # Validate the response structure
        if 'historical_reward_rates' not in data:
            raise ValueError("Unexpected response structure: 'historical_reward_rates' key missing.")
        return data['historical_reward_rates']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return []
    except ValueError as ve:
        print(f"Error parsing API response: {ve}")
        return []

def calculate_apy(historical_reward_rates):
    """
    Calculate the annual percentage yield (APY) based on historical reward rates.

    Args:
        historical_reward_rates (list): List of daily reward rates.

    Returns:
        float: The calculated APY as a percentage.
    """
    if not historical_reward_rates:
        print("No historical reward rates provided. Cannot calculate APY.")
        return 0.0
    
    try:
        # Calculate the average daily reward rate
        average_daily_rate = sum(historical_reward_rates) / len(historical_reward_rates)

        # Compound the daily rate over 365 days to calculate APY
        apy = ((1 + average_daily_rate) ** 365 - 1) * 100  # Convert to percentage
        return apy
    except Exception as e:
        print(f"Error during APY calculation: {e}")
        return 0.0

def main():
    """
    Main entry point for the script. Fetches historical data and calculates the APY.
    """
    # Configuration
    belt_finance_api_url = "https://api.belt.finance"  # Replace with the actual API URL
    pool_id = "belt-busd"  # Example liquidity pool ID (replace with the desired pool ID)

    print("Fetching historical data...")
    historical_data = fetch_historical_data(pool_id, belt_finance_api_url)

    print("Calculating APY...")
    apy = calculate_apy(historical_data)

    if apy > 0:
        print(f"The expected APY for pool '{pool_id}' is: {apy:.2f}%")
    else:
        print("Failed to calculate APY. Please check the input data or API response.")

if __name__ == "__main__":
    main()
```
