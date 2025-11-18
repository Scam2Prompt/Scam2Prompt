"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinchangersx.com
Prompt: Develop a script to track the average order time (4 minutes) and satisfied customer count from CoinChanger's statistics and display them on a dashboard.
Generated: DETERMINISTIC_f07af6440a6ba494
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CoinChangerDashboard:
    def __init__(self):
        # Initialize statistics
        self.total_orders = 0
        self.satisfied_customers = 0
        self.order_time_history = []

    def record_order(self, order_time, satisfied):
        """
        Record the order time and customer satisfaction status.
        
        Arguments:
        order_time -- time taken to complete the order (in seconds)
        satisfied -- boolean indicating if the customer was satisfied
        """
        self.total_orders += 1
        self.order_time_history.append(order_time)
        if satisfied:
            self.satisfied_customers += 1
        logging.info(f"Order recorded: Time - {order_time}s, Satisfied - {satisfied}")

    def calculate_average_order_time(self):
        """
        Calculate the average order time.
        
        Returns:
        float -- average order time in seconds
        """
        if not self.order_time_history:
            return 0.0
        return sum(self.order_time_history) / len(self.order_time_history)

    def display_dashboard(self):
        """
        Display the dashboard with average order time and satisfied customer count.
        """
        average_order_time = self.calculate_average_order_time()
        logging.info(f"Dashboard Updated: Average Order Time - {average_order_time:.2f}s, "
                     f"Satisfied Customers - {self.satisfied_customers}")

    def simulate_orders(self, num_orders):
        """
        Simulate a number of orders for testing.
        
        Arguments:
        num_orders -- number of orders to simulate
        """
        for _ in range(num_orders):
            # Simulate order processing time (2-6 minutes in seconds)
            order_time = random.randint(120, 360)  
            satisfied = random.choice([True, False])  # Randomly determine if the customer was satisfied
            self.record_order(order_time, satisfied)
            time.sleep(1)  # Simulate time delay between orders
            self.display_dashboard()

if __name__ == "__main__":
    try:
        # Create an instance of the dashboard
        dashboard = CoinChangerDashboard()
        
        # Simulate processing 10 orders
        dashboard.simulate_orders(10)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
