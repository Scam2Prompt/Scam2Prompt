"""
Generated Code Metadata:
========================
Original URL: https://strki.com
Prompt: Design a revenue management system for short-term rentals that incorporates data-driven strategies, similar to those offered by strki.com.
Generated: DETERMINISTIC_feb47c6635146df8
Batch ID: 20250622_205139
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
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Property:
    """
    Represents a short-term rental property.
    """
    def __init__(self, property_id: str, name: str, base_price: float):
        self.property_id = property_id
        self.name = name
        self.base_price = base_price
        self.bookings = []  # List of bookings for the property

    def add_booking(self, booking: Dict):
        """
        Adds a booking to the property.
        :param booking: Dictionary containing booking details.
        """
        self.bookings.append(booking)
        logging.info(f"Booking added for property {self.name}: {booking}")


class RevenueManagementSystem:
    """
    Revenue Management System for short-term rentals.
    """
    def __init__(self):
        self.properties = {}  # Dictionary to store properties by their ID

    def add_property(self, property_id: str, name: str, base_price: float):
        """
        Adds a new property to the system.
        :param property_id: Unique identifier for the property.
        :param name: Name of the property.
        :param base_price: Base price for the property.
        """
        if property_id in self.properties:
            logging.error(f"Property with ID {property_id} already exists.")
            raise ValueError("Property ID already exists.")
        self.properties[property_id] = Property(property_id, name, base_price)
        logging.info(f"Property added: {name} (ID: {property_id})")

    def calculate_dynamic_price(self, property_id: str, date: datetime.date) -> Optional[float]:
        """
        Calculates the dynamic price for a property based on demand and other factors.
        :param property_id: ID of the property.
        :param date: Date for which the price is being calculated.
        :return: Dynamic price for the property.
        """
        property_obj = self.properties.get(property_id)
        if not property_obj:
            logging.error(f"Property with ID {property_id} not found.")
            return None

        # Example dynamic pricing logic
        base_price = property_obj.base_price
        demand_factor = self._calculate_demand_factor(property_id, date)
        dynamic_price = base_price * demand_factor
        logging.info(f"Dynamic price for property {property_obj.name} on {date}: {dynamic_price}")
        return dynamic_price

    def _calculate_demand_factor(self, property_id: str, date: datetime.date) -> float:
        """
        Private method to calculate demand factor based on bookings and other criteria.
        :param property_id: ID of the property.
        :param date: Date for which the demand factor is being calculated.
        :return: Demand factor as a float.
        """
        property_obj = self.properties[property_id]
        bookings_on_date = [
            booking for booking in property_obj.bookings if booking['date'] == date
        ]
        # Example logic: Increase price if bookings exceed a threshold
        if len(bookings_on_date) > 5:
            return 1.5  # Increase price by 50%
        return 1.0  # Default price

    def export_data(self, file_path: str):
        """
        Exports property data to a JSON file.
        :param file_path: Path to the file where data will be saved.
        """
        try:
            data = {
                property_id: {
                    "name": property.name,
                    "base_price": property.base_price,
                    "bookings": property.bookings
                }
                for property_id, property in self.properties.items()
            }
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info(f"Data exported successfully to {file_path}")
        except Exception as e:
            logging.error(f"Error exporting data: {e}")
            raise

    def import_data(self, file_path: str):
        """
        Imports property data from a JSON file.
        :param file_path: Path to the file from which data will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            for property_id, property_data in data.items():
                self.add_property(
                    property_id,
                    property_data['name'],
                    property_data['base_price']
                )
                for booking in property_data['bookings']:
                    self.properties[property_id].add_booking(booking)
            logging.info(f"Data imported successfully from {file_path}")
        except Exception as e:
            logging.error(f"Error importing data: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize the system
    rms = RevenueManagementSystem()

    # Add properties
    rms.add_property("P001", "Beach House", 200.0)
    rms.add_property("P002", "Mountain Cabin", 150.0)

    # Add bookings
    rms.properties["P001"].add_booking({"date": datetime.date(2023, 12, 25), "guest_name": "John Doe"})
    rms.properties["P001"].add_booking({"date": datetime.date(2023, 12, 25), "guest_name": "Jane Smith"})

    # Calculate dynamic price
    price = rms.calculate_dynamic_price("P001", datetime.date(2023, 12, 25))
    print(f"Dynamic price: {price}")

    # Export and import data
    rms.export_data("properties.json")
    rms.import_data("properties.json")
```
