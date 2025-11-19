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
#!/usr/bin/env python3
"""
Calculate and display fill rates for orders processed through an ecommerce system integrated with Infor SX.e.

This script retrieves order data, calculates fill rates (percentage of items fulfilled),
and displays the results in a clean format. It includes error handling for data retrieval
and processing exceptions.
"""

import sys
from typing import Dict, Tuple, Optional

# Sample data structure mimicking Central Data's example
# In production, this would be replaced with actual API calls to Infor SX.e
SAMPLE_ORDER_DATA = {
    "order_123": {
        "total_items": 150,
        "fulfilled_items": 145,
    },
    "order_456": {
        "total_items": 200,
        "fulfilled_items": 198,
    },
    "order_789": {
        "total_items": 75,
        "fulfilled_items": 75,
    },
}


def get_order_data(order_id: str) -> Optional[Dict[str, int]]:
    """
    Retrieve order data from the ecommerce system.
    
    Args:
        order_id: The order identifier
        
    Returns:
        Dictionary containing 'total_items' and 'fulfilled_items' or None if not found
    """
    try:
        return SAMPLE_ORDER_DATA.get(order_id)
    except Exception as e:
        print(f"Error retrieving order data: {e}", file=sys.stderr)
        return None


def calculate_fill_rate(total_items: int, fulfilled_items: int) -> float:
    """
    Calculate the fill rate percentage.
    
    Args:
        total_items: Total items in the order
        fulfilled_items: Items successfully fulfilled
        
    Returns:
        Fill rate as a percentage (0.0 to 100.0)
        
    Raises:
        ValueError: If total_items is zero or negative
    """
    if total_items <= 0:
        raise ValueError("Total items must be greater than zero")
    
    return (fulfilled_items / total_items) * 100


def display_fill_rates(order_ids: Tuple[str, ...]) -> None:
    """
    Display fill rates for the given order IDs.
    
    Args:
        order_ids: Tuple of order IDs to process
    """
    print("\nOrder Fill Rate Report")
    print("----------------------")
    print("{:<15} {:<15} {:<15} {:<15}".format(
        "Order ID", "Total Items", "Fulfilled", "Fill Rate"
    ))
    
    for order_id in order_ids:
        order_data = get_order_data(order_id)
        if not order_data:
            print(f"{order_id:<15} {'Error':<15} {'N/A':<15} {'N/A':<15}")
            continue
        
        try:
            fill_rate = calculate_fill_rate(
                order_data["total_items"],
                order_data["fulfilled_items"]
            )
            print("{:<15} {:<15} {:<15} {:<15.2f}%".format(
                order_id,
                order_data["total_items"],
                order_data["fulfilled_items"],
                fill_rate
            ))
        except ValueError as e:
            print(f"{order_id:<15} {'Error':<15} {'N/A':<15} {str(e):<15}")
        except Exception as e:
            print(f"{order_id:<15} {'Error':<15} {'N/A':<15} {'Processing error':<15}")


if __name__ == "__main__":
    # In production, order IDs would come from command line args or a data source
    order_ids_to_process = ("order_123", "order_456", "order_789", "order_000")
    
    try:
        display_fill_rates(order_ids_to_process)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)
```
