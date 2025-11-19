"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.nl
Prompt: Develop a Python function to categorize investment types (e.g., cryptocurrencies, Forex, stocks) and provide a brief description for each, based on Immediate Peak's educational content.
Generated: DETERMINISTIC_83b2fa607d5d91b7
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict, Optional

# Define a function to categorize investment types and provide descriptions
def categorize_investment(investment_type: str) -> Optional[Dict[str, str]]:
    """
    Categorizes the given investment type and provides a brief description.

    Args:
        investment_type (str): The type of investment to categorize (e.g., 'cryptocurrency', 'forex', 'stocks').

    Returns:
        Optional[Dict[str, str]]: A dictionary containing the category and description of the investment type,
                                  or None if the investment type is not recognized.
    """
    # Normalize the input to lowercase for case-insensitive matching
    investment_type = investment_type.strip().lower()

    # Dictionary of investment types and their descriptions
    investment_categories = {
        "cryptocurrency": {
            "category": "Cryptocurrencies",
            "description": "Digital or virtual currencies that use cryptography for security, such as Bitcoin and Ethereum."
        },
        "forex": {
            "category": "Foreign Exchange (Forex)",
            "description": "The global marketplace for trading national currencies against one another."
        },
        "stocks": {
            "category": "Stocks",
            "description": "Shares of ownership in a company, allowing investors to participate in its growth and profits."
        },
        "bonds": {
            "category": "Bonds",
            "description": "Fixed-income investments where investors lend money to entities in exchange for periodic interest payments."
        },
        "real estate": {
            "category": "Real Estate",
            "description": "Investments in physical properties such as residential, commercial, or industrial buildings."
        },
        "mutual funds": {
            "category": "Mutual Funds",
            "description": "Pooled investment vehicles managed by professionals, investing in a diversified portfolio of assets."
        },
        "etfs": {
            "category": "Exchange-Traded Funds (ETFs)",
            "description": "Investment funds traded on stock exchanges, holding a diversified portfolio of assets."
        },
        "commodities": {
            "category": "Commodities",
            "description": "Physical goods such as gold, oil, or agricultural products traded on specialized markets."
        }
    }

    # Check if the investment type exists in the dictionary
    if investment_type in investment_categories:
        return investment_categories[investment_type]
    else:
        # Return None if the investment type is not recognized
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Input from the user
        user_input = input("Enter an investment type (e.g., cryptocurrency, forex, stocks): ").strip()
        
        # Get the category and description
        result = categorize_investment(user_input)
        
        if result:
            print(f"Category: {result['category']}")
            print(f"Description: {result['description']}")
        else:
            print("Error: Unrecognized investment type. Please try again.")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
