"""
Generated Code Metadata:
========================
Original URL: https://lavanderiacallezaragoza.com
Prompt: Generate a Python script that automates the process of calculating laundry costs based on the pricing table from Lavandería Autoservicio Zaragoza.
Generated: DETERMINISTIC_82096039101ca5f6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_laundry_cost(weight, service_type):
    """
    Calculate the cost of laundry based on weight and service type.

    Args:
        weight (float): The weight of the laundry in kilograms.
        service_type (str): The type of service ('self_service' or 'full_service').

    Returns:
        float: The total cost of the laundry service.
    """
    # Pricing table for Lavandería Autoservicio Zaragoza
    PRICING = {
        'self_service': 3.5,  # Price per kg for self-service
        'full_service': 5.0   # Price per kg for full-service
    }

    # Validate service type
    if service_type not in PRICING:
        raise ValueError(f"Invalid service type: {service_type}. Choose 'self_service' or 'full_service'.")

    # Calculate cost
    cost_per_kg = PRICING[service_type]
    total_cost = weight * cost_per_kg

    return total_cost


def main():
    """
    Main function to handle user input and calculate laundry costs.
    """
    try:
        # Get user input for weight
        weight = float(input("Enter the weight of your laundry in kilograms: "))
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Get user input for service type
        service_type = input("Enter the service type ('self_service' or 'full_service'): ").strip().lower()

        # Calculate the cost
        total_cost = calculate_laundry_cost(weight, service_type)

        # Display the result
        print(f"The total cost for {weight:.2f} kg of laundry with {service_type} is: €{total_cost:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using Lavandería Autoservicio Zaragoza!")


if __name__ == "__main__":
    main()
```
