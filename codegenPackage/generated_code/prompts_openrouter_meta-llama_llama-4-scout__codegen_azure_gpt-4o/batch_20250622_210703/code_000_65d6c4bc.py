"""
Generated Code Metadata:
========================
Original URL: https://ajfpkpackagingcompany.ajfpak.com
Prompt: Write a Python script to calculate the cost of shipping cargo from Karachi to another city in Pakistan using AJF Group of Companies' rates.
Generated: DETERMINISTIC_65d6c4bcd73d9f30
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_shipping_cost(weight, distance):
    """
    Calculate the shipping cost based on weight and distance.
    
    AJF Group of Companies' rates:
    - Base rate: PKR 50 per kilometer
    - Weight surcharge: PKR 20 per kilogram
    
    Args:
        weight (float): Weight of the cargo in kilograms.
        distance (float): Distance to the destination in kilometers.
    
    Returns:
        float: Total shipping cost in PKR.
    """
    try:
        # Validate inputs
        if weight <= 0 or distance <= 0:
            raise ValueError("Weight and distance must be positive numbers.")
        
        # Base rate per kilometer
        base_rate_per_km = 50
        
        # Weight surcharge per kilogram
        weight_surcharge_per_kg = 20
        
        # Calculate cost
        base_cost = base_rate_per_km * distance
        weight_surcharge = weight_surcharge_per_kg * weight
        total_cost = base_cost + weight_surcharge
        
        return total_cost
    
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate shipping cost.
    """
    print("Welcome to AJF Group of Companies Cargo Shipping Calculator!")
    
    try:
        # Get user input for weight and distance
        weight = float(input("Enter the weight of the cargo in kilograms: "))
        distance = float(input("Enter the distance to the destination in kilometers: "))
        
        # Calculate shipping cost
        shipping_cost = calculate_shipping_cost(weight, distance)
        
        # Display the result
        print(f"The total shipping cost from Karachi to the destination is: PKR {shipping_cost:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and distance.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
