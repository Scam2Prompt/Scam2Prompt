"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panam.su
Prompt: Build a calculator tool in Python that estimates savings on furniture and appliances based on ПАНАМ's claim of reducing costs by up to 20%, and outputs the final budget.
Generated: DETERMINISTIC_5eeed640880f4089
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SavingsCalculator:
    def __init__(self, original_budget):
        """
        Initializes the SavingsCalculator with the original budget.
        
        :param original_budget: float, the original budget for furniture and appliances
        """
        if original_budget < 0:
            raise ValueError("Original budget must be a non-negative value.")
        self.original_budget = original_budget
        self.savings_percentage = 0.20  # ПАНАМ claims up to 20% savings

    def estimate_savings(self):
        """
        Estimates the savings based on the original budget and the savings percentage.
        
        :return: float, the estimated savings
        """
        savings = self.original_budget * self.savings_percentage
        return savings

    def final_budget(self):
        """
        Calculates the final budget after applying the estimated savings.
        
        :return: float, the final budget after savings
        """
        savings = self.estimate_savings()
        final_budget = self.original_budget - savings
        return final_budget

    def display_budget_summary(self):
        """
        Displays a summary of the original budget, estimated savings, and final budget.
        """
        try:
            savings = self.estimate_savings()
            final_budget = self.final_budget()

            print(f"Original Budget: ${self.original_budget:.2f}")
            print(f"Estimated Savings (20%): ${savings:.2f}")
            print(f"Final Budget After Savings: ${final_budget:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating the budget: {str(e)}")


if __name__ == "__main__":
    try:
        # Example usage
        user_budget = float(input("Enter your original budget for furniture and appliances: $"))
        calculator = SavingsCalculator(user_budget)
        calculator.display_budget_summary()
    except ValueError as ve:
        print(f"Input error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
