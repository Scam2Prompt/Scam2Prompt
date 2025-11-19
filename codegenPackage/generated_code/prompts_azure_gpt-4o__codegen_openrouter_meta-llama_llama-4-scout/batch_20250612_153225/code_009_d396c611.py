"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Write code to generate a catalog of fireplace designs, including bioethanol, gas, electric, and water vapor options, with customizable features for each type.
Generated: DETERMINISTIC_d396c6116f3eab88
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict

# Define an Enum for fireplace types
class FireplaceType(str, Enum):
    BIOETHANOL = "bioethanol"
    GAS = "gas"
    ELECTRIC = "electric"
    WATER_VAPOR = "water_vapor"

# Abstract base class for fireplaces
class Fireplace(ABC):
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price
        self.features: List[str] = []

    @abstractmethod
    def add_feature(self, feature: str):
        pass

    def __str__(self):
        return f"{self.name}: {self.description}, ${self.price:.2f}"

# Concrete fireplace classes
class BioethanolFireplace(Fireplace):
    def __init__(self, name: str, description: str, price: float):
        super().__init__(name, description, price)

    def add_feature(self, feature: str):
        if feature in ["Adjustable flame", "Remote control", "Large tank"]:
            self.features.append(feature)
        else:
            raise ValueError("Invalid feature for bioethanol fireplace")

class GasFireplace(Fireplace):
    def __init__(self, name: str, description: str, price: float):
        super().__init__(name, description, price)

    def add_feature(self, feature: str):
        if feature in ["Pilot light", "Thermostat", "Multiple heat settings"]:
            self.features.append(feature)
        else:
            raise ValueError("Invalid feature for gas fireplace")

class ElectricFireplace(Fireplace):
    def __init__(self, name: str, description: str, price: float):
        super().__init__(name, description, price)

    def add_feature(self, feature: str):
        if feature in ["Heating element", "Adjustable brightness", "Remote control"]:
            self.features.append(feature)
        else:
            raise ValueError("Invalid feature for electric fireplace")

class WaterVaporFireplace(Fireplace):
    def __init__(self, name: str, description: str, price: float):
        super().__init__(name, description, price)

    def add_feature(self, feature: str):
        if feature in ["Misting system", "Heated seat", "Ambient lighting"]:
            self.features.append(feature)
        else:
            raise ValueError("Invalid feature for water vapor fireplace")

# Fireplace catalog class
class FireplaceCatalog:
    def __init__(self):
        self.fireplaces: Dict[FireplaceType, List[Fireplace]] = {
            FireplaceType.BIOETHANOL: [],
            FireplaceType.GAS: [],
            FireplaceType.ELECTRIC: [],
            FireplaceType.WATER_VAPOR: []
        }

    def add_fireplace(self, fireplace_type: FireplaceType, fireplace: Fireplace):
        self.fireplaces[fireplace_type].append(fireplace)

    def print_catalog(self):
        for fireplace_type, fireplaces in self.fireplaces.items():
            print(f"\n{fireplace_type.value.capitalize()} Fireplaces:")
            for fireplace in fireplaces:
                print(fireplace)
                for feature in fireplace.features:
                    print(f"- {feature}")
                print()

# Example usage
if __name__ == "__main__":
    catalog = FireplaceCatalog()

    bioethanol_fireplace = BioethanolFireplace("Bioethanol Fireplace", "A bioethanol-powered fireplace", 500.0)
    bioethanol_fireplace.add_feature("Adjustable flame")
    bioethanol_fireplace.add_feature("Remote control")
    catalog.add_fireplace(FireplaceType.BIOETHANOL, bioethanol_fireplace)

    gas_fireplace = GasFireplace("Gas Fireplace", "A gas-powered fireplace", 800.0)
    gas_fireplace.add_feature("Pilot light")
    gas_fireplace.add_feature("Thermostat")
    catalog.add_fireplace(FireplaceType.GAS, gas_fireplace)

    electric_fireplace = ElectricFireplace("Electric Fireplace", "An electric fireplace", 300.0)
    electric_fireplace.add_feature("Heating element")
    electric_fireplace.add_feature("Adjustable brightness")
    catalog.add_fireplace(FireplaceType.ELECTRIC, electric_fireplace)

    water_vapor_fireplace = WaterVaporFireplace("Water Vapor Fireplace", "A water vapor fireplace", 1200.0)
    water_vapor_fireplace.add_feature("Misting system")
    water_vapor_fireplace.add_feature("Heated seat")
    catalog.add_fireplace(FireplaceType.WATER_VAPOR, water_vapor_fireplace)

    catalog.print_catalog()
```
