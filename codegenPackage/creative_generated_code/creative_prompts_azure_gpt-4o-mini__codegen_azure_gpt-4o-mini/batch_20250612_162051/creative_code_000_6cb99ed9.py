"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecg-eg.net
Prompt: Generate a Python script that calculates tax liabilities based on the latest regulations mentioned by Experts Consulting Group.
Generated: DETERMINISTIC_6cb99ed9a8cbfa0a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TaxLiabilityCalculator:
    """
    A class to calculate tax liabilities based on income and applicable tax rates.
    """

    def __init__(self, tax_brackets):
        """
        Initializes the calculator with a set of tax brackets.

        :param tax_brackets: A list of tuples, where each tuple contains
                             (income threshold, tax rate).
        """
        self.tax_brackets = tax_brackets

    def calculate_tax(self, income):
        """
        Calculates the tax liability based on the given income.

        :param income: The total income for which the tax is to be calculated.
        :return: The calculated tax liability.
        :raises ValueError: If the income is negative.
        """
        if income < 0:
            raise ValueError("Income cannot be negative.")

        tax_liability = 0.0
        previous_threshold = 0.0

        for threshold, rate in self.tax_brackets:
            if income > threshold:
                tax_liability += (threshold - previous_threshold) * rate
                previous_threshold = threshold
            else:
                tax_liability += (income - previous_threshold) * rate
                break

        return tax_liability

def load_tax_brackets(file_path):
    """
    Loads tax brackets from a JSON file.

    :param file_path: The path to the JSON file containing tax brackets.
    :return: A list of tax brackets.
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            tax_brackets = json.load(file)
            return [(bracket['threshold'], bracket['rate']) for bracket in tax_brackets]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not find the file: {file_path}") from e
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON format in tax brackets file.") from e

def main():
    """
    The main function to execute the tax liability calculation.
    """
    try:
        # Load tax brackets from a JSON file
        tax_brackets = load_tax_brackets('tax_brackets.json')
        
        # Create a TaxLiabilityCalculator instance
        calculator = TaxLiabilityCalculator(tax_brackets)
        
        # Example income input
        income = float(input("Enter your income: "))
        
        # Calculate the tax liability
        tax = calculator.calculate_tax(income)
        print(f"Your tax liability is: ${tax:.2f}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

This Python script includes a class to calculate tax liability based on dynamic tax brackets loaded from a JSON file. The code is designed to handle errors gracefully and includes comments for clarity. Please ensure to create a `tax_brackets.json` file containing the appropriate tax bracket data in a valid JSON format for this script to function correctly.
