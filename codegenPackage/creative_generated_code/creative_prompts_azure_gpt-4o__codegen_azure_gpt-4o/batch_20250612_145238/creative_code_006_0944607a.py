"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmgroupnepal.com
Prompt: Develop a Python function to optimize the production schedule for HDPE jars and jerrycanes, ensuring on-time delivery as highlighted by MM Group Nepal.
Generated: DETERMINISTIC_0944607ac529c3ef
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Tuple


class ProductionScheduleOptimizer:
    """
    A class to optimize the production schedule for HDPE jars and jerrycans,
    ensuring on-time delivery based on demand and production capacities.
    """

    def __init__(self, daily_capacity: int):
        """
        Initialize the optimizer with the daily production capacity.

        :param daily_capacity: The maximum number of items (jars + jerrycans) 
                               that can be produced daily.
        """
        self.daily_capacity = daily_capacity

    def optimize_schedule(
        self,
        orders: List[Tuple[str, int, str, datetime]],
    ) -> List[Tuple[str, datetime, datetime]]:
        """
        Optimize the production schedule for on-time delivery.

        :param orders: A list of orders, where each order is represented as
                       a tuple (product_type, quantity, client_name, due_date).
                       product_type: 'jar' or 'jerrycan'
                       quantity: units needed
                       client_name: name of the client
                       due_date: deadline for the order (datetime)
        :return: A list of production schedules, where each schedule is represented as:
                 (client_name, start_date, end_date)
        """
        # Sort orders by due date to prioritize the earliest deadlines
        orders = sorted(orders, key=lambda x: x[3])

        # Schedule results (client_name, start_date, end_date)
        schedule = []

        # Start production on today's date
        current_date = datetime.now()

        for order in orders:
            product_type, quantity, client_name, due_date = order

            # Calculate the number of production days required for this order
            days_needed = -(-quantity // self.daily_capacity)  # Ceiling division

            # Calculate the end date for this order
            end_date = current_date + timedelta(days=days_needed - 1)

            # Check if the order can be completed by the due date
            if end_date > due_date:
                raise ValueError(
                    f"Order for {client_name} cannot be completed on time! "
                    f"Due date: {due_date.date()}, Estimated end date: {end_date.date()}."
                )

            # Add the production schedule for this order
            schedule.append((client_name, current_date, end_date))

            # Update the current date for the next order
            current_date = end_date + timedelta(days=1)  # Start new order the next day

        return schedule


# Example usage
if __name__ == "__main__":
    try:
        # Daily production capacity of 100 units
        optimizer = ProductionScheduleOptimizer(daily_capacity=100)

        # List of orders (product_type, quantity, client_name, due_date)
        orders = [
            ("jar", 200, "Client A", datetime(2023, 11, 10)),
            ("jerrycan", 150, "Client B", datetime(2023, 11, 12)),
            ("jar", 50, "Client C", datetime(2023, 11, 9)),
        ]

        # Get the optimized production schedule
        schedule = optimizer.optimize_schedule(orders)

        # Print the schedule
        print("Optimized Production Schedule:")
        for client_name, start_date, end_date in schedule:
            print(
                f"Client: {client_name}, Start Date: {start_date.date()}, End Date: {end_date.date()}"
            )
    except Exception as e:
        print(f"Error: {e}")
```
