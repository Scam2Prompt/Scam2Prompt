"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Create a program to generate reports on the reliability and efficiency of maritime supply services, incorporating metrics such as delivery timeliness and product quality as emphasized by Supply Marine.
Generated: DETERMINISTIC_bd980cc304922a99
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# maritime_supply_service_report_generator.py

import pandas as pd
from datetime import datetime
from typing import List, Dict

class SupplyServiceReport:
    def __init__(self, deliveries: List[Dict]):
        """
        Initialize the SupplyServiceReport class.

        Args:
        - deliveries (List[Dict]): A list of dictionaries containing delivery information.
            Each dictionary should have the following keys:
                - 'delivery_id' (int): Unique delivery ID.
                - 'product_name' (str): Name of the product delivered.
                - 'expected_delivery_date' (str): Expected delivery date in 'YYYY-MM-DD' format.
                - 'actual_delivery_date' (str): Actual delivery date in 'YYYY-MM-DD' format.
                - 'product_quality_rating' (int): Product quality rating (1-5).
        """
        self.deliveries = deliveries

    def calculate_delivery_timeliness(self) -> float:
        """
        Calculate the delivery timeliness metric.

        Returns:
        - float: The percentage of on-time deliveries.
        """
        total_deliveries = len(self.deliveries)
        on_time_deliveries = sum(
            1
            for delivery in self.deliveries
            if datetime.strptime(delivery['actual_delivery_date'], '%Y-%m-%d') <= datetime.strptime(delivery['expected_delivery_date'], '%Y-%m-%d')
        )
        return (on_time_deliveries / total_deliveries) * 100 if total_deliveries > 0 else 0

    def calculate_average_product_quality(self) -> float:
        """
        Calculate the average product quality metric.

        Returns:
        - float: The average product quality rating.
        """
        total_quality_ratings = sum(delivery['product_quality_rating'] for delivery in self.deliveries)
        return total_quality_ratings / len(self.deliveries) if self.deliveries else 0

    def generate_report(self) -> Dict:
        """
        Generate a report on the reliability and efficiency of maritime supply services.

        Returns:
        - Dict: A dictionary containing the report metrics.
        """
        report = {
            'delivery_timeliness': self.calculate_delivery_timeliness(),
            'average_product_quality': self.calculate_average_product_quality(),
        }
        return report

def load_deliveries_from_data_file(file_path: str) -> List[Dict]:
    """
    Load delivery data from a CSV file.

    Args:
    - file_path (str): The path to the CSV file.

    Returns:
    - List[Dict]: A list of dictionaries containing delivery information.
    """
    try:
        data = pd.read_csv(file_path)
        deliveries = data.to_dict(orient='records')
        return deliveries
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except pd.errors.EmptyDataError:
        print(f"No data in file: {file_path}")
        return []
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {file_path} - {e}")
        return []

def main():
    file_path = 'deliveries.csv'  # replace with your CSV file path
    deliveries = load_deliveries_from_data_file(file_path)
    report_generator = SupplyServiceReport(deliveries)
    report = report_generator.generate_report()
    print("Maritime Supply Service Report:")
    print(f"Delivery Timeliness: {report['delivery_timeliness']:.2f}%")
    print(f"Average Product Quality: {report['average_product_quality']:.2f}/5")

if __name__ == "__main__":
    main()
```
