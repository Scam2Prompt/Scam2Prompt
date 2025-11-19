"""
Generated Code Metadata:
========================
Original URL: https://venus.farm
Prompt: Generate a simple data model for tracking farm produce, inspired by the structure of data that venus.farm might handle.
Generated: DETERMINISTIC_308e73b178b5478b
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Optional
import json

class Produce:
    """
    A class to represent a type of farm produce.

    Attributes:
        name (str): The name of the produce.
        quantity (int): The quantity of the produce available.
        harvest_date (datetime): The date when the produce was harvested.
        price_per_unit (float): The price per unit of the produce.
    """

    def __init__(self, name: str, quantity: int, harvest_date: str, price_per_unit: float):
        """
        Initializes a Produce instance.

        Args:
            name (str): The name of the produce.
            quantity (int): The quantity of the produce available.
            harvest_date (str): The date when the produce was harvested in 'YYYY-MM-DD' format.
            price_per_unit (float): The price per unit of the produce.

        Raises:
            ValueError: If quantity is negative or price_per_unit is negative.
            ValueError: If harvest_date is not in the correct format.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if price_per_unit < 0:
            raise ValueError("Price per unit cannot be negative.")
        
        try:
            self.harvest_date = datetime.strptime(harvest_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Harvest date must be in 'YYYY-MM-DD' format.")

        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def total_value(self) -> float:
        """
        Calculates the total value of the produce based on quantity and price per unit.

        Returns:
            float: The total value of the produce.
        """
        return self.quantity * self.price_per_unit

    def to_dict(self) -> dict:
        """
        Converts the Produce instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Produce instance.
        """
        return {
            'name': self.name,
            'quantity': self.quantity,
            'harvest_date': self.harvest_date.strftime('%Y-%m-%d'),
            'price_per_unit': self.price_per_unit
        }

class Farm:
    """
    A class to represent a farm that tracks various produces.

    Attributes:
        produces (List[Produce]): A list of Produce instances.
    """

    def __init__(self):
        """Initializes a Farm instance with an empty produce list."""
        self.produces: List[Produce] = []

    def add_produce(self, produce: Produce):
        """
        Adds a Produce instance to the farm's produce list.

        Args:
            produce (Produce): The Produce instance to add.
        """
        self.produces.append(produce)

    def total_inventory_value(self) -> float:
        """
        Calculates the total inventory value of all produces in the farm.

        Returns:
            float: The total inventory value.
        """
        return sum(produce.total_value() for produce in self.produces)

    def to_json(self) -> str:
        """
        Converts the Farm instance to a JSON string.

        Returns:
            str: A JSON string representation of the Farm instance.
        """
        return json.dumps([produce.to_dict() for produce in self.produces], indent=4)

# Example usage
if __name__ == "__main__":
    try:
        farm = Farm()
        farm.add_produce(Produce("Tomatoes", 100, "2023-09-15", 0.5))
        farm.add_produce(Produce("Cucumbers", 50, "2023-09-10", 0.75))

        print("Total Inventory Value: $", farm.total_inventory_value())
        print("Farm Produce JSON:")
        print(farm.to_json())
    except ValueError as e:
        print(f"Error: {e}")
```
