"""
Generated Code Metadata:
========================
Original URL: https://sandboxii121.pages.dev
Prompt: Generate Python code to calculate event ticket fees, including discounts (e.g., 63% off) and additional fees, and display the order summary with total cost.
Generated: DETERMINISTIC_c46815de293fe7fa
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_ticket_calculator.py

class EventTicketCalculator:
    def __init__(self, base_price):
        """
        Initialize the EventTicketCalculator with a base ticket price.

        Args:
            base_price (float): The base price of the event ticket.
        """
        self.base_price = base_price

    def calculate_discount(self, discount_percentage):
        """
        Calculate the discount amount based on the given percentage.

        Args:
            discount_percentage (float): The discount percentage.

        Returns:
            float: The discount amount.
        """
        return self.base_price * (discount_percentage / 100)

    def calculate_additional_fees(self, additional_fees):
        """
        Calculate the total additional fees.

        Args:
            additional_fees (dict): A dictionary of additional fees with their descriptions.

        Returns:
            float: The total additional fees.
        """
        return sum(fees for fees in additional_fees.values())

    def calculate_total_cost(self, discount_percentage, additional_fees):
        """
        Calculate the total cost of the event ticket, including discounts and additional fees.

        Args:
            discount_percentage (float): The discount percentage.
            additional_fees (dict): A dictionary of additional fees with their descriptions.

        Returns:
            float: The total cost of the event ticket.
        """
        discount_amount = self.calculate_discount(discount_percentage)
        discounted_price = self.base_price - discount_amount
        total_additional_fees = self.calculate_additional_fees(additional_fees)
        return discounted_price + total_additional_fees

    def display_order_summary(self, discount_percentage, additional_fees):
        """
        Display the order summary, including the base price, discount, additional fees, and total cost.

        Args:
            discount_percentage (float): The discount percentage.
            additional_fees (dict): A dictionary of additional fees with their descriptions.
        """
        discount_amount = self.calculate_discount(discount_percentage)
        discounted_price = self.base_price - discount_amount
        total_additional_fees = self.calculate_additional_fees(additional_fees)
        total_cost = self.calculate_total_cost(discount_percentage, additional_fees)

        print("# Order Summary")
        print(f"## Base Price: ${self.base_price:.2f}")
        print(f"## Discount ({discount_percentage}%): -${discount_amount:.2f}")
        print(f"## Discounted Price: ${discounted_price:.2f}")
        print("## Additional Fees:")
        for description, fee in additional_fees.items():
            print(f"  - {description}: ${fee:.2f}")
        print(f"## Total Additional Fees: ${total_additional_fees:.2f}")
        print(f"## Total Cost: ${total_cost:.2f}")


def main():
    try:
        base_price = 100.0
        discount_percentage = 63.0
        additional_fees = {
            "Service Fee": 5.0,
            "Processing Fee": 2.0,
            "Tax": 8.0
        }

        calculator = EventTicketCalculator(base_price)
        calculator.display_order_summary(discount_percentage, additional_fees)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
