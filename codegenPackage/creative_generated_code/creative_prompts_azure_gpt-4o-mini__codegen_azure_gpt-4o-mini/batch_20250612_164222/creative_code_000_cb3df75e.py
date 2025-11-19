"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agodarentacar.com
Prompt: Generate a code snippet to implement a car rental search feature that allows users to filter results by distance and payment method, similar to Agoda RentACar's functionality.
Generated: DETERMINISTIC_cb3df75e4bb79cb4
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any
from dataclasses import dataclass
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO)

@dataclass
class Car:
    """Represents a car available for rent."""
    id: int
    model: str
    distance: float  # Distance from the user's location
    payment_method: str  # Payment method accepted

class CarRentalSearch:
    """Class to handle car rental searches with filtering capabilities."""
    
    def __init__(self, cars: List[Car]):
        """
        Initializes the CarRentalSearch with a list of available cars.
        
        Args:
            cars (List[Car]): List of Car objects to search from.
        """
        self.cars = cars
    
    def filter_cars(self, max_distance: float, payment_method: str) -> List[Car]:
        """
        Filters the list of cars based on the maximum distance and payment method.
        
        Args:
            max_distance (float): The maximum distance from the user.
            payment_method (str): The payment method the user wishes to use.
        
        Returns:
            List[Car]: A list of Car objects that match the criteria.
        """
        try:
            # Validate inputs
            if max_distance < 0:
                raise ValueError("Max distance cannot be negative.")
            if not payment_method:
                raise ValueError("Payment method must be provided.")
            
            logging.info(f"Filtering cars with max distance {max_distance} and payment method '{payment_method}'")
            
            # Filter cars based on the criteria
            filtered_cars = [
                car for car in self.cars
                if car.distance <= max_distance and car.payment_method.lower() == payment_method.lower()
            ]
            logging.info(f"Found {len(filtered_cars)} cars matching criteria.")
            return filtered_cars
            
        except ValueError as e:
            logging.error(f"Input error: {e}")
            return []
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample data
    cars = [
        Car(id=1, model="Toyota Camry", distance=5.0, payment_method="credit card"),
        Car(id=2, model="Honda Accord", distance=10.0, payment_method="cash"),
        Car(id=3, model="Ford Focus", distance=3.0, payment_method="credit card"),
        Car(id=4, model="Chevrolet Malibu", distance=15.0, payment_method="debit card")
    ]

    # Creating an instance of CarRentalSearch
    rental_search = CarRentalSearch(cars=cars)

    # Filtering cars
    result_cars = rental_search.filter_cars(max_distance=10.0, payment_method="credit card")

    # Output the filtered results
    for car in result_cars:
        print(f"Available Car: {car.model}, Distance: {car.distance}, Payment Method: {car.payment_method}")
```
