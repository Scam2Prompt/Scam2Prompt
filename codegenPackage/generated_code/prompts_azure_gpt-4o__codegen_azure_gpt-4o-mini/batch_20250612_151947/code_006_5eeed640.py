"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: Build a calculator tool in Python that estimates savings on furniture and appliances based on ПАНАМ's claim of reducing costs by up to 20%, and outputs the final budget.
Generated: DETERMINISTIC_5eeed640880f4089
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SavingsCalculator:
    """
    A class to calculate estimated savings on furniture and appliances based on a percentage reduction.
    """

    def __init__(self, original_budget: float, discount_percentage: float = 20.0):
        """
        Initializes the SavingsCalculator with the original budget and discount percentage.

        :param original_budget: The original budget for furniture and appliances.
        :param discount_percentage: The percentage reduction in costs (default is 20%).
        """
        if original_budget < 0:
            raise ValueError("Original budget must be a non-negative value.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        self.original_budget = original_budget
        self.discount_percentage = discount_percentage

    def calculate_savings(self) -> float:
        """
        Calculates the savings based on the original budget and discount percentage.

        :return: The amount saved.
        """
        savings = (self.discount_percentage / 100) * self.original_budget
        return savings

    def calculate_final_budget(self) -> float:
        """
        Calculates the final budget after applying the savings.

        :return: The final budget after savings.
        """
        savings = self.calculate_savings()
        final_budget = self.original_budget - savings
        return final_budget

    def display_results(self):
        """
        Displays the original budget, savings, and final budget.
        """
        try:
            savings = self.calculate_savings()
            final_budget = self.calculate_final_budget()

            print(f"Original Budget: ${self.original_budget:.2f}")
            print(f"Estimated Savings (at {self.discount_percentage}%): ${savings:.2f}")
            print(f"Final Budget after Savings: ${final_budget:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating savings: {e}")


def main():
    """
    Main function to run the SavingsCalculator tool.
    """
    try:
        # Input: Original budget from the user
        original_budget = float(input("Enter the original budget for furniture and appliances: $"))
        
        # Create an instance of SavingsCalculator
        calculator = SavingsCalculator(original_budget)

        # Display the results
        calculator.display_results()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
