"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.napatablets.com
Prompt: Create a tutorial on how to use the Delivery Tracker for tracking deliveries and analyzing performance metrics in an auto parts business.
Generated: DETERMINISTIC_3383e1f9900a5f7e
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# delivery_tracker.py

import datetime
import json
from typing import List, Dict, Optional

class Delivery:
    """Class to represent a delivery in the auto parts business."""
    
    def __init__(self, delivery_id: int, item: str, delivery_date: str, status: str):
        """
        Initializes a new delivery instance.

        Args:
            delivery_id (int): Unique identifier for the delivery.
            item (str): The item being delivered.
            delivery_date (str): Date of delivery in 'YYYY-MM-DD' format.
            status (str): Current status of the delivery (e.g., 'pending', 'delivered').
        """
        self.delivery_id = delivery_id
        self.item = item
        self.delivery_date = datetime.datetime.strptime(delivery_date, '%Y-%m-%d').date()
        self.status = status

    def __repr__(self):
        return f"Delivery({self.delivery_id}, {self.item}, {self.delivery_date}, {self.status})"

class DeliveryTracker:
    """Class to track deliveries and analyze performance metrics."""
    
    def __init__(self):
        """Initializes the delivery tracker with an empty delivery list."""
        self.deliveries: List[Delivery] = []

    def add_delivery(self, delivery: Delivery) -> None:
        """
        Adds a new delivery to the tracker.

        Args:
            delivery (Delivery): The delivery instance to add.
        """
        self.deliveries.append(delivery)

    def get_deliveries(self) -> List[Delivery]:
        """Returns the list of all deliveries."""
        return self.deliveries

    def analyze_performance(self) -> Dict[str, Optional[float]]:
        """
        Analyzes performance metrics based on the deliveries tracked.

        Returns:
            Dict[str, Optional[float]]: A dictionary containing metrics like total deliveries
            and percentage of delivered items.
        """
        total_deliveries = len(self.deliveries)
        delivered_count = sum(1 for delivery in self.deliveries if delivery.status == 'delivered')

        performance_metrics = {
            "total_deliveries": total_deliveries,
            "delivered_count": delivered_count,
            "delivery_success_rate": (delivered_count / total_deliveries * 100) if total_deliveries > 0 else None
        }
        
        return performance_metrics

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the current deliveries to a JSON file.

        Args:
            file_path (str): The file path to save the deliveries.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([delivery.__dict__ for delivery in self.deliveries], file, default=str)
        except IOError as e:
            print(f"Error saving to file {file_path}: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Loads deliveries from a JSON file.

        Args:
            file_path (str): The file path from which to load deliveries.
        """
        try:
            with open(file_path, 'r') as file:
                deliveries_data = json.load(file)
                for data in deliveries_data:
                    delivery = Delivery(data['delivery_id'], data['item'], data['delivery_date'], data['status'])
                    self.add_delivery(delivery)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {file_path}: {e}")

# Example of usage:

if __name__ == "__main__":
    tracker = DeliveryTracker()
    
    # Adding some deliveries
    tracker.add_delivery(Delivery(1, "Brake Pads", "2023-10-01", "delivered"))
    tracker.add_delivery(Delivery(2, "Oil Filter", "2023-10-02", "pending"))
    
    # Analyzing performance
    metrics = tracker.analyze_performance()
    print("Performance Metrics:", metrics)
    
    # Saving to a file
    tracker.save_to_file("deliveries.json")
    
    # Loading from a file
    new_tracker = DeliveryTracker()
    new_tracker.load_from_file("deliveries.json")
    print("Loaded Deliveries:", new_tracker.get_deliveries())
```
