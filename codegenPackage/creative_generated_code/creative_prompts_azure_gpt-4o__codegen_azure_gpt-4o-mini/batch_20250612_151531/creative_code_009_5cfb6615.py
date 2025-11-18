"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Write a script to simulate customer interactions for placing orders of thermal paper rolls, including customization options and bulk pricing, inspired by Apos Chile's offerings.
Generated: DETERMINISTIC_5cfb6615a1cd6365
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class ThermalPaperOrder:
    def __init__(self, roll_diameter, roll_width, roll_length, custom_print=None):
        """
        Initialize a ThermalPaperOrder instance.

        :param roll_diameter: Diameter of the thermal paper roll in mm.
        :param roll_width: Width of the thermal paper roll in mm.
        :param roll_length: Length of the thermal paper roll in meters.
        :param custom_print: Optional custom print text for the roll.
        """
        self.roll_diameter = roll_diameter
        self.roll_width = roll_width
        self.roll_length = roll_length
        self.custom_print = custom_print
        self.price_per_roll = self.calculate_price()
    
    def calculate_price(self):
        """
        Calculate the price of the order based on roll dimensions and custom printing.

        :return: Calculated price of the roll.
        """
        base_price = 10.0  # Base price for a standard roll
        length_price = self.roll_length * 0.5  # Price per meter of length
        diameter_price = (self.roll_diameter / 100) * 2.0  # Price based on diameter in cm

        # Add extra cost for custom print if applicable
        custom_print_cost = 5.0 if self.custom_print else 0.0
        
        total_price = base_price + length_price + diameter_price + custom_print_cost
        return round(total_price, 2)

    def get_order_summary(self):
        """
        Generate a summary of the order.

        :return: Summary string of the order details.
        """
        summary = f"Order Summary:\n" \
                  f"Roll Diameter: {self.roll_diameter} mm\n" \
                  f"Roll Width: {self.roll_width} mm\n" \
                  f"Roll Length: {self.roll_length} m\n" \
                  f"Custom Print: {'Yes' if self.custom_print else 'No'}\n" \
                  f"Price per Roll: ${self.price_per_roll}\n"
        return summary


def bulk_discount(price, quantity):
    """
    Calculate total price with bulk discount.

    :param price: Price per roll.
    :param quantity: Number of rolls ordered.
    :return: Total price after applying bulk discount, if applicable.
    """
    if quantity >= 100:
        discount = 0.2  # 20% discount for 100 or more rolls
    elif quantity >= 50:
        discount = 0.1  # 10% discount for 50 or more rolls
    else:
        discount = 0.0

    total_price = price * quantity * (1 - discount)
    return round(total_price, 2)


def main():
    """
    Main function to simulate customer interactions for placing orders.
    """
    try:
        # Gather user input for order details
        roll_diameter = float(input("Enter roll diameter (mm): "))
        roll_width = float(input("Enter roll width (mm): "))
        roll_length = float(input("Enter roll length (m): "))
        custom_print_option = input("Do you want custom printing? (yes/no): ").strip().lower()

        # Validate custom print input
        if custom_print_option not in ['yes', 'no']:
            raise ValueError("Invalid input for custom printing option. Please enter 'yes' or 'no'.")

        custom_print = custom_print_option == 'yes'
        
        # Create an order
        order = ThermalPaperOrder(roll_diameter, roll_width, roll_length, custom_print)

        # Output order summary
        print(order.get_order_summary())

        # Ask for quantity to order
        quantity = int(input("Enter quantity to order: "))
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        # Calculate total price with any applicable discounts
        total_price = bulk_discount(order.price_per_roll, quantity)
        print(f"Total price for {quantity} rolls: ${total_price}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
