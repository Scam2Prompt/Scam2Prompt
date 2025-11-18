"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Write a script to calculate shipping costs for wire mesh products based on customer location, referencing the international nature of Baochuan Wire Mesh's operations.
Generated: DETERMINISTIC_f8095b5da073c996
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_shipping_cost(weight, destination):
    """
    Calculate the shipping cost of wire mesh products based on weight and destination.

    Parameters:
        weight (float): Weight of the product in kilograms.
        destination (str): Destination country code (ISO 3166-1 alpha-2).

    Returns:
        float: Shipping cost in USD.

    Raises:
        ValueError: If weight is negative or destination is invalid.
    """
    # Shipping rate per kilogram based on region
    regional_shipping_rates = {
        "US": 5.0,  # USD per kg for shipments to the United States
        "EU": 4.0,  # USD per kg for shipments to Europe
        "AS": 3.5,  # USD per kg for shipments to Asia
        "AF": 6.0,  # USD per kg for shipments to Africa
        "AU": 4.5,  # USD per kg for shipments to Australia
        "SA": 5.5,  # USD per kg for shipments to South America
        "OTHER": 7.0  # USD per kg for shipments to other regions
    }

    # Validate weight
    if weight <= 0:
        raise ValueError("Weight must be a positive number.")
    
    # Determine shipping rate based on destination
    shipping_rate = regional_shipping_rates.get(destination.upper(), regional_shipping_rates["OTHER"])

    # Calculate shipping cost
    shipping_cost = weight * shipping_rate

    # Round to two decimal places for accuracy
    return round(shipping_cost, 2)


def main():
    """
    Main function to interact with the user and calculate shipping costs.
    """
    try:
        print("Welcome to Baochuan Wire Mesh Shipping Cost Calculator!")
        
        # Get user input for weight
        weight = float(input("Enter the weight of your wire mesh product (in kg): "))
        
        # Get user input for destination
        destination = input("Enter the destination country code (ISO 3166-1 alpha-2): ").strip()
        
        # Calculate cost
        cost = calculate_shipping_cost(weight, destination)
        
        # Display the shipping cost
        print(f"The shipping cost to {destination.upper()} for a product weighing {weight} kg is: ${cost:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
