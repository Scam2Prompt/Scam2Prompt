"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artocean.org
Prompt: Write a function to calculate the total earnings from NFT sales, using the top seller data provided on the Artlife platform.
Generated: DETERMINISTIC_7ed477616bc8ac8a
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class NFTSalesError(Exception):
    """Custom exception for errors related to NFT sales calculations."""
    pass

def calculate_total_earnings(sales_data: List[Dict[str, float]]) -> float:
    """
    Calculate the total earnings from NFT sales.

    Args:
        sales_data (List[Dict[str, float]]): A list of dictionaries containing sales data
            where each dictionary has 'sale_price' and 'quantity_sold'.

    Returns:
        float: The total earnings from all NFT sales.

    Raises:
        NFTSalesError: If sales_data is empty or if any sale record is invalid.
    """
    # Validate input
    if not sales_data:
        raise NFTSalesError("Sales data cannot be empty.")

    total_earnings = 0.0

    for record in sales_data:
        # Check if the record has the required keys and valid values
        if 'sale_price' not in record or 'quantity_sold' not in record:
            raise NFTSalesError("Each sales record must contain 'sale_price' and 'quantity_sold'.")
        
        sale_price = record['sale_price']
        quantity_sold = record['quantity_sold']
        
        # Validate that sale_price and quantity_sold are numeric and non-negative
        if not isinstance(sale_price, (int, float)) or not isinstance(quantity_sold, (int, float)):
            raise NFTSalesError("Sale price and quantity sold must be numeric.")
        
        if sale_price < 0 or quantity_sold < 0:
            raise NFTSalesError("Sale price and quantity sold must be non-negative.")
        
        # Calculate earnings for the current record
        earnings = sale_price * quantity_sold
        total_earnings += earnings

    return total_earnings

# Example usage:
if __name__ == "__main__":
    # Sample sales data from the Artlife platform
    sample_sales_data = [
        {'sale_price': 150.0, 'quantity_sold': 2},
        {'sale_price': 200.0, 'quantity_sold': 1},
        {'sale_price': 50.0, 'quantity_sold': 5},
    ]

    try:
        total = calculate_total_earnings(sample_sales_data)
        print(f"Total earnings from NFT sales: ${total:.2f}")
    except NFTSalesError as e:
        print(f"Error calculating earnings: {e}")
```
