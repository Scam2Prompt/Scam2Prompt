"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Create a Python script to automate the calculation of shipping costs for SmartPrice KE's products based on delivery location and product weight.
Generated: DETERMINISTIC_59108a4d4836741b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ShippingCalculator:
    """
    A class to calculate shipping costs based on delivery location and product weight.
    """

    def __init__(self):
        """
        Initializes the shipping rates for various locations and weight thresholds.
        """
        # Predefined shipping rates (example data; replace with actual rates)
        self.shipping_rates = {
            "Nairobi": {
                "base_rate": 100,
                "weight_rate": 10  # Cost per kg
            },
            "Mombasa": {
                "base_rate": 150,
                "weight_rate": 15
            },
            "Kisumu": {
                "base_rate": 120,
                "weight_rate": 12
            },
            "Other": {
                "base_rate": 200,
                "weight_rate": 20
            }
        }

    def calculate_shipping_cost(self, location, weight):
        """
        Calculate the shipping cost for a given location and product weight.

        Args:
            location (str): Delivery location.
            weight (float): Product weight in kilograms.

        Returns:
            float: Calculated shipping cost.
        """
        try:
            # Validate weight
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")

            # Get rates based on location
            rates = self.shipping_rates.get(location, self.shipping_rates["Other"])
            base_rate = rates["base_rate"]
            weight_rate = rates["weight_rate"]

            # Calculate total cost
            total_cost = base_rate + (weight * weight_rate)
            return round(total_cost, 2)

        except KeyError as e:
            raise Exception(f"Invalid location: {location}") from e
        except Exception as e:
            raise Exception(f"Error calculating shipping cost: {e}") from e

def main():
    """
    Main function to interact with the user and calculate shipping costs.
    """
    print("Welcome to SmartPrice KE's Shipping Cost Calculator!")

    try:
        # Collect user input
        location = input("Enter delivery location (e.g., Nairobi, Mombasa, Kisumu): ").strip()
        weight = float(input("Enter product weight in kilograms: "))

        # Initialize the calculator
        calculator = ShippingCalculator()

        # Calculate the shipping cost
        cost = calculator.calculate_shipping_cost(location, weight)
        print(f"The shipping cost to {location} for a product weighing {weight} kg is KES {cost}.")
    
    except ValueError:
        print("Invalid input. Please ensure weight is a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
