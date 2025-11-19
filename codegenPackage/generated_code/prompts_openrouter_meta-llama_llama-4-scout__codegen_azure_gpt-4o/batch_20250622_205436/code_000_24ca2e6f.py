"""
Generated Code Metadata:
========================
Original URL: https://uni-arbitrage.info
Prompt: Explain the concept of arbitrage in financial markets.
Generated: DETERMINISTIC_24ca2e6fa7e1575b
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Arbitrage in financial markets refers to the practice of taking advantage of price differences
between two or more markets to make a profit. This script demonstrates a simplified example
of arbitrage using currency exchange rates.

The program checks if there is an arbitrage opportunity between three currencies (e.g., USD, EUR, GBP)
and calculates the potential profit if such an opportunity exists.
"""

# Import necessary libraries
import sys

def detect_arbitrage(exchange_rates):
    """
    Detects arbitrage opportunities in a given set of exchange rates.

    Parameters:
        exchange_rates (dict): A dictionary containing exchange rates between currencies.
                               Example format:
                               {
                                   'USD': {'EUR': 0.9, 'GBP': 0.75},
                                   'EUR': {'USD': 1.11, 'GBP': 0.83},
                                   'GBP': {'USD': 1.33, 'EUR': 1.2}
                               }

    Returns:
        str: A message indicating whether an arbitrage opportunity exists and the potential profit.
    """
    try:
        # Iterate through all possible triangular arbitrage paths
        for base_currency in exchange_rates:
            for intermediate_currency in exchange_rates[base_currency]:
                for target_currency in exchange_rates[intermediate_currency]:
                    # Ensure the path returns to the base currency
                    if target_currency == base_currency:
                        # Calculate the product of exchange rates in the triangular path
                        rate_product = (
                            exchange_rates[base_currency][intermediate_currency] *
                            exchange_rates[intermediate_currency][target_currency] *
                            exchange_rates[target_currency][base_currency]
                        )
                        
                        # If the product is greater than 1, arbitrage opportunity exists
                        if rate_product > 1:
                            profit = rate_product - 1
                            return (f"Arbitrage opportunity detected! "
                                    f"Starting with {base_currency}, you can make a profit of {profit:.2%}.")
        
        # If no arbitrage opportunity is found
        return "No arbitrage opportunity detected."
    
    except KeyError as e:
        return f"Error: Missing exchange rate for {e}. Please check the input data."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example exchange rates (simplified for demonstration purposes)
exchange_rates = {
    'USD': {'EUR': 0.9, 'GBP': 0.75},
    'EUR': {'USD': 1.11, 'GBP': 0.83},
    'GBP': {'USD': 1.33, 'EUR': 1.2}
}

if __name__ == "__main__":
    # Detect arbitrage opportunities
    result = detect_arbitrage(exchange_rates)
    print(result)
```
