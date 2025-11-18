"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Write a program to compare the cost and delivery time between air freight and ocean freight for Uniair Cargo's logistics services.
Generated: DETERMINISTIC_a3adc8cee54f640e
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class FreightOption:
    """Class representing a freight option, including cost and delivery time."""
    
    def __init__(self, name, cost_per_kg, transit_time_days):
        """
        Initialize the freight option.
        
        :param name: The name of the freight option (e.g., "Air Freight", "Ocean Freight")
        :param cost_per_kg: The cost per kilogram for the freight option
        :param transit_time_days: The estimated delivery time in days
        """
        self.name = name
        self.cost_per_kg = cost_per_kg
        self.transit_time_days = transit_time_days


def calculate_cost_and_delivery(freight_option, weight_kg):
    """
    Calculate the cost and estimated delivery date for a given freight option.
    
    :param freight_option: A FreightOption object
    :param weight_kg: The weight of the shipment in kilograms
    :return: A tuple containing (total_cost, estimated_delivery_date)
    """
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0.")
    
    # Calculate total cost based on weight
    total_cost = freight_option.cost_per_kg * weight_kg
    
    # Calculate estimated delivery date
    estimated_delivery_date = datetime.date.today() + datetime.timedelta(days=freight_option.transit_time_days)
    
    return total_cost, estimated_delivery_date


def compare_freight_options(weight_kg):
    """
    Compare the cost and delivery time for air freight and ocean freight.
    
    :param weight_kg: The weight of the shipment in kilograms
    :return: None
    """
    # Define available freight options
    air_freight = FreightOption(name="Air Freight", cost_per_kg=5.0, transit_time_days=3)
    ocean_freight = FreightOption(name="Ocean Freight", cost_per_kg=2.0, transit_time_days=14)
    
    try:
        # Calculate cost and delivery for air freight
        air_cost, air_delivery_date = calculate_cost_and_delivery(air_freight, weight_kg)
        
        # Calculate cost and delivery for ocean freight
        ocean_cost, ocean_delivery_date = calculate_cost_and_delivery(ocean_freight, weight_kg)
        
        # Print comparison results
        print(f"\nComparison for {weight_kg}kg Shipment:")
        print(f"{air_freight.name}:")
        print(f"  Total Cost: ${air_cost:.2f}")
        print(f"  Estimated Delivery Date: {air_delivery_date}")
        
        print(f"{ocean_freight.name}:")
        print(f"  Total Cost: ${ocean_cost:.2f}")
        print(f"  Estimated Delivery Date: {ocean_delivery_date}")
        
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")


# Main program execution
if __name__ == "__main__":
    try:
        # Prompt user for shipment weight
        user_weight = float(input("Enter the shipment weight in kilograms: "))
        
        # Compare freight options
        compare_freight_options(user_weight)
    except ValueError:
        # Handle invalid user input
        print("Invalid input. Please enter a numeric value for the weight.")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
```
