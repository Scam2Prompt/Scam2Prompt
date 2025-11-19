"""
Generated Code Metadata:
========================
Original URL: https://motor-muse.com
Prompt: Design a data model for storing information about various car models, including their specifications, prices, and features, using the 2025 GMC Yukon Denali as an example.
Generated: DETERMINISTIC_293db24bfbd37626
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# car_model.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class CarType(str, Enum):
    """Enum for car types."""
    SUV = "SUV"
    TRUCK = "Truck"
    SEDAN = "Sedan"
    WAGON = "Wagon"
    VAN = "Van"

@dataclass
class CarSpecification:
    """Data class for car specifications."""
    engine_size: float  # in liters
    horsepower: int
    transmission: str
    drive_type: str

@dataclass
class CarFeature:
    """Data class for car features."""
    name: str
    description: str

@dataclass
class CarModel:
    """Data class for car models."""
    make: str
    model: str
    car_type: CarType
    specifications: CarSpecification
    base_price: float  # in USD
    features: List[CarFeature]

    def __post_init__(self):
        """Validate car model data."""
        if self.base_price < 0:
            raise ValueError("Base price cannot be negative")

    def add_feature(self, feature: CarFeature):
        """Add a feature to the car model."""
        self.features.append(feature)

    def remove_feature(self, feature_name: str):
        """Remove a feature from the car model."""
        self.features = [feature for feature in self.features if feature.name != feature_name]

def main():
    # Example usage
    yukon_denali_specifications = CarSpecification(
        engine_size=6.2,
        horsepower=420,
        transmission="10-speed automatic",
        drive_type="4-wheel drive"
    )

    yukon_denali_features = [
        CarFeature("Premium Infotainment", "10.2-inch touchscreen"),
        CarFeature("Navigation", "GPS navigation system"),
        CarFeature("Panoramic Sunroof", "large glass roof panel")
    ]

    yukon_denali = CarModel(
        make="GMC",
        model="Yukon Denali",
        car_type=CarType.SUV,
        specifications=yukon_denali_specifications,
        base_price=69995.0,
        features=yukon_denali_features
    )

    print(f"Make: {yukon_denali.make}")
    print(f"Model: {yukon_denali.model}")
    print(f"Type: {yukon_denali.car_type.value}")
    print(f"Engine Size: {yukon_denali.specifications.engine_size}L")
    print(f"Horsepower: {yukon_denali.specifications.horsepower}hp")
    print(f"Base Price: ${yukon_denali.base_price:,.2f}")
    print("Features:")
    for feature in yukon_denali.features:
        print(f"- {feature.name}: {feature.description}")

if __name__ == "__main__":
    main()
```
