"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-monprotocolcom.pages.dev
Prompt: Generate a code snippet that calculates the total cost in ETH for purchasing multiple Pixelmon lots during the MON Protocol presale.
Generated: DETERMINISTIC_3466f147475d3966
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(eth_price_per_lot, lots_to_purchase):
    """
    Calculate the total cost in ETH for purchasing multiple Pixelmon lots.

    Parameters:
        eth_price_per_lot (float): Price of one Pixelmon lot in ETH.
        lots_to_purchase (int): The number of Pixelmon lots to purchase.

    Returns:
        float: Total cost in ETH for the given number of lots.
    """
    try:
        # Validate input parameters
        if eth_price_per_lot <= 0:
            raise ValueError("ETH price per lot must be greater than zero.")
        if lots_to_purchase <= 0:
            raise ValueError("Number of lots to purchase must be greater than zero.")
        
        # Calculate and return total cost
        return eth_price_per_lot * lots_to_purchase
    except ValueError as e:
        # Handle invalid input
        print(f"Input Error: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    try:
        # Example usage
        # Prompt user for ETH price per lot and number of lots to purchase
        eth_price_per_lot = float(input("Enter the price per Pixelmon lot in ETH: "))
        lots_to_purchase = int(input("Enter the number of Pixelmon lots you wish to purchase: "))
        
        # Calculate total cost
        total_cost = calculate_total_cost(eth_price_per_lot, lots_to_purchase)
        
        if total_cost is not None:
            # Display the total cost in ETH
            print(f"Total cost for purchasing {lots_to_purchase} Pixelmon lots is {total_cost:.4f} ETH.")
        else:
            print("Failed to calculate total cost due to invalid input.")
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected Error: {e}", file=sys.stderr)
```
