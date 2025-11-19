"""
Generated Code Metadata:
========================
Original URL: https://feresplast.com
Prompt: Develop a code snippet to integrate a shipping and handling calculator into an e-commerce platform, considering factors like location and package weight, similar to Feresplast's shipping features.
Generated: DETERMINISTIC_076e66076c39bbdb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Optional, Tuple

class ShippingCalculator:
    """
    A shipping and handling calculator for e-commerce platforms.
    Calculates shipping costs based on destination, package weight, and dimensions.
    """
    
    def __init__(self):
        # Base shipping rates by region (in USD)
        self.base_rates = {
            'local': 5.00,
            'regional': 10.00,
            'national': 15.00,
            'international': 25.00
        }
        
        # Weight surcharge thresholds (in kg) and rates
        self.weight_surcharge = {
            'threshold': 5.0,
            'rate_per_kg': 2.0
        }
        
        # Oversize package surcharge
        self.size_surcharge = {
            'max_dimension': 150,  # cm
            'surcharge': 10.00
        }
        
        # Hazardous materials surcharge
        self.hazardous_surcharge = 15.00
        
        # Remote area surcharge
        self.remote_areas = {
            'Alaska': 12.00,
            'Hawaii': 10.00,
            'Puerto Rico': 8.00
        }
    
    def calculate_shipping(
        self,
        destination: str,
        weight: float,
        dimensions: Tuple[float, float, float],
        is_hazardous: bool = False,
        is_express: bool = False
    ) -> Dict[str, Optional[float]]:
        """
        Calculate total shipping cost based on various factors.
        
        Args:
            destination: Shipping destination (country/region)
            weight: Package weight in kilograms
            dimensions: Package dimensions (length, width, height) in centimeters
            is_hazardous: Whether package contains hazardous materials
            is_express: Whether express shipping is requested
            
        Returns:
            Dictionary containing:
            - base_cost: Base shipping cost
            - weight_surcharge: Additional cost for weight
            - size_surcharge: Additional cost for oversize
            - hazardous_surcharge: Additional cost for hazardous materials
            - remote_surcharge: Additional cost for remote areas
            - express_fee: Additional cost for express shipping
            - total_cost: Sum of all costs
        """
        result = {
            'base_cost': None,
            'weight_surcharge': 0.0,
            'size_surcharge': 0.0,
            'hazardous_surcharge': 0.0,
            'remote_surcharge': 0.0,
            'express_fee': 0.0,
            'total_cost': None
        }
        
        try:
            # Validate inputs
            if weight <= 0:
                raise ValueError("Package weight must be positive")
            if any(dim <= 0 for dim in dimensions):
                raise ValueError("All package dimensions must be positive")
            
            # Determine base rate based on destination
            region = self._determine_region(destination)
            base_cost = self.base_rates.get(region, self.base_rates['international'])
            result['base_cost'] = base_cost
            
            # Calculate weight surcharge
            if weight > self.weight_surcharge['threshold']:
                excess_weight = weight - self.weight_surcharge['threshold']
                result['weight_surcharge'] = math.ceil(excess_weight) * self.weight_surcharge['rate_per_kg']
            
            # Calculate size surcharge
            if any(dim > self.size_surcharge['max_dimension'] for dim in dimensions):
                result['size_surcharge'] = self.size_surcharge['surcharge']
            
            # Add hazardous materials surcharge
            if is_hazardous:
                result['hazardous_surcharge'] = self.hazardous_surcharge
            
            # Add remote area surcharge
            if destination in self.remote_areas:
                result['remote_surcharge'] = self.remote_areas[destination]
            
            # Add express shipping fee (50% of base cost)
            if is_express:
                result['express_fee'] = base_cost * 0.5
            
            # Calculate total cost
            result['total_cost'] = sum(v for v in result.values() if isinstance(v, (int, float)))
            
        except Exception as e:
            raise ValueError(f"Shipping calculation failed: {str(e)}")
        
        return result
    
    def _determine_region(self, destination: str) -> str:
        """
        Determine shipping region based on destination.
        This is a simplified version - in production you would use a geolocation API.
        """
        # US states
        us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                     'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                     'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                     'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                     'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
        
        if destination in us_states:
            if destination in ['AK', 'HI']:
                return 'national'  # These will get remote surcharge
            return 'local' if destination == 'CA' else 'national'
        elif destination in ['Canada', 'Mexico']:
            return 'regional'
        else:
            return 'international'
```
