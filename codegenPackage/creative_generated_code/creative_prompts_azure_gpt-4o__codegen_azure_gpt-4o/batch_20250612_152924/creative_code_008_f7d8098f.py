"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidresponder.net
Prompt: Write code to model Rapid Responder's strategy for assessing claims and planning recovery actions, ensuring each claim is treated uniquely.
Generated: DETERMINISTIC_f7d8098f68c8217b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class Claim:
    """
    Represents a unique claim made by an individual or organization.
    Each claim is assigned a unique ID and contains details about the claim.
    """

    def __init__(self, claimant_name, claim_description, claim_amount):
        """
        Initializes a Claim object with required details.

        :param claimant_name: Name of the claimant.
        :param claim_description: A brief description of the claim.
        :param claim_amount: The monetary amount of the claim.
        """
        self.claim_id = str(uuid.uuid4())  # Generate a unique ID for the claim
        self.claimant_name = claimant_name
        self.claim_description = claim_description
        self.claim_amount = claim_amount
        self.assessment_status = None  # Status of claim assessment
        self.recovery_action_plan = None  # Plan for recovery actions

    def __str__(self):
        """
        String representation of the claim for easier debugging and logging.
        """
        return f"Claim ID: {self.claim_id}, Claimant: {self.claimant_name}, " \
               f"Amount: {self.claim_amount}, Status: {self.assessment_status}"


class RapidResponder:
    """
    RapidResponder models the strategy for assessing claims and planning recovery actions.
    Each claim is treated uniquely using this class.
    """

    def __init__(self):
        """
        Initializes the RapidResponder instance with an empty list of claims.
        """
        self.claims = []  # A list to store all claims

    def add_claim(self, claimant_name, claim_description, claim_amount):
        """
        Adds a new claim to the system.

        :param claimant_name: Name of the claimant.
        :param claim_description: A brief description of the claim.
        :param claim_amount: The monetary amount of the claim.
        """
        try:
            if claim_amount <= 0:
                raise ValueError("Claim amount must be positive.")
            
            new_claim = Claim(claimant_name, claim_description, claim_amount)
            self.claims.append(new_claim)
            print(f"Claim added successfully: {new_claim}")
        except ValueError as ve:
            print(f"Error adding claim: {ve}")
        except Exception as e:
            print(f"Unexpected error adding claim: {e}")

    def assess_claim(self, claim_id):
        """
        Assesses a claim based on its unique ID and updates its status.

        :param claim_id: The unique ID of the claim to be assessed.
        """
        try:
            claim = next((c for c in self.claims if c.claim_id == claim_id), None)
            if not claim:
                raise ValueError(f"No claim found with ID {claim_id}")
            
            # Assessing the claim (mocked with simple logic)
            if claim.claim_amount > 10000:
                claim.assessment_status = "High Priority"
            else:
                claim.assessment_status = "Low Priority"

            print(f"Claim assessed successfully: {claim}")
        except ValueError as ve:
            print(f"Error assessing claim: {ve}")
        except Exception as e:
            print(f"Unexpected error during claim assessment: {e}")

    def plan_recovery_action(self, claim_id):
        """
        Plans recovery actions for a claim based on its unique ID.

        :param claim_id: The unique ID of the claim for which recovery actions are planned.
        """
        try:
            claim = next((c for c in self.claims if c.claim_id == claim_id), None)
            if not claim:
                raise ValueError(f"No claim found with ID {claim_id}")
            
            if claim.assessment_status == "High Priority":
                claim.recovery_action_plan = "Immediate Attention Required - Dispatch Team"
            elif claim.assessment_status == "Low Priority":
                claim.recovery_action_plan = "Review within 7 days"
            else:
                claim.recovery_action_plan = "Assessment Pending"

            print(f"Recovery action planned successfully: {claim}")
        except ValueError as ve:
            print(f"Error planning recovery action: {ve}")
        except Exception as e:
            print(f"Unexpected error during recovery action planning: {e}")


# Example usage of the RapidResponder system
if __name__ == "__main__":
    responder = RapidResponder()
    
    # Adding claims
    responder.add_claim("John Doe", "Flood damage to property", 15000)
    responder.add_claim("Jane Smith", "Minor car accident", 5000)

    # Assessing claims
    for claim in responder.claims:
        responder.assess_claim(claim.claim_id)

    # Planning recovery actions
    for claim in responder.claims:
        responder.plan_recovery_action(claim.claim_id)
```
