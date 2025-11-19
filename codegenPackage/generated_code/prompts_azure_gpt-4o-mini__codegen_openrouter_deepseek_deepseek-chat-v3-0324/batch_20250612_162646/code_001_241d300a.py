"""
Generated Code Metadata:
========================
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: What steps are involved in creating a proposal within the Futarchy framework on MetaDAO?
Generated: DETERMINISTIC_241d300ab217535c
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from typing import Dict, Any, Optional
from dataclasses import dataclass
import hashlib
import json
from datetime import datetime, timedelta

@dataclass
class Proposal:
    """
    Represents a proposal within the Futarchy framework on MetaDAO.
    """
    title: str
    description: str
    market_question: str
    creator: str
    creation_time: datetime
    voting_period: timedelta
    resolution_time: Optional[datetime] = None
    proposal_id: Optional[str] = None
    status: str = "draft"

class MetaDAO:
    """
    A class representing the MetaDAO and its Futarchy proposal system.
    """
    
    def __init__(self):
        self.proposals: Dict[str, Proposal] = {}
    
    def create_proposal(
        self,
        title: str,
        description: str,
        market_question: str,
        creator: str,
        voting_period_days: int = 7
    ) -> Proposal:
        """
        Creates a new proposal in the Futarchy framework.
        
        Args:
            title: Short title of the proposal
            description: Detailed description of the proposal
            market_question: The market prediction question for Futarchy
            creator: Address or identifier of the proposal creator
            voting_period_days: Duration of voting period in days (default: 7)
            
        Returns:
            The created Proposal object
            
        Raises:
            ValueError: If any required field is empty or invalid
        """
        # Validate inputs
        if not all([title, description, market_question, creator]):
            raise ValueError("All proposal fields must be non-empty")
            
        if voting_period_days <= 0:
            raise ValueError("Voting period must be positive")
            
        # Create proposal
        now = datetime.utcnow()
        voting_period = timedelta(days=voting_period_days)
        
        proposal = Proposal(
            title=title,
            description=description,
            market_question=market_question,
            creator=creator,
            creation_time=now,
            voting_period=voting_period
        )
        
        # Generate unique ID
        proposal_data = f"{title}{description}{market_question}{creator}{now.isoformat()}"
        proposal.proposal_id = hashlib.sha256(proposal_data.encode()).hexdigest()
        
        # Store proposal
        self.proposals[proposal.proposal_id] = proposal
        
        return proposal
    
    def submit_proposal(self, proposal_id: str) -> Proposal:
        """
        Submits a draft proposal to begin the voting process.
        
        Args:
            proposal_id: ID of the proposal to submit
            
        Returns:
            The updated Proposal object
            
        Raises:
            KeyError: If proposal with given ID doesn't exist
            ValueError: If proposal is not in draft status
        """
        if proposal_id not in self.proposals:
            raise KeyError(f"Proposal {proposal_id} not found")
            
        proposal = self.proposals[proposal_id]
        
        if proposal.status != "draft":
            raise ValueError("Only draft proposals can be submitted")
            
        proposal.status = "active"
        proposal.resolution_time = proposal.creation_time + proposal.voting_period
        
        return proposal
    
    def get_proposal(self, proposal_id: str) -> Proposal:
        """
        Retrieves a proposal by its ID.
        
        Args:
            proposal_id: ID of the proposal to retrieve
            
        Returns:
            The Proposal object
            
        Raises:
            KeyError: If proposal with given ID doesn't exist
        """
        if proposal_id not in self.proposals:
            raise KeyError(f"Proposal {proposal_id} not found")
            
        return self.proposals[proposal_id]
    
    def serialize_proposal(self, proposal: Proposal) -> Dict[str, Any]:
        """
        Serializes a proposal to a dictionary for storage or transmission.
        
        Args:
            proposal: Proposal object to serialize
            
        Returns:
            Dictionary containing proposal data
        """
        return {
            "proposal_id": proposal.proposal_id,
            "title": proposal.title,
            "description": proposal.description,
            "market_question": proposal.market_question,
            "creator": proposal.creator,
            "creation_time": proposal.creation_time.isoformat(),
            "voting_period": proposal.voting_period.total_seconds(),
            "resolution_time": proposal.resolution_time.isoformat() if proposal.resolution_time else None,
            "status": proposal.status
        }
    
    def deserialize_proposal(self, data: Dict[str, Any]) -> Proposal:
        """
        Deserializes a proposal from a dictionary.
        
        Args:
            data: Dictionary containing proposal data
            
        Returns:
            Reconstructed Proposal object
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        required_fields = [
            "title", "description", "market_question", "creator",
            "creation_time", "voting_period", "status"
        ]
        
        if not all(field in data for field in required_fields):
            raise ValueError("Missing required proposal fields")
            
        return Proposal(
            title=data["title"],
            description=data["description"],
            market_question=data["market_question"],
            creator=data["creator"],
            creation_time=datetime.fromisoformat(data["creation_time"]),
            voting_period=timedelta(seconds=data["voting_period"]),
            resolution_time=datetime.fromisoformat(data["resolution_time"]) if data["resolution_time"] else None,
            proposal_id=data.get("proposal_id"),
            status=data["status"]
        )

# Example usage
if __name__ == "__main__":
    metadao = MetaDAO()
    
    # Create a new proposal
    proposal = metadao.create_proposal(
        title="Increase Treasury Yield",
        description="Proposal to allocate 20% of treasury to yield-generating protocols",
        market_question="Will allocating 20% of treasury to yield protocols increase net treasury value by 10% in 6 months?",
        creator="0x123...abc"
    )
    
    print(f"Created proposal with ID: {proposal.proposal_id}")
    
    # Submit the proposal
    submitted_proposal = metadao.submit_proposal(proposal.proposal_id)
    print(f"Proposal status: {submitted_proposal.status}")
    
    # Serialize the proposal
    serialized = metadao.serialize_proposal(submitted_proposal)
    print("Serialized proposal:", json.dumps(serialized, indent=2))
```
