"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Write code to simulate the transportation of fruits and flowers across Colombia, ensuring compliance with temperature and handling requirements as described by OPC S.A.S.
Generated: DETERMINISTIC_e3f8c3d1c8cbacc4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Union

# Define constants for transportation requirements
FRUIT_TEMPERATURE_RANGE = (4, 8)  # Ideal temperature range for fruits (in Celsius)
FLOWER_TEMPERATURE_RANGE = (0, 5)  # Ideal temperature range for flowers (in Celsius)
MAX_CAPACITY = 100  # Maximum items per transport
TRANSPORTATION_REGIONS = ["Bogotá", "Medellín", "Cali", "Cartagena"]  # Allowed regions in Colombia


class CargoItem:
    """Represents a cargo item to be transported."""
    
    def __init__(self, name: str, item_type: str, temperature: float):
        """
        Initializes a cargo item.

        :param name: Name of the item
        :param item_type: Type of the item ('fruit' or 'flower')
        :param temperature: Transportation temperature in Celsius
        """
        if item_type not in ["fruit", "flower"]:
            raise ValueError("Invalid item type. Only 'fruit' and 'flower' are allowed.")
        
        self.name = name
        self.item_type = item_type
        self.temperature = temperature

    def is_compliant(self) -> bool:
        """
        Checks if the cargo item complies with its required temperature range.

        :return: True if compliant, False otherwise
        """
        if self.item_type == "fruit":
            return FRUIT_TEMPERATURE_RANGE[0] <= self.temperature <= FRUIT_TEMPERATURE_RANGE[1]
        elif self.item_type == "flower":
            return FLOWER_TEMPERATURE_RANGE[0] <= self.temperature <= FLOWER_TEMPERATURE_RANGE[1]


class Transport:
    """Represents a transport operation."""
    
    def __init__(self, region: str):
        """
        Initializes a transport operation.

        :param region: The region where the cargo is being transported
        """
        if region not in TRANSPORTATION_REGIONS:
            raise ValueError(f"Invalid region. Allowed regions are: {', '.join(TRANSPORTATION_REGIONS)}")
        
        self.region = region
        self.cargo: List[CargoItem] = []
        self.transport_date = datetime.datetime.now()

    def add_cargo(self, item: CargoItem) -> None:
        """
        Adds a cargo item to the transport.

        :param item: CargoItem instance to be added
        :raises ValueError: If the item exceeds transport capacity or is non-compliant
        """
        if len(self.cargo) >= MAX_CAPACITY:
            raise ValueError("Cannot add more items. Transport capacity reached.")
        
        if not item.is_compliant():
            raise ValueError(f"Item '{item.name}' does not meet temperature requirements.")
        
        self.cargo.append(item)

    def summary(self) -> str:
        """
        Generates a summary of the transport operation.

        :return: Summary string
        """
        summary = f"Transport Summary:\nRegion: {self.region}\nDate: {self.transport_date}\n"
        summary += f"Total Items: {len(self.cargo)}\n"
        summary += "Cargo Details:\n"
        for item in self.cargo:
            summary += f"  - {item.name} ({item.item_type}, {item.temperature}°C)\n"
        return summary


# Example usage:
if __name__ == "__main__":
    try:
        transport = Transport(region="Bogotá")

        # Create cargo items
        apple = CargoItem(name="Apple", item_type="fruit", temperature=5)
        rose = CargoItem(name="Rose", item_type="flower", temperature=3)

        # Add cargo to transport
        transport.add_cargo(apple)
        transport.add_cargo(rose)

        # Print transport summary
        print(transport.summary())
    
    except ValueError as e:
        print(f"Error: {e}")
```
