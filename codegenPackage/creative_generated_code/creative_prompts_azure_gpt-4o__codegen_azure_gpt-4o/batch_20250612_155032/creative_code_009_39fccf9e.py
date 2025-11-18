"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Create a script to automate the calculation of exchange rates and commissions for multiple cryptocurrencies (USDC, Bitcoin, Ethereum) as described by Kantor USDC Białystok.
Generated: DETERMINISTIC_39fccf9e450edb46
Batch ID: 20250612_155032
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd": {
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

def get_exchange_rate(crypto_symbol):
    """
    Fetch the current exchange rate for the given cryptocurrency symbol.
    Args:
        crypto_symbol (str): Cryptocurrency symbol (e.g., 'USDC', 'BTC', 'ETH').
    Returns:
        float: The current exchange rate in USD.
    Raises:
        ValueError: If the API call fails or the symbol is invalid.
    """
    try:
        # URL for a public cryptocurrency exchange rate API
        api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"

        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for HTTP issues
        data = response.json()
        
        if crypto_symbol.lower() in data:
            return data[crypto_symbol.lower()]['usd']
        else:
            raise ValueError(f"Invalid cryptocurrency symbol or data not found: {crypto_symbol}")
    except requests.RequestException as e:
        raise ValueError(f"Error fetching data from the API: {str(e)}")

def calculate_commission(exchange_rate, commission_percentage):
    """
    Calculate the commission for a given exchange rate and commission percentage.
    Args:
        exchange_rate (float): The exchange rate in USD.
        commission_percentage (float): The commission percentage (e.g., 2.5 for 2.5%).
    Returns:
        float: The commission amount.
    """
    return (exchange_rate * commission_percentage) / 100

def main():
    """
    Main function to automate the calculation of exchange rates and commissions
    for multiple cryptocurrencies.
    """
    # List of cryptocurrencies to fetch exchange rates for
    cryptocurrencies = ['bitcoin', 'ethereum', 'usd-coin']  # Coingecko uses specific IDs (e.g., 'bitcoin', 'ethereum', 'usd-coin')
    
    # Commission percentage charged for transactions (example: 2.5%)
    commission_percentage = 2.5
    
    # Output results
    print("Cryptocurrency Exchange Rates and Commissions\n")
    
    for crypto in cryptocurrencies:
        try:
            # Fetch current exchange rate
            exchange_rate = get_exchange_rate(crypto)
            
            # Calculate commission
            commission = calculate_commission(exchange_rate, commission_percentage)
            
            # Print results
            print(f"Cryptocurrency: {crypto.capitalize()}")
            print(f"Exchange Rate (USD): ${exchange_rate:.2f}")
            print(f"Commission ({commission_percentage}%): ${commission:.2f}\n")
        except ValueError as e:
            print(f"Error processing {crypto.capitalize()}: {str(e)}\n")

if __name__ == "__main__":
    main()
```
