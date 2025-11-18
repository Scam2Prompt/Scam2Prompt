"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Create a Python script to analyze the eligibility criteria for the Women Entrepreneur Loan Scheme offered by the Development Bank of Mauritius.
Generated: DETERMINISTIC_55f08293c88bad0c
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to analyze the eligibility criteria for the Women Entrepreneur Loan Scheme 
offered by the Development Bank of Mauritius (DBM).

This script checks if an applicant meets the eligibility requirements based on user input.
"""

# Import necessary libraries
import sys

def check_eligibility(age, gender, business_registered, business_sector, loan_amount):
    """
    Function to check eligibility for the Women Entrepreneur Loan Scheme.

    Parameters:
    - age (int): Age of the applicant
    - gender (str): Gender of the applicant ('F' for Female, 'M' for Male, etc.)
    - business_registered (bool): Whether the business is registered (True/False)
    - business_sector (str): Sector of the business (e.g., 'Retail', 'Agriculture')
    - loan_amount (float): Requested loan amount

    Returns:
    - str: Eligibility message
    """
    try:
        # Basic criteria checks
        if gender.upper() != 'F':
            return "Ineligible: This scheme is exclusively for women entrepreneurs."

        if not (18 <= age <= 60):
            return "Ineligible: Age must be between 18 and 60 years."

        if not business_registered:
            return "Ineligible: Business must be legally registered."

        # Sector-specific check (example: only certain sectors are eligible)
        eligible_sectors = {'Retail', 'Manufacturing', 'Agriculture', 'Services'}
        if business_sector.title() not in eligible_sectors:
            return f"Ineligible: Business sector '{business_sector}' is not supported. Eligible sectors are: {', '.join(eligible_sectors)}."

        # Loan amount check (example: max loan amount is Rs 500,000)
        max_loan_amount = 500000
        if loan_amount > max_loan_amount:
            return f"Ineligible: Loan amount exceeds the maximum limit of Rs {max_loan_amount}."

        return "Eligible: You meet all the criteria for the Women Entrepreneur Loan Scheme!"
    
    except Exception as e:
        return f"Error during eligibility check: {str(e)}"


def main():
    """
    Main function to gather user input and determine eligibility.
    """
    try:
        print("Welcome to the Women Entrepreneur Loan Scheme Eligibility Checker")
        print("Please provide the following details:")

        # Collect input from the user
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (F/M): ").strip()
        business_registered = input("Is your business registered? (yes/no): ").strip().lower() in ['yes', 'y']
        business_sector = input("Enter your business sector: ").strip()
        loan_amount = float(input("Enter the loan amount you are requesting (in Rs): "))

        # Perform eligibility check
        result = check_eligibility(age, gender, business_registered, business_sector, loan_amount)
        print("\nEligibility Result:")
        print(result)

    except ValueError:
        print("Invalid input! Please ensure age and loan amount are numeric values.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        print("Thank you for using the Women Entrepreneur Loan Scheme Eligibility Checker!")


# Entry point for the script
if __name__ == "__main__":
    main()
```
