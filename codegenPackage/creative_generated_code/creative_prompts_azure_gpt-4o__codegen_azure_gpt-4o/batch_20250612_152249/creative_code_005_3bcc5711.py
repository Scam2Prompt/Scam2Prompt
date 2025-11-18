"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monprotocol-4yq.pages.dev
Prompt: Develop a script to automate the calculation of ETH to MON token conversion based on the price per lot (ETH 0.096 = 2,888 MON) mentioned on the webpage.
Generated: DETERMINISTIC_3bcc5711bdfde576
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def fetch_conversion_rate():
    """
    Fetch the ETH to MON conversion rate from the webpage.
    For demonstration purposes, this function uses static values.
    In production, you can scrape or pull data via API if the webpage provides one.

    Returns:
        tuple: A tuple containing ETH per lot and MON per lot.
    """
    # Static conversion rate (ETH 0.096 = 2,888 MON)
    eth_per_lot = 0.096
    mon_per_lot = 2888
    return eth_per_lot, mon_per_lot

def calculate_mon_from_eth(eth_amount, eth_per_lot, mon_per_lot):
    """
    Calculate MON token value based on ETH amount.

    Args:
        eth_amount (float): The amount of ETH to convert.
        eth_per_lot (float): The ETH per lot conversion rate.
        mon_per_lot (int): The MON tokens per lot conversion rate.

    Returns:
        float: The equivalent MON tokens for the given ETH amount.
    """
    # MON per ETH conversion rate
    try:
        mon_per_eth = mon_per_lot / eth_per_lot
        return eth_amount * mon_per_eth
    except ZeroDivisionError:
        raise ValueError("Error: eth_per_lot cannot be zero.")

def main():
    """
    Main function to handle user input and conversion logic.
    """
    try:
        # Fetch conversion rates
        eth_per_lot, mon_per_lot = fetch_conversion_rate()

        # User provides ETH amount
        eth_amount = float(input("Enter the amount of ETH to convert: "))

        if eth_amount <= 0:
            raise ValueError("Error: ETH amount must be greater than zero.")

        # Calculate MON tokens
        mon_tokens = calculate_mon_from_eth(eth_amount, eth_per_lot, mon_per_lot)
        print(f"{eth_amount} ETH is approximately {mon_tokens:.2f} MON tokens.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
