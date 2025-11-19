"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Develop a system to manage funding opportunities for research projects, referencing the funding details provided by ORIC.
Generated: DETERMINISTIC_7dc827068ea93bb3
Batch ID: 20250612_153224
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
from typing import List, Dict, Optional
import uuid
from enum import Enum

class FundingStatus(Enum):
    """Enum representing different funding statuses."""
    OPEN = "Open"
    CLOSED = "Closed"
    ANNOUNCED = "Announced"
    UNDER_REVIEW = "Under Review"
    AWARDED = "Awarded"

class FundingOpportunity:
    """Class representing a funding opportunity."""
    
    def __init__(
        self,
        title: str,
        description: str,
        funding_organization: str,
        deadline: str,
        amount: float,
        status: FundingStatus,
        eligibility_criteria: List[str],
        contact_email: str,
        tags: Optional[List[str]] = None
    ):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.funding_organization = funding_organization
        self.deadline = deadline
        self.amount = amount
        self.status = status
        self.eligibility_criteria = eligibility_criteria
        self.contact_email = contact_email
        self.tags = tags if tags else []
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert the funding opportunity to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "funding_organization": self.funding_organization,
            "deadline": self.deadline,
            "amount": self.amount,
            "status": self.status.value,
            "eligibility_criteria": self.eligibility_criteria,
            "contact_email": self.contact_email,
            "tags": self.tags,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def update(self, **kwargs) -> None:
        """Update the funding opportunity attributes."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now().isoformat()

class FundingOpportunityManager:
    """Class to manage funding opportunities."""
    
    def __init__(self, storage_file: str = "funding_opportunities.json"):
        self.storage_file = storage_file
        self.opportunities: Dict[str, FundingOpportunity] = {}
        self.load_opportunities()
    
    def load_opportunities(self) -> None:
        """Load funding opportunities from the storage file."""
        try:
            with open(self.storage_file, "r") as file:
                data = json.load(file)
                for opp_data in data:
                    opp = FundingOpportunity(
                        title=opp_data["title"],
                        description=opp_data["description"],
                        funding_organization=opp_data["funding_organization"],
                        deadline=opp_data["deadline"],
                        amount=opp_data["amount"],
                        status=FundingStatus(opp_data["status"]),
                        eligibility_criteria=opp_data["eligibility_criteria"],
                        contact_email=opp_data["contact_email"],
                        tags=opp_data.get("tags", [])
                    )
                    opp.id = opp_data["id"]
                    opp.created_at = opp_data["created_at"]
                    opp.updated_at = opp_data["updated_at"]
                    self.opportunities[opp.id] = opp
        except FileNotFoundError:
            # File doesn't exist yet, initialize with empty list
            self.save_opportunities()
        except json.JSONDecodeError:
            # File is corrupted, initialize with empty list
            self.opportunities = {}
            self.save_opportunities()
    
    def save_opportunities(self) -> None:
        """Save funding opportunities to the storage file."""
        with open(self.storage_file, "w") as file:
            json.dump(
                [opp.to_dict() for opp in self.opportunities.values()],
                file,
                indent=2
            )
    
    def add_opportunity(self, opportunity: FundingOpportunity) -> str:
        """Add a new funding opportunity."""
        if opportunity.id in self.opportunities:
            raise ValueError("Opportunity with this ID already exists.")
        self.opportunities[opportunity.id] = opportunity
        self.save_opportunities()
        return opportunity.id
    
    def get_opportunity(self, opportunity_id: str) -> Optional[FundingOpportunity]:
        """Get a funding opportunity by ID."""
        return self.opportunities.get(opportunity_id)
    
    def update_opportunity(self, opportunity_id: str, **kwargs) -> None:
        """Update a funding opportunity."""
        opportunity = self.get_opportunity(opportunity_id)
        if not opportunity:
            raise ValueError("Opportunity not found.")
        opportunity.update(**kwargs)
        self.save_opportunities()
    
    def delete_opportunity(self, opportunity_id: str) -> None:
        """Delete a funding opportunity."""
        if opportunity_id not in self.opportunities:
            raise ValueError("Opportunity not found.")
        del self.opportunities[opportunity_id]
        self.save_opportunities()
    
    def list_opportunities(
        self,
        status: Optional[FundingStatus] = None,
        organization: Optional[str] = None,
        tag: Optional[str] = None
    ) -> List[FundingOpportunity]:
        """List funding opportunities with optional filters."""
        opportunities = list(self.opportunities.values())
        
        if status:
            opportunities = [opp for opp in opportunities if opp.status == status]
        if organization:
            opportunities = [
                opp for opp in opportunities
                if opp.funding_organization.lower() == organization.lower()
            ]
        if tag:
            opportunities = [
                opp for opp in opportunities
                if tag.lower() in [t.lower() for t in opp.tags]
            ]
        
        return opportunities

# Example usage
if __name__ == "__main__":
    manager = FundingOpportunityManager()
    
    # Create a new opportunity
    new_opp = FundingOpportunity(
        title="Climate Change Research Grant",
        description="Funding for research on climate change impacts.",
        funding_organization="ORIC",
        deadline="2023-12-31",
        amount=50000.0,
        status=FundingStatus.OPEN,
        eligibility_criteria=["PhD holders", "University faculty"],
        contact_email="grants@oric.org",
        tags=["climate", "research"]
    )
    
    # Add to manager
    opp_id = manager.add_opportunity(new_opp)
    print(f"Added opportunity with ID: {opp_id}")
    
    # List all open opportunities
    open_opps = manager.list_opportunities(status=FundingStatus.OPEN)
    print(f"Open opportunities: {len(open_opps)}")
    
    # Update an opportunity
    manager.update_opportunity(opp_id, amount=55000.0)
    
    # Get an opportunity
    opp = manager.get_opportunity(opp_id)
    print(f"Updated amount: {opp.amount}")
    
    # Delete an opportunity
    manager.delete_opportunity(opp_id)
    print(f"Opportunity {opp_id} deleted")
```
