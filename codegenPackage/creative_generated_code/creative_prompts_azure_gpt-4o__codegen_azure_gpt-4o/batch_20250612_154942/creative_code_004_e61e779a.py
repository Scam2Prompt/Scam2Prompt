"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theaflac.com
Prompt: Develop a program to calculate life insurance coverage options using Aflac's life insurance calculator and policy details from the B60000 series.
Generated: DETERMINISTIC_e61e779a340bc9f3
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Life Insurance Coverage Calculator using Aflac's policy details from the B60000 series.

This program calculates life insurance coverage options based on user input
such as age, annual income, number of dependents, and coverage preferences.

Author: Professional Software Developer
Date: October 2023
"""

import sys

class LifeInsuranceCalculator:
    """
    Class to encapsulate the life insurance coverage calculation logic.
    Policies are based on Aflac's B60000 series guidelines.
    """

    def __init__(self):
        """
        Initialize the calculator with policy parameters.
        """
        self.min_age = 18  # Minimum eligible age for coverage
        self.max_age = 70  # Maximum eligible age for coverage
        self.base_coverage_multiplier = 10  # Base multiplier for annual income
        self.dependent_coverage_addition = 50000  # Additional coverage per dependent

    def calculate_coverage(self, age, annual_income, num_dependents):
        """
        Calculate the recommended life insurance coverage.

        Args:
            age (int): Age of the applicant.
            annual_income (float): Applicant's annual income in USD.
            num_dependents (int): Number of dependents.

        Returns:
            float: Recommended life insurance coverage amount in USD.
        
        Raises:
            ValueError: If the age is outside eligible range.
        """
        if age < self.min_age or age > self.max_age:
            raise ValueError(f"Age must be between {self.min_age} and {self.max_age} years.")

        # Calculate base coverage based on annual income
        base_coverage = annual_income * self.base_coverage_multiplier

        # Calculate additional coverage for dependents
        dependent_coverage = num_dependents * self.dependent_coverage_addition

        # Total recommended coverage
        total_coverage = base_coverage + dependent_coverage
        return total_coverage


def main():
    """
    Main function to interact with the user and calculate life insurance coverage.
    """
    print("Welcome to Aflac's Life Insurance Coverage Calculator (B60000 Series).")

    try:
        # Get user input for age, annual income, and number of dependents
        age = int(input("Enter your age: "))
        annual_income = float(input("Enter your annual income (in USD): "))
        num_dependents = int(input("Enter the number of dependents: "))

        # Initialize the calculator
        calculator = LifeInsuranceCalculator()

        # Calculate the recommended coverage
        recommended_coverage = calculator.calculate_coverage(age, annual_income, num_dependents)

        # Output the result
        print(f"Based on your inputs, the recommended life insurance coverage is ${recommended_coverage:,.2f}.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Life Insurance Coverage Calculator. Stay safe!")


if __name__ == "__main__":
    # Start the program
    main()
```
