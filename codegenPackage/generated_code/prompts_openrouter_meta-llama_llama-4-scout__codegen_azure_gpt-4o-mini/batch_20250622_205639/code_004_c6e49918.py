"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Create a Python program to calculate the cost of study abroad programs, including tuition fees, living expenses, and other costs, as mentioned in the RNW.edu Scholarship program.
Generated: DETERMINISTIC_c6e49918c4448154
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StudyAbroadCostCalculator:
    """
    A class to calculate the total cost of study abroad programs including tuition fees,
    living expenses, and other associated costs.
    """

    def __init__(self, tuition_fee, living_expenses, other_costs):
        """
        Initializes the StudyAbroadCostCalculator with the given costs.

        :param tuition_fee: float, the tuition fee for the study abroad program
        :param living_expenses: float, the estimated living expenses
        :param other_costs: float, any other associated costs
        """
        self.tuition_fee = tuition_fee
        self.living_expenses = living_expenses
        self.other_costs = other_costs

    def calculate_total_cost(self):
        """
        Calculates the total cost of the study abroad program.

        :return: float, the total cost
        """
        try:
            total_cost = self.tuition_fee + self.living_expenses + self.other_costs
            return total_cost
        except TypeError as e:
            raise ValueError("All cost inputs must be numeric values.") from e

    def display_cost_breakdown(self):
        """
        Displays a breakdown of the costs associated with the study abroad program.
        """
        try:
            print("Cost Breakdown for Study Abroad Program:")
            print(f"Tuition Fees: ${self.tuition_fee:.2f}")
            print(f"Living Expenses: ${self.living_expenses:.2f}")
            print(f"Other Costs: ${self.other_costs:.2f}")
            print(f"Total Cost: ${self.calculate_total_cost():.2f}")
        except Exception as e:
            print(f"An error occurred while displaying the cost breakdown: {e}")

def main():
    """
    Main function to execute the cost calculator.
    """
    try:
        # Example costs (these could be replaced with user input or data from a database)
        tuition_fee = 15000.00  # Example tuition fee
        living_expenses = 12000.00  # Example living expenses
        other_costs = 3000.00  # Example other costs

        # Create an instance of the StudyAbroadCostCalculator
        cost_calculator = StudyAbroadCostCalculator(tuition_fee, living_expenses, other_costs)

        # Display the cost breakdown
        cost_calculator.display_cost_breakdown()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
