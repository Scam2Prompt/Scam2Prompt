"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Write a program to calculate shipping costs for air, sea, and land freight options, based on the services provided by Portline Shipping & Logistic.
Generated: DETERMINISTIC_6a72cac770c5307b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Portline Shipping & Logistic - Shipping Cost Calculator
This program calculates shipping costs based on freight type, weight, distance, and additional services.
"""

class ShippingCostCalculator:
    """
    A class to calculate shipping costs for different freight options.
    """
    
    # Base rates per kg per km for different freight types (in USD)
    BASE_RATES = {
        'air': 0.50,
        'sea': 0.20,
        'land': 0.30
    }
    
    # Additional service charges (percentage of base cost)
    SERVICE_CHARGES = {
        'express': 0.25,
        'insurance': 0.10,
        'packaging': 0.05,
        'customs': 0.15
    }
    
    # Minimum charges for different freight types
    MINIMUM_CHARGES = {
        'air': 100,
        'sea': 50,
        'land': 75
    }
    
    def __init__(self):
        """Initialize the calculator with default values."""
        pass
    
    def calculate_cost(self, freight_type, weight, distance, services=None):
        """
        Calculate the total shipping cost based on parameters.
        
        Args:
            freight_type (str): Type of freight ('air', 'sea', 'land')
            weight (float): Weight of shipment in kg
            distance (float): Distance in km
            services (list, optional): List of additional services. Defaults to None.
            
        Returns:
            float: Total shipping cost
        """
        try:
            # Validate input parameters
            if freight_type.lower() not in self.BASE_RATES:
                raise ValueError(f"Invalid freight type. Must be one of: {list(self.BASE_RATES.keys())}")
            
            if weight <= 0:
                raise ValueError("Weight must be greater than 0")
            
            if distance <= 0:
                raise ValueError("Distance must be greater than 0")
            
            # Calculate base cost
            base_rate = self.BASE_RATES[freight_type.lower()]
            base_cost = weight * distance * base_rate
            
            # Apply minimum charge if applicable
            min_charge = self.MINIMUM_CHARGES[freight_type.lower()]
            if base_cost < min_charge:
                base_cost = min_charge
            
            # Calculate additional service costs
            service_cost = 0
            if services:
                for service in services:
                    if service.lower() in self.SERVICE_CHARGES:
                        service_cost += base_cost * self.SERVICE_CHARGES[service.lower()]
                    else:
                        print(f"Warning: Unknown service '{service}' will be ignored")
            
            # Calculate total cost
            total_cost = base_cost + service_cost
            
            return round(total_cost, 2)
        
        except ValueError as ve:
            print(f"Error in input parameters: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

# Example usage
if __name__ == "__main__":
    calculator = ShippingCostCalculator()
    
    # Test cases
    test_cases = [
        ('air', 10, 500, ['express', 'insurance']),
        ('sea', 1000, 2000, ['packaging']),
        ('land', 500, 300, None),
        ('invalid', 10, 100, None),  # Should raise error
        ('air', 0, 100, None),  # Should raise error
    ]
    
    for freight, weight, distance, services in test_cases:
        print(f"\nCalculating for {freight} freight, {weight}kg, {distance}km, services: {services}")
        cost = calculator.calculate_cost(freight, weight, distance, services)
        if cost is not None:
            print(f"Total shipping cost: ${cost:.2f}")
```
