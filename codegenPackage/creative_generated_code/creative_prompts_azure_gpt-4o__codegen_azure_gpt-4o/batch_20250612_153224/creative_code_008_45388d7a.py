"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Write code to calculate the cost of personalized promotional items based on customization techniques such as serigraphy, vinyl printing, and sublimation, as described on CreatexPro.
Generated: DETERMINISTIC_45388d7a1d30698a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Promotional Item Cost Calculator
# Calculates the cost of personalized promotional items based on customization techniques.

class CustomizationTechniques:
    """Class for customization technique cost calculations."""

    # Base prices for each technique
    BASE_PRICES = {
        "serigraphy": 5.0,      # Base cost per item for serigraphy
        "vinyl_printing": 7.5,  # Base cost per item for vinyl printing
        "sublimation": 10.0     # Base cost per item for sublimation
    }

    @staticmethod
    def calculate_cost(technique, quantity):
        """
        Calculates the total cost for a given customization technique and quantity.
        
        :param technique: The customization technique (serigraphy, vinyl_printing, sublimation).
        :param quantity: The number of items to be customized.
        :return: Total cost for the customization.
        :raises ValueError: If an invalid technique is provided or quantity is non-positive.
        """
        if technique not in CustomizationTechniques.BASE_PRICES:
            raise ValueError(f"Invalid customization technique: {technique}")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        base_price = CustomizationTechniques.BASE_PRICES[technique]
        return base_price * quantity


def main():
    """Main function to handle user input and calculate costs."""
    print("Welcome to CreatexPro Promotional Item Cost Calculator!")
    print("Available customization techniques: serigraphy, vinyl_printing, sublimation")

    try:
        # Get user input for technique
        technique = input("Enter the customization technique: ").strip().lower()
        # Get user input for quantity
        quantity = int(input("Enter the quantity of items to customize: "))
        
        # Calculate total cost
        total_cost = CustomizationTechniques.calculate_cost(technique, quantity)
        print(f"The total cost for {quantity} items using {technique} is: ${total_cost:.2f}")
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
