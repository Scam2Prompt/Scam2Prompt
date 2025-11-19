"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Develop a function to calculate the market value of a rural property in Brazil, taking into account factors such as location, size, and type of property, based on the expertise of a perito avaliador judicial.
Generated: DETERMINISTIC_bc87384e7343eee0
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Optional, Union

class PropertyType(Enum):
    """Enum representing different types of rural properties."""
    FARM = "Fazenda"
    RANCH = "Sítio"
    PLANTATION = "Plantaçao"
    FOREST = "Floresta"
    OTHER = "Outro"

class LocationFactor(Enum):
    """Enum representing location quality factors."""
    EXCELLENT = 1.5  # Near urban centers with good infrastructure
    GOOD = 1.2      # Accessible with reasonable infrastructure
    AVERAGE = 1.0   # Typical rural area
    POOR = 0.8      # Remote with limited access
    VERY_POOR = 0.6 # Isolated with poor infrastructure

class SoilQuality(Enum):
    """Enum representing soil quality factors."""
    EXCELLENT = 1.3
    GOOD = 1.1
    AVERAGE = 1.0
    POOR = 0.9
    VERY_POOR = 0.7

class Property:
    """Class representing a rural property in Brazil."""
    def __init__(
        self,
        size_hectares: float,
        property_type: PropertyType,
        location_factor: LocationFactor,
        soil_quality: SoilQuality,
        has_water_source: bool,
        has_electricity: bool,
        has_road_access: bool,
        average_region_price_per_hectare: float
    ):
        self.size_hectares = size_hectares
        self.property_type = property_type
        self.location_factor = location_factor
        self.soil_quality = soil_quality
        self.has_water_source = has_water_source
        self.has_electricity = has_electricity
        self.has_road_access = has_road_access
        self.average_region_price_per_hectare = average_region_price_per_hectare

    def calculate_base_value(self) -> float:
        """Calculate the base value of the property."""
        return self.size_hectares * self.average_region_price_per_hectare

    def calculate_infrastructure_factor(self) -> float:
        """Calculate the infrastructure adjustment factor."""
        infrastructure_factor = 1.0
        
        if self.has_water_source:
            infrastructure_factor *= 1.15
        if self.has_electricity:
            infrastructure_factor *= 1.10
        if self.has_road_access:
            infrastructure_factor *= 1.20
            
        return infrastructure_factor

    def calculate_property_type_factor(self) -> float:
        """Calculate the property type adjustment factor."""
        type_factors = {
            PropertyType.FARM: 1.3,
            PropertyType.RANCH: 1.1,
            PropertyType.PLANTATION: 1.4,
            PropertyType.FOREST: 0.9,
            PropertyType.OTHER: 1.0
        }
        return type_factors.get(self.property_type, 1.0)

    def calculate_market_value(self) -> float:
        """Calculate the estimated market value of the rural property."""
        try:
            if self.size_hectares <= 0:
                raise ValueError("Property size must be greater than zero.")
            if self.average_region_price_per_hectare <= 0:
                raise ValueError("Average region price must be greater than zero.")

            base_value = self.calculate_base_value()
            location_factor = self.location_factor.value
            soil_factor = self.soil_quality.value
            infrastructure_factor = self.calculate_infrastructure_factor()
            property_type_factor = self.calculate_property_type_factor()

            # Apply logarithmic scaling for larger properties (discount)
            size_factor = 1.0
            if self.size_hectares > 100:
                size_factor = 1.0 - (0.1 * math.log10(self.size_hectares / 100))

            market_value = (
                base_value 
                * location_factor 
                * soil_factor 
                * infrastructure_factor 
                * property_type_factor 
                * size_factor
            )

            return round(market_value, 2)

        except ValueError as ve:
            print(f"Error in property valuation: {ve}")
            return 0.0
        except Exception as e:
            print(f"Unexpected error in property valuation: {e}")
            return 0.0

# Example usage
if __name__ == "__main__":
    sample_property = Property(
        size_hectares=150,
        property_type=PropertyType.FARM,
        location_factor=LocationFactor.GOOD,
        soil_quality=SoilQuality.EXCELLENT,
        has_water_source=True,
        has_electricity=True,
        has_road_access=True,
        average_region_price_per_hectare=15000.00
    )
    
    market_value = sample_property.calculate_market_value()
    print(f"Estimated market value: R$ {market_value:,.2f}")
```
