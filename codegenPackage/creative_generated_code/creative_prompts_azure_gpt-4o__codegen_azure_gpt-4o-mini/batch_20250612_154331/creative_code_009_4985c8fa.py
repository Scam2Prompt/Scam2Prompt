"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fstq.lol
Prompt: Develop a Python script to calculate the profitability of FastIQ's "под страховкой" (under insurance) projects based on their listed return percentages and durations.
Generated: DETERMINISTIC_4985c8fada393d8c
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class Project:
    """Class to represent a project with its return percentage and duration."""
    
    def __init__(self, name: str, return_percentage: float, duration: int):
        """
        Initializes a Project instance.

        :param name: Name of the project.
        :param return_percentage: Expected return percentage of the project.
        :param duration: Duration of the project in months.
        """
        self.name = name
        self.return_percentage = return_percentage
        self.duration = duration

    def calculate_profit(self, investment: float) -> float:
        """
        Calculates the profit for the project based on the investment.

        :param investment: Amount of money invested in the project.
        :return: Profit calculated from the investment.
        """
        if investment < 0:
            raise ValueError("Investment must be a non-negative amount.")
        profit = investment * (self.return_percentage / 100)
        return profit


def main():
    # Sample data for projects
    projects_data = [
        {"name": "Project A", "return_percentage": 15.0, "duration": 12},
        {"name": "Project B", "return_percentage": 10.0, "duration": 6},
        {"name": "Project C", "return_percentage": 25.0, "duration": 24},
    ]
    
    # Convert data to Project instances
    projects = [Project(**data) for data in projects_data]
    
    # Define the investment amount
    investment_amount = 10000.0  # Example investment amount

    # Calculate and display profitability for each project
    results = []
    for project in projects:
        try:
            profit = project.calculate_profit(investment_amount)
            results.append({
                "Project": project.name,
                "Return Percentage": project.return_percentage,
                "Duration (months)": project.duration,
                "Profit": profit
            })
        except ValueError as e:
            print(f"Error calculating profit for {project.name}: {e}")

    # Create a DataFrame for better visualization of results
    results_df = pd.DataFrame(results)
    print(results_df)


if __name__ == "__main__":
    main()
```
