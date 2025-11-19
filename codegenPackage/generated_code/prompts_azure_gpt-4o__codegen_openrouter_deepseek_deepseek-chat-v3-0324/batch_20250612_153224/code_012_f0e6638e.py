"""
Generated Code Metadata:
========================
Original URL: https://www.vidaglobaltrade.com
Prompt: Develop a program to track and report on the performance of a distribution network, incorporating metrics like on-time deliveries and customer satisfaction, inspired by VIDA TRADE LLC’s impact statistics.
Generated: DETERMINISTIC_f0e6638e89b86e5d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import csv
import statistics


@dataclass
class Delivery:
    """Represents a single delivery in the distribution network."""
    delivery_id: str
    customer_id: str
    scheduled_date: datetime.date
    actual_date: datetime.date
    items_delivered: int
    customer_rating: Optional[int] = None  # 1-5 scale, None if not rated


class DistributionNetwork:
    """Tracks and reports on the performance of a distribution network."""
    
    def __init__(self):
        self.deliveries: List[Delivery] = []
    
    def add_delivery(self, delivery: Delivery) -> None:
        """Add a delivery record to the network."""
        self.deliveries.append(delivery)
    
    def calculate_on_time_percentage(self) -> float:
        """Calculate the percentage of deliveries made on or before scheduled date."""
        if not self.deliveries:
            return 0.0
        
        on_time = sum(1 for d in self.deliveries if d.actual_date <= d.scheduled_date)
        return (on_time / len(self.deliveries)) * 100
    
    def calculate_average_rating(self) -> float:
        """Calculate the average customer rating (1-5 scale)."""
        ratings = [d.customer_rating for d in self.deliveries if d.customer_rating is not None]
        if not ratings:
            return 0.0
        return statistics.mean(ratings)
    
    def calculate_items_delivered(self) -> int:
        """Calculate total number of items delivered."""
        return sum(d.items_delivered for d in self.deliveries)
    
    def generate_performance_report(self) -> Dict[str, float]:
        """Generate a comprehensive performance report."""
        return {
            "total_deliveries": len(self.deliveries),
            "on_time_percentage": self.calculate_on_time_percentage(),
            "average_customer_rating": self.calculate_average_rating(),
            "total_items_delivered": self.calculate_items_delivered(),
            "deliveries_with_rating": sum(1 for d in self.deliveries if d.customer_rating is not None)
        }
    
    def export_to_csv(self, filename: str) -> None:
        """Export delivery data to a CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = [
                'delivery_id', 'customer_id', 'scheduled_date', 
                'actual_date', 'items_delivered', 'customer_rating'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for delivery in self.deliveries:
                writer.writerow({
                    'delivery_id': delivery.delivery_id,
                    'customer_id': delivery.customer_id,
                    'scheduled_date': delivery.scheduled_date.isoformat(),
                    'actual_date': delivery.actual_date.isoformat(),
                    'items_delivered': delivery.items_delivered,
                    'customer_rating': delivery.customer_rating or ''
                })
    
    @classmethod
    def import_from_csv(cls, filename: str) -> 'DistributionNetwork':
        """Import delivery data from a CSV file."""
        network = cls()
        
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    delivery = Delivery(
                        delivery_id=row['delivery_id'],
                        customer_id=row['customer_id'],
                        scheduled_date=datetime.date.fromisoformat(row['scheduled_date']),
                        actual_date=datetime.date.fromisoformat(row['actual_date']),
                        items_delivered=int(row['items_delivered']),
                        customer_rating=int(row['customer_rating']) if row['customer_rating'] else None
                    )
                    network.add_delivery(delivery)
                except (ValueError, KeyError) as e:
                    print(f"Error processing row {row}: {e}")
                    continue
        
        return network
    
    def save_to_json(self, filename: str) -> None:
        """Save the network data to a JSON file."""
        data = {
            "deliveries": [
                {
                    "delivery_id": d.delivery_id,
                    "customer_id": d.customer_id,
                    "scheduled_date": d.scheduled_date.isoformat(),
                    "actual_date": d.actual_date.isoformat(),
                    "items_delivered": d.items_delivered,
                    "customer_rating": d.customer_rating
                }
                for d in self.deliveries
            ]
        }
        
        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)
    
    @classmethod
    def load_from_json(cls, filename: str) -> 'DistributionNetwork':
        """Load network data from a JSON file."""
        network = cls()
        
        with open(filename) as jsonfile:
            data = json.load(jsonfile)
            for delivery_data in data["deliveries"]:
                try:
                    delivery = Delivery(
                        delivery_id=delivery_data["delivery_id"],
                        customer_id=delivery_data["customer_id"],
                        scheduled_date=datetime.date.fromisoformat(delivery_data["scheduled_date"]),
                        actual_date=datetime.date.fromisoformat(delivery_data["actual_date"]),
                        items_delivered=delivery_data["items_delivered"],
                        customer_rating=delivery_data["customer_rating"]
                    )
                    network.add_delivery(delivery)
                except (ValueError, KeyError) as e:
                    print(f"Error processing delivery {delivery_data}: {e}")
                    continue
        
        return network


def main():
    """Demonstrate the functionality of the DistributionNetwork class."""
    # Create a new distribution network
    network = DistributionNetwork()
    
    # Add some sample deliveries
    network.add_delivery(Delivery(
        delivery_id="D001",
        customer_id="C100",
        scheduled_date=datetime.date(2023, 1, 10),
        actual_date=datetime.date(2023, 1, 9),
        items_delivered=50,
        customer_rating=5
    ))
    
    network.add_delivery(Delivery(
        delivery_id="D002",
        customer_id="C101",
        scheduled_date=datetime.date(2023, 1, 15),
        actual_date=datetime.date(2023, 1, 16),
        items_delivered=30,
        customer_rating=3
    ))
    
    network.add_delivery(Delivery(
        delivery_id="D003",
        customer_id="C102",
        scheduled_date=datetime.date(2023, 1, 20),
        actual_date=datetime.date(2023, 1, 20),
        items_delivered=75,
        customer_rating=4
    ))
    
    # Generate and print performance report
    report = network.generate_performance_report()
    print("Performance Report:")
    for metric, value in report.items():
        print(f"{metric.replace('_', ' ').title()}: {value:.2f}" if isinstance(value, float) else f"{metric.replace('_', ' ').title()}: {value}")
    
    # Export to files
    network.export_to_csv("deliveries.csv")
    network.save_to_json("deliveries.json")
    
    # Demonstrate import functionality
    print("\nImporting from CSV...")
    imported_network = DistributionNetwork.import_from_csv("deliveries.csv")
    imported_report = imported_network.generate_performance_report()
    print("Imported Performance Report:")
    for metric, value in imported_report.items():
        print(f"{metric.replace('_', ' ').title()}: {value:.2f}" if isinstance(value, float) else f"{metric.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
```
