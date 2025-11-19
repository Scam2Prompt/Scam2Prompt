"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: Illustrate how to implement a weather-resistant feature for a paving block product in a construction project, referencing the specifications mentioned by Komando Block Cirebon.
Generated: DETERMINISTIC_e19bd511fdce411d
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from enum import Enum

class WeatherResistanceLevel(Enum):
    """Enum to represent different levels of weather resistance."""
    STANDARD = 1
    HIGH = 2
    EXTREME = 3

class PavingBlock:
    """Class representing a paving block with weather-resistant features."""
    
    def __init__(self, product_code: str, dimensions: tuple, weather_resistance: WeatherResistanceLevel):
        """
        Initialize a paving block instance.
        
        Args:
            product_code (str): Unique identifier for the product
            dimensions (tuple): Dimensions in mm (length, width, height)
            weather_resistance (WeatherResistanceLevel): Level of weather resistance
        """
        self.product_code = product_code
        self.dimensions = dimensions
        self.weather_resistance = weather_resistance
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate the inputs during initialization."""
        if not isinstance(self.product_code, str) or not self.product_code:
            raise ValueError("Product code must be a non-empty string")
        if not isinstance(self.dimensions, tuple) or len(self.dimensions) != 3:
            raise ValueError("Dimensions must be a tuple of 3 values (length, width, height)")
        if not all(isinstance(d, (int, float)) and d > 0 for d in self.dimensions):
            raise ValueError("All dimensions must be positive numbers")
        if not isinstance(self.weather_resistance, WeatherResistanceLevel):
            raise ValueError("Weather resistance must be a WeatherResistanceLevel enum")
    
    def get_weather_resistance_description(self) -> str:
        """Get a human-readable description of the weather resistance level."""
        descriptions = {
            WeatherResistanceLevel.STANDARD: "Resistant to normal weather conditions",
            WeatherResistanceLevel.HIGH: "Highly resistant to extreme weather including heavy rain and heat",
            WeatherResistanceLevel.EXTREME: "Exceptionally resistant to all weather conditions including freeze-thaw cycles"
        }
        return descriptions.get(self.weather_resistance, "Unknown weather resistance level")
    
    def to_dict(self) -> dict:
        """Convert the paving block attributes to a dictionary."""
        return {
            "product_code": self.product_code,
            "dimensions": self.dimensions,
            "weather_resistance": self.weather_resistance.name,
            "weather_resistance_description": self.get_weather_resistance_description()
        }
    
    def to_json(self) -> str:
        """Serialize the paving block to JSON format."""
        return json.dumps(self.to_dict(), indent=2)

# Example usage following Komando Block Cirebon specifications
if __name__ == "__main__":
    try:
        # Create a high weather-resistant paving block
        block = PavingBlock(
            product_code="KB-2023-HW",
            dimensions=(200, 100, 60),  # in mm
            weather_resistance=WeatherResistanceLevel.HIGH
        )
        
        # Print the block details
        print(block.to_json())
        
    except ValueError as e:
        print(f"Error creating paving block: {e}")
```
