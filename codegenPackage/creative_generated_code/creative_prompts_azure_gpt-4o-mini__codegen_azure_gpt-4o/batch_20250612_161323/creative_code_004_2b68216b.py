"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Develop a simple command-line tool in Python that converts Euros to British Pounds using the latest exchange rates, as discussed in the content.
Generated: DETERMINISTIC_2b68216b4cb46038
Batch ID: 20250612_161323
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate.host/latest?base=EUR&symbols=GBP": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.exchangerate-api.com": {
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
import sys

def fetch_exchange_rate():
    """
    Fetch the latest exchange rate for EUR to GBP from an online API.
    Returns:
        float: Exchange rate from EUR to GBP.
    Raises:
        Exception: If the API request fails or the response is invalid.
    """
    try:
        # Using a free exchange rate API (example endpoint: 'https://api.exchangerate-api.com')
        url = "https://api.exchangerate.host/latest?base=EUR&symbols=GBP"
        response = requests.get(url)
        
        # Raise an error if the request fails
        response.raise_for_status()
        
        # Parse the JSON response to extract the exchange rate
        data = response.json()
        if "rates" in data and "GBP" in data["rates"]:
            return data["rates"]["GBP"]
        else:
            raise ValueError("Unexpected response structure from the API.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching the exchange rate: {e}")
    except ValueError as e:
        raise Exception(f"Error processing the API response: {e}")

def convert_euros_to_pounds(amount_in_euros, exchange_rate):
    """
    Convert a given amount in Euros to British Pounds using the provided exchange rate.
    Args:
        amount_in_euros (float): Amount in Euros to be converted.
        exchange_rate (float): Exchange rate from EUR to GBP.
    Returns:
        float: Equivalent amount in British Pounds.
    """
    return round(amount_in_euros * exchange_rate, 2)

def main():
    """
    Main function to execute the command-line tool.
    """
    try:
        # Get the amount in Euros from the user
        amount_in_euros = input("Enter the amount in Euros: ")
        
        # Validate and convert user input to a float
        try:
            amount_in_euros = float(amount_in_euros)
            if amount_in_euros < 0:
                raise ValueError("Amount cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the amount in Euros.")
            sys.exit(1)
        
        # Fetch the latest exchange rate
        exchange_rate = fetch_exchange_rate()
        
        # Perform the conversion
        amount_in_pounds = convert_euros_to_pounds(amount_in_euros, exchange_rate)
        
        # Display the result
        print(f"€{amount_in_euros} is approximately £{amount_in_pounds} at the current exchange rate ({exchange_rate} GBP per EUR).")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
