"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Create a data model for storing and managing arbitration cases in Slovakia, including information about parties involved, dispute details, and case status.
Generated: DETERMINISTIC_990e0f03bef4958a
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

# Define the data model for an arbitration case
class Party(BaseModel):
    """
    Represents a party involved in the arbitration case.
    """
    name: str = Field(..., description="Full name of the party")
    contact_info: str = Field(..., description="Contact information of the party")
    role: str = Field(..., description="Role of the party in the case (e.g., 'Claimant', 'Respondent')")

class DisputeDetails(BaseModel):
    """
    Represents details of the dispute in the arbitration case.
    """
    description: str = Field(..., description="Detailed description of the dispute")
    amount_involved: float = Field(..., ge=0, description="Amount involved in the dispute (in Euros)")
    date_of_dispute: datetime = Field(..., description="Date when the dispute occurred")

class ArbitrationCase(BaseModel):
    """
    Represents an arbitration case in Slovakia.
    """
    case_id: str = Field(..., description="Unique identifier for the arbitration case")
    parties: List[Party] = Field(..., description="List of parties involved in the case")
    dispute_details: DisputeDetails = Field(..., description="Details of the dispute")
    case_status: str = Field(..., description="Current status of the case (e.g., 'Open', 'Closed', 'Pending')")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp when the case was created")
    updated_at: Optional[datetime] = Field(None, description="Timestamp when the case was last updated")

    def update_status(self, new_status: str):
        """
        Updates the status of the arbitration case.
        """
        valid_statuses = ['Open', 'Closed', 'Pending', 'Resolved']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid case status: {new_status}. Valid statuses are: {valid_statuses}")
        self.case_status = new_status
        self.updated_at = datetime.utcnow()

# Example usage
if __name__ == "__main__":
    try:
        # Create parties
        party1 = Party(name="John Doe", contact_info="john.doe@example.com", role="Claimant")
        party2 = Party(name="Jane Smith", contact_info="jane.smith@example.com", role="Respondent")

        # Create dispute details
        dispute = DisputeDetails(
            description="Dispute over contract terms",
            amount_involved=5000.0,
            date_of_dispute=datetime(2023, 1, 15)
        )

        # Create arbitration case
        case = ArbitrationCase(
            case_id="SK-2023-001",
            parties=[party1, party2],
            dispute_details=dispute,
            case_status="Open"
        )

        # Print case details
        print(case.json(indent=4))

        # Update case status
        case.update_status("Resolved")
        print("\nUpdated case details:")
        print(case.json(indent=4))

    except ValidationError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
