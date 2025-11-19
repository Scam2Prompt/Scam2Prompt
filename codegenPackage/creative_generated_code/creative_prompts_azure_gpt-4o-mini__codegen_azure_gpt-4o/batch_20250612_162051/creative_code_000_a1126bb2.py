"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Generate a code snippet for a property rental simulator that calculates monthly payments based on user input for property type and location as described on the Nueva Ciudad website.
Generated: DETERMINISTIC_a1126bb265c694bb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_monthly_payment(property_type, location):
    """
    Calculate monthly payment based on property type and location.
    :param property_type: str - Type of property (e.g., "apartment", "house", "condo").
    :param location: str - Location of the property (e.g., "downtown", "suburbs", "rural").
    :return: float - Monthly payment amount.
    """
    # Base rental prices by property type
    property_base_prices = {
        "apartment": 1200,
        "house": 2000,
        "condo": 1500
    }

    # Location multipliers
    location_multipliers = {
        "downtown": 1.5,
        "suburbs": 1.2,
        "rural": 1.0
    }

    # Validate input
    if property_type not in property_base_prices:
        raise ValueError(f"Invalid property type: {property_type}. Valid options are {list(property_base_prices.keys())}.")

    if location not in location_multipliers:
        raise ValueError(f"Invalid location: {location}. Valid options are {list(location_multipliers.keys())}.")

    # Calculate monthly payment
    base_price = property_base_prices[property_type]
    multiplier = location_multipliers[location]
    monthly_payment = base_price * multiplier

    return monthly_payment

def main():
    """
    Main function to simulate property rental calculations.
    """
    print("Welcome to the Property Rental Simulator!")

    try:
        # Get user input
        property_type = input("Enter the property type (apartment/house/condo): ").strip().lower()
        location = input("Enter the location (downtown/suburbs/rural): ").strip().lower()

        # Perform calculation
        monthly_payment = calculate_monthly_payment(property_type, location)

        # Display the result
        print(f"Your estimated monthly payment for a {property_type} in {location} is: ${monthly_payment:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Property Rental Simulator!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user. Exiting...")
        sys.exit(1)
```
