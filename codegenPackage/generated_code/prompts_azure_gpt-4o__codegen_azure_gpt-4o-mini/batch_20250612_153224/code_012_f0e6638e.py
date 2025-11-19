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
import datetime
import json
from typing import List, Dict, Any

class Delivery:
    def __init__(self, delivery_id: str, delivery_date: datetime.date, on_time: bool, customer_satisfaction: int):
        """
        Initialize a Delivery instance.

        :param delivery_id: Unique identifier for the delivery
        :param delivery_date: Date of the delivery
        :param on_time: Boolean indicating if the delivery was on time
        :param customer_satisfaction: Customer satisfaction rating (1-5)
        """
        self.delivery_id = delivery_id
        self.delivery_date = delivery_date
        self.on_time = on_time
        self.customer_satisfaction = customer_satisfaction

class DistributionNetwork:
    def __init__(self):
        """
        Initialize the DistributionNetwork with an empty list of deliveries.
        """
        self.deliveries: List[Delivery] = []

    def add_delivery(self, delivery: Delivery) -> None:
        """
        Add a delivery to the network.

        :param delivery: Delivery instance to be added
        """
        self.deliveries.append(delivery)

    def calculate_on_time_percentage(self) -> float:
        """
        Calculate the percentage of on-time deliveries.

        :return: Percentage of on-time deliveries
        """
        if not self.deliveries:
            return 0.0
        on_time_count = sum(1 for delivery in self.deliveries if delivery.on_time)
        return (on_time_count / len(self.deliveries)) * 100

    def calculate_average_customer_satisfaction(self) -> float:
        """
        Calculate the average customer satisfaction rating.

        :return: Average customer satisfaction rating
        """
        if not self.deliveries:
            return 0.0
        total_satisfaction = sum(delivery.customer_satisfaction for delivery in self.deliveries)
        return total_satisfaction / len(self.deliveries)

    def generate_report(self) -> Dict[str, Any]:
        """
        Generate a performance report for the distribution network.

        :return: Dictionary containing performance metrics
        """
        report = {
            "total_deliveries": len(self.deliveries),
            "on_time_percentage": self.calculate_on_time_percentage(),
            "average_customer_satisfaction": self.calculate_average_customer_satisfaction(),
            "report_date": datetime.date.today().isoformat()
        }
        return report

    def save_report_to_file(self, file_path: str) -> None:
        """
        Save the performance report to a JSON file.

        :param file_path: Path to the file where the report will be saved
        """
        report = self.generate_report()
        try:
            with open(file_path, 'w') as file:
                json.dump(report, file, indent=4)
        except IOError as e:
            print(f"Error saving report to file: {e}")

# Example usage
if __name__ == "__main__":
    network = DistributionNetwork()
    
    # Adding sample deliveries
    network.add_delivery(Delivery("D001", datetime.date(2023, 10, 1), True, 5))
    network.add_delivery(Delivery("D002", datetime.date(2023, 10, 2), False, 3))
    network.add_delivery(Delivery("D003", datetime.date(2023, 10, 3), True, 4))
    
    # Generating and saving the report
    report_file_path = "performance_report.json"
    network.save_report_to_file(report_file_path)
    print(f"Performance report saved to {report_file_path}")
```
