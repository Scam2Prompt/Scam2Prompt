"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Create a program to calculate the total cost for a student planning to study abroad, factoring in visa fees, travel expenses, and discounts offered by Ikogwe International Limited.
Generated: DETERMINISTIC_c586aa4f5f39a976
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import sys


class StudyAbroadCostCalculator:
    """
    A class to calculate the total cost for a student planning to study abroad.
    """

    def __init__(self, visa_fee, travel_expenses, discount_percentage):
        """
        Initializes the calculator with the given parameters.

        :param visa_fee: The cost of the visa fee (float)
        :param travel_expenses: The estimated travel expenses (float)
        :param discount_percentage: Discount provided by Ikogwe International Limited (float, percentage)
        """
        self.visa_fee = visa_fee
        self.travel_expenses = travel_expenses
        self.discount_percentage = discount_percentage

    def calculate_total_cost(self):
        """
        Calculates the total cost after applying the discount.
        """
        try:
            # Calculate the total before discount
            total_before_discount = self.visa_fee + self.travel_expenses

            # Apply the discount
            discount_amount = (self.discount_percentage / 100) * total_before_discount
            total_after_discount = total_before_discount - discount_amount

            # Return the final total
            return round(total_after_discount, 2)

        except Exception as e:
            # Handle unexpected errors
            print(f"An error occurred while calculating the total cost: {e}", file=sys.stderr)
            raise


def main():
    """
    Main function to interact with the user and calculate the total cost.
    """
    try:
        print("Welcome to the Study Abroad Cost Calculator by Ikogwe International Limited!")

        # User inputs
        visa_fee = float(input("Enter the visa fee (in USD): "))
        travel_expenses = float(input("Enter the estimated travel expenses (in USD): "))
        discount_percentage = float(input("Enter the discount percentage offered by Ikogwe International Limited: "))

        # Validate inputs
        if visa_fee < 0 or travel_expenses < 0 or discount_percentage < 0:
            print("Error: All input values must be non-negative.", file=sys.stderr)
            return

        # Create an instance of the calculator
        calculator = StudyAbroadCostCalculator(visa_fee, travel_expenses, discount_percentage)

        # Calculate the total cost
        total_cost = calculator.calculate_total_cost()

        # Display the result
        print(f"\nThe total cost after applying the discount is: ${total_cost}")

    except ValueError:
        # Handle invalid input
        print("Error: Please enter valid numeric values for all inputs.", file=sys.stderr)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Entry point of the program
if __name__ == "__main__":
    main()
```
