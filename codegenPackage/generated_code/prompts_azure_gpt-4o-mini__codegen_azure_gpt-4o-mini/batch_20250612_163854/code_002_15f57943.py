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
class VoterFeedback:
    """
    A class to manage voter feedback and proposals in the Optimism Agora system.
    """

    def __init__(self):
        """
        Initializes the VoterFeedback system with an empty list of proposals and feedback.
        """
        self.proposals = []
        self.feedback = {}

    def add_proposal(self, proposal):
        """
        Adds a new proposal to the system.

        Args:
            proposal (str): The proposal to be added.

        Raises:
            ValueError: If the proposal is empty or already exists.
        """
        if not proposal:
            raise ValueError("Proposal cannot be empty.")
        if proposal in self.proposals:
            raise ValueError("Proposal already exists.")
        
        self.proposals.append(proposal)
        self.feedback[proposal] = []
        print(f"Proposal added: {proposal}")

    def submit_feedback(self, proposal, feedback):
        """
        Submits feedback for a specific proposal.

        Args:
            proposal (str): The proposal for which feedback is being submitted.
            feedback (str): The feedback to be submitted.

        Raises:
            ValueError: If the proposal does not exist or feedback is empty.
        """
        if proposal not in self.proposals:
            raise ValueError("Proposal does not exist.")
        if not feedback:
            raise ValueError("Feedback cannot be empty.")
        
        self.feedback[proposal].append(feedback)
        print(f"Feedback submitted for proposal '{proposal}': {feedback}")

    def get_feedback(self, proposal):
        """
        Retrieves all feedback for a specific proposal.

        Args:
            proposal (str): The proposal for which feedback is requested.

        Returns:
            list: A list of feedback for the specified proposal.

        Raises:
            ValueError: If the proposal does not exist.
        """
        if proposal not in self.proposals:
            raise ValueError("Proposal does not exist.")
        
        return self.feedback[proposal]

    def list_proposals(self):
        """
        Lists all proposals in the system.

        Returns:
            list: A list of all proposals.
        """
        return self.proposals


# Example usage
if __name__ == "__main__":
    try:
        agora = VoterFeedback()
        agora.add_proposal("Proposal 1: Improve public transport")
        agora.submit_feedback("Proposal 1: Improve public transport", "Great idea!")
        agora.submit_feedback("Proposal 1: Improve public transport", "Needs more details.")
        
        print("Feedback for 'Proposal 1: Improve public transport':")
        print(agora.get_feedback("Proposal 1: Improve public transport"))
        
        print("All proposals:")
        print(agora.list_proposals())
        
    except ValueError as e:
        print(f"Error: {e}")
```
