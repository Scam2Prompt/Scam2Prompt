"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Generate a sample insurance policy document in Spanish for a homeowner's insurance plan in Torreón, Coahuila, Mexico, incorporating details like coverage for natural disasters and theft.
Generated: DETERMINISTIC_78013a1671c1fe2a
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class InsurancePolicy:
    def __init__(self, policy_holder, address, coverage_details):
        """
        Initialize the insurance policy with the policy holder's information,
        address, and coverage details.

        :param policy_holder: str - Name of the policy holder
        :param address: str - Address of the insured property
        :param coverage_details: dict - Details of the coverage
        """
        self.policy_holder = policy_holder
        self.address = address
        self.coverage_details = coverage_details
        self.policy_number = self.generate_policy_number()
        self.issue_date = datetime.now().strftime("%Y-%m-%d")

    def generate_policy_number(self):
        """
        Generate a unique policy number.

        :return: str - A unique policy number
        """
        return f"POL-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def to_json(self):
        """
        Convert the policy details to a JSON format.

        :return: str - JSON representation of the policy
        """
        policy_data = {
            "policy_number": self.policy_number,
            "policy_holder": self.policy_holder,
            "address": self.address,
            "issue_date": self.issue_date,
            "coverage_details": self.coverage_details
        }
        return json.dumps(policy_data, ensure_ascii=False, indent=4)

def create_homeowners_insurance_policy():
    """
    Create a sample homeowner's insurance policy document in Spanish.

    :return: str - JSON representation of the insurance policy
    """
    try:
        policy_holder = "Juan Pérez"
        address = "Calle Falsa 123, Torreón, Coahuila, México"
        coverage_details = {
            "cobertura_por_desastres_naturales": "Hasta $1,000,000 MXN",
            "cobertura_por_robo": "Hasta $500,000 MXN",
            "responsabilidad_civil": "Hasta $1,000,000 MXN",
            "cobertura_adicional": "Incendio, inundación, y terremoto"
        }

        # Create the insurance policy
        policy = InsurancePolicy(policy_holder, address, coverage_details)

        # Return the policy in JSON format
        return policy.to_json()

    except Exception as e:
        # Handle any exceptions that may occur
        return json.dumps({"error": str(e)}, ensure_ascii=False)

if __name__ == "__main__":
    # Generate and print the insurance policy
    policy_document = create_homeowners_insurance_policy()
    print(policy_document)
```
