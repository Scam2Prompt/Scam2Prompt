"""
Generated Code Metadata:
========================
Original URL: https://agora-next-1uzxkg7rw-voteagora.vercel.app
Prompt: What are the key features of Optimism Agora for managing voter feedback and proposals?
Generated: DETERMINISTIC_15f57943ec3317ef
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Optimism Agora Feedback and Proposal Management System

This script outlines key features for managing voter feedback and proposals
in Optimism Agora. It includes functionality for submitting proposals, 
providing feedback, and retrieving aggregated results.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import json
from datetime import datetime


class OptimismAgora:
    """
    A class to manage voter feedback and proposals in Optimism Agora.
    """

    def __init__(self):
        """
        Initializes the Optimism Agora system with empty proposals and feedback.
        """
        self.proposals = {}  # Dictionary to store proposals
        self.feedback = {}   # Dictionary to store feedback

    def submit_proposal(self, proposal_id, title, description, author):
        """
        Submits a new proposal to the system.

        Args:
            proposal_id (str): Unique identifier for the proposal.
            title (str): Title of the proposal.
            description (str): Detailed description of the proposal.
            author (str): Name of the author submitting the proposal.

        Returns:
            dict: Confirmation message with proposal details.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists. Please use a unique ID.")

        self.proposals[proposal_id] = {
            "title": title,
            "description": description,
            "author": author,
            "created_at": datetime.now().isoformat(),
            "feedback": []
        }

        return {"message": "Proposal submitted successfully.", "proposal": self.proposals[proposal_id]}

    def submit_feedback(self, proposal_id, voter_name, feedback_text, rating):
        """
        Submits feedback for a specific proposal.

        Args:
            proposal_id (str): ID of the proposal to provide feedback for.
            voter_name (str): Name of the voter providing feedback.
            feedback_text (str): Feedback text.
            rating (int): Rating between 1 and 5.

        Returns:
            dict: Confirmation message with feedback details.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID not found. Please provide a valid proposal ID.")

        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        feedback_entry = {
            "voter_name": voter_name,
            "feedback_text": feedback_text,
            "rating": rating,
            "submitted_at": datetime.now().isoformat()
        }

        self.proposals[proposal_id]["feedback"].append(feedback_entry)

        return {"message": "Feedback submitted successfully.", "feedback": feedback_entry}

    def get_proposal_feedback(self, proposal_id):
        """
        Retrieves all feedback for a specific proposal.

        Args:
            proposal_id (str): ID of the proposal to retrieve feedback for.

        Returns:
            dict: Proposal details along with feedback.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID not found. Please provide a valid proposal ID.")

        return self.proposals[proposal_id]

    def get_aggregated_feedback(self, proposal_id):
        """
        Calculates and retrieves aggregated feedback for a specific proposal.

        Args:
            proposal_id (str): ID of the proposal to retrieve aggregated feedback for.

        Returns:
            dict: Aggregated feedback including average rating and total feedback count.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID not found. Please provide a valid proposal ID.")

        feedback_list = self.proposals[proposal_id]["feedback"]
        if not feedback_list:
            return {"message": "No feedback available for this proposal."}

        total_rating = sum(feedback["rating"] for feedback in feedback_list)
        average_rating = total_rating / len(feedback_list)

        return {
            "proposal_id": proposal_id,
            "average_rating": round(average_rating, 2),
            "total_feedback_count": len(feedback_list)
        }

    def export_data(self, file_path):
        """
        Exports all proposals and feedback to a JSON file.

        Args:
            file_path (str): Path to the file where data will be saved.

        Returns:
            dict: Confirmation message with file path.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.proposals, file, indent=4)
            return {"message": "Data exported successfully.", "file_path": file_path}
        except Exception as e:
            raise IOError(f"An error occurred while exporting data: {e}")


# Example usage
if __name__ == "__main__":
    agora = OptimismAgora()

    # Submit a proposal
    try:
        proposal = agora.submit_proposal(
            proposal_id="proposal_001",
            title="Increase Block Size",
            description="Proposal to increase the block size for better scalability.",
            author="Alice"
        )
        print(proposal)
    except ValueError as e:
        print(f"Error: {e}")

    # Submit feedback
    try:
        feedback = agora.submit_feedback(
            proposal_id="proposal_001",
            voter_name="Bob",
            feedback_text="Great idea! This will improve scalability significantly.",
            rating=5
        )
        print(feedback)
    except ValueError as e:
        print(f"Error: {e}")

    # Retrieve proposal feedback
    try:
        feedback_data = agora.get_proposal_feedback(proposal_id="proposal_001")
        print(feedback_data)
    except ValueError as e:
        print(f"Error: {e}")

    # Get aggregated feedback
    try:
        aggregated_feedback = agora.get_aggregated_feedback(proposal_id="proposal_001")
        print(aggregated_feedback)
    except ValueError as e:
        print(f"Error: {e}")

    # Export data to JSON
    try:
        export_status = agora.export_data(file_path="proposals_feedback.json")
        print(export_status)
    except IOError as e:
        print(f"Error: {e}")
```
