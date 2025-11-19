"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Develop a simple command-line tool in Python that converts Euros to British Pounds using the latest exchange rates, as discussed in the content.
Generated: DETERMINISTIC_2b68216b4cb46038
Batch ID: 20250612_161323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate-api.com/v4/latest/EUR": {
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

def fetch_exchange_rate():
    """
    Fetch the latest exchange rate for Euro to British Pound.
    
    Returns:
        float: The current exchange rate from Euro to British Pound.
        
    Raises:
        RuntimeError: If there is an issue with fetching the exchange rate.
    """
    try:
        # URL for the exchange rate API
        url = "https://api.exchangerate-api.com/v4/latest/EUR"
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            raise RuntimeError("Failed to fetch exchange rates.")
        
        # Parse the JSON response
        data = response.json()
        
        # Get the exchange rate for GBP
        exchange_rate = data["rates"]["GBP"]
        return exchange_rate
    except requests.RequestException as e:
        raise RuntimeError(f"An error occurred while fetching exchange rates: {e}")

def convert_euros_to_pounds(euros):
    """
    Convert Euros to British Pounds using the latest exchange rate.
    
    Args:
        euros (float): The amount in Euros to convert.
        
    Returns:
        float: The equivalent amount in British Pounds.
    """
    exchange_rate = fetch_exchange_rate()
    pounds = euros * exchange_rate
    return pounds

def main():
    """
    Main function to run the command-line tool.
    Prompts the user for an amount in Euros and converts it to British Pounds.
    """
    try:
        euros = float(input("Enter the amount in Euros to convert to British Pounds: "))
        if euros < 0:
            raise ValueError("The amount cannot be negative.")
        
        pounds = convert_euros_to_pounds(euros)
        print(f"{euros} Euros is equivalent to {pounds:.2f} British Pounds.")
    except ValueError as e:
        print(f"Input error: {e}")
    except RuntimeError as e:
        print(f"Currency conversion error: {e}")

if __name__ == "__main__":
    main()
```
