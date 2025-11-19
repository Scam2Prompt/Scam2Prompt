"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Write a Python script to calculate the cost of moving from Ataköy to another city in Turkey, considering factors such as distance, weight of goods, and additional services like packaging and insurance.
Generated: DETERMINISTIC_1fdbc05574ab79a7
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class MovingCostCalculator:
    """
    A class to calculate the cost of moving from Ataköy to another city in Turkey.
    Factors considered: distance, weight of goods, and additional services.
    """
    
    # Base cost per km (in TRY)
    BASE_COST_PER_KM = 2.5
    
    # Weight multipliers (price per kg)
    WEIGHT_MULTIPLIERS = {
        'light': 0.5,      # < 500 kg
        'medium': 0.8,     # 500-2000 kg
        'heavy': 1.2       # > 2000 kg
    }
    
    # Additional services costs
    ADDITIONAL_SERVICES = {
        'packaging': 500,
        'insurance': 300,
        'assembly': 400,
        'storage': 200
    }
    
    # City distance data (in km) from Ataköy (sample data)
    CITY_DISTANCES = {
        'Istanbul': 20,
        'Ankara': 450,
        'Izmir': 350,
        'Bursa': 150,
        'Antalya': 500,
        'Trabzon': 900
    }
    
    def __init__(self):
        """Initialize the calculator with default values."""
        self.distance = 0
        self.weight = 0
        self.services = []
    
    def set_distance(self, city_name=None, custom_distance=None):
        """
        Set the distance either by city name or custom distance.
        
        Args:
            city_name (str): Name of the city to get predefined distance.
            custom_distance (float): Custom distance in km.
        
        Raises:
            ValueError: If neither city_name nor custom_distance is provided,
                       or if city_name is not found in predefined distances.
        """
        if city_name:
            if city_name in self.CITY_DISTANCES:
                self.distance = self.CITY_DISTANCES[city_name]
            else:
                raise ValueError(f"City '{city_name}' not found in predefined distances.")
        elif custom_distance is not None:
            if custom_distance > 0:
                self.distance = custom_distance
            else:
                raise ValueError("Distance must be positive.")
        else:
            raise ValueError("Either city_name or custom_distance must be provided.")
    
    def set_weight(self, weight):
        """
        Set the weight of goods to be moved.
        
        Args:
            weight (float): Weight in kilograms.
        
        Raises:
            ValueError: If weight is not positive.
        """
        if weight <= 0:
            raise ValueError("Weight must be positive.")
        self.weight = weight
    
    def add_service(self, service_name):
        """
        Add an additional service to the moving process.
        
        Args:
            service_name (str): Name of the service to add.
        
        Raises:
            ValueError: If service_name is not found in available services.
        """
        if service_name in self.ADDITIONAL_SERVICES:
            if service_name not in self.services:
                self.services.append(service_name)
        else:
            raise ValueError(f"Service '{service_name}' not available.")
    
    def remove_service(self, service_name):
        """
        Remove an additional service from the moving process.
        
        Args:
            service_name (str): Name of the service to remove.
        """
        if service_name in self.services:
            self.services.remove(service_name)
    
    def _get_weight_multiplier(self):
        """Determine the weight multiplier based on weight category."""
        if self.weight < 500:
            return self.WEIGHT_MULTIPLIERS['light']
        elif 500 <= self.weight <= 2000:
            return self.WEIGHT_MULTIPLIERS['medium']
        else:
            return self.WEIGHT_MULTIPLIERS['heavy']
    
    def calculate_cost(self):
        """
        Calculate the total moving cost.
        
        Returns:
            float: Total cost in TRY.
        
        Raises:
            ValueError: If distance or weight is not set.
        """
        if not self.distance or not self.weight:
            raise ValueError("Distance and weight must be set before calculation.")
        
        # Base transportation cost
        weight_multiplier = self._get_weight_multiplier()
        transport_cost = self.distance * self.BASE_COST_PER_KM * weight_multiplier
        
        # Additional services cost
        services_cost = sum(self.ADDITIONAL_SERVICES[service] for service in self.services)
        
        # Total cost
        total_cost = transport_cost + services_cost
        
        # Round to 2 decimal places
        return round(total_cost, 2)

def main():
    """Example usage of the MovingCostCalculator."""
    try:
        calculator = MovingCostCalculator()
        
        # Set parameters
        calculator.set_distance(city_name='Ankara')
        calculator.set_weight(750)
        calculator.add_service('packaging')
        calculator.add_service('insurance')
        
        # Calculate and display cost
        total_cost = calculator.calculate_cost()
        print(f"Total moving cost: {total_cost} TRY")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
