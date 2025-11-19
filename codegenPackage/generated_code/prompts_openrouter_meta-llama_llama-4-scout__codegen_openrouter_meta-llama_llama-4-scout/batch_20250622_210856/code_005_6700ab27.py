"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Create a data model for storing and managing Oticon hearing aid product information, including product types (e.g., Oticon Real, Oticon Own), features, and technical specifications.
Generated: DETERMINISTIC_6700ab276dd8b6bb
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class ProductType(str, Enum):
    """Enum for Oticon hearing aid product types."""
    OTICON_REAL = "Oticon Real"
    OTICON_OWN = "Oticon Own"

class Feature(str, Enum):
    """Enum for Oticon hearing aid features."""
    WATER_RESISTANT = "Water Resistant"
    RECHARGEABLE = "Rechargeable"
    BLUETOOTH_CONNECTIVITY = "Bluetooth Connectivity"

class TechnicalSpecification:
    """Class representing technical specifications of an Oticon hearing aid."""
    def __init__(self, 
                 frequency_range: str, 
                 max_sound_gain: str, 
                 battery_life: str):
        """
        Initialize technical specifications.

        Args:
        - frequency_range (str): Frequency range of the hearing aid.
        - max_sound_gain (str): Maximum sound gain of the hearing aid.
        - battery_life (str): Battery life of the hearing aid.
        """
        self.frequency_range = frequency_range
        self.max_sound_gain = max_sound_gain
        self.battery_life = battery_life

class OticonHearingAid:
    """Class representing an Oticon hearing aid product."""
    def __init__(self, 
                 product_type: ProductType, 
                 model_name: str, 
                 features: List[Feature], 
                 technical_specifications: TechnicalSpecification):
        """
        Initialize an Oticon hearing aid product.

        Args:
        - product_type (ProductType): Type of the Oticon hearing aid product.
        - model_name (str): Model name of the hearing aid.
        - features (List[Feature]): List of features of the hearing aid.
        - technical_specifications (TechnicalSpecification): Technical specifications of the hearing aid.
        """
        self.product_type = product_type
        self.model_name = model_name
        self.features = features
        self.technical_specifications = technical_specifications

    def __str__(self):
        return f"Oticon {self.product_type.value} - {self.model_name}"

    def to_dict(self) -> Dict:
        """Convert the Oticon hearing aid product to a dictionary."""
        return {
            "product_type": self.product_type.value,
            "model_name": self.model_name,
            "features": [feature.value for feature in self.features],
            "technical_specifications": {
                "frequency_range": self.technical_specifications.frequency_range,
                "max_sound_gain": self.technical_specifications.max_sound_gain,
                "battery_life": self.technical_specifications.battery_life
            }
        }

class OticonHearingAidManager:
    """Class for managing Oticon hearing aid products."""
    def __init__(self):
        self.products = []

    def add_product(self, product: OticonHearingAid):
        """Add an Oticon hearing aid product to the manager."""
        self.products.append(product)

    def get_products(self) -> List[Dict]:
        """Get a list of all Oticon hearing aid products."""
        return [product.to_dict() for product in self.products]

def main():
    try:
        # Create technical specifications
        tech_specs = TechnicalSpecification(
            frequency_range="20 Hz - 20 kHz",
            max_sound_gain="60 dB",
            battery_life="Up to 24 hours"
        )

        # Create features
        features = [Feature.WATER_RESISTANT, Feature.RECHARGEABLE, Feature.BLUETOOTH_CONNECTIVITY]

        # Create Oticon hearing aid products
        product1 = OticonHearingAid(
            product_type=ProductType.OTICON_REAL,
            model_name="Oticon Real 1",
            features=features,
            technical_specifications=tech_specs
        )

        product2 = OticonHearingAid(
            product_type=ProductType.OTICON_OWN,
            model_name="Oticon Own 1",
            features=features,
            technical_specifications=tech_specs
        )

        # Create a product manager
        manager = OticonHearingAidManager()
        manager.add_product(product1)
        manager.add_product(product2)

        # Get and print products
        products = manager.get_products()
        for product in products:
            print(product)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
