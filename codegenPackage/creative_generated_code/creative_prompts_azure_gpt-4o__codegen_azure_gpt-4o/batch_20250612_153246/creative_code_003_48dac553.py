"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop.zircon-ssd.com
Prompt: Write a script to calculate the total cost of purchasing multiple Zircon Z1 SSDs (e.g., 128GB, 256GB, and 512GB) with their current sale prices.
Generated: DETERMINISTIC_48dac5537d47bda3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the total cost of purchasing multiple Zircon Z1 SSDs

# Importing necessary module for error handling
import sys

def calculate_total_cost(ssd_prices, quantities):
    """
    Calculate the total cost of purchasing multiple SSDs based on their prices and quantities.

    Args:
        ssd_prices (dict): A dictionary containing SSD models and their sale prices.
        quantities (dict): A dictionary containing SSD models and their desired quantities.

    Returns:
        float: The total cost of the purchase.

    Raises:
        ValueError: If a model in quantities does not exist in ssd_prices.
    """
    total_cost = 0.0

    for model, qty in quantities.items():
        # Check if the model exists in the price list
        if model not in ssd_prices:
            raise ValueError(f"Model '{model}' not found in the price list.")
        
        # Ensure quantity is a non-negative integer
        if qty < 0:
            raise ValueError(f"Quantity for model '{model}' cannot be negative.")
        
        # Add the cost for the current model to the total cost
        total_cost += ssd_prices[model] * qty

    return total_cost


def main():
    """
    Main function to calculate the total cost for purchasing SSDs.
    """
    # Dictionary of SSD models and their sale prices (in USD)
    ssd_prices = {
        "128GB": 49.99,
        "256GB": 79.99,
        "512GB": 129.99,
    }

    # Dictionary of SSD models and their quantities to purchase
    quantities = {
        "128GB": 3,
        "256GB": 2,
        "512GB": 1,
    }

    try:
        # Calculate the total cost
        total_cost = calculate_total_cost(ssd_prices, quantities)

        # Output the result
        print(f"The total cost of purchasing the SSDs is: ${total_cost:.2f}")

    except ValueError as e:
        # Handle value errors gracefully and display a meaningful message
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
