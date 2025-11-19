"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write code to calculate the cost of multiple cleaning services (e.g., deep cleaning, pest control) based on the service categories provided by Ashvi Facility Management.
Generated: DETERMINISTIC_7191bfb4cec1e492
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CleaningServiceCalculator:
    """
    A class to calculate the cost of various cleaning services provided by Ashvi Facility Management.
    """
    
    def __init__(self):
        """
        Initialize the service categories and their base prices.
        """
        self.service_prices = {
            'deep_cleaning': {
                'small': 150,
                'medium': 250,
                'large': 400
            },
            'regular_cleaning': {
                'small': 100,
                'medium': 180,
                'large': 300
            },
            'pest_control': {
                'small': 200,
                'medium': 350,
                'large': 500
            },
            'window_cleaning': {
                'small': 80,
                'medium': 150,
                'large': 250
            },
            'carpet_cleaning': {
                'small': 120,
                'medium': 220,
                'large': 350
            }
        }
    
    def calculate_cost(self, service_type: str, property_size: str, frequency: int = 1) -> float:
        """
        Calculate the total cost for a cleaning service.
        
        Args:
            service_type (str): Type of cleaning service (e.g., 'deep_cleaning')
            property_size (str): Size of property ('small', 'medium', 'large')
            frequency (int): Number of times service is requested (default: 1)
            
        Returns:
            float: Total cost for the service
            
        Raises:
            ValueError: If service_type or property_size is invalid
        """
        if service_type not in self.service_prices:
            raise ValueError(f"Invalid service type: {service_type}")
        
        if property_size not in ['small', 'medium', 'large']:
            raise ValueError(f"Invalid property size: {property_size}")
        
        if frequency <= 0:
            raise ValueError("Frequency must be a positive integer")
        
        base_price = self.service_prices[service_type][property_size]
        total_cost = base_price * frequency
        
        return total_cost
    
    def calculate_multiple_services(self, services: list) -> float:
        """
        Calculate the total cost for multiple cleaning services.
        
        Args:
            services (list): List of dictionaries containing service details
                Each dictionary should have:
                - 'service_type': str
                - 'property_size': str
                - 'frequency': int (optional, default: 1)
                
        Returns:
            float: Total cost for all services
            
        Raises:
            ValueError: If any service details are invalid
        """
        total_cost = 0.0
        
        for service in services:
            service_type = service.get('service_type')
            property_size = service.get('property_size')
            frequency = service.get('frequency', 1)
            
            if not service_type or not property_size:
                raise ValueError("Each service must include 'service_type' and 'property_size'")
            
            total_cost += self.calculate_cost(service_type, property_size, frequency)
        
        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = CleaningServiceCalculator()
    
    # Single service calculation
    try:
        cost = calculator.calculate_cost('deep_cleaning', 'medium')
        print(f"Single service cost: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Multiple services calculation
    services = [
        {'service_type': 'deep_cleaning', 'property_size': 'medium', 'frequency': 2},
        {'service_type': 'pest_control', 'property_size': 'small'},
        {'service_type': 'window_cleaning', 'property_size': 'large', 'frequency': 3}
    ]
    
    try:
        total_cost = calculator.calculate_multiple_services(services)
        print(f"Total cost for multiple services: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
