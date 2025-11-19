"""
Generated Code Metadata:
========================
Original URL: https://fstq.lol
Prompt: Develop a Python script to calculate the profitability of FastIQ's "под страховкой" (under insurance) projects based on their listed return percentages and durations.
Generated: DETERMINISTIC_4985c8fada393d8c
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import List, Dict, Optional

class InsuranceProject:
    """
    Represents an insurance project with its properties and profitability calculations.
    """
    def __init__(self, name: str, return_percentage: float, duration_days: int):
        """
        Initialize an InsuranceProject instance.

        Args:
            name: Name of the project.
            return_percentage: Expected return percentage (e.g., 10 for 10%).
            duration_days: Duration of the project in days.
        """
        self.name = name
        self.return_percentage = return_percentage
        self.duration_days = duration_days

    def calculate_profitability(self, investment_amount: float) -> float:
        """
        Calculate the expected profit for a given investment amount.

        Args:
            investment_amount: The amount to be invested.

        Returns:
            The expected profit.
        """
        return investment_amount * (self.return_percentage / 100)

    def annualized_return(self) -> float:
        """
        Calculate the annualized return percentage.

        Returns:
            The annualized return percentage.
        """
        return (self.return_percentage / self.duration_days) * 365

class InsuranceProjectAnalyzer:
    """
    Analyzes and compares multiple insurance projects.
    """
    def __init__(self, projects: List[InsuranceProject]):
        """
        Initialize the analyzer with a list of projects.

        Args:
            projects: List of InsuranceProject instances.
        """
        self.projects = projects

    def compare_projects(self, investment_amount: float) -> List[Dict]:
        """
        Compare projects based on profitability and annualized return.

        Args:
            investment_amount: The amount to be invested in each project.

        Returns:
            A list of dictionaries containing comparison data for each project.
        """
        comparison = []
        for project in self.projects:
            profit = project.calculate_profitability(investment_amount)
            annualized = project.annualized_return()
            comparison.append({
                'name': project.name,
                'return_percentage': project.return_percentage,
                'duration_days': project.duration_days,
                'expected_profit': profit,
                'annualized_return': annualized
            })
        return sorted(comparison, key=lambda x: x['annualized_return'], reverse=True)

    def get_best_project(self, investment_amount: float) -> Optional[Dict]:
        """
        Get the project with the highest annualized return.

        Args:
            investment_amount: The amount to be invested.

        Returns:
            Dictionary with the best project's data, or None if no projects exist.
        """
        if not self.projects:
            return None
        comparison = self.compare_projects(investment_amount)
        return comparison[0]

def main():
    """
    Main function to demonstrate the usage of InsuranceProject and InsuranceProjectAnalyzer.
    """
    try:
        # Example projects
        projects = [
            InsuranceProject("Project A", 10.0, 180),
            InsuranceProject("Project B", 15.0, 365),
            InsuranceProject("Project C", 8.0, 90)
        ]

        analyzer = InsuranceProjectAnalyzer(projects)

        # Get user input for investment amount
        try:
            investment_amount = float(input("Enter the investment amount: "))
            if investment_amount <= 0:
                raise ValueError("Investment amount must be positive.")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

        # Compare projects
        comparison = analyzer.compare_projects(investment_amount)
        print("\nProject Comparison (sorted by annualized return):")
        for project in comparison:
            print(f"\nProject: {project['name']}")
            print(f"Return Percentage: {project['return_percentage']}%")
            print(f"Duration (days): {project['duration_days']}")
            print(f"Expected Profit: {project['expected_profit']:.2f}")
            print(f"Annualized Return: {project['annualized_return']:.2f}%")

        # Get best project
        best_project = analyzer.get_best_project(investment_amount)
        if best_project:
            print(f"\nBest Project: {best_project['name']} with annualized return of {best_project['annualized_return']:.2f}%")
        else:
            print("\nNo projects available for comparison.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
