"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-halo.pages.dev
Prompt: Write a function to calculate total airdrop gains and paperhanded amounts, similar to the metrics provided by Halo's analytics.
Generated: DETERMINISTIC_463b175a92357c97
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

def calculate_airdrop_metrics(transactions: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Calculate total airdrop gains and paperhanded amounts.
    
    Args:
        transactions (List[Dict[str, float]]): List of dictionaries containing transaction data.
            Each dictionary should have the following keys:
            - 'amount_airdropped': The amount of tokens initially airdropped.
            - 'amount_sold': The amount of tokens sold.
            - 'sale_price': The price at which the tokens were sold.
            - 'current_price': The current price of the token.
    
    Returns:
        Dict[str, float]: A dictionary containing:
            - 'total_airdrop_gains': Total profit or gain from airdropped tokens.
            - 'total_paperhanded_amount': Total potential profit lost by selling early.
    """
    
    # Initialize metrics
    total_airdrop_gains = 0.0
    total_paperhanded_amount = 0.0
    
    # Process each transaction
    for transaction in transactions:
        try:
            # Extract transaction data
            amount_airdropped = transaction.get('amount_airdropped', 0.0)
            amount_sold = transaction.get('amount_sold', 0.0)
            sale_price = transaction.get('sale_price', 0.0)
            current_price = transaction.get('current_price', 0.0)
            
            # Calculate profit from sold tokens
            gain_from_sold = amount_sold * sale_price
            
            # Calculate potential gain if tokens were held
            potential_gain = amount_sold * current_price
            
            # Calculate paperhanded amount (lost potential profit)
            paperhanded_amount = max(0, potential_gain - gain_from_sold)
            
            # Add gains from airdropped tokens that are still held
            gain_from_unsold = (amount_airdropped - amount_sold) * current_price
            
            # Update metrics
            total_airdrop_gains += gain_from_sold + gain_from_unsold
            total_paperhanded_amount += paperhanded_amount
        
        except TypeError:
            # Handle potential type errors during calculations
            print("Error: Invalid transaction format or data type.")
            continue
    
    return {
        'total_airdrop_gains': total_airdrop_gains,
        'total_paperhanded_amount': total_paperhanded_amount
    }

# Example usage
if __name__ == "__main__":
    # Example transaction data
    transactions = [
        {
            'amount_airdropped': 1000.0,
            'amount_sold': 500.0,
            'sale_price': 2.0,
            'current_price': 5.0
        },
        {
            'amount_airdropped': 2000.0,
            'amount_sold': 1500.0,
            'sale_price': 3.0,
            'current_price': 4.0
        }
    ]
    
    # Calculate metrics
    result = calculate_airdrop_metrics(transactions)
    print("Airdrop Metrics:", result)
```
