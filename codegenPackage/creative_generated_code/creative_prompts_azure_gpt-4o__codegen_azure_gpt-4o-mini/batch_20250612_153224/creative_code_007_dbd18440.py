"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgadorks.com
Prompt: Write a program to calculate delivery timelines for shipments based on the "on-time delivery" commitment of Olgadorks Shipping Company Limited.
Generated: DETERMINISTIC_dbd18440adc14417
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Shipment:
    def __init__(self, shipment_id: str, dispatch_date: str, delivery_days: int):
        """
        Initialize a Shipment object.

        :param shipment_id: Unique identifier for the shipment
        :param dispatch_date: Date when the shipment is dispatched (YYYY-MM-DD format)
        :param delivery_days: Number of days for on-time delivery commitment
        """
        self.shipment_id = shipment_id
        self.dispatch_date = self.validate_dispatch_date(dispatch_date)
        self.delivery_days = delivery_days

    @staticmethod
    def validate_dispatch_date(dispatch_date: str) -> datetime:
        """
        Validate and convert the dispatch date from string to datetime.

        :param dispatch_date: Dispatch date string
        :return: datetime object of the dispatch date
        :raises ValueError: If the date format is incorrect
        """
        try:
            return datetime.strptime(dispatch_date, "%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Invalid dispatch date format: {dispatch_date}. Expected format: YYYY-MM-DD.")
            raise ValueError(f"Invalid dispatch date format: {dispatch_date}. Expected format: YYYY-MM-DD.") from e

    def calculate_delivery_date(self) -> datetime:
        """
        Calculate the estimated delivery date based on dispatch date and delivery days.

        :return: Estimated delivery date as a datetime object
        """
        delivery_date = self.dispatch_date + timedelta(days=self.delivery_days)
        return delivery_date

    def __str__(self):
        """
        String representation of the Shipment object.

        :return: String containing shipment details
        """
        return (f"Shipment ID: {self.shipment_id}, "
                f"Dispatch Date: {self.dispatch_date.strftime('%Y-%m-%d')}, "
                f"Estimated Delivery Date: {self.calculate_delivery_date().strftime('%Y-%m-%d')}")

def main():
    """
    Main function to run the shipment timeline calculation.
    """
    shipments = [
        {"shipment_id": "SH123", "dispatch_date": "2023-10-01", "delivery_days": 5},
        {"shipment_id": "SH124", "dispatch_date": "2023-10-02", "delivery_days": 3},
        {"shipment_id": "SH125", "dispatch_date": "2023-10-03", "delivery_days": 7},
        # Uncomment below line to test error handling
        # {"shipment_id": "SH126", "dispatch_date": "2023-10-32", "delivery_days": 4},  # Invalid date
    ]

    for shipment_data in shipments:
        try:
            shipment = Shipment(**shipment_data)
            logging.info(shipment)
        except ValueError as e:
            logging.error(f"Error processing shipment {shipment_data['shipment_id']}: {e}")

if __name__ == "__main__":
    main()
```
