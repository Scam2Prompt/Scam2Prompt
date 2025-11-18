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
class Claim:
    """
    Represents a claim with details necessary for assessment and recovery actions.
    """
    def __init__(self, claim_id, claimant_name, claim_amount, severity_level):
        """
        Initializes a new claim with the given parameters.

        :param claim_id: Unique identifier for the claim
        :param claimant_name: Name of the claimant
        :param claim_amount: Amount claimed
        :param severity_level: Severity level of the claim (1-5)
        """
        self.claim_id = claim_id
        self.claimant_name = claimant_name
        self.claim_amount = claim_amount
        self.severity_level = severity_level

    def __str__(self):
        return f"Claim(ID: {self.claim_id}, Name: {self.claimant_name}, Amount: {self.claim_amount}, Severity: {self.severity_level})"


class ClaimHandler:
    """
    Handles the assessment and recovery actions for claims.
    """
    def __init__(self):
        self.claims = {}

    def add_claim(self, claim):
        """
        Adds a claim to the handler.

        :param claim: An instance of Claim to be added
        """
        if not isinstance(claim, Claim):
            raise TypeError("Expected an instance of Claim.")
        self.claims[claim.claim_id] = claim

    def assess_claim(self, claim_id):
        """
        Assess the claim and determine recovery actions based on severity.

        :param claim_id: The ID of the claim to assess
        :return: Recovery actions as a string
        """
        claim = self.claims.get(claim_id)
        if claim is None:
            raise ValueError(f"No claim found with ID: {claim_id}")

        recovery_actions = self._determine_recovery_actions(claim.severity_level)
        return f"Claim ID: {claim_id} requires the following actions: {recovery_actions}"

    def _determine_recovery_actions(self, severity_level):
        """
        Determines recovery actions based on the severity level of the claim.

        :param severity_level: Severity level of the claim (1-5)
        :return: Suggested recovery actions
        """
        action_plan = {
            1: "Monitor the situation.",
            2: "Contact the claimant for more information.",
            3: "Initiate a preliminary investigation.",
            4: "Engage a recovery team for intervention.",
            5: "Immediate action required; escalate to management."
        }
        return action_plan.get(severity_level, "No actions defined for this severity level.")

    def list_claims(self):
        """
        Lists all claims in the handler.

        :return: List of claims
        """
        return [str(claim) for claim in self.claims.values()]


# Example Usage
if __name__ == '__main__':
    claim_handler = ClaimHandler()

    # Adding claims
    try:
        claim_handler.add_claim(Claim(1, "Alice", 5000, 3))
        claim_handler.add_claim(Claim(2, "Bob", 15000, 5))
        claim_handler.add_claim(Claim(3, "Charlie", 1000, 1))

        # Assessing claims
        print(claim_handler.assess_claim(1))
        print(claim_handler.assess_claim(2))
        print(claim_handler.assess_claim(3))

        # Listing all claims
        print("All claims:")
        for claim in claim_handler.list_claims():
            print(claim)

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
```
