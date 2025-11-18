"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pavainc.com
Prompt: Create a program to generate automated delivery schedules for bulk salt orders, ensuring fast delivery throughout the Mid-Atlantic region as described on the PAVA Salt & Stone website.
Generated: DETERMINISTIC_82e7b67ce2df721c
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Tuple
import random

# Constants for the Mid-Atlantic region
MID_ATLANTIC_STATES = ["MD", "VA", "PA", "DC", "DE", "NJ"]
DELIVERY_TIMES = {
    "MD": 2,  # Delivery time in days
    "VA": 3,
    "PA": 3,
    "DC": 2,
    "DE": 1,
    "NJ": 2
}

class SaltOrder:
    """Class representing a bulk salt order."""
    
    def __init__(self, customer_name: str, quantity: float, delivery_state: str):
        if delivery_state not in MID_ATLANTIC_STATES:
            raise ValueError(f"Invalid delivery state: {delivery_state}. Must be one of {MID_ATLANTIC_STATES}.")
            
        self.customer_name = customer_name
        self.quantity = quantity  # in tons
        self.delivery_state = delivery_state
        self.order_date = datetime.datetime.now()
        
    def calculate_delivery_date(self) -> datetime.datetime:
        """Calculates the expected delivery date based on the order date."""
        delivery_days = DELIVERY_TIMES[self.delivery_state]
        return self.order_date + datetime.timedelta(days=delivery_days)

class DeliveryScheduler:
    """Class to handle delivery scheduling for bulk salt orders."""
    
    def __init__(self):
        self.orders: List[SaltOrder] = []
        
    def add_order(self, order: SaltOrder) -> None:
        """Adds a new order to the delivery schedule."""
        self.orders.append(order)
    
    def generate_schedule(self) -> List[Dict[str, str]]:
        """Generates a delivery schedule for all orders."""
        schedule = []
        for order in self.orders:
            delivery_date = order.calculate_delivery_date()
            schedule_entry = {
                "Customer Name": order.customer_name,
                "Quantity (tons)": order.quantity,
                "Delivery State": order.delivery_state,
                "Order Date": order.order_date.strftime("%Y-%m-%d"),
                "Expected Delivery Date": delivery_date.strftime("%Y-%m-%d")
            }
            schedule.append(schedule_entry)
        return schedule

def main() -> None:
    """Main function to execute the delivery scheduling program."""
    try:
        scheduler = DeliveryScheduler()
        
        # Sample orders
        orders_data = [
            ("John Doe", 10.0, "MD"),
            ("Alice Smith", 5.0, "VA"),
            ("Bob Johnson", 15.0, "PA"),
            ("Charlie Brown", 8.0, "DC"),
            ("Daisy Miller", 12.0, "DE"),
            ("Eve Davis", 20.0, "NJ"),
            ("Invalid User", 5.0, "XX")  # This will raise an exception
        ]
        
        for customer_name, quantity, delivery_state in orders_data:
            try:
                order = SaltOrder(customer_name, quantity, delivery_state)
                scheduler.add_order(order)
            except ValueError as e:
                print(f"Error adding order: {e}")
        
        # Generate the delivery schedule
        schedule = scheduler.generate_schedule()
        
        # Output the schedule
        for entry in schedule:
            print(entry)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
