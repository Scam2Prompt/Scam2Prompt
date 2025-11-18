"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Write a program to calculate estimated costs for studying abroad, including tuition fees, housing, and living expenses, as mentioned in RNW International's scholarship program.
Generated: DETERMINISTIC_c6bf502a66ce9e09
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StudyAbroadCostEstimator:
    """
    A class to estimate the total costs for studying abroad, including tuition fees,
    housing, and living expenses.
    """

    def __init__(self, tuition_fee, housing_cost, living_expenses, scholarship_amount=0):
        """
        Initializes the cost estimator with the provided parameters.

        :param tuition_fee: float - The tuition fees for the study program.
        :param housing_cost: float - The housing costs for the duration of study.
        :param living_expenses: float - Estimated living expenses per year.
        :param scholarship_amount: float - Any scholarship amount to be subtracted from the total cost.
        """
        self.tuition_fee = tuition_fee
        self.housing_cost = housing_cost
        self.living_expenses = living_expenses
        self.scholarship_amount = scholarship_amount

    def calculate_total_cost(self, duration_years):
        """
        Calculates the total estimated cost for studying abroad based on the duration.

        :param duration_years: int - The number of years the student will be studying abroad.
        :return: float - The total estimated cost after applying the scholarship.
        :raises ValueError: If duration_years is not a positive integer.
        """
        if not isinstance(duration_years, int) or duration_years <= 0:
            raise ValueError("Duration must be a positive integer representing the number of years.")

        total_tuition = self.tuition_fee * duration_years
        total_housing = self.housing_cost * duration_years
        total_living_expenses = self.living_expenses * duration_years

        total_cost = total_tuition + total_housing + total_living_expenses - self.scholarship_amount
        return total_cost

    def display_cost_breakdown(self, duration_years):
        """
        Displays a detailed breakdown of the estimated costs.

        :param duration_years: int - The number of years the student will be studying abroad.
        """
        try:
            total_cost = self.calculate_total_cost(duration_years)
            print(f"Estimated Cost Breakdown for {duration_years} year(s):")
            print(f"  Tuition Fees: ${self.tuition_fee * duration_years:.2f}")
            print(f"  Housing Costs: ${self.housing_cost * duration_years:.2f}")
            print(f"  Living Expenses: ${self.living_expenses * duration_years:.2f}")
            print(f"  Total Estimated Cost (after scholarship): ${total_cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    # Example costs (modify these values as needed)
    tuition_fee = 20000.0  # Annual tuition fee
    housing_cost = 10000.0  # Annual housing cost
    living_expenses = 5000.0  # Annual living expenses
    scholarship_amount = 5000.0  # Available scholarship amount

    # Create an instance of the cost estimator
    estimator = StudyAbroadCostEstimator(tuition_fee, housing_cost, living_expenses, scholarship_amount)

    # Define the duration of the study abroad program
    duration_years = 4  # Example duration in years

    # Display the estimated cost breakdown
    estimator.display_cost_breakdown(duration_years)
```
