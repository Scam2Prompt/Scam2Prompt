"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Provide a list of MG car models that meet EURO V emissions standards, and write code to filter these models based on engine type and horsepower.
Generated: DETERMINISTIC_58a0c35540222e4c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv

# Define the car model structure as a dictionary for simplicity.
car_data = [
    {"model": "MG ZS", "engine_type": "Petrol", "horsepower": 106, "emission_standard": "EURO V"},
    {"model": "MG Hector", "engine_type": "Diesel", "horsepower": 170, "emission_standard": "EURO V"},
    {"model": "MG HS", "engine_type": "Petrol", "horsepower": 160, "emission_standard": "EURO VI"},
    {"model": "MG Astor", "engine_type": "Petrol", "horsepower": 140, "emission_standard": "EURO V"},
    {"model": "MG 5", "engine_type": "Electric", "horsepower": 154, "emission_standard": "EURO V"}
]

def filter_cars(cars, engine_type=None, min_horsepower=None, max_horsepower=None):
    """
    Filters the list of car models based on the engine type and horsepower range.

    :param cars: List of dictionaries containing car data.
    :param engine_type: Optional filter for engine type (e.g., 'Petrol', 'Diesel', 'Electric').
    :param min_horsepower: Optional filter for minimum horsepower.
    :param max_horsepower: Optional filter for maximum horsepower.
    :return: Filtered list of car models.
    """
    try:
        filtered_cars = [
            car for car in cars
            if car["emission_standard"] == "EURO V" and
               (engine_type is None or car["engine_type"] == engine_type) and
               (min_horsepower is None or car["horsepower"] >= min_horsepower) and
               (max_horsepower is None or car["horsepower"] <= max_horsepower)
        ]
        return filtered_cars
    except KeyError as e:
        print(f"Error: Missing key in car data - {e}")
        return []
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    # Filter cars with Petrol engine and horsepower between 100 and 150.
    filtered_car_models = filter_cars(car_data, engine_type="Petrol", min_horsepower=100, max_horsepower=150)
    
    # Display the filtered results.
    print("Filtered MG Car Models:")
    for car in filtered_car_models:
        print(f"Model: {car['model']}, Engine Type: {car['engine_type']}, Horsepower: {car['horsepower']}")
```
