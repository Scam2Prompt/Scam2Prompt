"""
Generated Code Metadata:
========================
Original URL: https://appbalancer.pages.dev
Prompt: Develop a script that lists delivery areas for a takeaway service, inspired by the delivery areas mentioned for Rob N Roll in Kirkcudbright and Auchenlarie.
Generated: DETERMINISTIC_01a370802b211ab3
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# delivery_areas.py

class DeliveryArea:
    """Represents a delivery area for a takeaway service."""

    def __init__(self, name, postcode_prefixes, min_order_value):
        """
        Initializes a DeliveryArea object.

        Args:
            name (str): The name of the delivery area.
            postcode_prefixes (list[str]): A list of postcode prefixes for the area.
            min_order_value (float): The minimum order value for delivery.
        """
        self.name = name
        self.postcode_prefixes = postcode_prefixes
        self.min_order_value = min_order_value

    def __str__(self):
        return f"{self.name}: {', '.join(self.postcode_prefixes)}"


class TakeawayService:
    """Represents a takeaway service with delivery areas."""

    def __init__(self):
        self.delivery_areas = []

    def add_delivery_area(self, area):
        """
        Adds a delivery area to the takeaway service.

        Args:
            area (DeliveryArea): The delivery area to add.
        """
        self.delivery_areas.append(area)

    def list_delivery_areas(self):
        """
        Lists all delivery areas for the takeaway service.

        Returns:
            list[DeliveryArea]: A list of delivery areas.
        """
        return self.delivery_areas


def main():
    try:
        # Create a takeaway service
        service = TakeawayService()

        # Define delivery areas
        kirkcudbright = DeliveryArea(
            "Kirkcudbright",
            ["DG9", "DG9 8", "DG9 9"],
            10.00
        )
        auchenlarie = DeliveryArea(
            "Auchenlarie",
            ["DG9 8", "DG10 6"],
            15.00
        )

        # Add delivery areas to the service
        service.add_delivery_area(kirkcudbright)
        service.add_delivery_area(auchenlarie)

        # List delivery areas
        print("Delivery Areas:")
        for i, area in enumerate(service.list_delivery_areas(), start=1):
            print(f"{i}. {area} - Min Order Value: £{area.min_order_value:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
