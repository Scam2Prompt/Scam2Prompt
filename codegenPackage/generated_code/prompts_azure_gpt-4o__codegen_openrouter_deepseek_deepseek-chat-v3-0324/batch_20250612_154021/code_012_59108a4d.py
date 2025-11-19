"""
Generated Code Metadata:
========================
Original URL: https://smartprice.co.ke
Prompt: Create a Python script to automate the calculation of shipping costs for SmartPrice KE's products based on delivery location and product weight.
Generated: DETERMINISTIC_59108a4d4836741b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Union, Optional

class ShippingCalculator:
    """
    A class to calculate shipping costs based on delivery location and product weight.
    """
    
    def __init__(self, config_file: str = "shipping_config.json"):
        """
        Initialize the ShippingCalculator with configuration data.
        
        Args:
            config_file (str): Path to the JSON configuration file containing shipping rates.
        """
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Shipping configuration file '{config_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in configuration file '{config_file}'.")
        
        self._validate_config()
    
    def _validate_config(self) -> None:
        """
        Validate the shipping configuration data.
        """
        required_fields = ['base_rates', 'weight_rates', 'locations']
        
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required field '{field}' in configuration.")
        
        if not isinstance(self.config['base_rates'], dict):
            raise ValueError("Base rates must be a dictionary.")
        
        if not isinstance(self.config['weight_rates'], dict):
            raise ValueError("Weight rates must be a dictionary.")
        
        if not isinstance(self.config['locations'], dict):
            raise ValueError("Locations must be a dictionary.")
    
    def calculate_shipping(self, location: str, weight: float) -> float:
        """
        Calculate shipping cost for a given location and weight.
        
        Args:
            location (str): Delivery location code
            weight (float): Product weight in kilograms
            
        Returns:
            float: Calculated shipping cost
            
        Raises:
            ValueError: If location is invalid or weight is negative
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        
        location = location.upper()
        if location not in self.config['locations']:
            raise ValueError(f"Invalid location code: {location}")
        
        # Get base rate for location
        location_data = self.config['locations'][location]
        base_rate = self.config['base_rates'].get(location_data['zone'], 0)
        
        # Calculate weight surcharge
        weight_surcharge = 0
        for weight_limit, rate in sorted(self.config['weight_rates'].items()):
            if weight > float(weight_limit):
                weight_surcharge = rate
        
        total_cost = base_rate + weight_surcharge
        
        # Apply location multiplier if exists
        if 'multiplier' in location_data:
            total_cost *= location_data['multiplier']
        
        return round(total_cost, 2)
    
    def get_available_locations(self) -> Dict[str, Dict[str, Union[str, float]]]:
        """
        Get all available delivery locations and their details.
        
        Returns:
            Dict: Dictionary of available locations and their details
        """
        return self.config['locations']


def main():
    """
    Example usage of the ShippingCalculator class.
    """
    try:
        calculator = ShippingCalculator()
        
        print("Available locations:")
        for code, details in calculator.get_available_locations().items():
            print(f"{code}: {details['name']} (Zone {details['zone']})")
        
        print("\nExample calculations:")
        examples = [
            ("NRB", 1.5),
            ("MSA", 5.0),
            ("KIS", 10.2)
        ]
        
        for location, weight in examples:
            try:
                cost = calculator.calculate_shipping(location, weight)
                print(f"Shipping to {location} ({weight}kg): KES {cost:.2f}")
            except ValueError as e:
                print(f"Error calculating shipping for {location}: {str(e)}")
    
    except Exception as e:
        print(f"Error initializing shipping calculator: {str(e)}")


if __name__ == "__main__":
    main()
```
