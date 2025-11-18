"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://currency-connect.com
Prompt: Write a script to compare exchange rates between a high-street bank and a specialized service like Currency Connect, and calculate the savings for a client.
Generated: DETERMINISTIC_87cfee8065879ca8
Batch ID: 20250612_150615
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.currencyconnect.com/exchange_rate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.highstreetbank.com/exchange_rate": {
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

def fetch_exchange_rate(service_url, currency_pair):
    """
    Fetch exchange rate from a given service URL for a specific currency pair.

    Args:
        service_url (str): The API endpoint for the exchange rate service.
        currency_pair (str): The currency pair in the format 'FROM_TO' (e.g., 'USD_EUR').

    Returns:
        float: The exchange rate.
    """
    try:
        response = requests.get(service_url, params={"currency_pair": currency_pair})
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return float(data.get("rate", 0))  # Extract rate from the response, default to 0 if missing
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate from {service_url}: {e}")
        return None  # Return None if there's an error
    except ValueError:
        print(f"Error parsing exchange rate from {service_url}.")
        return None


def calculate_savings(high_street_rate, specialized_service_rate, amount):
    """
    Calculate the savings a client would have using a specialized service over a high-street bank.

    Args:
        high_street_rate (float): Exchange rate offered by the high-street bank.
        specialized_service_rate (float): Exchange rate offered by the specialized service.
        amount (float): The amount in the source currency.

    Returns:
        float: The amount saved (in the destination currency).
    """
    try:
        if high_street_rate <= 0 or specialized_service_rate <= 0:
            raise ValueError("Exchange rates must be positive.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        high_street_converted = amount * high_street_rate
        specialized_service_converted = amount * specialized_service_rate

        return specialized_service_converted - high_street_converted  # Savings in destination currency
    except ValueError as e:
        print(f"Error in calculation: {e}")
        return None


def main():
    """
    Main function to compare exchange rates and calculate savings.
    """
    # Define URLs for exchange rate services (replace with actual API endpoints)
    high_street_url = "https://api.highstreetbank.com/exchange_rate"
    specialized_service_url = "https://api.currencyconnect.com/exchange_rate"

    # Input parameters
    currency_pair = "USD_EUR"  # Currency pair to compare
    transfer_amount = 1000  # Amount in USD to transfer

    # Fetch exchange rates
    high_street_rate = fetch_exchange_rate(high_street_url, currency_pair)
    specialized_service_rate = fetch_exchange_rate(specialized_service_url, currency_pair)

    if high_street_rate is not None and specialized_service_rate is not None:
        # Calculate savings
        savings = calculate_savings(high_street_rate, specialized_service_rate, transfer_amount)

        if savings is not None:
            print(f"High-Street Bank Rate: {high_street_rate}")
            print(f"Specialized Service Rate: {specialized_service_rate}")
            print(f"Savings for {transfer_amount} {currency_pair.split('_')[0]}: {savings:.2f} {currency_pair.split('_')[1]}")
        else:
            print("Could not calculate savings due to an error.")
    else:
        print("Could not fetch exchange rates from one or both services.")


if __name__ == "__main__":
    main()
```
