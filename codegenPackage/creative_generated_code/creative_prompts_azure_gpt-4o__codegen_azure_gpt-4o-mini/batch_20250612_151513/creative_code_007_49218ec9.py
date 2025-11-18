"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Create a function to calculate payroll taxes and address payroll tax problems, referencing the payroll tax services offered by Hispanic Services.
Generated: DETERMINISTIC_49218ec983870a89
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PayrollTaxCalculator:
    """
    A class to calculate payroll taxes and address payroll tax issues.
    This class provides methods to compute various payroll taxes based on provided salary and applicable tax rates.
    """

    def __init__(self, federal_tax_rate, state_tax_rate, social_security_rate, medicare_rate):
        """
        Initializes the PayrollTaxCalculator with the provided tax rates.

        Parameters:
        federal_tax_rate (float): The federal tax rate as a percentage.
        state_tax_rate (float): The state tax rate as a percentage.
        social_security_rate (float): The social security tax rate as a percentage.
        medicare_rate (float): The Medicare tax rate as a percentage.
        """
        self.federal_tax_rate = federal_tax_rate / 100
        self.state_tax_rate = state_tax_rate / 100
        self.social_security_rate = social_security_rate / 100
        self.medicare_rate = medicare_rate / 100

    def calculate_payroll_taxes(self, salary):
        """
        Calculates total payroll taxes based on the provided salary.

        Parameters:
        salary (float): The gross salary of the employee.

        Returns:
        dict: A dictionary containing the calculated federal, state, social security, and Medicare taxes.
        """
        if salary < 0:
            raise ValueError("Salary must be a non-negative value.")

        # Calculate individual tax components
        federal_tax = salary * self.federal_tax_rate
        state_tax = salary * self.state_tax_rate
        social_security_tax = salary * self.social_security_rate
        medicare_tax = salary * self.medicare_rate

        # Total taxes
        total_tax = federal_tax + state_tax + social_security_tax + medicare_tax

        # Return a summary of the taxes
        return {
            'federal_tax': federal_tax,
            'state_tax': state_tax,
            'social_security_tax': social_security_tax,
            'medicare_tax': medicare_tax,
            'total_tax': total_tax,
        }

    def address_payroll_tax_issues(self, issue_description):
        """
        Provides guidance on addressing payroll tax issues.

        Parameters:
        issue_description (str): A description of the payroll tax issue.

        Returns:
        str: Suggested actions to resolve the payroll tax issue.
        """
        # Simple case handling for common payroll tax issues
        if "incorrect withholding" in issue_description.lower():
            return "Review employee withholding forms and adjust accordingly."
        elif "missing payment" in issue_description.lower():
            return "Check payment schedules and ensure timely payments."
        elif "audit" in issue_description.lower():
            return "Consult with a payroll tax expert for assistance."
        else:
            return "Contact a tax professional for personalized assistance."

# Example usage
if __name__ == "__main__":
    # Initialize the PayrollTaxCalculator with sample tax rates
    calculator = PayrollTaxCalculator(federal_tax_rate=12, state_tax_rate=5, social_security_rate=6.2, medicare_rate=1.45)
    
    try:
        # Calculate payroll taxes for a given salary
        salary = 50000  # Example gross salary
        taxes = calculator.calculate_payroll_taxes(salary)
        print("Payroll Tax Breakdown:", taxes)

        # Address a sample payroll tax issue
        issue_response = calculator.address_payroll_tax_issues("Incorrect withholding")
        print("Issue Resolution Suggestion:", issue_response)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
