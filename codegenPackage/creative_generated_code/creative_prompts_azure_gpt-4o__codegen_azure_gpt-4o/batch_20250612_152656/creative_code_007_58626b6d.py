"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gratisbitcoin-no.pages.dev
Prompt: Write a Python program to calculate the total value of free Bitcoin offers from the four platforms mentioned on the site, converting amounts to USD or NOK.
Generated: DETERMINISTIC_58626b6d7b63693a
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

# Constants for currency conversion rates (mock values, ideally fetched from an API)
BTC_TO_USD_RATE = 30000  # Example: 1 Bitcoin = 30,000 USD
BTC_TO_NOK_RATE = 300000  # Example: 1 Bitcoin = 300,000 NOK

# Sample data: Free Bitcoin offers from platforms (mock data)
platform_offers = {
    "PlatformA": 0.0025,  # Amount in BTC
    "PlatformB": 0.0018,  # Amount in BTC
    "PlatformC": 0.0032,  # Amount in BTC
    "PlatformD": 0.0021,  # Amount in BTC
}

# Function to convert Bitcoin to USD
def convert_btc_to_usd(btc_amount):
    """
    Converts Bitcoin amount to USD using BTC_TO_USD_RATE.
    :param btc_amount: Amount in Bitcoin
    :return: Equivalent amount in USD
    """
    return btc_amount * BTC_TO_USD_RATE

# Function to convert Bitcoin to NOK
def convert_btc_to_nok(btc_amount):
    """
    Converts Bitcoin amount to NOK using BTC_TO_NOK_RATE.
    :param btc_amount: Amount in Bitcoin
    :return: Equivalent amount in NOK
    """
    return btc_amount * BTC_TO_NOK_RATE

# Function to calculate total value of free Bitcoin offers
def calculate_total_value(platform_offers, currency='USD'):
    """
    Calculates the total value of free Bitcoin offers in the specified currency.
    :param platform_offers: Dictionary containing platform names and Bitcoin amounts
    :param currency: Target currency for conversion ('USD' or 'NOK')
    :return: Total value in the specified currency
    """
    total_btc = sum(platform_offers.values())
    if currency.upper() == 'USD':
        return convert_btc_to_usd(total_btc)
    elif currency.upper() == 'NOK':
        return convert_btc_to_nok(total_btc)
    else:
        raise ValueError("Unsupported currency. Please use 'USD' or 'NOK'.")

# Main function
def main():
    """
    Main function to calculate and display the total value of free Bitcoin offers.
    """
    try:
        print("Calculating total value of free Bitcoin offers...")
        
        # Calculate in USD
        total_in_usd = calculate_total_value(platform_offers, currency='USD')
        print(f"Total value in USD: ${total_in_usd:,.2f}")
        
        # Calculate in NOK
        total_in_nok = calculate_total_value(platform_offers, currency='NOK')
        print(f"Total value in NOK: {total_in_nok:,.2f} NOK")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for script execution
if __name__ == "__main__":
    main()
```
