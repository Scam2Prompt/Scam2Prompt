"""
Generated Code Metadata:
========================
Original URL: https://t528.com
Prompt: Write a Python script to calculate the maximum cargo weight for a Boeing 787-9 aircraft based on its cargo dimensions.
Generated: DETERMINISTIC_18fd22afd3d3c664
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class CargoWeightCalculator:
    """
    A class to calculate the maximum cargo weight for a Boeing 787-9 aircraft
    based on cargo dimensions and aircraft specifications.
    """
    
    def __init__(self):
        """Initialize aircraft specifications for Boeing 787-9."""
        self.max_payload = 44000  # kg (maximum payload capacity)
        self.max_volume = 136.0   # m³ (total cargo volume capacity)
        self.pallet_dimensions = {
            'LD3': {'length': 1.56, 'width': 1.54, 'height': 1.60, 'max_weight': 1588},
            'LD8': {'length': 3.18, 'width': 2.44, 'height': 1.60, 'max_weight': 3175},
            'LD11': {'length': 3.18, 'width': 2.44, 'height': 1.60, 'max_weight': 3175}
        }
    
    def calculate_max_weight(self, cargo_type, cargo_count):
        """
        Calculate the maximum cargo weight based on pallet type and count.
        
        Args:
            cargo_type (str): Type of cargo pallet (LD3, LD8, LD11)
            cargo_count (int): Number of pallets
            
        Returns:
            float: Maximum weight in kg that can be carried
        """
        try:
            if cargo_type not in self.pallet_dimensions:
                raise ValueError(f"Invalid cargo type. Must be one of: {list(self.pallet_dimensions.keys())}")
            
            if not isinstance(cargo_count, int) or cargo_count <= 0:
                raise ValueError("Cargo count must be a positive integer")
            
            pallet_spec = self.pallet_dimensions[cargo_type]
            total_weight = pallet_spec['max_weight'] * cargo_count
            
            return min(total_weight, self.max_payload)
        
        except ValueError as e:
            print(f"Error: {e}")
            return 0.0
    
    def calculate_volume_constraint(self, cargo_type, cargo_count):
        """
        Calculate if cargo exceeds volume capacity.
        
        Args:
            cargo_type (str): Type of cargo pallet (LD3, LD8, LD11)
            cargo_count (int): Number of pallets
            
        Returns:
            bool: True if within volume limits, False otherwise
        """
        try:
            if cargo_type not in self.pallet_dimensions:
                raise ValueError(f"Invalid cargo type. Must be one of: {list(self.pallet_dimensions.keys())}")
            
            pallet_spec = self.pallet_dimensions[cargo_type]
            pallet_volume = pallet_spec['length'] * pallet_spec['width'] * pallet_spec['height']
            total_volume = pallet_volume * cargo_count
            
            return total_volume <= self.max_volume
        
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def calculate_max_cargo(self, cargo_type, cargo_count):
        """
        Calculate maximum cargo considering both weight and volume constraints.
        
        Args:
            cargo_type (str): Type of cargo pallet (LD3, LD8, LD11)
            cargo_count (int): Number of pallets
            
        Returns:
            dict: {
                'max_weight': float,
                'within_volume': bool,
                'weight_constraint': bool,
                'volume_constraint': bool
            }
        """
        try:
            max_weight = self.calculate_max_weight(cargo_type, cargo_count)
            within_volume = self.calculate_volume_constraint(cargo_type, cargo_count)
            
            weight_constraint = max_weight == self.max_payload
            volume_constraint = not within_volume
            
            return {
                'max_weight': max_weight,
                'within_volume': within_volume,
                'weight_constraint': weight_constraint,
                'volume_constraint': volume_constraint
            }
            
        except Exception as e:
            print(f"Error: {e}")
            return {
                'max_weight': 0.0,
                'within_volume': False,
                'weight_constraint': False,
                'volume_constraint': False
            }


# Example usage
if __name__ == "__main__":
    calculator = CargoWeightCalculator()
    
    # Test cases
    test_cases = [
        ('LD3', 10),
        ('LD8', 5),
        ('LD11', 20),
        ('Invalid', 5)
    ]
    
    for cargo_type, count in test_cases:
        print(f"\nTesting {cargo_type} x {count}:")
        result = calculator.calculate_max_cargo(cargo_type, count)
        print(f"Max weight: {result['max_weight']} kg")
        print(f"Within volume: {'Yes' if result['within_volume'] else 'No'}")
        print(f"Weight constraint: {'Yes' if result['weight_constraint'] else 'No'}")
        print(f"Volume constraint: {'Yes' if result['volume_constraint'] else 'No'}")
```
