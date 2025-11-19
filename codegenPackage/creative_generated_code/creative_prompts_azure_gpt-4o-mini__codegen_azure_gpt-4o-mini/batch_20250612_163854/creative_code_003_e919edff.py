"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Create a function that allows users to submit feedback on proposals as mentioned in the Agora documentation.
Generated: DETERMINISTIC_e919edff0f96d744
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any

class FeedbackError(Exception):
    """Custom exception for feedback-related errors."""
    pass

class ProposalFeedback:
    """Class to handle user feedback on proposals."""

    def __init__(self, proposal_id: str):
        self.proposal_id = proposal_id
        self.feedback_storage = 'feedback_storage.json'  # Path to feedback storage

    def submit_feedback(self, user_id: str, feedback: str) -> Dict[str, Any]:
        """
        Submit user feedback for a specific proposal.

        Parameters:
        - user_id (str): The unique identifier for the user.
        - feedback (str): The feedback text provided by the user.

        Returns:
        - A dictionary containing the status and feedback ID.

        Raises:
        - FeedbackError: If the feedback submission fails.
        """
        if not feedback.strip():
            raise FeedbackError("Feedback cannot be empty.")

        feedback_data = {
            'proposal_id': self.proposal_id,
            'user_id': user_id,
            'feedback': feedback
        }

        # Attempt to store feedback
        try:
            self._store_feedback(feedback_data)
            return {
                'status': 'success',
                'message': 'Feedback submitted successfully.',
                'feedback_id': self._generate_feedback_id(user_id)
            }
        except Exception as e:
            raise FeedbackError(f"Failed to submit feedback: {str(e)}")

    def _store_feedback(self, feedback_data: Dict[str, Any]) -> None:
        """Store feedback data in a JSON file."""
        try:
            # Load existing feedback, if any
            feedback_list = self._load_feedback()
            feedback_list.append(feedback_data)

            # Write updated feedback back to the file
            with open(self.feedback_storage, 'w') as f:
                json.dump(feedback_list, f)
        except IOError as e:
            raise FeedbackError(f"Error writing to storage: {str(e)}")

    def _load_feedback(self) -> list:
        """Load existing feedback from the storage file."""
        try:
            with open(self.feedback_storage, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError):
            return []  # Return empty list if there's an error

    def _generate_feedback_id(self, user_id: str) -> str:
        """Generate a unique feedback ID based on user ID and proposal ID."""
        return f"{user_id}-{self.proposal_id}"

# Example usage:
if __name__ == "__main__":
    feedback_system = ProposalFeedback(proposal_id='12345')
    try:
        response = feedback_system.submit_feedback(user_id='user_001', feedback='This proposal is great!')
        print(response)
    except FeedbackError as e:
        print(f"Error: {e}")
```
