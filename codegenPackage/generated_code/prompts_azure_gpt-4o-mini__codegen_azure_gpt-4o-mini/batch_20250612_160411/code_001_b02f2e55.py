"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Write a Python function that calculates the total cost of a glass installation kit, including the Betaseal 1001 adhesive, based on user input for quantity and delivery options.
Generated: DETERMINISTIC_b02f2e556cfe06bc
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GlassInstallationKit:
    def __init__(self, adhesive_price=25.0, delivery_fee=5.0):
        """
        Initializes the GlassInstallationKit with default prices.
        
        :param adhesive_price: Price of a single adhesive unit (default is $25.0)
        :param delivery_fee: Base delivery fee (default is $5.0)
        """
        self.adhesive_price = adhesive_price
        self.delivery_fee = delivery_fee

    def calculate_total_cost(self, quantity, delivery_option):
        """
        Calculates the total cost of the glass installation kit.
        
        :param quantity: Number of adhesive units to purchase
        :param delivery_option: Delivery option selected by the user
        :return: Total cost including adhesive and delivery
        :raises ValueError: If quantity is not a positive integer or if delivery_option is invalid
        """
        # Validate quantity
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Validate delivery option
        if delivery_option not in ['standard', 'express']:
            raise ValueError("Invalid delivery option. Choose 'standard' or 'express'.")

        # Calculate adhesive cost
        adhesive_cost = self.adhesive_price * quantity

        # Determine delivery fee based on option
        if delivery_option == 'standard':
            total_delivery_fee = self.delivery_fee
        elif delivery_option == 'express':
            total_delivery_fee = self.delivery_fee * 2  # Express delivery costs double

        # Calculate total cost
        total_cost = adhesive_cost + total_delivery_fee
        return total_cost


def main():
    """
    Main function to execute the glass installation kit cost calculation.
    """
    kit = GlassInstallationKit()

    try:
        # User input for quantity
        quantity = int(input("Enter the quantity of adhesive units: "))
        # User input for delivery option
        delivery_option = input("Enter delivery option (standard/express): ").strip().lower()

        # Calculate total cost
        total_cost = kit.calculate_total_cost(quantity, delivery_option)
        print(f"The total cost for {quantity} adhesive units with {delivery_option} delivery is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
