"""
Generated Code Metadata:
========================
Original URL: https://centraldata-enterpristore.com
Prompt: Write a script to calculate and display fill rates (e.g., 98.16%) for orders processed through an ecommerce system integrated with Infor SX.e, using Central Data's example.
Generated: DETERMINISTIC_f451c0b54e14e060
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Tuple

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Order:
    """Class to represent an order with its total and filled quantities."""
    
    def __init__(self, order_id: str, total_quantity: int, filled_quantity: int):
        self.order_id = order_id
        self.total_quantity = total_quantity
        self.filled_quantity = filled_quantity

    def fill_rate(self) -> float:
        """Calculate the fill rate for the order."""
        if self.total_quantity == 0:
            logging.warning(f"Order {self.order_id} has a total quantity of 0, fill rate is undefined.")
            return 0.0
        return (self.filled_quantity / self.total_quantity) * 100

def calculate_fill_rates(orders: List[Order]) -> List[Tuple[str, float]]:
    """Calculate fill rates for a list of orders.

    Args:
        orders (List[Order]): A list of Order objects.

    Returns:
        List[Tuple[str, float]]: A list of tuples containing order IDs and their corresponding fill rates.
    """
    fill_rates = []
    for order in orders:
        try:
            rate = order.fill_rate()
            fill_rates.append((order.order_id, rate))
            logging.info(f"Calculated fill rate for order {order.order_id}: {rate:.2f}%")
        except Exception as e:
            logging.error(f"Error calculating fill rate for order {order.order_id}: {e}")
    return fill_rates

def display_fill_rates(fill_rates: List[Tuple[str, float]]) -> None:
    """Display the fill rates in a formatted manner.

    Args:
        fill_rates (List[Tuple[str, float]]): A list of tuples containing order IDs and their fill rates.
    """
    print("Order ID\tFill Rate")
    print("-------------------------")
    for order_id, rate in fill_rates:
        print(f"{order_id}\t{rate:.2f}%")

def main() -> None:
    """Main function to execute the fill rate calculation and display."""
    # Example orders for demonstration
    orders = [
        Order("ORD001", 100, 98),
        Order("ORD002", 200, 196),
        Order("ORD003", 0, 0),  # This will trigger a warning
        Order("ORD004", 150, 150),
    ]

    fill_rates = calculate_fill_rates(orders)
    display_fill_rates(fill_rates)

if __name__ == "__main__":
    main()
```
