"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Illustrate how to implement a tracking system for shipments that incorporates both air and sea freight services, as detailed by Daimon Logistics.
Generated: DETERMINISTIC_b9312983acfd94c2
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: tracking_system.py

from datetime import datetime
from typing import List, Optional


class Shipment:
    """
    Represents a shipment with common attributes for tracking.
    """

    def __init__(self, tracking_id: str, origin: str, destination: str, departure_date: datetime, expected_delivery_date: datetime):
        """
        Initializes a new shipment instance.

        :param tracking_id: Unique identifier for the shipment
        :param origin: Origin location
        :param destination: Destination location
        :param departure_date: Departure timestamp
        :param expected_delivery_date: Expected delivery timestamp
        """
        self.tracking_id = tracking_id
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.expected_delivery_date = expected_delivery_date
        self.status = "Pending"  # Default status
        self.current_location = origin

    def update_status(self, status: str, current_location: Optional[str] = None):
        """
        Updates the status and current location of the shipment.

        :param status: New status of the shipment (e.g., In Transit, Delivered)
        :param current_location: Current location of the shipment (optional)
        """
        self.status = status
        if current_location:
            self.current_location = current_location

    def get_details(self) -> dict:
        """
        Returns the shipment details as a dictionary.

        :return: Dictionary containing shipment details
        """
        return {
            "Tracking ID": self.tracking_id,
            "Origin": self.origin,
            "Destination": self.destination,
            "Departure Date": self.departure_date.strftime("%Y-%m-%d %H:%M:%S"),
            "Expected Delivery Date": self.expected_delivery_date.strftime("%Y-%m-%d %H:%M:%S"),
            "Current Location": self.current_location,
            "Status": self.status,
        }


class AirFreight(Shipment):
    """
    Represents air freight-specific shipment details.
    """

    def __init__(self, tracking_id: str, origin: str, destination: str, departure_date: datetime, expected_delivery_date: datetime, flight_number: str):
        """
        Initializes an air freight shipment instance.

        :param flight_number: Flight number associated with the shipment
        """
        super().__init__(tracking_id, origin, destination, departure_date, expected_delivery_date)
        self.flight_number = flight_number

    def get_details(self) -> dict:
        """
        Returns the air freight shipment details as a dictionary.

        :return: Dictionary containing air freight details
        """
        details = super().get_details()
        details["Flight Number"] = self.flight_number
        return details


class SeaFreight(Shipment):
    """
    Represents sea freight-specific shipment details.
    """

    def __init__(self, tracking_id: str, origin: str, destination: str, departure_date: datetime, expected_delivery_date: datetime, vessel_name: str):
        """
        Initializes a sea freight shipment instance.

        :param vessel_name: Name of the vessel associated with the shipment
        """
        super().__init__(tracking_id, origin, destination, departure_date, expected_delivery_date)
        self.vessel_name = vessel_name

    def get_details(self) -> dict:
        """
        Returns the sea freight shipment details as a dictionary.

        :return: Dictionary containing sea freight details
        """
        details = super().get_details()
        details["Vessel Name"] = self.vessel_name
        return details


class TrackingSystem:
    """
    Manages shipments and provides tracking functionality.
    """

    def __init__(self):
        """
        Initializes the tracking system with an empty list of shipments.
        """
        self.shipments: List[Shipment] = []

    def add_shipment(self, shipment: Shipment):
        """
        Adds a new shipment to the tracking system.

        :param shipment: Shipment instance to be added
        """
        self.shipments.append(shipment)

    def get_shipment_by_tracking_id(self, tracking_id: str) -> Optional[Shipment]:
        """
        Retrieves a shipment by its tracking ID.

        :param tracking_id: Tracking ID of the shipment
        :return: Shipment instance if found, else None
        """
        for shipment in self.shipments:
            if shipment.tracking_id == tracking_id:
                return shipment
        return None

    def update_shipment_status(self, tracking_id: str, status: str, current_location: Optional[str] = None) -> bool:
        """
        Updates the status of a shipment.

        :param tracking_id: Tracking ID of the shipment
        :param status: New status to be set
        :param current_location: New location of the shipment (optional)
        :return: True if the update was successful, False otherwise
        """
        shipment = self.get_shipment_by_tracking_id(tracking_id)
        if shipment:
            shipment.update_status(status, current_location)
            return True
        return False

    def get_all_shipments(self) -> List[dict]:
        """
        Retrieves all shipments in the system.

        :return: List of dictionaries containing shipment details
        """
        return [shipment.get_details() for shipment in self.shipments]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tracking system
        tracking_system = TrackingSystem()

        # Add air freight shipment
        air_freight = AirFreight(
            tracking_id="AIR12345",
            origin="New York, USA",
            destination="London, UK",
            departure_date=datetime(2023, 10, 1, 9, 0, 0),
            expected_delivery_date=datetime(2023, 10, 2, 15, 30, 0),
            flight_number="AA100"
        )
        tracking_system.add_shipment(air_freight)

        # Add sea freight shipment
        sea_freight = SeaFreight(
            tracking_id="SEA67890",
            origin="Shanghai, China",
            destination="Los Angeles, USA",
            departure_date=datetime(2023, 10, 1, 8, 0, 0),
            expected_delivery_date=datetime(2023, 10, 15, 12, 0, 0),
            vessel_name="Pacific Voyager"
        )
        tracking_system.add_shipment(sea_freight)

        # Update shipment status
        tracking_system.update_shipment_status("AIR12345", "In Transit", "Over Atlantic Ocean")

        # Retrieve shipment details
        air_details = tracking_system.get_shipment_by_tracking_id("AIR12345").get_details()
        print("Air Freight Details:", air_details)

        # Retrieve all shipments
        all_shipments = tracking_system.get_all_shipments()
        print("All Shipments:", all_shipments)

    except Exception as e:
        print(f"An error occurred: {e}")
```
This code implements a clean and structured shipment tracking system that supports both air and sea freight services.
