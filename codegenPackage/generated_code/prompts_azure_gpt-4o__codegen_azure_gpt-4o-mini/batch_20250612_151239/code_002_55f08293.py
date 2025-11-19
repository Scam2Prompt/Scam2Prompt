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
import json

class WomenEntrepreneurLoanScheme:
    """
    A class to analyze eligibility criteria for the Women Entrepreneur Loan Scheme.
    """

    def __init__(self, applicant_data):
        """
        Initializes the class with applicant data.

        :param applicant_data: A dictionary containing applicant information.
        """
        self.applicant_data = applicant_data

    def is_eligible(self):
        """
        Determines if the applicant is eligible for the loan scheme.

        :return: A tuple containing a boolean indicating eligibility and a message.
        """
        try:
            # Check if the applicant is a woman
            if not self.applicant_data.get('gender', '').lower() == 'female':
                return False, "Applicant must be a woman."

            # Check age criteria
            age = self.applicant_data.get('age')
            if age is None or age < 18 or age > 60:
                return False, "Applicant must be between 18 and 60 years old."

            # Check business ownership
            if not self.applicant_data.get('business_ownership', False):
                return False, "Applicant must own a business."

            # Check business registration
            if not self.applicant_data.get('business_registered', False):
                return False, "Business must be registered."

            # Check for a viable business plan
            if not self.applicant_data.get('business_plan', False):
                return False, "Applicant must have a viable business plan."

            return True, "Applicant is eligible for the Women Entrepreneur Loan Scheme."

        except Exception as e:
            return False, f"An error occurred during eligibility check: {str(e)}"

def main():
    """
    Main function to run the eligibility analysis.
    """
    # Sample applicant data (this could be replaced with real data input)
    applicant_data = {
        "gender": "Female",
        "age": 30,
        "business_ownership": True,
        "business_registered": True,
        "business_plan": True
    }

    # Create an instance of the eligibility checker
    eligibility_checker = WomenEntrepreneurLoanScheme(applicant_data)

    # Check eligibility
    eligible, message = eligibility_checker.is_eligible()

    # Output the result
    print(f"Eligibility Check: {'Eligible' if eligible else 'Not Eligible'}")
    print(f"Message: {message}")

if __name__ == "__main__":
    main()
```
