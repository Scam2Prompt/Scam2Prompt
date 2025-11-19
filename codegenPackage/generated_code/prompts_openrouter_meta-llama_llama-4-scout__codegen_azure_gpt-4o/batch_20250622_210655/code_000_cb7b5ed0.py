"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Write a Python script to simulate rental payments for a property in Bogotá, Colombia, considering factors like property value and location, as offered by Inmobiliaria Nueva Ciudad.
Generated: DETERMINISTIC_cb7b5ed06316a441
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_rental_payment(property_value, location_factor):
    """
    Calculate the monthly rental payment for a property based on its value and location factor.

    Args:
        property_value (float): The value of the property in Colombian pesos.
        location_factor (float): A multiplier based on the location of the property.
                                 Typically ranges from 0.8 to 1.5 (e.g., 1.0 for average location).

    Returns:
        float: The calculated monthly rental payment.
    """
    try:
        # Validate inputs
        if property_value <= 0:
            raise ValueError("Property value must be greater than zero.")
        if location_factor <= 0:
            raise ValueError("Location factor must be greater than zero.")

        # Base rental rate as a percentage of property value (e.g., 0.5%)
        base_rental_rate = 0.005

        # Calculate rental payment
        rental_payment = property_value * base_rental_rate * location_factor
        return rental_payment

    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to simulate rental payments for a property.
    """
    print("Welcome to Inmobiliaria Nueva Ciudad Rental Payment Simulator!")
    try:
        # Get user input for property value and location factor
        property_value = float(input("Enter the property value in Colombian pesos: "))
        location_factor = float(input("Enter the location factor (e.g., 1.0 for average location): "))

        # Calculate rental payment
        rental_payment = calculate_rental_payment(property_value, location_factor)

        if rental_payment is not None:
            print(f"The estimated monthly rental payment is: COP {rental_payment:,.2f}")
        else:
            print("Failed to calculate rental payment due to invalid inputs.")

    except ValueError:
        print("Invalid input. Please enter numeric values for property value and location factor.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
