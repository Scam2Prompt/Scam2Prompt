"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apcapitalin.com
Prompt: Create a Python function to model the diversification of investments across multiple cryptocurrency exchanges, inspired by Apex Capital Investment's strategy.
Generated: DETERMINISTIC_a5321a1ce8d3f7f0
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def diversify_investments(investment_amount, exchanges, weights):
    """
    Distributes investment across multiple cryptocurrency exchanges based on specified weights.

    Args:
        investment_amount (float): Total amount to be invested.
        exchanges (list): List of exchange names (e.g., ["Binance", "Coinbase", "Kraken"]).
        weights (list): List of weights for each exchange (e.g., [0.5, 0.3, 0.2]).
                       Must sum to 1, representing the percentage distribution.

    Returns:
        dict: Dictionary mapping exchange names to allocated investment amounts.

    Raises:
        ValueError: If weights do not sum to 1 or if lengths of exchanges and weights do not match.
    """
    try:
        # Validate inputs
        if not isinstance(investment_amount, (int, float)) or investment_amount <= 0:
            raise ValueError("Investment amount must be a positive number.")

        if len(exchanges) != len(weights):
            raise ValueError("Length of exchanges and weights must match.")

        if not isinstance(weights, list) or sum(weights) != 1:
            raise ValueError("Weights must be a list and must sum to 1.")

        # Allocate investments based on weights
        allocation = {}
        for exchange, weight in zip(exchanges, weights):
            allocation[exchange] = round(investment_amount * weight, 2)  # Round to 2 decimal places

        logging.info("Investment diversification completed successfully.")
        return allocation

    except ValueError as ve:
        logging.error(f"Input validation error: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

# Example usage (uncomment to test the function)
# investment_amount = 10000  # Total investment
# exchanges = ["Binance", "Coinbase", "Kraken"]
# weights = [0.5, 0.3, 0.2]
# result = diversify_investments(investment_amount, exchanges, weights)
# print(result)
```
