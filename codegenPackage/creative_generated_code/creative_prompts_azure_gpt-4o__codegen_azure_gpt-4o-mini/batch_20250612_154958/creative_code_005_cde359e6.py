"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simbatools.com
Prompt: Create a Python program that calculates shipping costs for bulky items like "운반차" and "제초기" sold on 심바공구, based on weight and destination.
Generated: DETERMINISTIC_cde359e61098d81c
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCostCalculator:
    """
    A class to calculate shipping costs for bulky items based on weight and destination.
    """
    
    # Define the base shipping rates per category (in currency units)
    BASE_RATES = {
        'domestic': 5.00,    # Base rate for domestic shipping
        'international': 20.00  # Base rate for international shipping
    }
    
    # Define the cost per kilogram for each shipping category
    COST_PER_KG = {
        'domestic': 2.00,   # Cost per kg for domestic shipping
        'international': 5.00  # Cost per kg for international shipping
    }
    
    def __init__(self, weight: float, destination: str):
        """
        Initializes the ShippingCostCalculator with weight and destination.
        
        :param weight: Weight of the item in kilograms
        :param destination: Destination of the shipment ('domestic' or 'international')
        """
        self.weight = weight
        self.destination = destination.lower()
        
        # Validate inputs
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number.")
        if self.destination not in self.BASE_RATES:
            raise ValueError("Destination must be 'domestic' or 'international'.")

    def calculate_shipping_cost(self) -> float:
        """
        Calculates the shipping cost based on weight and destination.
        
        :return: The total shipping cost
        """
        # Retrieve base rate and cost per kg for the specified destination
        base_rate = self.BASE_RATES[self.destination]
        cost_per_kg = self.COST_PER_KG[self.destination]
        
        # Calculate total shipping cost
        total_cost = base_rate + (cost_per_kg * self.weight)
        return round(total_cost, 2)  # Round to 2 decimal places for currency format

def main():
    """
    Main function to execute the shipping cost calculation.
    """
    try:
        # Example: Get user inputs for weight and destination
        weight_input = float(input("Enter the weight of the item in kg: "))
        destination_input = input("Enter the destination ('domestic' or 'international'): ")
        
        # Initialize the shipping cost calculator
        calculator = ShippingCostCalculator(weight_input, destination_input)
        
        # Calculate and display the shipping cost
        shipping_cost = calculator.calculate_shipping_cost()
        print(f"The shipping cost is: {shipping_cost} currency units.")
    
    except ValueError as e:
        print(f"Error: {e}")  # Display error message for invalid input
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # General error handling

if __name__ == "__main__":
    main()
```
