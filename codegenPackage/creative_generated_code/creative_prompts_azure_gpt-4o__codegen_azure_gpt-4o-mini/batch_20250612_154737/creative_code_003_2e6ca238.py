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

```python
class GranteeApplication:
    """
    A class representing a grantee application with eligibility criteria
    based on Gitcoin's Playbook recommendations.
    """

    def __init__(self, applicant_name: str, project_title: str, funding_required: float, 
                 project_type: str, experience_years: int, has_community_support: bool):
        """
        Initializes a new GranteeApplication instance.

        :param applicant_name: Name of the applicant
        :param project_title: Title of the project
        :param funding_required: Amount of funding requested
        :param project_type: Type of project (e.g., "open-source", "research", etc.)
        :param experience_years: Number of years of relevant experience
        :param has_community_support: Whether the applicant has community support
        """
        self.applicant_name = applicant_name
        self.project_title = project_title
        self.funding_required = funding_required
        self.project_type = project_type
        self.experience_years = experience_years
        self.has_community_support = has_community_support

    def is_eligible(self) -> bool:
        """
        Evaluates the eligibility of the application based on set criteria.

        :return: True if the application is eligible, False otherwise
        """
        try:
            # Check if funding required is within acceptable limits
            if not (0 < self.funding_required <= 50000):
                raise ValueError("Funding required must be between 1 and 50,000.")

            # Check project type eligibility
            eligible_project_types = ["open-source", "research", "education"]
            if self.project_type not in eligible_project_types:
                raise ValueError(f"Project type must be one of {eligible_project_types}.")

            # Check experience requirement
            if self.experience_years < 2:
                raise ValueError("Applicant must have at least 2 years of relevant experience.")

            # Check for community support
            if not self.has_community_support:
                raise ValueError("Applicant must have community support.")

            # If all criteria are met, the application is eligible
            return True

        except ValueError as ve:
            print(f"Eligibility check failed: {ve}")
            return False

# Example usage:
if __name__ == "__main__":
    try:
        application = GranteeApplication(
            applicant_name="Alice Doe",
            project_title="Innovative Open Source Tool",
            funding_required=25000,
            project_type="open-source",
            experience_years=3,
            has_community_support=True
        )

        if application.is_eligible():
            print("The application is eligible for funding.")
        else:
            print("The application is not eligible for funding.")
    
    except Exception as e:
        print(f"An error occurred while processing the application: {e}")
```
