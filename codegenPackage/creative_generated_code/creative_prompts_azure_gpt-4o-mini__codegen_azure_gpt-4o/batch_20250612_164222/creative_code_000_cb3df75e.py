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
# Import necessary modules
import math
from typing import List, Dict, Union

class CarRental:
    def __init__(self, name: str, distance: float, payment_methods: List[str]):
        """
        Initialize a CarRental object.

        Args:
            name (str): The name of the car rental service.
            distance (float): The distance of the car rental service from the user's location (in km).
            payment_methods (List[str]): Supported payment methods for the car rental service.
        """
        self.name = name
        self.distance = distance
        self.payment_methods = payment_methods


def search_car_rentals(
    rentals: List[CarRental], 
    max_distance: float, 
    preferred_payment_method: str
) -> List[Dict[str, Union[str, float]]]:
    """
    Searches for car rental options based on distance and payment method.

    Args:
        rentals (List[CarRental]): List of CarRental objects to search from.
        max_distance (float): Maximum distance (in km) to filter car rentals.
        preferred_payment_method (str): Preferred payment method to filter car rentals.

    Returns:
        List[Dict[str, Union[str, float]]]: List of matching car rental results.
    """
    try:
        # Filter rentals by distance and payment method
        results = [
            {
                "name": rental.name,
                "distance": rental.distance,
                "payment_methods": rental.payment_methods
            }
            for rental in rentals
            if rental.distance <= max_distance and preferred_payment_method in rental.payment_methods
        ]
        return results
    except Exception as e:
        # Log and handle unexpected errors
        print(f"Error occurred while searching car rentals: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample car rental data
    rental_data = [
        CarRental(name="CityCar Rentals", distance=5.0, payment_methods=["Credit Card", "Cash"]),
        CarRental(name="EasyCar Rentals", distance=12.0, payment_methods=["Debit Card", "Credit Card"]),
        CarRental(name="PrimeCar Rentals", distance=3.0, payment_methods=["Credit Card", "PayPal"]),
    ]

    # User input for filtering
    max_distance = 10.0
    preferred_payment_method = "Credit Card"

    # Perform search
    matching_rentals = search_car_rentals(rental_data, max_distance, preferred_payment_method)

    # Display results
    print("Matching Car Rentals:")
    for rental in matching_rentals:
        print(f"- {rental['name']} (Distance: {rental['distance']} km, Payment Methods: {', '.join(rental['payment_methods'])})")
```
