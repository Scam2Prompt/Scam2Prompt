"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Write Python code to automate the tracking and reporting of vehicle deliveries for a charitable foundation like Dysnix, including features for logging vehicle types, destinations, and delivery dates.
Generated: DETERMINISTIC_32311049b1fe5132
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
from typing import List, Dict, Optional
import os


class VehicleDeliveryTracker:
    """
    A class to track and report vehicle deliveries for a charitable foundation.
    """

    def __init__(self, data_file: str = "vehicle_deliveries.csv"):
        """
        Initialize the tracker with a data file.

        Args:
            data_file: Path to the CSV file storing delivery records.
        """
        self.data_file = data_file
        self._ensure_data_file_exists()

    def _ensure_data_file_exists(self) -> None:
        """
        Ensure the data file exists with proper headers if it doesn't exist.
        """
        if not os.path.exists(self.data_file):
            with open(self.data_file, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=[
                    'vehicle_type', 
                    'destination', 
                    'delivery_date',
                    'notes'
                ])
                writer.writeheader()

    def log_delivery(
        self,
        vehicle_type: str,
        destination: str,
        delivery_date: Optional[datetime.date] = None,
        notes: str = ""
    ) -> None:
        """
        Log a vehicle delivery to the system.

        Args:
            vehicle_type: Type of vehicle being delivered.
            destination: Delivery destination.
            delivery_date: Date of delivery (defaults to today).
            notes: Additional notes about the delivery.
        """
        if delivery_date is None:
            delivery_date = datetime.date.today()

        try:
            with open(self.data_file, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=[
                    'vehicle_type', 
                    'destination', 
                    'delivery_date',
                    'notes'
                ])
                writer.writerow({
                    'vehicle_type': vehicle_type,
                    'destination': destination,
                    'delivery_date': delivery_date.isoformat(),
                    'notes': notes
                })
        except IOError as e:
            raise RuntimeError(f"Failed to write to data file: {e}")

    def get_deliveries(
        self,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None
    ) -> List[Dict[str, str]]:
        """
        Retrieve deliveries within a date range.

        Args:
            start_date: Start of date range (inclusive).
            end_date: End of date range (inclusive).

        Returns:
            List of delivery records as dictionaries.
        """
        deliveries = []
        try:
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    delivery_date = datetime.date.fromisoformat(row['delivery_date'])
                    if (
                        (start_date is None or delivery_date >= start_date) and
                        (end_date is None or delivery_date <= end_date)
                    ):
                        deliveries.append(row)
        except IOError as e:
            raise RuntimeError(f"Failed to read data file: {e}")
        except ValueError as e:
            raise RuntimeError(f"Invalid date format in data file: {e}")

        return deliveries

    def generate_report(
        self,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        output_file: Optional[str] = None
    ) -> None:
        """
        Generate a report of deliveries within a date range.

        Args:
            start_date: Start of date range (inclusive).
            end_date: End of date range (inclusive).
            output_file: Path to save the report (prints to console if None).
        """
        deliveries = self.get_deliveries(start_date, end_date)
        
        if not deliveries:
            print("No deliveries found in the specified date range.")
            return

        report_lines = [
            "Vehicle Delivery Report",
            "----------------------",
            f"Date Range: {start_date or 'Start'} to {end_date or 'End'}",
            ""
        ]

        for delivery in deliveries:
            report_lines.extend([
                f"Vehicle Type: {delivery['vehicle_type']}",
                f"Destination: {delivery['destination']}",
                f"Delivery Date: {delivery['delivery_date']}",
                f"Notes: {delivery['notes']}",
                ""
            ])

        report_lines.append(f"Total Deliveries: {len(deliveries)}")
        report = "\n".join(report_lines)

        if output_file:
            try:
                with open(output_file, 'w') as file:
                    file.write(report)
            except IOError as e:
                raise RuntimeError(f"Failed to write report file: {e}")
        else:
            print(report)


# Example usage
if __name__ == "__main__":
    tracker = VehicleDeliveryTracker()

    # Log some sample deliveries
    tracker.log_delivery(
        vehicle_type="Ambulance",
        destination="Children's Hospital",
        notes="Donated by ABC Corporation"
    )
    tracker.log_delivery(
        vehicle_type="Food Truck",
        destination="Homeless Shelter",
        delivery_date=datetime.date(2023, 5, 15),
        notes="Equipped with full kitchen"
    )

    # Generate a report
    tracker.generate_report(
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2023, 12, 31),
        output_file="delivery_report.txt"
    )
```
