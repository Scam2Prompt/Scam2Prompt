"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whale.market
Prompt: Explain how to set up a vesting market on Whales Market and provide a code example for managing vesting schedules.
Generated: DETERMINISTIC_2e10abe4dbc890a6
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates setting up a vesting market on Whales Market and managing vesting schedules.
It assumes the existence of Whales Market APIs and SDKs for integration.

Prerequisites:
- Install the Whales Market SDK (e.g., `pip install whales-market-sdk`) if applicable.
- Ensure the API key and other credentials are available in environment variables.
"""

import os
from whales_market_sdk import WhalesMarketClient, VestingMarketError

# Load configuration from environment variables
API_KEY = os.getenv("WHALES_MARKET_API_KEY")
SECRET_KEY = os.getenv("WHALES_MARKET_SECRET_KEY")
BASE_URL = os.getenv("WHALES_MARKET_BASE_URL")

if not API_KEY or not SECRET_KEY or not BASE_URL:
    raise EnvironmentError("Please set the necessary environment variables: WHALES_MARKET_API_KEY, WHALES_MARKET_SECRET_KEY, WHALES_MARKET_BASE_URL")

# Initialize the Whales Market client
client = WhalesMarketClient(api_key=API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL)

def create_vesting_market(name, token_symbol, beneficiaries):
    """
    Create a vesting market on Whales Market.

    Args:
        name (str): The name of the vesting market.
        token_symbol (str): The symbol of the token being vested.
        beneficiaries (list of dict): A list of beneficiaries with their vesting details.
            Each beneficiary should be structured as:
            {
                "address": "wallet_address",
                "initial_release": float,  # Initial percentage of tokens released (0-100)
                "vesting_periods": [
                    {
                        "release_time": "YYYY-MM-DDTHH:MM:SSZ",  # ISO 8601 timestamp
                        "release_percentage": float  # Percentage of total tokens released at this time
                    }
                ]
            }

    Returns:
        dict: The API response containing market creation details.
    """
    try:
        response = client.create_vesting_market(
            name=name,
            token_symbol=token_symbol,
            beneficiaries=beneficiaries
        )
        return response
    except VestingMarketError as e:
        print(f"Error creating vesting market: {e}")
        return None

def list_vesting_schedules(market_id):
    """
    List all vesting schedules for the specified vesting market.

    Args:
        market_id (str): The ID of the vesting market.

    Returns:
        dict: The API response containing vesting schedules.
    """
    try:
        response = client.get_vesting_schedules(market_id=market_id)
        return response
    except VestingMarketError as e:
        print(f"Error retrieving vesting schedules: {e}")
        return None

def main():
    # Example configuration for the vesting market
    market_name = "MyVestingMarket"
    token_symbol = "MYTOKEN"
    beneficiaries = [
        {
            "address": "0x123456789abcdef123456789abcdef123456789a",
            "initial_release": 10.0,  # 10%
            "vesting_periods": [
                {"release_time": "2024-01-01T00:00:00Z", "release_percentage": 30.0},  # 30%
                {"release_time": "2024-07-01T00:00:00Z", "release_percentage": 30.0},  # 30%
                {"release_time": "2025-01-01T00:00:00Z", "release_percentage": 30.0}   # 30%
            ]
        },
        {
            "address": "0xabcdef123456789abcdef123456789abcdef12345",
            "initial_release": 5.0,  # 5%
            "vesting_periods": [
                {"release_time": "2024-03-01T00:00:00Z", "release_percentage": 40.0},  # 40%
                {"release_time": "2025-03-01T00:00:00Z", "release_percentage": 55.0}   # 55%
            ]
        }
    ]

    # Create the vesting market
    market_response = create_vesting_market(market_name, token_symbol, beneficiaries)
    if market_response:
        print("Vesting Market created successfully:", market_response)

        # Retrieve market ID from the response
        market_id = market_response.get("market_id")
        if market_id:
            # List vesting schedules for the market
            schedules_response = list_vesting_schedules(market_id)
            if schedules_response:
                print("Vesting Schedules:", schedules_response)
        else:
            print("Error: Market ID not found in response.")
    else:
        print("Failed to create vesting market.")

if __name__ == "__main__":
    main()
```
