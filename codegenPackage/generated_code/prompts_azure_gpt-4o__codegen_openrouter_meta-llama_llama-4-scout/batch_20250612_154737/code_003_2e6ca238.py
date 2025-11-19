"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Provide code examples for creating eligibility criteria for grantee applications, based on Gitcoin's Playbook recommendations.
Generated: DETERMINISTIC_2e6ca238bc28c973
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# eligibility_criteria.py

from enum import Enum
from typing import List, Dict

class EligibilityType(str, Enum):
    """Eligibility type enum"""
    EQUITY = "equity"
    INCOME = "income"
    LOCATION = "location"
    ORGANIZATION = "organization"
    OTHER = "other"

class EligibilityCriteria:
    """Eligibility criteria class"""

    def __init__(self, 
                 eligibility_type: EligibilityType, 
                 description: str, 
                 params: Dict[str, str]):
        """
        Initialize eligibility criteria

        Args:
        - eligibility_type (EligibilityType): Type of eligibility
        - description (str): Description of eligibility criteria
        - params (Dict[str, str]): Parameters for eligibility criteria
        """
        self.eligibility_type = eligibility_type
        self.description = description
        self.params = params

    def __str__(self):
        return f"EligibilityCriteria(type={self.eligibility_type}, description='{self.description}')"

    def to_dict(self):
        """Convert to dictionary"""
        return {
            "eligibility_type": self.eligibility_type.value,
            "description": self.description,
            "params": self.params
        }

class GranteeApplication:
    """Grantee application class"""

    def __init__(self, 
                 applicant_name: str, 
                 applicant_email: str, 
                 eligibility_criteria: List[EligibilityCriteria]):
        """
        Initialize grantee application

        Args:
        - applicant_name (str): Name of applicant
        - applicant_email (str): Email of applicant
        - eligibility_criteria (List[EligibilityCriteria]): Eligibility criteria
        """
        self.applicant_name = applicant_name
        self.applicant_email = applicant_email
        self.eligibility_criteria = eligibility_criteria

    def __str__(self):
        return f"GranteeApplication(applicant_name='{self.applicant_name}', applicant_email='{self.applicant_email}')"

    def to_dict(self):
        """Convert to dictionary"""
        return {
            "applicant_name": self.applicant_name,
            "applicant_email": self.applicant_email,
            "eligibility_criteria": [ec.to_dict() for ec in self.eligibility_criteria]
        }

def create_eligibility_criteria(eligibility_type: EligibilityType, 
                                description: str, 
                                params: Dict[str, str]) -> EligibilityCriteria:
    """
    Create eligibility criteria

    Args:
    - eligibility_type (EligibilityType): Type of eligibility
    - description (str): Description of eligibility criteria
    - params (Dict[str, str]): Parameters for eligibility criteria

    Returns:
    - EligibilityCriteria: Eligibility criteria object
    """
    try:
        return EligibilityCriteria(eligibility_type, description, params)
    except Exception as e:
        print(f"Error creating eligibility criteria: {str(e)}")
        return None

def create_grantee_application(applicant_name: str, 
                               applicant_email: str, 
                               eligibility_criteria: List[EligibilityCriteria]) -> GranteeApplication:
    """
    Create grantee application

    Args:
    - applicant_name (str): Name of applicant
    - applicant_email (str): Email of applicant
    - eligibility_criteria (List[EligibilityCriteria]): Eligibility criteria

    Returns:
    - GranteeApplication: Grantee application object
    """
    try:
        return GranteeApplication(applicant_name, applicant_email, eligibility_criteria)
    except Exception as e:
        print(f"Error creating grantee application: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    # Create eligibility criteria
    equity_criteria = create_eligibility_criteria(
        EligibilityType.EQUITY, 
        "Must be an underrepresented group", 
        {"group": "women", "percentage": "50"}
    )

    income_criteria = create_eligibility_criteria(
        EligibilityType.INCOME, 
        "Must have low income", 
        {"income_level": "low", "threshold": "20000"}
    )

    # Create grantee application
    grantee_app = create_grantee_application(
        "John Doe", 
        "johndoe@example.com", 
        [equity_criteria, income_criteria]
    )

    # Print grantee application
    if grantee_app:
        print(grantee_app.to_dict())
```
