"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: Write a Python script to calculate the monthly renting cost for a vehicle based on the principles described by Innova Renting, including maintenance, insurance, and other expenses.
Generated: DETERMINISTIC_12bde535107da4b0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Optional, Dict, List

@dataclass
class Vehicle:
    """Represents a vehicle with its rental-related attributes."""
    name: str
    base_price: float  # Base rental price per month
    insurance_rate: float  # Insurance cost as a percentage of base price
    maintenance_rate: float  # Maintenance cost as a percentage of base price
    other_expenses: float  # Fixed other expenses per month

@dataclass
class RentalCalculation:
    """Stores the results of a rental cost calculation."""
    vehicle_name: str
    base_price: float
    insurance_cost: float
    maintenance_cost: float
    other_expenses: float
    total_cost: float

class VehicleRentalCalculator:
    """Calculates the monthly renting cost for a vehicle including all expenses."""
    
    def __init__(self, vehicles: List[Vehicle]):
        """Initialize with a list of available vehicles."""
        self.vehicles = {vehicle.name: vehicle for vehicle in vehicles}
    
    def calculate_monthly_cost(self, vehicle_name: str) -> Optional[RentalCalculation]:
        """
        Calculate the total monthly rental cost for a given vehicle.
        
        Args:
            vehicle_name: Name of the vehicle to calculate costs for.
            
        Returns:
            RentalCalculation object with detailed costs, or None if vehicle not found.
        """
        vehicle = self.vehicles.get(vehicle_name)
        if not vehicle:
            return None
        
        insurance_cost = vehicle.base_price * (vehicle.insurance_rate / 100)
        maintenance_cost = vehicle.base_price * (vehicle.maintenance_rate / 100)
        total_cost = vehicle.base_price + insurance_cost + maintenance_cost + vehicle.other_expenses
        
        return RentalCalculation(
            vehicle_name=vehicle.name,
            base_price=vehicle.base_price,
            insurance_cost=insurance_cost,
            maintenance_cost=maintenance_cost,
            other_expenses=vehicle.other_expenses,
            total_cost=total_cost
        )
    
    def get_available_vehicles(self) -> List[str]:
        """Return a list of available vehicle names."""
        return list(self.vehicles.keys())

def load_vehicles_from_file(file_path: str) -> List[Vehicle]:
    """
    Load vehicle data from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing vehicle data.
        
    Returns:
        List of Vehicle objects.
        
    Raises:
        FileNotFoundError: If the file doesn't exist.
        json.JSONDecodeError: If the file contains invalid JSON.
        KeyError: If required fields are missing in the JSON data.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    vehicles = []
    for item in data['vehicles']:
        vehicle = Vehicle(
            name=item['name'],
            base_price=item['base_price'],
            insurance_rate=item['insurance_rate'],
            maintenance_rate=item['maintenance_rate'],
            other_expenses=item['other_expenses']
        )
        vehicles.append(vehicle)
    
    return vehicles

def main():
    """Main function to demonstrate the rental cost calculation."""
    try:
        # Load vehicle data from file
        vehicles = load_vehicles_from_file('vehicles.json')
        calculator = VehicleRentalCalculator(vehicles)
        
        # Display available vehicles
        print("Available vehicles:")
        for vehicle_name in calculator.get_available_vehicles():
            print(f"- {vehicle_name}")
        
        # Get user input
        selected_vehicle = input("\nEnter vehicle name to calculate monthly cost: ")
        
        # Calculate and display results
        calculation = calculator.calculate_monthly_cost(selected_vehicle)
        if calculation:
            print("\nMonthly Rental Cost Breakdown:")
            print(f"Vehicle: {calculation.vehicle_name}")
            print(f"Base Price: ${calculation.base_price:.2f}")
            print(f"Insurance: ${calculation.insurance_cost:.2f}")
            print(f"Maintenance: ${calculation.maintenance_cost:.2f}")
            print(f"Other Expenses: ${calculation.other_expenses:.2f}")
            print(f"Total Monthly Cost: ${calculation.total_cost:.2f}")
        else:
            print("Error: Vehicle not found.")
    
    except FileNotFoundError:
        print("Error: vehicles.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in vehicles.json.")
    except KeyError as e:
        print(f"Error: Missing required field in vehicles.json - {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
