"""
Generated Code Metadata:
========================
Original URL: https://hackway.su
Prompt: Generate a list of VK.com account types (e.g., active, non-active, spam block) and their corresponding prices in different regions (e.g., Russia, Belarus, CIS).
Generated: DETERMINISTIC_787f843c709fc0d7
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, TypedDict

class AccountType(TypedDict):
    """Represents an account type and its prices in different regions."""
    name: str
    prices: Dict[str, float]

def get_vk_account_types() -> List[AccountType]:
    """
    Returns a list of VK.com account types with their corresponding prices in different regions.
    
    Returns:
        List[AccountType]: A list of account types with regional pricing information.
    """
    return [
        {
            "name": "Active",
            "prices": {
                "Russia": 10.0,
                "Belarus": 8.5,
                "CIS": 7.0,
                "Other": 5.0
            }
        },
        {
            "name": "Non-active",
            "prices": {
                "Russia": 5.0,
                "Belarus": 4.0,
                "CIS": 3.5,
                "Other": 2.5
            }
        },
        {
            "name": "Spam block",
            "prices": {
                "Russia": 2.0,
                "Belarus": 1.5,
                "CIS": 1.0,
                "Other": 0.5
            }
        },
        {
            "name": "Premium",
            "prices": {
                "Russia": 20.0,
                "Belarus": 18.0,
                "CIS": 15.0,
                "Other": 12.0
            }
        }
    ]

def display_account_types(account_types: List[AccountType]) -> None:
    """Displays the account types and their prices in a formatted table."""
    print("\nVK.com Account Types and Prices:")
    print("-" * 50)
    print(f"{'Account Type':<15} | {'Russia':<10} | {'Belarus':<10} | {'CIS':<10} | {'Other':<10}")
    print("-" * 50)
    
    for account in account_types:
        prices = account["prices"]
        print(
            f"{account['name']:<15} | "
            f"{prices['Russia']:<10.2f} | "
            f"{prices['Belarus']:<10.2f} | "
            f"{prices['CIS']:<10.2f} | "
            f"{prices['Other']:<10.2f}"
        )

if __name__ == "__main__":
    try:
        account_types = get_vk_account_types()
        display_account_types(account_types)
    except Exception as e:
        print(f"An error occurred: {e}")
```
