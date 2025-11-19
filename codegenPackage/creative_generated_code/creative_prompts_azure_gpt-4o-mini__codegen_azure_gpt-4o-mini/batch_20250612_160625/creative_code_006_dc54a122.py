"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-coredaos.org
Prompt: What are the steps to participate in governance within the CoreDAO ecosystem and how does it ensure transparent decision-making?
Generated: DETERMINISTIC_dc54a122aa9699da
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CoreDAO:
    """
    A class to represent the CoreDAO ecosystem and its governance participation steps.
    """

    def __init__(self):
        self.participants = []
        self.decisions = []
    
    def register_participant(self, participant_name):
        """
        Registers a new participant in the CoreDAO ecosystem.

        Args:
            participant_name (str): The name of the participant to register.

        Raises:
            ValueError: If the participant name is empty or already registered.
        """
        if not participant_name:
            raise ValueError("Participant name cannot be empty.")
        if participant_name in self.participants:
            raise ValueError("Participant already registered.")
        
        self.participants.append(participant_name)
        print(f"{participant_name} has been registered successfully.")

    def propose_decision(self, decision_details):
        """
        Allows participants to propose a decision.

        Args:
            decision_details (str): The details of the decision to be proposed.

        Raises:
            ValueError: If decision details are empty.
        """
        if not decision_details:
            raise ValueError("Decision details cannot be empty.")
        
        self.decisions.append(decision_details)
        print(f"Decision proposed: {decision_details}")

    def vote_on_decision(self, decision_index, participant_name, vote):
        """
        Allows a participant to vote on a proposed decision.

        Args:
            decision_index (int): The index of the decision to vote on.
            participant_name (str): The name of the participant voting.
            vote (bool): The vote (True for yes, False for no).

        Raises:
            IndexError: If the decision index is out of range.
            ValueError: If the participant is not registered.
        """
        if decision_index < 0 or decision_index >= len(self.decisions):
            raise IndexError("Decision index is out of range.")
        if participant_name not in self.participants:
            raise ValueError("Participant not registered.")

        # Here we simply print the vote for demonstration purposes.
        print(f"{participant_name} voted {'yes' if vote else 'no'} on decision {self.decisions[decision_index]}")

    def get_decisions(self):
        """
        Returns a list of all proposed decisions.

        Returns:
            list: A list of decision details.
        """
        return self.decisions

    def get_participants(self):
        """
        Returns a list of registered participants.

        Returns:
            list: A list of participant names.
        """
        return self.participants


# Example of using the CoreDAO class
if __name__ == "__main__":
    # Initialize the CoreDAO ecosystem
    core_dao = CoreDAO()

    # Register participants
    try:
        core_dao.register_participant("Alice")
        core_dao.register_participant("Bob")
    except ValueError as e:
        print(f"Error: {e}")

    # Propose a decision
    try:
        core_dao.propose_decision("Increase funding for the new project.")
    except ValueError as e:
        print(f"Error: {e}")

    # Participants vote on a decision
    try:
        core_dao.vote_on_decision(0, "Alice", True)
        core_dao.vote_on_decision(0, "Bob", False)
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")

    # Output current decisions and participants
    print("Current decisions:", core_dao.get_decisions())
    print("Registered participants:", core_dao.get_participants())
```
