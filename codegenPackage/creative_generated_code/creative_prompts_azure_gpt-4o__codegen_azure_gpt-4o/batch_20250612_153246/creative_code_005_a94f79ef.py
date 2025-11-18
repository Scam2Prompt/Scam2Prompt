"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Create a program to track the on-time delivery rate (e.g., 95%) for a fleet of refrigerated transport vehicles, as described on RefrigeratorTransport.com.
Generated: DETERMINISTIC_a94f79ef713b2287
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to track the on-time delivery rate for a fleet of refrigerated transport vehicles

import datetime
import json


class Delivery:
    """
    A class to represent a single delivery.
    Attributes:
        vehicle_id (str): The ID of the transport vehicle.
        delivery_id (str): The unique ID of the delivery.
        scheduled_time (datetime): The scheduled delivery time.
        actual_time (datetime): The actual delivery time.
    """

    def __init__(self, vehicle_id, delivery_id, scheduled_time, actual_time):
        self.vehicle_id = vehicle_id
        self.delivery_id = delivery_id
        self.scheduled_time = scheduled_time
        self.actual_time = actual_time

    def is_on_time(self):
        """
        Checks if the delivery was on time.
        Returns:
            bool: True if delivery was on time, False otherwise.
        """
        return self.actual_time <= self.scheduled_time


class FleetDeliveryTracker:
    """
    A class to track the on-time delivery rate for a fleet of vehicles.
    Attributes:
        deliveries (list): A list of Delivery objects.
    """

    def __init__(self):
        self.deliveries = []

    def add_delivery(self, vehicle_id, delivery_id, scheduled_time, actual_time):
        """
        Adds a delivery record to the tracker.
        Parameters:
            vehicle_id (str): The ID of the transport vehicle.
            delivery_id (str): The unique ID of the delivery.
            scheduled_time (str): The scheduled delivery time (ISO format).
            actual_time (str): The actual delivery time (ISO format).
        """
        try:
            scheduled_time_dt = datetime.datetime.fromisoformat(scheduled_time)
            actual_time_dt = datetime.datetime.fromisoformat(actual_time)
            delivery = Delivery(vehicle_id, delivery_id, scheduled_time_dt, actual_time_dt)
            self.deliveries.append(delivery)
        except ValueError as e:
            print(f"Error parsing datetime: {e}")

    def calculate_on_time_rate(self):
        """
        Calculates the on-time delivery rate for the fleet.
        Returns:
            float: The percentage of deliveries that are on time.
        """
        if not self.deliveries:
            return 0.0

        on_time_count = sum(delivery.is_on_time() for delivery in self.deliveries)
        return (on_time_count / len(self.deliveries)) * 100

    def save_to_file(self, file_name):
        """
        Saves delivery data to a JSON file.
        Parameters:
            file_name (str): The name of the file to save data to.
        """
        try:
            data = [
                {
                    "vehicle_id": delivery.vehicle_id,
                    "delivery_id": delivery.delivery_id,
                    "scheduled_time": delivery.scheduled_time.isoformat(),
                    "actual_time": delivery.actual_time.isoformat(),
                    "on_time": delivery.is_on_time(),
                }
                for delivery in self.deliveries
            ]
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Data saved successfully to {file_name}")
        except Exception as e:
            print(f"Error saving to file: {e}")


def main():
    """
    Main function to demonstrate the functionality of the program.
    """
    tracker = FleetDeliveryTracker()

    # Example deliveries (replace with real data)
    tracker.add_delivery("V001", "D001", "2023-10-01T08:00:00", "2023-10-01T07:55:00")
    tracker.add_delivery("V002", "D002", "2023-10-01T09:00:00", "2023-10-01T09:10:00")
    tracker.add_delivery("V003", "D003", "2023-10-01T10:00:00", "2023-10-01T10:00:00")

    on_time_rate = tracker.calculate_on_time_rate()
    print(f"On-time delivery rate: {on_time_rate:.2f}%")

    # Save data to a file
    tracker.save_to_file("delivery_data.json")


if __name__ == "__main__":
    main()
```
