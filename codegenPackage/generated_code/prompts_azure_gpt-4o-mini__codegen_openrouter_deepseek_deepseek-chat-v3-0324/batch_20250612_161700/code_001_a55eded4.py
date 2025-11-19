"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Write a Python script that automates the management of glass and aluminum project proposals, similar to the project management solutions provided by CristalesGraf.
Generated: DETERMINISTIC_a55eded4a91c7a7e
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

class ProposalManager:
    """
    A class to manage glass and aluminum project proposals.
    Handles creation, storage, retrieval, and updates of proposals.
    """

    def __init__(self, storage_file: str = "proposals.json"):
        """
        Initialize the ProposalManager with a storage file.
        
        Args:
            storage_file (str): Path to the JSON file storing proposals. Defaults to "proposals.json".
        """
        self.storage_file = storage_file
        self.proposals = self._load_proposals()

    def _load_proposals(self) -> Dict[str, Dict]:
        """
        Load proposals from the storage file.
        
        Returns:
            Dict[str, Dict]: Dictionary of proposals with proposal IDs as keys.
        
        Raises:
            FileNotFoundError: If the storage file does not exist.
            json.JSONDecodeError: If the storage file contains invalid JSON.
        """
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as file:
                    return json.load(file)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in {self.storage_file}: {e}", e.doc, e.pos)
        except Exception as e:
            raise Exception(f"Error loading proposals: {e}")

    def _save_proposals(self) -> None:
        """
        Save proposals to the storage file.
        
        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump(self.proposals, file, indent=4)
        except Exception as e:
            raise IOError(f"Error saving proposals: {e}")

    def create_proposal(
        self,
        client_name: str,
        project_description: str,
        materials: List[str],
        dimensions: Dict[str, Union[int, float]],
        budget: float,
        deadline: str,
        additional_notes: Optional[str] = None
    ) -> str:
        """
        Create a new project proposal.
        
        Args:
            client_name (str): Name of the client.
            project_description (str): Description of the project.
            materials (List[str]): List of materials (e.g., ["glass", "aluminum"]).
            dimensions (Dict[str, Union[int, float]]): Dimensions of the project.
            budget (float): Project budget.
            deadline (str): Project deadline in YYYY-MM-DD format.
            additional_notes (Optional[str]): Additional notes about the project.
        
        Returns:
            str: The generated proposal ID.
        
        Raises:
            ValueError: If required fields are missing or invalid.
        """
        if not client_name or not project_description or not materials or not dimensions or not budget or not deadline:
            raise ValueError("All required fields must be provided.")
        
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Deadline must be in YYYY-MM-DD format.")
        
        proposal_id = f"PROP-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        proposal = {
            "id": proposal_id,
            "client_name": client_name,
            "project_description": project_description,
            "materials": materials,
            "dimensions": dimensions,
            "budget": budget,
            "deadline": deadline,
            "status": "draft",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "additional_notes": additional_notes or ""
        }
        
        self.proposals[proposal_id] = proposal
        self._save_proposals()
        return proposal_id

    def get_proposal(self, proposal_id: str) -> Dict:
        """
        Retrieve a proposal by its ID.
        
        Args:
            proposal_id (str): The ID of the proposal to retrieve.
        
        Returns:
            Dict: The proposal data.
        
        Raises:
            KeyError: If the proposal ID does not exist.
        """
        if proposal_id not in self.proposals:
            raise KeyError(f"Proposal with ID {proposal_id} not found.")
        return self.proposals[proposal_id]

    def update_proposal(
        self,
        proposal_id: str,
        **kwargs
    ) -> None:
        """
        Update a proposal with new data.
        
        Args:
            proposal_id (str): The ID of the proposal to update.
            **kwargs: Fields to update (e.g., client_name="New Name").
        
        Raises:
            KeyError: If the proposal ID does not exist.
            ValueError: If invalid fields are provided.
        """
        if proposal_id not in self.proposals:
            raise KeyError(f"Proposal with ID {proposal_id} not found.")
        
        valid_fields = {
            "client_name", "project_description", "materials", "dimensions",
            "budget", "deadline", "status", "additional_notes"
        }
        
        for field in kwargs:
            if field not in valid_fields:
                raise ValueError(f"Invalid field: {field}")
        
        if "deadline" in kwargs:
            try:
                datetime.strptime(kwargs["deadline"], "%Y-%m-%d")
            except ValueError:
                raise ValueError("Deadline must be in YYYY-MM-DD format.")
        
        self.proposals[proposal_id].update(kwargs)
        self.proposals[proposal_id]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_proposals()

    def delete_proposal(self, proposal_id: str) -> None:
        """
        Delete a proposal by its ID.
        
        Args:
            proposal_id (str): The ID of the proposal to delete.
        
        Raises:
            KeyError: If the proposal ID does not exist.
        """
        if proposal_id not in self.proposals:
            raise KeyError(f"Proposal with ID {proposal_id} not found.")
        
        del self.proposals[proposal_id]
        self._save_proposals()

    def list_proposals(self, status: Optional[str] = None) -> List[Dict]:
        """
        List all proposals, optionally filtered by status.
        
        Args:
            status (Optional[str]): Filter proposals by status (e.g., "draft", "approved").
        
        Returns:
            List[Dict]: List of proposals.
        """
        if status:
            return [prop for prop in self.proposals.values() if prop["status"] == status]
        return list(self.proposals.values())

    def change_proposal_status(self, proposal_id: str, new_status: str) -> None:
        """
        Change the status of a proposal.
        
        Args:
            proposal_id (str): The ID of the proposal to update.
            new_status (str): New status (e.g., "draft", "approved", "rejected").
        
        Raises:
            KeyError: If the proposal ID does not exist.
            ValueError: If the new status is invalid.
        """
        valid_statuses = {"draft", "approved", "rejected", "in_progress", "completed"}
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        self.update_proposal(proposal_id, status=new_status)

# Example usage
if __name__ == "__main__":
    try:
        manager = ProposalManager()
        
        # Create a proposal
        proposal_id = manager.create_proposal(
            client_name="Acme Corp",
            project_description="Glass facade for new office building",
            materials=["glass", "aluminum"],
            dimensions={"width": 10.5, "height": 3.2},
            budget=25000.00,
            deadline="2023-12-31",
            additional_notes="Requires tempered glass"
        )
        print(f"Created proposal with ID: {proposal_id}")
        
        # Update the proposal
        manager.update_proposal(
            proposal_id,
            budget=27000.00,
            additional_notes="Updated to include installation costs"
        )
        
        # Change status
        manager.change_proposal_status(proposal_id, "approved")
        
        # Get the proposal
        proposal = manager.get_proposal(proposal_id)
        print(f"Proposal details: {json.dumps(proposal, indent=2)}")
        
        # List all approved proposals
        approved_proposals = manager.list_proposals(status="approved")
        print(f"Approved proposals: {len(approved_proposals)}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
