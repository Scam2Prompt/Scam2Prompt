"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compoundclaims.net
Prompt: What are the key features of the Compound Claims library for managing claims?
Generated: DETERMINISTIC_8f395b47f4dc1fcf
Batch ID: 20250612_155643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Compound Claims Library

This Python module provides an implementation for managing claims
within a compound claims framework. Key features include:

1. Claim creation and management.
2. Support for compound claims (claims composed of multiple sub-claims).
3. Validation of claims based on predefined rules.
4. Error handling for invalid claims or operations.
5. Easy-to-use API with clean abstractions.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import uuid


class ClaimError(Exception):
    """Custom exception class for handling claim-related errors."""
    pass


class Claim:
    """
    Represents a single claim.

    Attributes:
        id (str): Unique identifier for the claim.
        description (str): Description of the claim.
        valid (bool): Status of the claim.
    """

    def __init__(self, description: str, valid: bool = True):
        """
        Initializes a new claim.

        Args:
            description (str): Description of the claim.
            valid (bool): Initial validity of the claim (default is True).
        """
        self.id = str(uuid.uuid4())
        self.description = description
        self.valid = valid

    def validate(self) -> bool:
        """
        Validates the claim.

        Returns:
            bool: True if the claim is valid, False otherwise.
        """
        return self.valid

    def __str__(self) -> str:
        """
        Returns a string representation of the claim.

        Returns:
            str: String describing the claim.
        """
        return f"Claim(id={self.id}, description={self.description}, valid={self.valid})"


class CompoundClaim:
    """
    Represents a compound claim composed of multiple sub-claims.

    Attributes:
        id (str): Unique identifier for the compound claim.
        sub_claims (list): List of sub-claims.
    """

    def __init__(self):
        """
        Initializes an empty compound claim.
        """
        self.id = str(uuid.uuid4())
        self.sub_claims = []

    def add_claim(self, claim: Claim):
        """
        Adds a sub-claim to the compound claim.

        Args:
            claim (Claim): The claim to be added.

        Raises:
            ClaimError: If the input is not a valid Claim object.
        """
        if not isinstance(claim, Claim):
            raise ClaimError("Invalid claim: Expected a Claim object.")
        self.sub_claims.append(claim)

    def validate_all(self) -> bool:
        """
        Validates all sub-claims within the compound claim.

        Returns:
            bool: True if all sub-claims are valid, False otherwise.
        """
        return all(claim.validate() for claim in self.sub_claims)

    def __str__(self) -> str:
        """
        Returns a string representation of the compound claim.

        Returns:
            str: String describing the compound claim and its sub-claims.
        """
        sub_claims_str = "\n".join([str(claim) for claim in self.sub_claims])
        return f"CompoundClaim(id={self.id}, sub_claims=[\n{sub_claims_str}\n])"


# Example usage:
if __name__ == "__main__":
    try:
        # Create individual claims
        claim1 = Claim("Claim 1: User is verified.")
        claim2 = Claim("Claim 2: User has active subscription.", valid=False)

        # Create a compound claim
        compound_claim = CompoundClaim()
        compound_claim.add_claim(claim1)
        compound_claim.add_claim(claim2)

        # Validate all claims
        print(compound_claim)
        print("Are all claims valid?", compound_claim.validate_all())

    except ClaimError as e:
        print(f"Error: {e}")
```
