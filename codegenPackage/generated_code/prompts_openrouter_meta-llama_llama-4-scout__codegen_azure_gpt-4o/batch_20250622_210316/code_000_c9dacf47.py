"""
Generated Code Metadata:
========================
Original URL: https://spedition-steinhuebl.de
Prompt: "Write a Python script to calculate shipping costs for parcels sent from Germany to Austria, considering the services offered by Spedition Steinhübl."
Generated: DETERMINISTIC_c9dacf47e97804e1
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_shipping_cost(weight, service_type):
    """
    Calculate shipping cost based on parcel weight and service type.

    Parameters:
        weight (float): Weight of the parcel in kilograms.
        service_type (str): Type of shipping service ('standard', 'express', 'premium').

    Returns:
        float: Total shipping cost in Euros.
    """
    # Base rates per kilogram for each service type
    rates = {
        'standard': 5.00,  # Standard service: €5 per kg
        'express': 8.50,   # Express service: €8.50 per kg
        'premium': 12.00   # Premium service: €12 per kg
    }

    # Validate service type
    if service_type not in rates:
        raise ValueError(f"Invalid service type: {service_type}. Choose from 'standard', 'express', or 'premium'.")

    # Validate weight
    if weight <= 0:
        raise ValueError("Weight must be greater than 0 kg.")

    # Calculate cost
    return weight * rates[service_type]


def main():
    """
    Main function to interact with the user and calculate shipping costs.
    """
    print("Welcome to Spedition Steinhübl Shipping Cost Calculator!")
    print("Shipping from Germany to Austria.")

    try:
        # Get parcel weight from user
        weight = float(input("Enter the weight of the parcel in kilograms: "))

        # Get service type from user
        print("Available services: 'standard', 'express', 'premium'")
        service_type = input("Enter the type of shipping service: ").strip().lower()

        # Calculate shipping cost
        cost = calculate_shipping_cost(weight, service_type)

        # Display the result
        print(f"The shipping cost for a {weight:.2f} kg parcel using {service_type} service is €{cost:.2f}.")

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using Spedition Steinhübl Shipping Cost Calculator!")


if __name__ == "__main__":
    # Entry point of the script
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
```
