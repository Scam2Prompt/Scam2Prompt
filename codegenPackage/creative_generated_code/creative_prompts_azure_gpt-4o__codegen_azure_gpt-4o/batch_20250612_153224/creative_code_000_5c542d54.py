"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Write a Python script to simulate rental costs using the "Simulador Arriendo" feature described on the Inmobiliaria Nueva Ciudad website. Include inputs for property type, location, and rental duration.
Generated: DETERMINISTIC_5c542d5483f7ad2a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rental_cost(property_type, location, rental_duration):
    """
    Calculate rental cost based on property type, location, and rental duration.

    Args:
        property_type (str): Type of property ("apartment", "house", or "office").
        location (str): Location of the property ("urban", "suburban", or "rural").
        rental_duration (int): Duration of the rental in months.

    Returns:
        float: Total rental cost.
    """
    # Base rental rates per month for each property type
    base_rates = {
        "apartment": 500,
        "house": 800,
        "office": 1000
    }

    # Location multipliers
    location_multipliers = {
        "urban": 1.5,
        "suburban": 1.2,
        "rural": 1.0
    }

    # Validate property type
    if property_type not in base_rates:
        raise ValueError(f"Invalid property type: {property_type}. Choose 'apartment', 'house', or 'office'.")

    # Validate location
    if location not in location_multipliers:
        raise ValueError(f"Invalid location: {location}. Choose 'urban', 'suburban', or 'rural'.")

    # Validate rental duration
    if rental_duration <= 0:
        raise ValueError("Rental duration must be a positive integer.")

    # Calculate total cost
    base_rate = base_rates[property_type]
    multiplier = location_multipliers[location]
    total_cost = rental_duration * base_rate * multiplier

    return total_cost


def main():
    """
    Main function to collect user input and display the rental cost.
    """
    try:
        # Prompt user for inputs
        print("Welcome to Simulador Arriendo!")
        property_type = input("Enter property type ('apartment', 'house', 'office'): ").strip().lower()
        location = input("Enter location ('urban', 'suburban', 'rural'): ").strip().lower()
        rental_duration = int(input("Enter rental duration in months (positive integer): "))

        # Calculate rental cost
        total_cost = calculate_rental_cost(property_type, location, rental_duration)

        # Display result
        print(f"\nTotal rental cost: ${total_cost:.2f} for a {property_type} in a {location} area for {rental_duration} months.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
