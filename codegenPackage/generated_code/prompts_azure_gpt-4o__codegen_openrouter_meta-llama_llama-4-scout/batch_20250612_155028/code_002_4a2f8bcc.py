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
# on_time_delivery_calculator.py

from datetime import datetime
from typing import List, Dict

class Shipment:
    """Represents a shipment with its tracking information and delivery status."""

    def __init__(self, tracking_number: str, scheduled_delivery_date: str, actual_delivery_date: str = None):
        """
        Initializes a Shipment object.

        Args:
        - tracking_number (str): The unique tracking number for the shipment.
        - scheduled_delivery_date (str): The scheduled delivery date in 'YYYY-MM-DD' format.
        - actual_delivery_date (str, optional): The actual delivery date in 'YYYY-MM-DD' format. Defaults to None.
        """
        self.tracking_number = tracking_number
        self.scheduled_delivery_date = datetime.strptime(scheduled_delivery_date, '%Y-%m-%d')
        if actual_delivery_date:
            self.actual_delivery_date = datetime.strptime(actual_delivery_date, '%Y-%m-%d')
        else:
            self.actual_delivery_date = None

    def is_on_time(self) -> bool:
        """
        Checks if the shipment was delivered on time.

        Returns:
        - bool: True if the shipment was delivered on or before the scheduled delivery date, False otherwise.
        """
        if self.actual_delivery_date is None:
            return False
        return self.actual_delivery_date <= self.scheduled_delivery_date


class OnTimeDeliveryCalculator:
    """Calculates on-time delivery rates for shipments."""

    def __init__(self):
        self.shipments: List[Shipment] = []

    def add_shipment(self, shipment: Shipment):
        """
        Adds a shipment to the calculator.

        Args:
        - shipment (Shipment): The shipment to add.
        """
        self.shipments.append(shipment)

    def calculate_on_time_delivery_rate(self) -> float:
        """
        Calculates the on-time delivery rate.

        Returns:
        - float: The on-time delivery rate as a percentage.
        """
        total_shipments = len(self.shipments)
        if total_shipments == 0:
            return 0.0

        on_time_shipments = sum(1 for shipment in self.shipments if shipment.is_on_time())
        on_time_delivery_rate = (on_time_shipments / total_shipments) * 100
        return round(on_time_delivery_rate, 2)


def main():
    calculator = OnTimeDeliveryCalculator()

    # Example shipments
    shipments: List[Dict] = [
        {'tracking_number': 'ABC123', 'scheduled_delivery_date': '2022-01-01', 'actual_delivery_date': '2022-01-01'},
        {'tracking_number': 'DEF456', 'scheduled_delivery_date': '2022-01-05', 'actual_delivery_date': '2022-01-06'},
        {'tracking_number': 'GHI789', 'scheduled_delivery_date': '2022-01-10', 'actual_delivery_date': '2022-01-10'},
        {'tracking_number': 'JKL012', 'scheduled_delivery_date': '2022-01-15'},
    ]

    for shipment_data in shipments:
        try:
            shipment = Shipment(
                tracking_number=shipment_data['tracking_number'],
                scheduled_delivery_date=shipment_data['scheduled_delivery_date'],
                actual_delivery_date=shipment_data.get('actual_delivery_date')
            )
            calculator.add_shipment(shipment)
        except Exception as e:
            print(f"Error creating shipment: {e}")

    on_time_delivery_rate = calculator.calculate_on_time_delivery_rate()
    print(f"On-time delivery rate: {on_time_delivery_rate}%")

if __name__ == "__main__":
    main()
```
