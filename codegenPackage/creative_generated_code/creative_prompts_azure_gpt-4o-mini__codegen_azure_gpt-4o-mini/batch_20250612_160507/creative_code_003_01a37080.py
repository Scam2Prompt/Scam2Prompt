"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appbalancer.pages.dev
Prompt: Develop a script that lists delivery areas for a takeaway service, inspired by the delivery areas mentioned for Rob N Roll in Kirkcudbright and Auchenlarie.
Generated: DETERMINISTIC_01a370802b211ab3
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DeliveryArea:
    """
    A class to represent a delivery area for a takeaway service.
    """

    def __init__(self, name, postal_codes):
        """
        Initialize a DeliveryArea.

        :param name: The name of the delivery area.
        :param postal_codes: A list of postal codes for the delivery area.
        """
        self.name = name
        self.postal_codes = postal_codes

    def __str__(self):
        return f"{self.name}: {', '.join(self.postal_codes)}"


class DeliveryService:
    """
    A class to manage delivery areas for a takeaway service.
    """

    def __init__(self):
        """
        Initialize the delivery service with an empty list of delivery areas.
        """
        self.delivery_areas = []

    def add_delivery_area(self, delivery_area):
        """
        Add a new delivery area to the service.

        :param delivery_area: An instance of DeliveryArea to be added.
        """
        if not isinstance(delivery_area, DeliveryArea):
            logging.error("Attempted to add a non-DeliveryArea object.")
            raise ValueError("Only DeliveryArea instances can be added.")
        self.delivery_areas.append(delivery_area)
        logging.info(f"Added delivery area: {delivery_area.name}")

    def list_delivery_areas(self):
        """
        List all delivery areas in the service.
        """
        if not self.delivery_areas:
            logging.warning("No delivery areas available.")
            return "No delivery areas available."
        
        return '\n'.join(str(area) for area in self.delivery_areas)


def main():
    """
    Main function to demonstrate the delivery service.
    """
    # Create an instance of the delivery service
    service = DeliveryService()

    # Define delivery areas inspired by Rob N Roll
    try:
        service.add_delivery_area(DeliveryArea("Kirkcudbright", ["DG6 4LT", "DG6 4LY", "DG6 4LZ"]))
        service.add_delivery_area(DeliveryArea("Auchenlarie", ["DG6 4UG", "DG6 4UE"]))
        
        # List the delivery areas
        print("Delivery Areas:")
        print(service.list_delivery_areas())

    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
