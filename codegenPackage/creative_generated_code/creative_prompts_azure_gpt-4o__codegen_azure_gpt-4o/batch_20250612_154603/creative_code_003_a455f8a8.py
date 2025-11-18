"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainecotrust.cc
Prompt: Create a Python function to simulate forex trading between EUR/USD, incorporating buy/sell spreads as explained on mainecotrust.cc.
Generated: DETERMINISTIC_a455f8a878658a92
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def simulate_forex_trading(amount_in_eur, buy_spread=0.0002, sell_spread=0.0002, exchange_rate=1.1):
    """
    Simulates forex trading between EUR/USD with buy and sell spreads.
    
    Parameters:
        amount_in_eur (float): The amount of EUR to trade.
        buy_spread (float): The spread applied when buying USD (default is 0.0002).
        sell_spread (float): The spread applied when selling USD (default is 0.0002).
        exchange_rate (float): The base EUR/USD exchange rate (default is 1.1).
    
    Returns:
        dict: A dictionary containing transaction details:
            - 'initial_eur': Original amount in EUR
            - 'usd_after_buy': Amount of USD acquired after buying
            - 'eur_after_sell': Amount of EUR acquired after selling
            - 'profit_loss_eur': Profit or loss in EUR after the transaction
    """
    try:
        if amount_in_eur <= 0:
            raise ValueError("Amount in EUR must be greater than zero.")
        if buy_spread < 0 or sell_spread < 0 or exchange_rate <= 0:
            raise ValueError("Spreads and exchange rate must be positive values.")

        # Adjust the exchange rate for buying USD (include buy spread)
        adjusted_buy_rate = exchange_rate * (1 + buy_spread)
        # Convert EUR to USD at the adjusted buy rate
        usd_after_buy = amount_in_eur * adjusted_buy_rate

        # Adjust the exchange rate for selling USD (include sell spread)
        adjusted_sell_rate = exchange_rate * (1 - sell_spread)
        # Convert USD back to EUR at the adjusted sell rate
        eur_after_sell = usd_after_buy / adjusted_sell_rate

        # Calculate profit or loss in EUR
        profit_loss_eur = eur_after_sell - amount_in_eur

        return {
            "initial_eur": amount_in_eur,
            "usd_after_buy": usd_after_buy,
            "eur_after_sell": eur_after_sell,
            "profit_loss_eur": profit_loss_eur,
        }

    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == "__main__":
    # Simulate trading 1000 EUR
    result = simulate_forex_trading(amount_in_eur=1000)
    print(result)
```
