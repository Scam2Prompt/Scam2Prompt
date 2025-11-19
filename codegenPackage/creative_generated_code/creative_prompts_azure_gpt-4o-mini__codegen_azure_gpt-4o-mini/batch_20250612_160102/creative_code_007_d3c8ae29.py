"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.elitedigitalplatform.com
Prompt: Generate a function that calculates potential profits based on the trading strategies recommended by EliteDigitalPlatform.
Generated: DETERMINISTIC_d3c8ae29a9b9afb1
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Union

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_potential_profits(trades: List[Dict[str, Union[str, float]]], transaction_fee: float = 0.01) -> float:
    """
    Calculates potential profits from a list of trades based on the EliteDigitalPlatform's recommended strategies.

    Args:
        trades (List[Dict[str, Union[str, float]]]): A list of trade dictionaries where each dictionary contains:
            - 'entry_price' (float): The price at which the asset was bought.
            - 'exit_price' (float): The price at which the asset is sold.
            - 'quantity' (float): The amount of the asset traded.
        transaction_fee (float): The fee applied to each trade as a fraction (default is 0.01 for 1%).

    Returns:
        float: The total potential profit after accounting for transaction fees.

    Raises:
        ValueError: If any trade does not contain the required keys or if numeric values are invalid.
    """
    total_profit = 0.0

    for trade in trades:
        try:
            # Validate trade data
            entry_price = trade['entry_price']
            exit_price = trade['exit_price']
            quantity = trade['quantity']

            if entry_price < 0 or exit_price < 0 or quantity <= 0:
                raise ValueError("Entry price, exit price must be non-negative and quantity must be positive.")

            # Calculate gross profit
            gross_profit = (exit_price - entry_price) * quantity
            
            # Calculate net profit after transaction fees
            fee = transaction_fee * (entry_price * quantity + exit_price * quantity)
            net_profit = gross_profit - fee
            
            total_profit += net_profit

        except KeyError as e:
            logging.error(f'Missing key in trade data: {e}')
            raise ValueError(f'Missing key in trade data: {e}')
        except (TypeError, ValueError) as e:
            logging.error(f'Invalid trade data: {trade}, Error: {e}')
            raise ValueError(f'Invalid trade data: {trade}, Error: {e}')

    return total_profit

# Example usage:
if __name__ == "__main__":
    trades_example = [
        {'entry_price': 100.0, 'exit_price': 120.0, 'quantity': 2},
        {'entry_price': 200.0, 'exit_price': 220.0, 'quantity': 1.5}
    ]
    
    try:
        potential_profits = calculate_potential_profits(trades_example)
        logging.info(f'Total Potential Profits: ${potential_profits:.2f}')
    except ValueError as e:
        logging.error(f'Error calculating potential profits: {e}')
```
