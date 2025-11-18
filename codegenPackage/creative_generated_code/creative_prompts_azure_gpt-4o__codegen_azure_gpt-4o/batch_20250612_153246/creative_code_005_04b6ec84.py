"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hameiriz.co.il
Prompt: Write a function to compute tax refunds for salaried employees in Israel, incorporating deductions and credits mentioned in Zvika Hameiri's services.
Generated: DETERMINISTIC_04b6ec847cc71c83
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def compute_tax_refund(salary: float, tax_paid: float, deductions: dict, credits: dict) -> float:
    """
    Compute the tax refund for salaried employees in Israel.

    Parameters:
    salary (float): The annual salary of the employee.
    tax_paid (float): The amount of tax already paid by the employee.
    deductions (dict): A dictionary of deductions with keys as deduction types and values as amounts.
    credits (dict): A dictionary of tax credits with keys as credit types and values as amounts.

    Returns:
    float: The calculated tax refund amount. If no refund is due, returns 0.0.
    """
    try:
        # Input validation
        if salary < 0 or tax_paid < 0:
            raise ValueError("Salary and tax paid must be non-negative.")
        if not isinstance(deductions, dict) or not isinstance(credits, dict):
            raise ValueError("Deductions and credits must be provided as dictionaries.")

        # Constants for Israeli tax brackets (example values, replace with actual rates)
        TAX_BRACKETS = [
            (0, 7480, 0.1),    # Up to 7,480 NIS, 10% tax
            (7481, 12090, 0.14),  # 7,481 to 12,090 NIS, 14% tax
            (12091, 19420, 0.2),  # 12,091 to 19,420 NIS, 20% tax
            (19421, 25920, 0.31), # 19,421 to 25,920 NIS, 31% tax
            (25921, float('inf'), 0.35) # Above 25,920 NIS, 35% tax
        ]

        # Function to calculate tax liability based on salary and brackets
        def calculate_tax_liability(salary):
            tax = 0.0
            for lower, upper, rate in TAX_BRACKETS:
                if salary > lower:
                    taxable_income = min(salary, upper) - lower
                    tax += taxable_income * rate
            return tax

        # Calculate total deductions and credits
        total_deductions = sum(deductions.values())
        total_credits = sum(credits.values())

        # Adjust salary based on deductions and calculate tax liability
        adjusted_salary = max(salary - total_deductions, 0)  # Salary cannot be negative
        tax_liability = calculate_tax_liability(adjusted_salary)

        # Calculate the refund
        tax_liability_after_credits = max(tax_liability - total_credits, 0)  # Tax liability cannot be negative
        refund = max(tax_paid - tax_liability_after_credits, 0)  # Refund cannot be negative

        logging.info(f"Salary: {salary}, Tax Paid: {tax_paid}, Deductions: {total_deductions}, Credits: {total_credits}")
        logging.info(f"Tax Liability: {tax_liability}, Refund: {refund}")

        return refund

    except ValueError as e:
        logging.error(f"ValueError: {str(e)}")
        return 0.0  # Return 0 for invalid inputs
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return 0.0  # Return 0 for unknown errors

# Example usage:
if __name__ == "__main__":
    salary = 120000  # Annual salary in NIS
    tax_paid = 25000  # Tax already paid in NIS
    deductions = {"pension_fund": 5000, "charitable_donations": 2000}  # Example deductions
    credits = {"education_credit": 1500, "child_tax_credit": 3000}  # Example credits

    refund = compute_tax_refund(salary, tax_paid, deductions, credits)
    print(f"Tax refund: {refund:.2f} NIS")
```
