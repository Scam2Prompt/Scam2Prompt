"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: Provide code examples for creating eligibility criteria for grantee applications, based on Gitcoin's Playbook recommendations.
Generated: DETERMINISTIC_2e6ca238bc28c973
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python implementation for eligibility criteria based on Gitcoin's Playbook recommendations. Note that the code adheres to your requirements:

```python
import re

class GranteeApplication:
    """
    Class to handle grantee application eligibility checks
    based on Gitcoin's Playbook recommendations.
    """

    def __init__(self, applicant_name, applicant_email, project_description, funding_requested, credibility_score):
        """
        Initialize the grantee application with required fields.

        :param applicant_name: Full name of the applicant (string).
        :param applicant_email: Email address of the applicant (string).
        :param project_description: Brief description of the project (string).
        :param funding_requested: Amount of funding requested (float).
        :param credibility_score: Credibility score of the applicant (integer between 0 and 100).
        """
        self.applicant_name = applicant_name
        self.applicant_email = applicant_email
        self.project_description = project_description
        self.funding_requested = funding_requested
        self.credibility_score = credibility_score

    def validate_email(self):
        """
        Validates the email format using a regex pattern.

        :return: True if the email format is valid, False otherwise.
        """
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(email_pattern, self.applicant_email))

    def check_eligibility(self):
        """
        Perform eligibility checks based on the following criteria:
        1. Applicant must have a valid email address.
        2. Project description must be at least 50 characters long.
        3. Funding requested must be greater than 0 and less than or equal to $100,000.
        4. Credibility score must be 70 or higher.

        :return: Tuple (is_eligible: bool, message: str).
        """
        # Validate email
        if not self.validate_email():
            return False, "Invalid email format."

        # Validate project description length
        if len(self.project_description) < 50:
            return False, "Project description must be at least 50 characters long."

        # Validate funding requested
        if self.funding_requested <= 0 or self.funding_requested > 100000:
            return False, "Funding requested must be between $1 and $100,000."

        # Validate credibility score
        if self.credibility_score < 70:
            return False, "Credibility score must be 70 or higher."

        # Passed all checks
        return True, "Application is eligible."

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of GranteeApplication
        application = GranteeApplication(
            applicant_name="Jane Doe",
            applicant_email="jane.doe@example.com",
            project_description="This project aims to improve access to education in rural areas using innovative technology.",
            funding_requested=50000,
            credibility_score=85
        )

        # Check eligibility
        is_eligible, message = application.check_eligibility()
        print(f"Eligibility: {is_eligible}, Message: {message}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
```

This code is structured to meet all the requirements while ensuring clarity and production-readiness.
