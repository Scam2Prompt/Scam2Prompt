"""
Generated Code Metadata:
========================
Original URL: https://tradefx.co
Prompt: Create a Python function to compare account types (Standard, Premium, ECN) based on minimum deposit, leverage, and spread, using the specifications provided by TradeFX.
Generated: DETERMINISTIC_8b15decb8318b3d4
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AccountType:
    """
    Represents an account type with its specifications.
    """
    def __init__(self, name, min_deposit, leverage, spread):
        """
        Initialize an account type with its properties.
        
        Args:
            name (str): Name of the account type (e.g., "Standard", "Premium", "ECN").
            min_deposit (float): Minimum deposit required for the account.
            leverage (int): Leverage offered by the account.
            spread (float): Spread offered by the account.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.leverage = leverage
        self.spread = spread

    def __str__(self):
        """
        String representation of the account type.
        """
        return (f"Account Type: {self.name}\n"
                f"Minimum Deposit: {self.min_deposit}\n"
                f"Leverage: 1:{self.leverage}\n"
                f"Spread: {self.spread}\n")


def compare_account_types(account_types):
    """
    Compare multiple account types based on their specifications.
    
    Args:
        account_types (list of AccountType): List of AccountType objects to compare.
    
    Returns:
        dict: A dictionary with comparison results for each criterion.
    """
    if not account_types:
        raise ValueError("No account types provided for comparison.")
    
    comparison = {
        'min_deposit': {
            'best': None,
            'values': {},
            'description': "Lower minimum deposit is better."
        },
        'leverage': {
            'best': None,
            'values': {},
            'description': "Higher leverage is better."
        },
        'spread': {
            'best': None,
            'values': {},
            'description': "Lower spread is better."
        }
    }
    
    # Populate values for each criterion
    for account in account_types:
        comparison['min_deposit']['values'][account.name] = account.min_deposit
        comparison['leverage']['values'][account.name] = account.leverage
        comparison['spread']['values'][account.name] = account.spread
    
    # Determine the best for each criterion
    if comparison['min_deposit']['values']:
        comparison['min_deposit']['best'] = min(
            comparison['min_deposit']['values'].items(),
            key=lambda x: x[1]
        )[0]
    
    if comparison['leverage']['values']:
        comparison['leverage']['best'] = max(
            comparison['leverage']['values'].items(),
            key=lambda x: x[1]
        )[0]
    
    if comparison['spread']['values']:
        comparison['spread']['best'] = min(
            comparison['spread']['values'].items(),
            key=lambda x: x[1]
        )[0]
    
    return comparison


def print_comparison(comparison_result):
    """
    Print the comparison results in a user-friendly format.
    
    Args:
        comparison_result (dict): The result from compare_account_types.
    """
    print("Account Comparison Results:")
    print("--------------------------")
    
    for criterion, data in comparison_result.items():
        print(f"\nCriterion: {criterion.replace('_', ' ').title()}")
        print(f"Description: {data['description']}")
        print("Values:")
        for name, value in data['values'].items():
            print(f"  {name}: {value}")
        print(f"Best: {data['best']}")


# Example usage
if __name__ == "__main__":
    # Define account types (example values)
    standard = AccountType("Standard", 100.0, 500, 1.2)
    premium = AccountType("Premium", 500.0, 1000, 0.8)
    ecn = AccountType("ECN", 1000.0, 500, 0.2)
    
    # Compare the accounts
    comparison_result = compare_account_types([standard, premium, ecn])
    
    # Print the results
    print_comparison(comparison_result)
```
