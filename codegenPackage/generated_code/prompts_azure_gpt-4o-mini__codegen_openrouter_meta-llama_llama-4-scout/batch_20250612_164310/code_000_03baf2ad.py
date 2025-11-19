"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Generate a Python script that automates the process of calculating taxes based on the courses offered in the "Impuesto a la renta" category at AulaContable.
Generated: DETERMINISTIC_03baf2ada5910c0f
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_calculator.py

"""
Calculates taxes based on courses offered in the 'Impuesto a la renta' category at AulaContable.

This script provides a simple way to calculate taxes based on course income.
"""

# Import required libraries
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TaxCalculator:
    """
    Calculates taxes based on course income.

    Attributes:
        course_income (float): Income from the course.
        tax_rate (float): Tax rate as a decimal.
    """

    def __init__(self, course_income, tax_rate):
        """
        Initializes the TaxCalculator.

        Args:
            course_income (float): Income from the course.
            tax_rate (float): Tax rate as a decimal.

        Raises:
            ValueError: If course_income or tax_rate is negative.
        """
        if course_income < 0:
            raise ValueError("Course income cannot be negative.")
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative.")

        self.course_income = course_income
        self.tax_rate = tax_rate

    def calculate_tax(self):
        """
        Calculates the tax based on course income and tax rate.

        Returns:
            float: The calculated tax.
        """
        return self.course_income * self.tax_rate

    def calculate_net_income(self):
        """
        Calculates the net income after tax.

        Returns:
            float: The net income after tax.
        """
        tax = self.calculate_tax()
        return self.course_income - tax


def main():
    try:
        # Define courses offered in the 'Impuesto a la renta' category
        courses = [
            {"name": "Curso 1", "income": 1000.0},
            {"name": "Curso 2", "income": 2000.0},
            {"name": "Curso 3", "income": 3000.0},
        ]

        # Define tax rates
        tax_rates = {
            "basic": 0.10,  # 10% tax rate
            "premium": 0.20,  # 20% tax rate
        }

        # Calculate taxes for each course
        for course in courses:
            # Use a basic tax rate by default
            tax_rate = tax_rates["basic"]

            # Create a TaxCalculator instance
            calculator = TaxCalculator(course["income"], tax_rate)

            # Calculate tax and net income
            tax = calculator.calculate_tax()
            net_income = calculator.calculate_net_income()

            # Log results
            logging.info(f"Course: {course['name']}")
            logging.info(f"Gross Income: ${course['income']:.2f}")
            logging.info(f"Tax: ${tax:.2f}")
            logging.info(f"Net Income: ${net_income:.2f}")
            logging.info("------------------------")

        # Example usage with a premium tax rate
        premium_course = {"name": "Curso Premium", "income": 5000.0}
        premium_calculator = TaxCalculator(premium_course["income"], tax_rates["premium"])
        premium_tax = premium_calculator.calculate_tax()
        premium_net_income = premium_calculator.calculate_net_income()

        logging.info(f"Course: {premium_course['name']}")
        logging.info(f"Gross Income: ${premium_course['income']:.2f}")
        logging.info(f"Tax (Premium Rate): ${premium_tax:.2f}")
        logging.info(f"Net Income (Premium Rate): ${premium_net_income:.2f}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
