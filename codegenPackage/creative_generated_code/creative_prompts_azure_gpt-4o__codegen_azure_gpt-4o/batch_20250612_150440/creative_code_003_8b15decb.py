"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradefx.co
Prompt: Create a Python function to compare account types (Standard, Premium, ECN) based on minimum deposit, leverage, and spread, using the specifications provided by TradeFX.
Generated: DETERMINISTIC_8b15decb8318b3d4
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

def compare_account_types(account_specs: List[Dict[str, any]]) -> List[str]:
    """
    Compare account types based on given specifications.

    Args:
        account_specs (List[Dict[str, any]]): A list of dictionaries where each dictionary
                                              represents an account type with attributes:
                                              - 'name' (str): Account name (e.g., Standard, Premium, ECN)
                                              - 'min_deposit' (float): Minimum deposit required
                                              - 'leverage' (int): Maximum leverage offered
                                              - 'spread' (float): Spread in pips
    
    Returns:
        List[str]: A list of formatted strings comparing the account types.
    """
    try:
        # Sort accounts by minimum deposit (ascending), leverage (descending), and spread (ascending)
        sorted_accounts = sorted(
            account_specs,
            key=lambda x: (x['min_deposit'], -x['leverage'], x['spread'])
        )
        
        # Create a comparison report
        comparison_results = []
        for account in sorted_accounts:
            result = (
                f"Account: {account['name']}\n"
                f"- Minimum Deposit: ${account['min_deposit']}\n"
                f"- Leverage: {account['leverage']}x\n"
                f"- Spread: {account['spread']} pips\n"
            )
            comparison_results.append(result)
        
        return comparison_results
    
    except KeyError as e:
        raise ValueError(f"Missing required key in account specification: {e}")
    except TypeError as e:
        raise ValueError(f"Invalid type in account specification: {e}")

# Example usage
if __name__ == "__main__":
    # Define account specifications
    account_data = [
        {"name": "Standard", "min_deposit": 100.0, "leverage": 100, "spread": 1.2},
        {"name": "Premium", "min_deposit": 500.0, "leverage": 200, "spread": 0.8},
        {"name": "ECN", "min_deposit": 1000.0, "leverage": 500, "spread": 0.2},
    ]

    # Compare accounts and print results
    try:
        results = compare_account_types(account_data)
        print("\nAccount Comparison Results:\n")
        for result in results:
            print(result)
    except ValueError as e:
        print(f"Error: {e}")
```
