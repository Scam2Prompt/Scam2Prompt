"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Create a program to calculate the total cost for a student planning to study abroad, factoring in visa fees, travel expenses, and discounts offered by Ikogwe International Limited.
Generated: DETERMINISTIC_c586aa4f5f39a976
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_abroad_cost_calculator.py

class StudentAbroadCostCalculator:
    """
    Calculates the total cost for a student planning to study abroad.

    Attributes:
        visa_fees (float): The cost of the visa.
        travel_expenses (float): The cost of travel.
        discount_rate (float): The discount rate offered by Ikogwe International Limited.
    """

    def __init__(self, visa_fees, travel_expenses, discount_rate=0.0):
        """
        Initializes a StudentAbroadCostCalculator instance.

        Args:
            visa_fees (float): The cost of the visa.
            travel_expenses (float): The cost of travel.
            discount_rate (float, optional): The discount rate. Defaults to 0.0.
        """
        self.visa_fees = visa_fees
        self.travel_expenses = travel_expenses
        self.discount_rate = discount_rate

    def calculate_total_cost(self):
        """
        Calculates the total cost for the student.

        Returns:
            float: The total cost.
        """
        # Calculate subtotal
        subtotal = self.visa_fees + self.travel_expenses
        
        # Apply discount
        discount = subtotal * self.discount_rate
        total_cost = subtotal - discount
        
        return total_cost


def main():
    try:
        # Get user input
        visa_fees = float(input("Enter the visa fees: $"))
        travel_expenses = float(input("Enter the travel expenses: $"))
        discount_rate = float(input("Enter the discount rate (as a decimal, e.g., 5% = 0.05): "))

        # Create a calculator instance
        calculator = StudentAbroadCostCalculator(visa_fees, travel_expenses, discount_rate)

        # Calculate total cost
        total_cost = calculator.calculate_total_cost()

        # Print the result
        print(f"Total cost: ${total_cost:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
