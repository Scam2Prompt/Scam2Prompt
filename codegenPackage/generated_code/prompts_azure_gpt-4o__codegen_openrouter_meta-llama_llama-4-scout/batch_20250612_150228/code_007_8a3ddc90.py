"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Provide an example of a governance proposal for adjusting collateral factors at the Silo level in the Silo Finance protocol.
Generated: DETERMINISTIC_8a3ddc90d897cbe0
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Governance Proposal: Adjust Collateral Factors at Silo Level
# ============================================================

from dataclasses import dataclass
from enum import Enum
from typing import List

# Define the Silo Finance protocol's supported collateral types
class CollateralType(str, Enum):
    """Supported collateral types in the Silo Finance protocol."""
    SILO = "silo"
    OTHER = "other"

# Define a dataclass for collateral factor adjustments
@dataclass
class CollateralFactorAdjustment:
    """Dataclass representing a collateral factor adjustment proposal."""
    collateral_type: CollateralType
    new_collateral_factor: float  # in percentage (e.g., 50.0 for 50%)

# Define a class for governance proposals
class GovernanceProposal:
    """Class representing a governance proposal for adjusting collateral factors."""
    def __init__(self, proposal_id: str, description: str, adjustments: List[CollateralFactorAdjustment]):
        """
        Initializes a governance proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.
        - description (str): Human-readable description of the proposal.
        - adjustments (List[CollateralFactorAdjustment]): List of collateral factor adjustments.
        """
        self.proposal_id = proposal_id
        self.description = description
        self.adjustments = adjustments

    def validate(self) -> bool:
        """
        Validates the governance proposal.

        Returns:
        - bool: True if the proposal is valid, False otherwise.
        """
        if not self.proposal_id:
            return False
        if not self.description:
            return False
        if not self.adjustments:
            return False

        for adjustment in self.adjustments:
            if adjustment.new_collateral_factor < 0.0 or adjustment.new_collateral_factor > 100.0:
                return False  # Collateral factor must be between 0% and 100%

        return True

    def execute(self) -> None:
        """
        Executes the governance proposal by adjusting collateral factors.

        Raises:
        - Exception: If the proposal is invalid or execution fails.
        """
        if not self.validate():
            raise Exception("Invalid proposal")

        try:
            # Simulate adjusting collateral factors (replace with actual implementation)
            for adjustment in self.adjustments:
                print(f"Adjusting collateral factor for {adjustment.collateral_type}: {adjustment.new_collateral_factor}%")
        except Exception as e:
            raise Exception(f"Execution failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    proposal_id = "silo-001"
    description = "Adjust collateral factors for Silo Finance protocol"
    adjustments = [
        CollateralFactorAdjustment(CollateralType.SILO, 50.0),
        CollateralFactorAdjustment(CollateralType.OTHER, 30.0)
    ]

    proposal = GovernanceProposal(proposal_id, description, adjustments)
    proposal.execute()
```
