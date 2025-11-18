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
from typing import List, Dict
from datetime import datetime, timedelta

class ProductionScheduleOptimizer:
    def __init__(self, production_lead_time: int, deadlines: Dict[str, str]):
        """
        Initializes the ProductionScheduleOptimizer with lead time and deadlines.

        :param production_lead_time: Time in days required for production.
        :param deadlines: Dictionary where keys are product types and values are their deadlines.
        """
        self.production_lead_time = production_lead_time
        self.deadlines = {k: datetime.strptime(v, '%Y-%m-%d') for k, v in deadlines.items()}

    def schedule_production(self, product_orders: Dict[str, int]) -> Dict[str, str]:
        """
        Schedules production for given product orders ensuring on-time delivery.

        :param product_orders: Dictionary where keys are product types and values are quantities ordered.
        :return: Dictionary with product types and their scheduled production dates.
        """
        production_schedule = {}
        
        for product, quantity in product_orders.items():
            if product not in self.deadlines:
                raise ValueError(f"Product '{product}' not found in deadlines.")

            delivery_date = self.deadlines[product]
            start_production_date = delivery_date - timedelta(days=self.production_lead_time)

            # Validate if production can start on or before the current date
            if start_production_date < datetime.now():
                raise RuntimeError(f"Cannot schedule production for '{product}'. "
                                   f"Lead time exceeds available days before the deadline.")

            production_schedule[product] = start_production_date.strftime('%Y-%m-%d')

        return production_schedule

if __name__ == "__main__":
    # Example usage of the ProductionScheduleOptimizer
    
    # Define production lead time (in days)
    LEAD_TIME = 5  
    
    # Define product deadlines
    deadlines = {
        "HDPE Jars": "2023-12-15",
        "Jerrycanes": "2023-12-20"
    }
    
    # Define product orders
    product_orders = {
        "HDPE Jars": 100,
        "Jerrycanes": 50
    }

    try:
        optimizer = ProductionScheduleOptimizer(LEAD_TIME, deadlines)
        schedule = optimizer.schedule_production(product_orders)
        print("Production Schedule:", schedule)
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
