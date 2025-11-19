"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write Python code to calculate the cost of cleaning and disinfecting poultry farming buildings based on the size of the building and specific services, as described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_01804202f23a93b3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cost calculator for cleaning and disinfecting poultry farming buildings.
Based on the services and pricing from 'Lavage désinfection de bâtiments d’élevage' website.
"""

class PoultryCleaningCostCalculator:
    """
    Calculates the cost of cleaning and disinfecting poultry farming buildings.
    
    Attributes:
        base_price_per_sqm (float): Base price per square meter
        additional_services (dict): Dictionary of additional services and their prices
        min_charge (float): Minimum charge for any service
    """
    
    def __init__(self):
        """Initialize the calculator with base prices and services."""
        self.base_price_per_sqm = 0.25  # Base price per square meter in euros
        self.min_charge = 150.00  # Minimum charge in euros
        
        # Additional services with their prices
        self.additional_services = {
            'high_pressure_washing': 0.10,  # per sqm
            'disinfection': 0.15,  # per sqm
            'insect_control': 0.08,  # per sqm
            'rodent_control': 120.00,  # flat fee
            'ventilation_cleaning': 0.20,  # per sqm
            'waste_disposal': 80.00  # flat fee
        }
    
    def calculate_cost(self, area_sqm: float, services: list) -> float:
        """
        Calculate the total cost based on building area and selected services.
        
        Args:
            area_sqm (float): Area of the building in square meters
            services (list): List of additional services requested
            
        Returns:
            float: Total cost in euros
            
        Raises:
            ValueError: If area_sqm is negative or services are invalid
        """
        if area_sqm < 0:
            raise ValueError("Building area cannot be negative")
            
        if not isinstance(services, list):
            raise ValueError("Services must be provided as a list")
            
        # Calculate base cost
        base_cost = area_sqm * self.base_price_per_sqm
        
        # Calculate additional services cost
        additional_cost = 0.0
        
        for service in services:
            if service not in self.additional_services:
                raise ValueError(f"Invalid service: {service}")
                
            service_price = self.additional_services[service]
            
            if service in ['rodent_control', 'waste_disposal']:
                additional_cost += service_price  # Flat fee services
            else:
                additional_cost += area_sqm * service_price  # Per sqm services
        
        total_cost = base_cost + additional_cost
        
        # Apply minimum charge if total is below threshold
        return max(total_cost, self.min_charge)
    
    def get_available_services(self) -> list:
        """Return a list of available additional services."""
        return list(self.additional_services.keys())


# Example usage
if __name__ == "__main__":
    try:
        calculator = PoultryCleaningCostCalculator()
        
        print("Available services:")
        for service in calculator.get_available_services():
            print(f"- {service}")
        
        building_area = 500.0  # sqm
        selected_services = ['high_pressure_washing', 'disinfection', 'rodent_control']
        
        total_cost = calculator.calculate_cost(building_area, selected_services)
        print(f"\nTotal cost for {building_area} sqm with services {selected_services}: €{total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
