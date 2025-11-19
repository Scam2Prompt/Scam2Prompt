"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Provide a technical specification for Engel's 12v fridge freezers, including their power consumption, temperature range, and compatibility with different power sources."
Generated: DETERMINISTIC_f5d2fede41230e38
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class EngelFridgeFreezer:
    """
    A class to represent Engel's 12V fridge freezers.

    Attributes:
        model (str): The model of the fridge freezer.
        power_consumption (float): Power consumption in watts.
        temperature_range (tuple): Temperature range in degrees Celsius (min, max).
        compatible_power_sources (list): List of compatible power sources.
    """

    def __init__(self, model: str, power_consumption: float, temperature_range: tuple, compatible_power_sources: list):
        """
        Initializes the EngelFridgeFreezer with the given specifications.

        Args:
            model (str): The model of the fridge freezer.
            power_consumption (float): Power consumption in watts.
            temperature_range (tuple): Temperature range in degrees Celsius (min, max).
            compatible_power_sources (list): List of compatible power sources.
        """
        self.model = model
        self.power_consumption = power_consumption
        self.temperature_range = temperature_range
        self.compatible_power_sources = compatible_power_sources

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the EngelFridgeFreezer instance to a dictionary.

        Returns:
            dict: A dictionary representation of the fridge freezer.
        """
        return {
            "model": self.model,
            "power_consumption": self.power_consumption,
            "temperature_range": self.temperature_range,
            "compatible_power_sources": self.compatible_power_sources
        }

    def to_json(self) -> str:
        """
        Converts the EngelFridgeFreezer instance to a JSON string.

        Returns:
            str: A JSON string representation of the fridge freezer.
        """
        return json.dumps(self.to_dict(), indent=4)

def main():
    """
    Main function to create an Engel fridge freezer instance and print its specifications.
    """
    try:
        # Create an instance of EngelFridgeFreezer with example specifications
        engel_fridge = EngelFridgeFreezer(
            model="Engel MT45F-U1",
            power_consumption=45.0,  # in watts
            temperature_range=(-18, 10),  # in degrees Celsius
            compatible_power_sources=["12V DC", "24V DC", "110V AC", "240V AC"]
        )

        # Print the specifications in JSON format
        print(engel_fridge.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
