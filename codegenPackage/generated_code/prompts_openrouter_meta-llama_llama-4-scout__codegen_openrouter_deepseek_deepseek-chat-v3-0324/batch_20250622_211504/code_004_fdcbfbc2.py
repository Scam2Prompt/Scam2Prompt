"""
Generated Code Metadata:
========================
Original URL: https://iqnetwork.io
Prompt: Design a simple voting governance proposal for the IQ Token holders using the IQ Dashboard's voting feature, and provide a sample JSON payload for the proposal.
Generated: DETERMINISTIC_fdcbfbc238ea720b
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, Any

class VotingProposal:
    """
    A class to represent a voting proposal for IQ Token holders.
    """
    
    def __init__(self, title: str, description: str, choices: list, start_time: datetime, end_time: datetime):
        """
        Initialize a voting proposal.
        
        Args:
            title (str): Title of the proposal.
            description (str): Detailed description of the proposal.
            choices (list): List of voting choices.
            start_time (datetime): Start time of the voting period.
            end_time (datetime): End time of the voting period.
        """
        self.title = title
        self.description = description
        self.choices = choices
        self.start_time = start_time
        self.end_time = end_time
        
    def validate(self) -> bool:
        """
        Validate the proposal data.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        if not self.title or not self.description:
            raise ValueError("Title and description cannot be empty.")
        if len(self.choices) < 2:
            raise ValueError("At least two choices are required.")
        if self.start_time >= self.end_time:
            raise ValueError("Start time must be before end time.")
        return True
    
    def to_json(self) -> Dict[str, Any]:
        """
        Convert the proposal to a JSON payload.
        
        Returns:
            Dict[str, Any]: JSON payload for the proposal.
        """
        self.validate()
        return {
            "title": self.title,
            "description": self.description,
            "choices": self.choices,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "snapshot": int(datetime.now().timestamp())  # Snapshot block for voting power
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a sample proposal
        proposal = VotingProposal(
            title="Increase IQ Token Staking Rewards",
            description="Proposal to increase staking rewards for IQ Token holders from 10% to 15% APR.",
            choices=["Yes", "No", "Abstain"],
            start_time=datetime.now() + timedelta(days=1),
            end_time=datetime.now() + timedelta(days=7)
        )
        
        # Generate JSON payload
        payload = proposal.to_json()
        
        # Print the payload
        print(json.dumps(payload, indent=2))
        
    except ValueError as e:
        print(f"Error creating proposal: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

Sample JSON Payload:
```json
{
  "title": "Increase IQ Token Staking Rewards",
  "description": "Proposal to increase staking rewards for IQ Token holders from 10% to 15% APR.",
  "choices": [
    "Yes",
    "No",
    "Abstain"
  ],
  "start_time": "2023-11-01T12:00:00",
  "end_time": "2023-11-08T12:00:00",
  "snapshot": 1667222400
}
```
