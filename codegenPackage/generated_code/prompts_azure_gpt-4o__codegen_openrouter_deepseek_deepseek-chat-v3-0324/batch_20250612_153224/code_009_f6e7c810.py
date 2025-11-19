"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: Generate a script to calculate the total cost of multi-day excursions offered by "Rehiletes," including options for destinations like San Miguel de Allende and Veracruz.
Generated: DETERMINISTIC_f6e7c8102fa454ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to calculate the total cost of multi-day excursions offered by "Rehiletes".
Supports destinations: San Miguel de Allende and Veracruz.
"""

class ExcursionCalculator:
    """
    A class to calculate the total cost of multi-day excursions.
    """
    
    def __init__(self):
        """
        Initialize the calculator with destination prices and options.
        """
        self.destinations = {
            'San Miguel de Allende': {
                'base_price': 1500,  # per person per day
                'options': {
                    'guided_tour': 300,
                    'luxury_accommodation': 500,
                    'meal_plan': 200
                }
            },
            'Veracruz': {
                'base_price': 1200,  # per person per day
                'options': {
                    'boat_tour': 400,
                    'beach_resort': 600,
                    'meal_plan': 150
                }
            }
        }
    
    def calculate_cost(self, destination, num_people, num_days, selected_options=None):
        """
        Calculate the total cost for an excursion.
        
        Args:
            destination (str): Destination name (must be in self.destinations)
            num_people (int): Number of people attending (must be > 0)
            num_days (int): Number of days for the excursion (must be > 0)
            selected_options (list): List of optional services to include
            
        Returns:
            float: Total cost of the excursion
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        if selected_options is None:
            selected_options = []
        
        # Validate inputs
        if destination not in self.destinations:
            raise ValueError(f"Invalid destination. Available: {', '.join(self.destinations.keys())}")
        
        if not isinstance(num_people, int) or num_people <= 0:
            raise ValueError("Number of people must be a positive integer")
            
        if not isinstance(num_days, int) or num_days <= 0:
            raise ValueError("Number of days must be a positive integer")
            
        # Get destination info
        dest_info = self.destinations[destination]
        
        # Calculate base cost
        base_cost = dest_info['base_price'] * num_people * num_days
        
        # Calculate options cost
        options_cost = 0
        for option in selected_options:
            if option not in dest_info['options']:
                raise ValueError(f"Invalid option '{option}' for destination {destination}")
            options_cost += dest_info['options'][option] * num_people * num_days
        
        # Calculate total cost
        total_cost = base_cost + options_cost
        
        return total_cost
    
    def get_available_destinations(self):
        """
        Return a list of available destinations.
        """
        return list(self.destinations.keys())
    
    def get_destination_options(self, destination):
        """
        Return available options for a specific destination.
        
        Args:
            destination (str): Destination name
            
        Returns:
            dict: Available options and their prices
            
        Raises:
            ValueError: If destination is invalid
        """
        if destination not in self.destinations:
            raise ValueError(f"Invalid destination. Available: {', '.join(self.destinations.keys())}")
        
        return self.destinations[destination]['options']


def main():
    """
    Main function to demonstrate the ExcursionCalculator.
    """
    calculator = ExcursionCalculator()
    
    print("Welcome to Rehiletes Excursion Calculator")
    print(f"Available destinations: {', '.join(calculator.get_available_destinations())}")
    
    try:
        # Get user input
        destination = input("Enter destination: ")
        num_people = int(input("Enter number of people: "))
        num_days = int(input("Enter number of days: "))
        
        # Show available options
        options = calculator.get_destination_options(destination)
        print("\nAvailable options:")
        for option, price in options.items():
            print(f"- {option}: ${price} per person per day")
        
        # Get selected options
        selected = input("\nEnter desired options (comma separated, leave empty if none): ")
        selected_options = [opt.strip() for opt in selected.split(',')] if selected else []
        
        # Calculate and display total
        total = calculator.calculate_cost(destination, num_people, num_days, selected_options)
        print(f"\nTotal cost for {num_people} people for {num_days} days in {destination}: ${total:,.2f}")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
