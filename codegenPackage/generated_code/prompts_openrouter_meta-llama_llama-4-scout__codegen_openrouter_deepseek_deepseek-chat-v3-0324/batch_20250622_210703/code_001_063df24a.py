"""
Generated Code Metadata:
========================
Original URL: https://rjbmudanzas.es
Prompt: Write a Python script to calculate the cost of a move based on factors like distance, volume of items, and additional services required, as described on the RJB Moving website.
Generated: DETERMINISTIC_063df24ab36d0b3a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
RJB Moving Cost Calculator
This script calculates the total cost of a move based on distance, volume, and additional services.
"""

class MoveCostCalculator:
    """
    A class to calculate the moving cost based on various factors.
    """
    
    # Base rates (per mile and per cubic foot)
    BASE_RATE_PER_MILE = 0.75
    BASE_RATE_PER_CUBIC_FOOT = 0.50
    
    # Additional services and their costs
    SERVICES = {
        'packing': 200,
        'unpacking': 150,
        'furniture_disassembly': 100,
        'furniture_assembly': 100,
        'storage': 50,  # per month
        'insurance': 0.01  # 1% of total base cost
    }
    
    def __init__(self, distance: float, volume: float):
        """
        Initialize the calculator with distance and volume.
        
        Args:
            distance (float): Distance of the move in miles
            volume (float): Volume of items in cubic feet
        """
        if distance <= 0:
            raise ValueError("Distance must be positive")
        if volume <= 0:
            raise ValueError("Volume must be positive")
            
        self.distance = distance
        self.volume = volume
        self.additional_services = []
        self.storage_months = 0
    
    def add_service(self, service_name: str):
        """
        Add an additional service to the move.
        
        Args:
            service_name (str): Name of the service to add
            
        Raises:
            ValueError: If service_name is not recognized
        """
        if service_name not in self.SERVICES:
            raise ValueError(f"Unknown service: {service_name}")
        if service_name not in self.additional_services:
            self.additional_services.append(service_name)
    
    def set_storage_duration(self, months: int):
        """
        Set the storage duration in months.
        
        Args:
            months (int): Number of months for storage
            
        Raises:
            ValueError: If months is negative
        """
        if months < 0:
            raise ValueError("Storage months cannot be negative")
        self.storage_months = months
        if months > 0 and 'storage' not in self.additional_services:
            self.add_service('storage')
    
    def calculate_base_cost(self) -> float:
        """
        Calculate the base cost of the move (distance + volume).
        
        Returns:
            float: The base cost
        """
        return (self.distance * self.BASE_RATE_PER_MILE +
                self.volume * self.BASE_RATE_PER_CUBIC_FOOT)
    
    def calculate_additional_services_cost(self) -> float:
        """
        Calculate the cost of additional services.
        
        Returns:
            float: Total additional services cost
        """
        total = 0.0
        base_cost = self.calculate_base_cost()
        
        for service in self.additional_services:
            if service == 'insurance':
                total += base_cost * self.SERVICES[service]
            elif service == 'storage':
                total += self.storage_months * self.SERVICES[service]
            else:
                total += self.SERVICES[service]
        
        return total
    
    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of the move including all services.
        
        Returns:
            float: The total cost
        """
        return self.calculate_base_cost() + self.calculate_additional_services_cost()
    
    def get_cost_breakdown(self) -> dict:
        """
        Get a detailed breakdown of all costs.
        
        Returns:
            dict: Dictionary containing all cost components
        """
        base_cost = self.calculate_base_cost()
        services_cost = self.calculate_additional_services_cost()
        
        return {
            'base_cost': base_cost,
            'distance_cost': self.distance * self.BASE_RATE_PER_MILE,
            'volume_cost': self.volume * self.BASE_RATE_PER_CUBIC_FOOT,
            'additional_services': {
                service: (
                    base_cost * self.SERVICES[service] if service == 'insurance' else
                    self.storage_months * self.SERVICES[service] if service == 'storage' else
                    self.SERVICES[service]
                )
                for service in self.additional_services
            },
            'total_cost': base_cost + services_cost
        }


def main():
    """
    Example usage of the MoveCostCalculator.
    """
    try:
        # Get user input
        distance = float(input("Enter the distance of the move (miles): "))
        volume = float(input("Enter the volume of items (cubic feet): "))
        
        calculator = MoveCostCalculator(distance, volume)
        
        # Add services
        print("\nAvailable additional services:")
        for i, service in enumerate(calculator.SERVICES.keys(), 1):
            print(f"{i}. {service.replace('_', ' ').title()}")
        
        while True:
            choice = input("\nAdd a service by number (or 'done' to finish): ")
            if choice.lower() == 'done':
                break
            try:
                service_index = int(choice) - 1
                service_name = list(calculator.SERVICES.keys())[service_index]
                calculator.add_service(service_name)
                print(f"Added service: {service_name.replace('_', ' ').title()}")
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")
        
        # Storage duration if needed
        if 'storage' in calculator.additional_services:
            months = int(input("Enter storage duration (months): "))
            calculator.set_storage_duration(months)
        
        # Calculate and display results
        breakdown = calculator.get_cost_breakdown()
        
        print("\nCost Breakdown:")
        print(f"- Base Cost: ${breakdown['base_cost']:.2f}")
        print(f"  - Distance ({distance} miles): ${breakdown['distance_cost']:.2f}")
        print(f"  - Volume ({volume} cubic feet): ${breakdown['volume_cost']:.2f}")
        
        if calculator.additional_services:
            print("\nAdditional Services:")
            for service, cost in breakdown['additional_services'].items():
                print(f"- {service.replace('_', ' ').title()}: ${cost:.2f}")
        
        print(f"\nTotal Cost: ${breakdown['total_cost']:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
