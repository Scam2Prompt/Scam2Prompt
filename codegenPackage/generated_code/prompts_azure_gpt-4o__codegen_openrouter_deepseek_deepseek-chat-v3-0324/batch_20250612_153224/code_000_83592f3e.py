"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Write Python code to calculate shipping costs for international freight based on weight and destination, referencing Alexa Shipping's services like air and ocean freight.
Generated: DETERMINISTIC_83592f3ea3c12446
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from dataclasses import dataclass
from typing import Dict, Optional


class ShippingMethod(enum.Enum):
    """Enum representing available shipping methods."""
    AIR = "air"
    OCEAN = "ocean"


@dataclass
class ShippingRate:
    """Data class representing shipping rate details."""
    base_cost: float
    weight_surcharge: float
    destination_surcharge: float


class ShippingCalculator:
    """Class to calculate international shipping costs based on weight and destination."""
    
    # Shipping rates per method (base cost + surcharges)
    _RATES: Dict[ShippingMethod, Dict[str, ShippingRate]] = {
        ShippingMethod.AIR: {
            "europe": ShippingRate(50.0, 10.0, 15.0),
            "asia": ShippingRate(60.0, 12.0, 20.0),
            "americas": ShippingRate(55.0, 11.0, 18.0),
            "africa": ShippingRate(70.0, 15.0, 25.0),
            "oceania": ShippingRate(65.0, 13.0, 22.0),
        },
        ShippingMethod.OCEAN: {
            "europe": ShippingRate(30.0, 5.0, 10.0),
            "asia": ShippingRate(35.0, 6.0, 12.0),
            "americas": ShippingRate(32.0, 5.5, 11.0),
            "africa": ShippingRate(40.0, 8.0, 15.0),
            "oceania": ShippingRate(38.0, 7.0, 14.0),
        }
    }
    
    # Minimum and maximum weight limits in kg
    MIN_WEIGHT = 0.1  # 100 grams
    MAX_WEIGHT = 1000.0  # 1000 kg
    
    @classmethod
    def calculate_cost(
        cls,
        weight: float,
        destination: str,
        method: ShippingMethod = ShippingMethod.AIR,
    ) -> float:
        """
        Calculate shipping cost based on weight, destination, and shipping method.
        
        Args:
            weight: Weight of the shipment in kilograms.
            destination: Destination region (europe, asia, americas, africa, oceania).
            method: Shipping method (air or ocean).
            
        Returns:
            Total shipping cost in USD.
            
        Raises:
            ValueError: If weight or destination is invalid.
        """
        # Validate input parameters
        if weight < cls.MIN_WEIGHT or weight > cls.MAX_WEIGHT:
            raise ValueError(
                f"Weight must be between {cls.MIN_WEIGHT}kg and {cls.MAX_WEIGHT}kg"
            )
        
        destination = destination.lower()
        if destination not in cls._RATES[method]:
            raise ValueError(
                f"Invalid destination. Must be one of: {list(cls._RATES[method].keys())}"
            )
        
        # Get the applicable rate
        rate = cls._RATES[method][destination]
        
        # Calculate total cost
        total_cost = (
            rate.base_cost
            + (weight * rate.weight_surcharge)
            + rate.destination_surcharge
        )
        
        return round(total_cost, 2)


# Example usage
if __name__ == "__main__":
    try:
        weight = 5.5  # kg
        destination = "asia"
        method = ShippingMethod.AIR
        
        cost = ShippingCalculator.calculate_cost(weight, destination, method)
        print(f"Shipping cost for {weight}kg to {destination} via {method.value}: ${cost}")
        
        # Ocean freight example
        method = ShippingMethod.OCEAN
        cost = ShippingCalculator.calculate_cost(weight, destination, method)
        print(f"Shipping cost for {weight}kg to {destination} via {method.value}: ${cost}")
        
    except ValueError as e:
        print(f"Error calculating shipping cost: {e}")
```
