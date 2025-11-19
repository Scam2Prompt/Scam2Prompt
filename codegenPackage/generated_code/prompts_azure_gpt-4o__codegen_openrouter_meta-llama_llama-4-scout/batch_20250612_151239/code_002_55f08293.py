"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Create a Python script to analyze the eligibility criteria for the Women Entrepreneur Loan Scheme offered by the Development Bank of Mauritius.
Generated: DETERMINISTIC_55f08293c88bad0c
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# women_entrepreneur_loan_scheme.py

class WomenEntrepreneurLoanScheme:
    def __init__(self, applicant_name, age, business_type, years_of_experience, loan_amount):
        """
        Initialize the applicant's details.

        Args:
            applicant_name (str): Name of the applicant.
            age (int): Age of the applicant.
            business_type (str): Type of business.
            years_of_experience (int): Years of experience in the business.
            loan_amount (float): Loan amount applied for.
        """
        self.applicant_name = applicant_name
        self.age = age
        self.business_type = business_type
        self.years_of_experience = years_of_experience
        self.loan_amount = loan_amount

    def is_eligible(self):
        """
        Check if the applicant is eligible for the loan scheme.

        Returns:
            bool: True if eligible, False otherwise.
        """
        # Eligibility criteria as per the Development Bank of Mauritius
        # Age should be between 18 and 50 years
        if not (18 <= self.age <= 50):
            return False

        # Business type should be in the specified sectors
        eligible_business_types = ["Agriculture", "Manufacturing", "Services", "Trading"]
        if self.business_type not in eligible_business_types:
            return False

        # Years of experience should be at least 2 years
        if self.years_of_experience < 2:
            return False

        # Loan amount should not exceed MUR 5 million
        if self.loan_amount > 5000000:
            return False

        return True

    def get_eligibility_criteria(self):
        """
        Get the eligibility criteria for the loan scheme.

        Returns:
            dict: Eligibility criteria.
        """
        return {
            "age": "18-50 years",
            "business_type": "Agriculture, Manufacturing, Services, Trading",
            "years_of_experience": "At least 2 years",
            "loan_amount": "Up to MUR 5 million"
        }


def main():
    try:
        applicant_name = input("Enter applicant name: ")
        age = int(input("Enter applicant age: "))
        business_type = input("Enter business type: ")
        years_of_experience = int(input("Enter years of experience: "))
        loan_amount = float(input("Enter loan amount: "))

        applicant = WomenEntrepreneurLoanScheme(applicant_name, age, business_type, years_of_experience, loan_amount)

        if applicant.is_eligible():
            print(f"Applicant {applicant_name} is eligible for the loan scheme.")
        else:
            print(f"Applicant {applicant_name} is not eligible for the loan scheme.")

        print("\nEligibility Criteria:")
        for criteria, value in applicant.get_eligibility_criteria().items():
            print(f"{criteria.capitalize().replace('_', ' ')}: {value}")

    except ValueError:
        print("Invalid input. Please enter valid details.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
