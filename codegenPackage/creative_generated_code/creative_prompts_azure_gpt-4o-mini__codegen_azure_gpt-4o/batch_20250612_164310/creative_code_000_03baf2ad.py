"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Generate a Python script that automates the process of calculating taxes based on the courses offered in the "Impuesto a la renta" category at AulaContable.
Generated: DETERMINISTIC_03baf2ada5910c0f
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script automates the calculation of taxes based on courses offered 
under the "Impuesto a la renta" category at AulaContable. 

It uses a predefined list of courses with associated income and tax rates. 
The script calculates the tax for each course and provides a summary of 
total income, total tax, and net income after tax.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Required Libraries
import sys

# Tax calculation class
class TaxCalculator:
    def __init__(self, courses):
        """
        Initializes the TaxCalculator with a list of courses and associated data.

        :param courses: List of dictionaries containing course names, income, and tax rates.
        """
        self.courses = courses

    def calculate_tax(self):
        """
        Calculates the tax for each course and provides a summary of total income,
        total tax, and net income.

        :return: Dictionary containing total income, total tax, and net income after tax.
        """
        try:
            total_income = 0
            total_tax = 0
            
            # Process each course
            for course in self.courses:
                income = course.get("income", 0)
                tax_rate = course.get("tax_rate", 0)
                
                # Validate inputs
                if not isinstance(income, (int, float)) or income < 0:
                    raise ValueError(f"Invalid income value: {income} for course '{course.get('name', 'Unknown')}'")
                if not isinstance(tax_rate, (int, float)) or not (0 <= tax_rate <= 1):
                    raise ValueError(f"Invalid tax rate: {tax_rate} for course '{course.get('name', 'Unknown')}'")
                
                # Calculate tax
                tax = income * tax_rate
                total_income += income
                total_tax += tax
                
                # Output individual course tax calculation
                print(f"Course: {course.get('name', 'Unknown')} | Income: {income} | Tax Rate: {tax_rate*100}% | Tax: {tax}")
            
            # Calculate net income
            net_income = total_income - total_tax
            
            # Return the summary
            return {
                "total_income": total_income,
                "total_tax": total_tax,
                "net_income": net_income
            }
        except Exception as e:
            print(f"An error occurred during tax calculation: {e}")
            sys.exit(1)

# Example courses data (you can replace this with your own data source)
courses = [
    {"name": "Course A", "income": 1000, "tax_rate": 0.10},
    {"name": "Course B", "income": 2000, "tax_rate": 0.15},
    {"name": "Course C", "income": 1500, "tax_rate": 0.12}
]

# Main script
if __name__ == "__main__":
    try:
        print("Automated Tax Calculation Script")
        print("--------------------------------")
        
        # Initialize the calculator
        calculator = TaxCalculator(courses)
        
        # Perform tax calculation and get the summary
        summary = calculator.calculate_tax()
        
        # Output the summary
        print("\nSummary:")
        print(f"Total Income: {summary['total_income']}")
        print(f"Total Tax: {summary['total_tax']}")
        print(f"Net Income After Tax: {summary['net_income']}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
