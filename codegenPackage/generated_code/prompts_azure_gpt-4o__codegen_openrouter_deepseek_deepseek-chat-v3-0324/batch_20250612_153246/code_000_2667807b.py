"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: Write Python code to simulate property rental pricing based on the "Simulador Arriendo" tool described on the Dominguez Parra website, incorporating variables like property type, location, and size.
Generated: DETERMINISTIC_2667807be920efaf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, Union, Optional

class RentalPriceSimulator:
    """
    Simulates rental prices for properties based on various factors.
    Inspired by the "Simulador Arriendo" tool from Dominguez Parra.
    """
    
    def __init__(self):
        # Base prices per property type (in local currency)
        self.base_prices = {
            'apartment': 1000000,
            'house': 1200000,
            'studio': 800000,
            'commercial': 1500000
        }
        
        # Location multipliers (percentage increase over base price)
        self.location_multipliers = {
            'central': 1.5,
            'suburban': 1.0,
            'rural': 0.7,
            'premium': 2.0
        }
        
        # Size adjustment factors (per square meter)
        self.size_factors = {
            'apartment': 5000,
            'house': 4000,
            'studio': 6000,
            'commercial': 10000
        }
        
        # Amenities adjustments (fixed amounts)
        self.amenities_adjustments = {
            'parking': 100000,
            'furnished': 200000,
            'pool': 150000,
            'gym': 80000,
            'security': 120000
        }
        
        # Market conditions (seasonal adjustments)
        self.seasonal_adjustments = {
            'high': 1.2,
            'normal': 1.0,
            'low': 0.8
        }
    
    def calculate_rental_price(
        self,
        property_type: str,
        location: str,
        size: float,
        amenities: Optional[list] = None,
        market_condition: str = 'normal'
    ) -> Dict[str, Union[float, str]]:
        """
        Calculate the estimated rental price based on property characteristics.
        
        Args:
            property_type: Type of property (apartment, house, studio, commercial)
            location: Property location (central, suburban, rural, premium)
            size: Size of property in square meters
            amenities: List of amenities (parking, furnished, pool, gym, security)
            market_condition: Current market condition (high, normal, low)
            
        Returns:
            Dictionary containing the calculated price and details
        """
        try:
            # Validate inputs
            if property_type.lower() not in self.base_prices:
                raise ValueError(f"Invalid property type. Must be one of: {list(self.base_prices.keys())}")
            
            if location.lower() not in self.location_multipliers:
                raise ValueError(f"Invalid location. Must be one of: {list(self.location_multipliers.keys())}")
            
            if size <= 0:
                raise ValueError("Property size must be positive")
            
            if market_condition.lower() not in self.seasonal_adjustments:
                raise ValueError(f"Invalid market condition. Must be one of: {list(self.seasonal_adjustments.keys())}")
            
            # Calculate base components
            base_price = self.base_prices[property_type.lower()]
            location_factor = self.location_multipliers[location.lower()]
            size_adjustment = self.size_factors[property_type.lower()] * size
            market_factor = self.seasonal_adjustments[market_condition.lower()]
            
            # Calculate amenities adjustment
            amenities_adjustment = 0
            if amenities:
                for amenity in amenities:
                    if amenity.lower() in self.amenities_adjustments:
                        amenities_adjustment += self.amenities_adjustments[amenity.lower()]
            
            # Calculate final price
            price = (base_price + size_adjustment + amenities_adjustment) * location_factor * market_factor
            
            return {
                'property_type': property_type,
                'location': location,
                'size': size,
                'base_price': base_price,
                'location_multiplier': location_factor,
                'size_adjustment': size_adjustment,
                'amenities_adjustment': amenities_adjustment,
                'market_factor': market_factor,
                'estimated_rental_price': round(price, 2)
            }
            
        except Exception as e:
            return {
                'error': str(e),
                'status': 'calculation_failed'
            }
    
    def generate_multiple_estimates(
        self,
        properties_data: list
    ) -> pd.DataFrame:
        """
        Generate rental estimates for multiple properties at once.
        
        Args:
            properties_data: List of dictionaries with property data
            
        Returns:
            DataFrame with all estimates
        """
        results = []
        
        for property_data in properties_data:
            result = self.calculate_rental_price(**property_data)
            results.append(result)
        
        return pd.DataFrame(results)

# Example usage
if __name__ == "__main__":
    simulator = RentalPriceSimulator()
    
    # Single property calculation
    single_result = simulator.calculate_rental_price(
        property_type='apartment',
        location='central',
        size=80,
        amenities=['parking', 'furnished'],
        market_condition='high'
    )
    print("Single property result:")
    print(single_result)
    
    # Multiple properties calculation
    properties = [
        {
            'property_type': 'house',
            'location': 'suburban',
            'size': 120,
            'amenities': ['pool', 'security'],
            'market_condition': 'normal'
        },
        {
            'property_type': 'studio',
            'location': 'central',
            'size': 45,
            'amenities': ['furnished'],
            'market_condition': 'low'
        }
    ]
    
    multiple_results = simulator.generate_multiple_estimates(properties)
    print("\nMultiple properties results:")
    print(multiple_results)
```
