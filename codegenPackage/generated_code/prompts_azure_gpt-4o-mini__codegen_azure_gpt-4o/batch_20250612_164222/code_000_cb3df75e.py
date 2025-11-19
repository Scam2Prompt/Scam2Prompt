"""
Generated Code Metadata:
========================
Original URL: https://agodarentacar.com
Prompt: Generate a code snippet to implement a car rental search feature that allows users to filter results by distance and payment method, similar to Agoda RentACar's functionality.
Generated: DETERMINISTIC_cb3df75e4bb79cb4
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class CarRental:
    def __init__(self, car_id, name, distance, payment_methods, price_per_day):
        """
        Initialize a CarRental object.

        :param car_id: Unique identifier for the car
        :param name: Name of the car or rental service
        :param distance: Distance from the user's location in kilometers
        :param payment_methods: List of accepted payment methods (e.g., ['Credit Card', 'PayPal'])
        :param price_per_day: Rental price per day in USD
        """
        self.car_id = car_id
        self.name = name
        self.distance = distance
        self.payment_methods = payment_methods
        self.price_per_day = price_per_day

def search_car_rentals(car_rentals, max_distance, preferred_payment_method):
    """
    Filters car rentals based on distance and payment method.

    :param car_rentals: List of CarRental objects
    :param max_distance: Maximum distance in kilometers
    :param preferred_payment_method: Preferred payment method (e.g., 'Credit Card')
    :return: List of filtered CarRental objects
    """
    try:
        # Validate inputs
        if not isinstance(max_distance, (int, float)) or max_distance < 0:
            raise ValueError("max_distance must be a positive number.")
        if not isinstance(preferred_payment_method, str):
            raise ValueError("preferred_payment_method must be a string.")

        # Filter car rentals
        filtered_rentals = [
            rental for rental in car_rentals
            if rental.distance <= max_distance and preferred_payment_method in rental.payment_methods
        ]
        return filtered_rentals
    except Exception as e:
        print(f"Error occurred during search: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample car rental data
    car_rentals = [
        CarRental(1, "Toyota Corolla", 5, ["Credit Card", "PayPal"], 40),
        CarRental(2, "Honda Civic", 10, ["Credit Card"], 50),
        CarRental(3, "Ford Focus", 15, ["PayPal"], 35),
        CarRental(4, "Chevrolet Malibu", 3, ["Credit Card", "PayPal"], 45),
    ]

    # User search criteria
    max_distance = 10  # kilometers
    preferred_payment_method = "Credit Card"

    # Perform search
    results = search_car_rentals(car_rentals, max_distance, preferred_payment_method)

    # Display results
    print("Available car rentals:")
    for rental in results:
        print(f"ID: {rental.car_id}, Name: {rental.name}, Distance: {rental.distance} km, Price: ${rental.price_per_day}/day")
```
