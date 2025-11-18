"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hfm88.com
Prompt: Create a script to calculate the cost of transferring money internationally, factoring in exchange rates and fees, as described on the HFM platform.
Generated: DETERMINISTIC_0c0f958250173b46
Batch ID: 20250612_154111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate-api.com/v4/latest/{base_currency": {
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

def fetch_exchange_rate(base_currency, target_currency):
    """
    Fetch the exchange rate between two currencies from a public API.
    Args:
        base_currency (str): The currency to convert from (e.g., "USD").
        target_currency (str): The currency to convert to (e.g., "EUR").
    Returns:
        float: The exchange rate from base_currency to target_currency.
    Raises:
        Exception: If the API request fails or the currencies are invalid.
    """
    try:
        # Example API endpoint for exchange rates (replace with actual HFM endpoint if available)
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        data = response.json()
        if target_currency not in data['rates']:
            raise ValueError(f"Invalid target currency: {target_currency}")
        return data['rates'][target_currency]
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching exchange rate: {e}")

def calculate_transfer_cost(amount, base_currency, target_currency, fixed_fee, percentage_fee):
    """
    Calculate the total cost of transferring money internationally.
    Args:
        amount (float): The amount to be transferred in the base currency.
        base_currency (str): The currency to convert from.
        target_currency (str): The currency to convert to.
        fixed_fee (float): The fixed transaction fee (in base currency).
        percentage_fee (float): The percentage fee for the transfer (as a decimal, e.g., 0.02 for 2%).
    Returns:
        dict: A dictionary containing the transfer cost breakdown.
    """
    try:
        # Fetch the exchange rate
        exchange_rate = fetch_exchange_rate(base_currency, target_currency)

        # Calculate fees
        percentage_cost = amount * percentage_fee
        total_fees = fixed_fee + percentage_cost

        # Calculate the converted amount after fees
        amount_after_fees = amount - total_fees
        converted_amount = amount_after_fees * exchange_rate

        # Build result dictionary
        result = {
            "base_currency": base_currency,
            "target_currency": target_currency,
            "amount": amount,
            "exchange_rate": exchange_rate,
            "fixed_fee": fixed_fee,
            "percentage_fee": percentage_fee,
            "total_fees": total_fees,
            "amount_after_fees": amount_after_fees,
            "converted_amount": converted_amount,
        }
        return result
    except Exception as e:
        raise Exception(f"Error calculating transfer cost: {e}")

def main():
    """
    Main function to demonstrate the money transfer cost calculation.
    """
    try:
        # Example input values (replace with inputs from HFM platform or user)
        amount = 1000.0  # Amount in base currency
        base_currency = "USD"
        target_currency = "EUR"
        fixed_fee = 10.0  # Fixed fee in base currency
        percentage_fee = 0.02  # Percentage fee (2%)

        # Calculate transfer cost
        transfer_cost = calculate_transfer_cost(amount, base_currency, target_currency, fixed_fee, percentage_fee)

        # Display the results
        print("Money Transfer Cost Calculation:")
        for key, value in transfer_cost.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
