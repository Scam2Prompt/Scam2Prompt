"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraldata-enterpristore.com
Prompt: Write a script to calculate and display fill rates (e.g., 98.16%) for orders processed through an ecommerce system integrated with Infor SX.e, using Central Data's example.
Generated: DETERMINISTIC_f451c0b54e14e060
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import logging
from decimal import Decimal, ROUND_HALF_UP

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_fill_rate(total_orders, fulfilled_orders):
    """
    Calculate the fill rate as a percentage.

    Args:
        total_orders (int): Total number of orders processed.
        fulfilled_orders (int): Number of orders successfully fulfilled.

    Returns:
        str: Fill rate percentage formatted as a string (e.g., "98.16%").
    """
    try:
        # Ensure total_orders and fulfilled_orders are valid
        if total_orders <= 0:
            raise ValueError("Total orders must be greater than 0.")
        if fulfilled_orders < 0:
            raise ValueError("Fulfilled orders cannot be negative.")
        
        # Calculate the fill rate
        fill_rate = (Decimal(fulfilled_orders) / Decimal(total_orders)) * 100
        
        # Round to 2 decimal places
        fill_rate = fill_rate.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        # Return the fill rate as a formatted string
        return f"{fill_rate}%"
    except Exception as e:
        logging.error(f"Error calculating fill rate: {e}")
        raise

def main():
    """
    Main function to calculate and display fill rates for ecommerce orders.
    """
    try:
        # Example data for orders processed through an ecommerce system
        # These values should ideally come from an integrated system or a database
        total_orders = 1234  # Total number of processed orders
        fulfilled_orders = 1210  # Number of successfully fulfilled orders

        # Calculate fill rate
        fill_rate = calculate_fill_rate(total_orders, fulfilled_orders)

        # Display the fill rate
        logging.info(f"Total Orders: {total_orders}, Fulfilled Orders: {fulfilled_orders}, Fill Rate: {fill_rate}")
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")
        sys.exit(1)

# Entry point for script execution
if __name__ == "__main__":
    main()
```
