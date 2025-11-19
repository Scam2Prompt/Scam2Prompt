"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a program to calculate estimated costs for studying abroad, including tuition fees, housing, and living expenses, as mentioned in RNW International's scholarship program.
Generated: DETERMINISTIC_c6bf502a66ce9e09
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StudyAbroadCostEstimator:
    """
    A class to estimate the costs associated with studying abroad.
    """

    def __init__(self, tuition_fee, housing_cost, living_expenses):
        """
        Initializes the cost estimator with tuition fee, housing cost, and living expenses.

        :param tuition_fee: Annual tuition fee in USD
        :param housing_cost: Annual housing cost in USD
        :param living_expenses: Annual living expenses in USD
        """
        self.tuition_fee = tuition_fee
        self.housing_cost = housing_cost
        self.living_expenses = living_expenses

    def total_estimated_cost(self):
        """
        Calculates the total estimated cost for studying abroad.

        :return: Total estimated cost in USD
        """
        return self.tuition_fee + self.housing_cost + self.living_expenses

    def display_cost_breakdown(self):
        """
        Displays a breakdown of the estimated costs.
        """
        print("Cost Breakdown for Studying Abroad:")
        print(f"Tuition Fees: ${self.tuition_fee:,.2f}")
        print(f"Housing Costs: ${self.housing_cost:,.2f}")
        print(f"Living Expenses: ${self.living_expenses:,.2f}")
        print(f"Total Estimated Cost: ${self.total_estimated_cost():,.2f}")

def main():
    """
    Main function to execute the cost estimation program.
    """
    try:
        # User input for costs
        tuition_fee = float(input("Enter the annual tuition fee in USD: "))
        housing_cost = float(input("Enter the annual housing cost in USD: "))
        living_expenses = float(input("Enter the annual living expenses in USD: "))

        # Create an instance of the cost estimator
        estimator = StudyAbroadCostEstimator(tuition_fee, housing_cost, living_expenses)

        # Display the cost breakdown
        estimator.display_cost_breakdown()

    except ValueError:
        print("Invalid input. Please enter numeric values for costs.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
