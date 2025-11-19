"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Generate code to calculate the cost of car repair services based on service type (e.g., oil change, brake repair) and car brand, using a predefined pricing structure.
Generated: DETERMINISTIC_466c365664e0f0b9
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CarRepairCostCalculator:
    """
    A class to calculate the cost of car repair services based on service type and car brand.
    Uses a predefined pricing structure with base prices and brand multipliers.
    """
    
    def __init__(self):
        # Base prices for services (in USD)
        self.base_prices = {
            'oil_change': 50,
            'brake_repair': 120,
            'tire_rotation': 40,
            'battery_replacement': 100,
            'engine_diagnostic': 80
        }
        
        # Brand multipliers (applied to base price)
        self.brand_multipliers = {
            'toyota': 1.0,
            'honda': 1.0,
            'ford': 1.1,
            'chevrolet': 1.1,
            'bmw': 1.5,
            'mercedes': 1.6,
            'audi': 1.4,
            'lexus': 1.3
        }
    
    def calculate_cost(self, service_type: str, car_brand: str) -> float:
        """
        Calculate the total cost for a given service and car brand.
        
        Args:
            service_type: Type of service (e.g., 'oil_change')
            car_brand: Car brand (e.g., 'toyota')
            
        Returns:
            float: Total cost after applying brand multiplier
            
        Raises:
            ValueError: If service_type or car_brand is not found in pricing structure
        """
        try:
            base_price = self.base_prices[service_type.lower()]
        except KeyError:
            raise ValueError(f"Service type '{service_type}' not found in pricing structure")
        
        try:
            multiplier = self.brand_multipliers[car_brand.lower()]
        except KeyError:
            raise ValueError(f"Car brand '{car_brand}' not found in pricing structure")
        
        total_cost = base_price * multiplier
        return round(total_cost, 2)
    
    def get_available_services(self) -> list:
        """Return list of available service types"""
        return list(self.base_prices.keys())
    
    def get_supported_brands(self) -> list:
        """Return list of supported car brands"""
        return list(self.brand_multipliers.keys())


# Example usage
if __name__ == "__main__":
    calculator = CarRepairCostCalculator()
    
    try:
        service = 'oil_change'
        brand = 'bmw'
        cost = calculator.calculate_cost(service, brand)
        print(f"Cost for {service} on a {brand}: ${cost}")
        
        # Uncomment to test error handling
        # cost = calculator.calculate_cost('invalid_service', 'toyota')
    except ValueError as e:
        print(f"Error: {e}")
```
