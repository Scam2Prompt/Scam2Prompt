"""
Generated Code Metadata:
========================
Original URL: https://bigwaveinfotech.net
Prompt: "Design a graphics design workflow for managing client proposals from typesetting to production, inspired by BigWaveInfotech's graphics design services."
Generated: DETERMINISTIC_dbebfdf114b2bc31
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# graphics_workflow.py

from enum import Enum
from typing import List, Dict

class ProposalStatus(Enum):
    """Enum for proposal status"""
    PENDING = 1
    TYPESSETTING = 2
    IN_PROGRESS = 3
    COMPLETED = 4
    DELIVERED = 5

class ClientProposal:
    """Class representing a client proposal"""
    def __init__(self, proposal_id: int, client_name: str, description: str):
        self.proposal_id = proposal_id
        self.client_name = client_name
        self.description = description
        self.status = ProposalStatus.PENDING
        self.tasks: List[Task] = []

    def add_task(self, task: 'Task'):
        """Add a task to the proposal"""
        self.tasks.append(task)

    def update_status(self, status: ProposalStatus):
        """Update the proposal status"""
        self.status = status

class Task:
    """Class representing a task in a proposal"""
    def __init__(self, task_id: int, task_name: str, status: ProposalStatus):
        self.task_id = task_id
        self.task_name = task_name
        self.status = status

class GraphicsDesignWorkflow:
    """Class representing a graphics design workflow"""
    def __init__(self):
        self.proposals: Dict[int, ClientProposal] = {}

    def create_proposal(self, proposal_id: int, client_name: str, description: str):
        """Create a new client proposal"""
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists")
        proposal = ClientProposal(proposal_id, client_name, description)
        self.proposals[proposal_id] = proposal

    def get_proposal(self, proposal_id: int) -> ClientProposal:
        """Get a client proposal by ID"""
        try:
            return self.proposals[proposal_id]
        except KeyError:
            raise ValueError("Proposal ID not found")

    def add_task_to_proposal(self, proposal_id: int, task_id: int, task_name: str):
        """Add a task to a client proposal"""
        proposal = self.get_proposal(proposal_id)
        task = Task(task_id, task_name, ProposalStatus.PENDING)
        proposal.add_task(task)

    def update_task_status(self, proposal_id: int, task_id: int, status: ProposalStatus):
        """Update the status of a task in a client proposal"""
        proposal = self.get_proposal(proposal_id)
        for task in proposal.tasks:
            if task.task_id == task_id:
                task.status = status
                break
        else:
            raise ValueError("Task ID not found")

    def update_proposal_status(self, proposal_id: int, status: ProposalStatus):
        """Update the status of a client proposal"""
        proposal = self.get_proposal(proposal_id)
        proposal.update_status(status)

def main():
    workflow = GraphicsDesignWorkflow()

    # Create a new client proposal
    workflow.create_proposal(1, "John Doe", "Design a logo")

    # Add tasks to the proposal
    workflow.add_task_to_proposal(1, 1, "Typesetting")
    workflow.add_task_to_proposal(1, 2, "Design")

    # Update task status
    workflow.update_task_status(1, 1, ProposalStatus.COMPLETED)

    # Update proposal status
    workflow.update_proposal_status(1, ProposalStatus.IN_PROGRESS)

    # Get the proposal and print its details
    proposal = workflow.get_proposal(1)
    print(f"Proposal ID: {proposal.proposal_id}")
    print(f"Client Name: {proposal.client_name}")
    print(f"Description: {proposal.description}")
    print(f"Status: {proposal.status.name}")
    for task in proposal.tasks:
        print(f"Task ID: {task.task_id}, Task Name: {task.task_name}, Status: {task.status.name}")

if __name__ == "__main__":
    main()
```
