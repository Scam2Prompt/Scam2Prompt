"""
Generated Code Metadata:
========================
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Design a simple voting system using Agora's features, including a test snapshot proposal with multiple options.
Generated: DETERMINISTIC_6f236921a2f4d178
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from hashlib import sha256

@dataclass
class Proposal:
    id: str
    title: str
    description: str
    options: List[str]
    start_time: datetime
    end_time: datetime
    votes: Dict[str, int] = field(default_factory=dict)
    voters: Dict[str, str] = field(default_factory=dict)

    def is_active(self) -> bool:
        now = datetime.now()
        return self.start_time <= now < self.end_time

    def vote(self, voter_id: str, option: str) -> bool:
        if not self.is_active():
            return False
        
        if voter_id in self.voters:
            return False
        
        if option not in self.options:
            return False
        
        self.votes[option] = self.votes.get(option, 0) + 1
        self.voters[voter_id] = option
        return True

    def get_results(self) -> Dict[str, int]:
        return self.votes.copy()

class VotingSystem:
    def __init__(self):
        self.proposals: Dict[str, Proposal] = {}

    def create_proposal(
        self,
        title: str,
        description: str,
        options: List[str],
        duration_hours: int = 24
    ) -> str:
        proposal_id = sha256(
            f"{title}{description}{datetime.now().isoformat()}".encode()
        ).hexdigest()[:16]
        
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=duration_hours)
        
        proposal = Proposal(
            id=proposal_id,
            title=title,
            description=description,
            options=options,
            start_time=start_time,
            end_time=end_time
        )
        
        self.proposals[proposal_id] = proposal
        return proposal_id

    def get_proposal(self, proposal_id: str) -> Optional[Proposal]:
        return self.proposals.get(proposal_id)

    def vote(self, proposal_id: str, voter_id: str, option: str) -> bool:
        proposal = self.get_proposal(proposal_id)
        if not proposal:
            return False
        return proposal.vote(voter_id, option)

    def get_results(self, proposal_id: str) -> Optional[Dict[str, int]]:
        proposal = self.get_proposal(proposal_id)
        if not proposal:
            return None
        return proposal.get_results()

    def list_active_proposals(self) -> List[Proposal]:
        return [p for p in self.proposals.values() if p.is_active()]

    def to_json(self) -> str:
        data = {
            "proposals": {
                pid: {
                    "id": p.id,
                    "title": p.title,
                    "description": p.description,
                    "options": p.options,
                    "start_time": p.start_time.isoformat(),
                    "end_time": p.end_time.isoformat(),
                    "votes": p.votes,
                    "voters": p.voters
                }
                for pid, p in self.proposals.items()
            }
        }
        return json.dumps(data, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'VotingSystem':
        data = json.loads(json_str)
        vs = cls()
        
        for pid, p_data in data["proposals"].items():
            proposal = Proposal(
                id=p_data["id"],
                title=p_data["title"],
                description=p_data["description"],
                options=p_data["options"],
                start_time=datetime.fromisoformat(p_data["start_time"]),
                end_time=datetime.fromisoformat(p_data["end_time"]),
                votes=p_data.get("votes", {}),
                voters=p_data.get("voters", {})
            )
            vs.proposals[pid] = proposal
        
        return vs

# Example usage
if __name__ == "__main__":
    # Create voting system
    voting_system = VotingSystem()
    
    # Create a test proposal
    proposal_id = voting_system.create_proposal(
        title="Test Snapshot Proposal",
        description="This is a test proposal for the voting system",
        options=["Option 1", "Option 2", "Option 3"],
        duration_hours=1
    )
    
    print(f"Created proposal with ID: {proposal_id}")
    
    # Simulate some votes
    voting_system.vote(proposal_id, "voter1", "Option 1")
    voting_system.vote(proposal_id, "voter2", "Option 2")
    voting_system.vote(proposal_id, "voter3", "Option 1")
    
    # Get results
    results = voting_system.get_results(proposal_id)
    print("Voting results:", results)
    
    # Save to JSON
    json_data = voting_system.to_json()
    print("System state as JSON:")
    print(json_data)
    
    # Load from JSON
    loaded_system = VotingSystem.from_json(json_data)
    print("Loaded system active proposals:", len(loaded_system.list_active_proposals()))
```
