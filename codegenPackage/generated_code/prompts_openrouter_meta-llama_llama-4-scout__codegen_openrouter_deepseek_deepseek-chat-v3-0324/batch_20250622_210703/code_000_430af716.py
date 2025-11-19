"""
Generated Code Metadata:
========================
Original URL: https://dextranslogistics.com
Prompt: "Write a Python code snippet to calculate the cost of shipping a container from India to a global destination using air freight or sea freight services."
Generated: DETERMINISTIC_430af7163f20adbc
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

class ShippingCostCalculator:
    """
    A class to calculate shipping costs for air and sea freight from India to global destinations.
    """
    
    def __init__(self):
        # Base rates in USD (per kg for air, per container for sea)
        self.air_freight_rates = {
            'North America': 5.50,
            'Europe': 4.75,
            'Asia': 3.25,
            'Africa': 6.00,
            'South America': 7.25,
            'Australia': 5.00
        }
        
        self.sea_freight_rates = {
            'North America': 2500,
            'Europe': 2200,
            'Asia': 1800,
            'Africa': 3000,
            'South America': 3500,
            'Australia': 2800
        }
        
        # Additional charges
        self.fuel_surcharge = 0.15  # 15% of base rate
        self.customs_clearance = 150  # Flat fee in USD
        self.insurance_rate = 0.01  # 1% of cargo value
        
    def calculate_air_freight(self, destination: str, weight_kg: float, cargo_value: float = 0) -> float:
        """
        Calculate total air freight cost.
        
        Args:
            destination: Destination region
            weight_kg: Weight of cargo in kilograms
            cargo_value: Value of cargo for insurance (optional)
            
        Returns:
            Total cost in USD
            
        Raises:
            ValueError: If destination is invalid or weight is <= 0
        """
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than 0 kg")
            
        if destination not in self.air_freight_rates:
            raise ValueError(f"Invalid destination. Available options: {list(self.air_freight_rates.keys())}")
            
        base_rate = self.air_freight_rates[destination]
        fuel_charge = base_rate * self.fuel_surcharge
        insurance = cargo_value * self.insurance_rate
        
        total_cost = (base_rate + fuel_charge) * weight_kg + self.customs_clearance + insurance
        return round(total_cost, 2)
    
    def calculate_sea_freight(self, destination: str, container_size: str, cargo_value: float = 0) -> float:
        """
        Calculate total sea freight cost.
        
        Args:
            destination: Destination region
            container_size: '20ft' or '40ft'
            cargo_value: Value of cargo for insurance (optional)
            
        Returns:
            Total cost in USD
            
        Raises:
            ValueError: If destination or container size is invalid
        """
        if destination not in self.sea_freight_rates:
            raise ValueError(f"Invalid destination. Available options: {list(self.sea_freight_rates.keys())}")
            
        if container_size not in ['20ft', '40ft']:
            raise ValueError("Container size must be either '20ft' or '40ft'")
            
        base_rate = self.sea_freight_rates[destination]
        # 40ft containers cost 1.7x more than 20ft
        size_multiplier = 1.7 if container_size == '40ft' else 1.0
        fuel_charge = base_rate * self.fuel_surcharge
        insurance = cargo_value * self.insurance_rate
        
        total_cost = (base_rate + fuel_charge) * size_multiplier + self.customs_clearance + insurance
        return round(total_cost, 2)
    
    def get_available_destinations(self) -> list:
        """Return list of available destination regions"""
        return list(self.air_freight_rates.keys())


# Example usage
if __name__ == "__main__":
    try:
        calculator = ShippingCostCalculator()
        
        # Air freight example
        air_cost = calculator.calculate_air_freight('Europe', 150, 5000)
        print(f"Air freight cost: ${air_cost}")
        
        # Sea freight example
        sea_cost = calculator.calculate_sea_freight('North America', '40ft', 25000)
        print(f"Sea freight cost: ${sea_cost}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
