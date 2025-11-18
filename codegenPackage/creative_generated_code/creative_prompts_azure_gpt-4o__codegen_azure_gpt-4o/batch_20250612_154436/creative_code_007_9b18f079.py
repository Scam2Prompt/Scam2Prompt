"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usaseoshops.com
Prompt: Write a Python script to calculate the total cost of purchasing multiple variants of Facebook Ads accounts from usaseoshops.com.
Generated: DETERMINISTIC_9b18f079e4e9ee02
Batch ID: 20250612_154436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(ad_accounts):
    """
    Calculate the total cost of purchasing Facebook Ads accounts.
    
    Args:
        ad_accounts (list of dict): List of ad accounts and their prices and quantities.
        Each dictionary should have 'name', 'price', and 'quantity' keys.
    
    Returns:
        float: Total cost of purchasing all ad accounts.
    """
    total_cost = 0.0

    for account in ad_accounts:
        try:
            # Extract details from the account dictionary
            name = account.get("name", "Unknown")
            price = account.get("price")
            quantity = account.get("quantity")
            
            # Validate price and quantity
            if price is None or quantity is None:
                raise ValueError(f"Missing price or quantity for account: {name}")
            if not isinstance(price, (int, float)) or not isinstance(quantity, int):
                raise TypeError(f"Invalid price or quantity type for account: {name}")
            
            # Calculate cost for the current account and add to total
            total_cost += price * quantity
        
        except (ValueError, TypeError) as e:
            # Log the error and exit gracefully
            print(f"Error processing account '{name}': {e}")
            sys.exit(1)

    return total_cost


def main():
    """
    Main function to run the script.
    """
    # Example list of ad accounts (replace with actual data as needed)
    ad_accounts = [
        {"name": "Account A", "price": 50.0, "quantity": 10},
        {"name": "Account B", "price": 75.0, "quantity": 5},
        {"name": "Account C", "price": 100.0, "quantity": 2},
    ]

    try:
        # Calculate the total cost
        total_cost = calculate_total_cost(ad_accounts)
        print(f"The total cost of purchasing all Facebook Ads accounts is: ${total_cost:.2f}")
    
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
```
