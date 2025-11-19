"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Develop a Python script to calculate shipping costs for furniture products from "moveisonlinepelotasbraz," based on product dimensions and weight for items like "Cômoda Infantil."
Generated: DETERMINISTIC_4408c94e610ae793
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ShippingCalculator:
    """
    A class to calculate shipping costs for furniture products based on dimensions and weight.
    
    Attributes:
        base_rate (float): Base shipping rate in BRL.
        weight_rate (float): Rate per kilogram in BRL.
        volumetric_rate (float): Rate per cubic meter in BRL.
        max_weight (float): Maximum allowed weight in kg.
        max_volume (float): Maximum allowed volume in cubic meters.
    """
    
    def __init__(self):
        """Initialize the ShippingCalculator with default rates and limits."""
        self.base_rate = 50.0  # BRL
        self.weight_rate = 10.0  # BRL per kg
        self.volumetric_rate = 100.0  # BRL per cubic meter
        self.max_weight = 50.0  # kg
        self.max_volume = 2.0  # cubic meters
    
    def calculate_volumetric_weight(self, length, width, height):
        """
        Calculate the volumetric weight based on dimensions.
        
        Args:
            length (float): Length in meters.
            width (float): Width in meters.
            height (float): Height in meters.
            
        Returns:
            float: Volumetric weight in kg.
        """
        return (length * width * height) * 250  # 250 kg per cubic meter
    
    def calculate_shipping_cost(self, weight, length, width, height):
        """
        Calculate the total shipping cost based on weight and dimensions.
        
        Args:
            weight (float): Actual weight in kg.
            length (float): Length in meters.
            width (float): Width in meters.
            height (float): Height in meters.
            
        Returns:
            float: Total shipping cost in BRL.
            
        Raises:
            ValueError: If weight or dimensions exceed maximum limits.
        """
        # Validate inputs
        if weight <= 0 or length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Weight and dimensions must be positive values.")
        
        if weight > self.max_weight:
            raise ValueError(f"Weight exceeds maximum limit of {self.max_weight} kg.")
        
        volume = length * width * height
        if volume > self.max_volume:
            raise ValueError(f"Volume exceeds maximum limit of {self.max_volume} cubic meters.")
        
        # Calculate volumetric weight
        volumetric_weight = self.calculate_volumetric_weight(length, width, height)
        
        # Use the greater of actual weight or volumetric weight
        chargeable_weight = max(weight, volumetric_weight)
        
        # Calculate cost
        cost = self.base_rate + (chargeable_weight * self.weight_rate) + (volume * self.volumetric_rate)
        
        return round(cost, 2)

# Example usage
if __name__ == "__main__":
    calculator = ShippingCalculator()
    
    try:
        # Example: Cômoda Infantil
        weight = 15.0  # kg
        length = 0.8  # meters
        width = 0.5  # meters
        height = 0.6  # meters
        
        cost = calculator.calculate_shipping_cost(weight, length, width, height)
        print(f"Shipping cost: R${cost}")
    
    except ValueError as e:
        print(f"Error calculating shipping cost: {e}")
```
