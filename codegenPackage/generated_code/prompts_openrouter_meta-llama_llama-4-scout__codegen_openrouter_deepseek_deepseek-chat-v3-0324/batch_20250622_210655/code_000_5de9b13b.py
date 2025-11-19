"""
Generated Code Metadata:
========================
Original URL: https://www.reliableridesllc.org
Prompt: Write a Python script to create a simple car rental system with a fleet of vehicles, including compact, crossover, and SUV options, with prices starting from $45 per day.
Generated: DETERMINISTIC_5de9b13bead180ee
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class Car:
    """Represents a car in the rental system."""
    
    def __init__(self, make: str, model: str, year: int, car_type: str, daily_price: float, available: bool = True):
        """
        Initialize a car with its attributes.
        
        Args:
            make: Manufacturer of the car
            model: Model of the car
            year: Manufacturing year
            car_type: Type of car (compact, crossover, SUV)
            daily_price: Rental price per day
            available: Whether the car is available for rent
        """
        self.make = make
        self.model = model
        self.year = year
        self.car_type = car_type
        self.daily_price = daily_price
        self.available = available
    
    def to_dict(self) -> Dict:
        """Convert car object to dictionary for serialization."""
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'car_type': self.car_type,
            'daily_price': self.daily_price,
            'available': self.available
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Car':
        """Create a car object from dictionary data."""
        return cls(
            make=data['make'],
            model=data['model'],
            year=data['year'],
            car_type=data['car_type'],
            daily_price=data['daily_price'],
            available=data['available']
        )

class RentalSystem:
    """Manages the car rental operations."""
    
    def __init__(self):
        """Initialize the rental system with an empty fleet."""
        self.fleet: List[Car] = []
        self.rentals: Dict[str, Tuple[Car, datetime, datetime]] = {}
    
    def add_car(self, car: Car) -> None:
        """Add a car to the fleet."""
        self.fleet.append(car)
    
    def remove_car(self, car: Car) -> None:
        """Remove a car from the fleet."""
        if car in self.fleet:
            self.fleet.remove(car)
    
    def find_available_cars(self, car_type: Optional[str] = None) -> List[Car]:
        """
        Find available cars optionally filtered by type.
        
        Args:
            car_type: Optional car type filter (compact, crossover, SUV)
        
        Returns:
            List of available cars matching the criteria
        """
        available_cars = [car for car in self.fleet if car.available]
        if car_type:
            available_cars = [car for car in available_cars if car.car_type.lower() == car_type.lower()]
        return available_cars
    
    def rent_car(self, customer_id: str, car: Car, start_date: datetime, end_date: datetime) -> float:
        """
        Rent a car to a customer.
        
        Args:
            customer_id: Unique identifier for the customer
            car: Car to be rented
            start_date: Rental start date
            end_date: Rental end date
        
        Returns:
            Total rental cost
        
        Raises:
            ValueError: If car is not available or dates are invalid
        """
        if not car.available:
            raise ValueError("Car is not available for rent")
        if end_date <= start_date:
            raise ValueError("End date must be after start date")
        
        rental_days = (end_date - start_date).days
        total_cost = car.daily_price * rental_days
        
        car.available = False
        self.rentals[customer_id] = (car, start_date, end_date)
        
        return total_cost
    
    def return_car(self, customer_id: str) -> None:
        """
        Return a rented car.
        
        Args:
            customer_id: Customer ID who rented the car
        
        Raises:
            KeyError: If customer ID is not found in rentals
        """
        if customer_id not in self.rentals:
            raise KeyError("No rental found for this customer ID")
        
        car, _, _ = self.rentals[customer_id]
        car.available = True
        del self.rentals[customer_id]
    
    def save_to_file(self, filename: str) -> None:
        """Save the current fleet and rentals to a JSON file."""
        data = {
            'fleet': [car.to_dict() for car in self.fleet],
            'rentals': {
                customer_id: {
                    'car': car.to_dict(),
                    'start_date': start_date.isoformat(),
                    'end_date': end_date.isoformat()
                }
                for customer_id, (car, start_date, end_date) in self.rentals.items()
            }
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load fleet and rentals from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.fleet = [Car.from_dict(car_data) for car_data in data['fleet']]
        self.rentals = {
            customer_id: (
                Car.from_dict(rental_data['car']),
                datetime.fromisoformat(rental_data['start_date']),
                datetime.fromisoformat(rental_data['end_date'])
            )
            for customer_id, rental_data in data.get('rentals', {}).items()
        }

def initialize_sample_system() -> RentalSystem:
    """Initialize a rental system with sample data."""
    system = RentalSystem()
    
    # Add compact cars
    system.add_car(Car("Toyota", "Corolla", 2022, "compact", 45.00))
    system.add_car(Car("Honda", "Civic", 2023, "compact", 48.00))
    
    # Add crossover cars
    system.add_car(Car("Toyota", "RAV4", 2022, "crossover", 65.00))
    system.add_car(Car("Honda", "CR-V", 2023, "crossover", 68.00))
    
    # Add SUVs
    system.add_car(Car("Ford", "Explorer", 2022, "SUV", 85.00))
    system.add_car(Car("Chevrolet", "Tahoe", 2023, "SUV", 95.00))
    
    return system

def main():
    """Main function to demonstrate the rental system."""
    system = initialize_sample_system()
    
    # Display available cars
    print("Available Cars:")
    for car in system.find_available_cars():
        print(f"{car.year} {car.make} {car.model} ({car.car_type}) - ${car.daily_price}/day")
    
    # Rent a car
    customer_id = "cust123"
    available_cars = system.find_available_cars("compact")
    if available_cars:
        car_to_rent = available_cars[0]
        start_date = datetime.now()
        end_date = start_date + timedelta(days=3)
        
        try:
            total_cost = system.rent_car(customer_id, car_to_rent, start_date, end_date)
            print(f"\nRented {car_to_rent.make} {car_to_rent.model} for 3 days. Total cost: ${total_cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Return the car
    try:
        system.return_car(customer_id)
        print("\nCar returned successfully.")
    except KeyError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
