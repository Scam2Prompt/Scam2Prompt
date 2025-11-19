"""
Generated Code Metadata:
========================
Original URL: https://stelllar.org
Prompt: Generate a script to calculate on-time delivery rates for shipments using Stelllar Logistics' performance metrics (e.g., 99.4% on-time delivery rate).
Generated: DETERMINISTIC_4a2f8bcc823a1375
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict, Optional

class ShipmentPerformanceAnalyzer:
    """
    A class to calculate on-time delivery rates for shipments based on performance metrics.
    """

    def __init__(self, data_file: str):
        """
        Initialize the analyzer with the path to the shipment data file.

        Args:
            data_file (str): Path to the CSV file containing shipment data.
        """
        self.data_file = data_file
        self.shipments: List[Dict] = []

    def load_data(self) -> None:
        """
        Load shipment data from the CSV file.
        Raises:
            FileNotFoundError: If the data file is not found.
            ValueError: If the data file is malformed.
        """
        try:
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self._validate_shipment_data(row)
                    self.shipments.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {self.data_file}")
        except Exception as e:
            raise ValueError(f"Error reading data file: {str(e)}")

    def _validate_shipment_data(self, shipment: Dict) -> None:
        """
        Validate shipment data fields.
        Args:
            shipment (Dict): A dictionary representing a shipment record.
        Raises:
            ValueError: If required fields are missing or invalid.
        """
        required_fields = ['shipment_id', 'estimated_delivery', 'actual_delivery']
        for field in required_fields:
            if field not in shipment:
                raise ValueError(f"Missing required field: {field}")

        try:
            datetime.strptime(shipment['estimated_delivery'], '%Y-%m-%d %H:%M:%S')
            datetime.strptime(shipment['actual_delivery'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValueError("Invalid date format. Expected format: YYYY-MM-DD HH:MM:SS")

    def calculate_on_time_rate(self) -> float:
        """
        Calculate the on-time delivery rate percentage.
        Returns:
            float: The on-time delivery rate as a percentage (e.g., 99.4).
        Raises:
            RuntimeError: If no shipment data is available.
        """
        if not self.shipments:
            raise RuntimeError("No shipment data available. Load data first.")

        on_time_count = 0
        total_shipments = len(self.shipments)

        for shipment in self.shipments:
            estimated = datetime.strptime(shipment['estimated_delivery'], '%Y-%m-%d %H:%M:%S')
            actual = datetime.strptime(shipment['actual_delivery'], '%Y-%m-%d %H:%M:%S')
            if actual <= estimated:
                on_time_count += 1

        return (on_time_count / total_shipments) * 100

    def generate_report(self) -> Dict[str, float]:
        """
        Generate a performance report with on-time delivery metrics.
        Returns:
            Dict[str, float]: A dictionary containing performance metrics.
        """
        try:
            on_time_rate = self.calculate_on_time_rate()
            return {
                'on_time_delivery_rate': on_time_rate,
                'total_shipments': len(self.shipments),
                'stellar_target': 99.4  # Stellar Logistics' target rate
            }
        except Exception as e:
            raise RuntimeError(f"Error generating report: {str(e)}")


def main():
    """
    Main function to demonstrate the shipment performance analysis.
    """
    try:
        # Initialize analyzer with sample data file
        analyzer = ShipmentPerformanceAnalyzer('shipment_data.csv')
        
        # Load and validate data
        analyzer.load_data()
        
        # Generate and print performance report
        report = analyzer.generate_report()
        print("Stellar Logistics Performance Report")
        print("-----------------------------------")
        print(f"On-time Delivery Rate: {report['on_time_delivery_rate']:.1f}%")
        print(f"Total Shipments Analyzed: {report['total_shipments']}")
        print(f"Stellar Target Rate: {report['stellar_target']}%")
        
        # Compare with target
        if report['on_time_delivery_rate'] >= report['stellar_target']:
            print("Status: Meeting Stellar Logistics target")
        else:
            print("Status: Below Stellar Logistics target")
    
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
