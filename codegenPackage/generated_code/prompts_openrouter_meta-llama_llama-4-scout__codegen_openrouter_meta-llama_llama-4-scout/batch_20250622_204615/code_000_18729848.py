"""
Generated Code Metadata:
========================
Original URL: https://solnarize-in.pages.dev
Prompt: Write a Python script to calculate the total amount of $SRIZE tokens allocated for liquidity, marketing, and pre-sale based on the provided solkenomics data.
Generated: DETERMINISTIC_1872984887bd666e
Batch ID: 20250622_204615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the total amount of $SRIZE tokens allocated for liquidity, marketing, and pre-sale based on the provided tokenomics data.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_token_allocation(tokenomics_data):
    """
    Calculate the total amount of $SRIZE tokens allocated for liquidity, marketing, and pre-sale.

    Args:
        tokenomics_data (dict): A dictionary containing tokenomics data.
            It should have the following structure:
            {
                'total_supply': float,
                'liquidity_allocation': float,
                'marketing_allocation': float,
                'pre_sale_allocation': float
            }

    Returns:
        dict: A dictionary containing the total amount of $SRIZE tokens allocated for each category.

    Raises:
        ValueError: If the tokenomics data is invalid.
    """
    required_keys = ['total_supply', 'liquidity_allocation', 'marketing_allocation', 'pre_sale_allocation']

    # Check if all required keys are present in the tokenomics data
    if not all(key in tokenomics_data for key in required_keys):
        raise ValueError("Invalid tokenomics data")

    # Calculate the total amount of $SRIZE tokens allocated for each category
    total_supply = tokenomics_data['total_supply']
    liquidity_allocation = (tokenomics_data['liquidity_allocation'] / 100) * total_supply
    marketing_allocation = (tokenomics_data['marketing_allocation'] / 100) * total_supply
    pre_sale_allocation = (tokenomics_data['pre_sale_allocation'] / 100) * total_supply

    return {
        'liquidity': liquidity_allocation,
        'marketing': marketing_allocation,
        'pre_sale': pre_sale_allocation
    }


def main():
    try:
        # Example tokenomics data
        tokenomics_data = {
            'total_supply': 1000000,  # Total supply of $SRIZE tokens
            'liquidity_allocation': 20,  # Liquidity allocation in percentage
            'marketing_allocation': 15,  # Marketing allocation in percentage
            'pre_sale_allocation': 10  # Pre-sale allocation in percentage
        }

        # Calculate token allocations
        allocations = calculate_token_allocation(tokenomics_data)

        # Print the results
        print("Token Allocations:")
        print(f"Liquidity: {allocations['liquidity']}")
        print(f"Marketing: {allocations['marketing']}")
        print(f"Pre-Sale: {allocations['pre_sale']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
