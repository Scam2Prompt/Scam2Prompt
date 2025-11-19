"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Generate code to calculate shipping costs for products purchased from an online store that "ENVIAMOS PARA TODO O BRASIL" via the postal service.
Generated: DETERMINISTIC_014ce7b1301fd63e
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional, Tuple

class ShippingCalculator:
    """
    Calculates shipping costs for products purchased from an online store in Brazil.
    Uses Correios API (simulated) to calculate shipping costs based on weight, dimensions, and destination.
    """
    
    # Shipping options with base prices (in BRL) and weight limits (in kg)
    SHIPPING_OPTIONS = {
        'PAC': {
            'base_price': 15.00,
            'max_weight': 30.0,
            'price_per_kg': 2.50,
            'dimension_limit': 200  # sum of dimensions (length + width + height) in cm
        },
        'SEDEX': {
            'base_price': 25.00,
            'max_weight': 30.0,
            'price_per_kg': 5.00,
            'dimension_limit': 200
        },
        'SEDEX_10': {
            'base_price': 35.00,
            'max_weight': 10.0,
            'price_per_kg': 7.00,
            'dimension_limit': 200
        }
    }
    
    # Regional factors for different Brazilian states (multipliers for base price)
    REGIONAL_FACTORS = {
        'SP': 1.0,
        'RJ': 1.1,
        'MG': 1.1,
        'ES': 1.2,
        'RS': 1.3,
        'SC': 1.3,
        'PR': 1.2,
        'DF': 1.4,
        'GO': 1.4,
        'MT': 1.5,
        'MS': 1.5,
        'BA': 1.4,
        'SE': 1.5,
        'PE': 1.5,
        'AL': 1.5,
        'PB': 1.6,
        'RN': 1.6,
        'CE': 1.6,
        'PI': 1.7,
        'MA': 1.7,
        'PA': 1.8,
        'AP': 2.0,
        'AM': 2.0,
        'RR': 2.2,
        'AC': 2.2,
        'RO': 1.9,
        'TO': 1.8
    }
    
    def __init__(self):
        pass
    
    def calculate_shipping(
        self,
        items: List[Dict[str, float]],
        destination_zip: str,
        destination_state: str
    ) -> Dict[str, Optional[float]]:
        """
        Calculate shipping costs for given items to a destination in Brazil.
        
        Args:
            items: List of dictionaries containing 'weight' (kg), 'length', 'width', 'height' (cm)
            destination_zip: Destination ZIP code (not used in this simplified version)
            destination_state: Destination state (2-letter code)
            
        Returns:
            Dictionary with shipping options and their costs (None if not available)
        """
        try:
            # Validate inputs
            if not items or not destination_state or len(destination_state) != 2:
                raise ValueError("Invalid input parameters")
            
            # Calculate total weight and dimensions
            total_weight = sum(item.get('weight', 0) for item in items)
            total_volume = sum(item.get('length', 0) + item.get('width', 0) + item.get('height', 0) for item in items)
            
            if total_weight <= 0 or total_volume <= 0:
                raise ValueError("Invalid item dimensions or weight")
            
            # Get regional factor
            regional_factor = self.REGIONAL_FACTORS.get(destination_state.upper(), 1.5)
            
            # Calculate shipping options
            shipping_costs = {}
            for option, params in self.SHIPPING_OPTIONS.items():
                if (total_weight > params['max_weight'] or 
                    total_volume > params['dimension_limit']):
                    shipping_costs[option] = None
                else:
                    cost = params['base_price'] + (total_weight * params['price_per_kg'])
                    cost *= regional_factor
                    shipping_costs[option] = round(cost, 2)
            
            return shipping_costs
            
        except Exception as e:
            print(f"Error calculating shipping: {str(e)}")
            return {option: None for option in self.SHIPPING_OPTIONS.keys()}
    
    def get_cheapest_option(self, shipping_costs: Dict[str, Optional[float]]) -> Tuple[str, float]:
        """
        Get the cheapest available shipping option from calculated costs.
        
        Args:
            shipping_costs: Dictionary of shipping options and their costs
            
        Returns:
            Tuple of (option_name, cost) for cheapest available option
        """
        try:
            available_options = {k: v for k, v in shipping_costs.items() if v is not None}
            if not available_options:
                raise ValueError("No shipping options available")
            
            cheapest_option = min(available_options.items(), key=lambda x: x[1])
            return cheapest_option
        except Exception as e:
            print(f"Error finding cheapest option: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    calculator = ShippingCalculator()
    
    # Sample items in cart
    items = [
        {'weight': 1.5, 'length': 30, 'width': 20, 'height': 10},
        {'weight': 0.5, 'length': 15, 'width': 15, 'height': 15}
    ]
    
    # Calculate shipping to different destinations
    destinations = [
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro'),
        ('AM', 'Amazonas')
    ]
    
    for state, name in destinations:
        print(f"\nShipping to {name} ({state}):")
        costs = calculator.calculate_shipping(items, '00000000', state)
        for option, cost in costs.items():
            print(f"{option}: R${cost if cost is not None else 'N/A'}")
        
        try:
            cheapest = calculator.get_cheapest_option(costs)
            print(f"Cheapest option: {cheapest[0]} at R${cheapest[1]}")
        except ValueError:
            print("No shipping options available for this destination")
```
