"""
Generated Code Metadata:
========================
Original URL: https://bernwears.com
Prompt: Develop a function that calculates the estimated delivery time for bulk orders, taking into account the production and shipping processes mentioned by Bern Wears.
Generated: DETERMINISTIC_9df2c67da30bdfe9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta
from typing import Optional

def calculate_delivery_time(
    order_quantity: int,
    production_capacity_per_day: int = 100,
    production_days_offset: int = 2,
    shipping_days: int = 3,
    current_date: Optional[datetime] = None
) -> datetime:
    """
    Calculate the estimated delivery date for bulk orders based on production and shipping time.

    Args:
        order_quantity: Number of items ordered
        production_capacity_per_day: Number of items that can be produced per day (default: 100)
        production_days_offset: Additional days before production starts (default: 2)
        shipping_days: Days required for shipping after production completes (default: 3)
        current_date: Date from which to calculate (default: current date if None)

    Returns:
        Estimated delivery date as datetime object

    Raises:
        ValueError: If order_quantity or any time parameter is negative
    """
    # Validate inputs
    if order_quantity < 0:
        raise ValueError("Order quantity cannot be negative")
    if production_capacity_per_day <= 0:
        raise ValueError("Production capacity must be positive")
    if production_days_offset < 0:
        raise ValueError("Production days offset cannot be negative")
    if shipping_days < 0:
        raise ValueError("Shipping days cannot be negative")

    # Use current date if not provided
    if current_date is None:
        current_date = datetime.now()

    # Calculate production days needed (rounded up)
    production_days_needed = math.ceil(order_quantity / production_capacity_per_day)

    # Calculate total days required
    total_days = production_days_offset + production_days_needed + shipping_days

    # Calculate delivery date
    delivery_date = current_date + timedelta(days=total_days)

    return delivery_date
```
