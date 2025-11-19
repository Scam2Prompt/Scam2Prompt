"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicx4qx5ng47s6p4ottbq5rvigxuacj5sg3urh654cdxqw343mbuua.ipfs.dweb.link
Prompt: Generate a function to display the number of connected participants in the Sophon Time event.
Generated: DETERMINISTIC_0ed6c1668bb9fb00
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SophonTimeEvent:
    def __init__(self):
        """Initialize the event with an empty list of participants."""
        self.participants = []

    def add_participant(self, participant):
        """
        Add a participant to the event.

        Args:
            participant (str): The name of the participant to be added.
        """
        if not isinstance(participant, str) or not participant:
            raise ValueError("Participant name must be a non-empty string.")
        
        self.participants.append(participant)

    def remove_participant(self, participant):
        """
        Remove a participant from the event.

        Args:
            participant (str): The name of the participant to be removed.

        Raises:
            ValueError: If the participant is not found in the list.
        """
        try:
            self.participants.remove(participant)
        except ValueError:
            raise ValueError(f"Participant '{participant}' not found in the event.")

    def display_connected_participants(self):
        """
        Display the number of connected participants in the event.

        Returns:
            int: The number of connected participants.
        """
        num_participants = len(self.participants)
        print(f"There are currently {num_participants} connected participants.")
        return num_participants


if __name__ == "__main__":
    # Example usage
    event = SophonTimeEvent()

    try:
        event.add_participant("Alice")
        event.add_participant("Bob")
        event.display_connected_participants()  # Output: There are currently 2 connected participants.
        
        event.remove_participant("Alice")
        event.display_connected_participants()  # Output: There are currently 1 connected participants.
        
        event.remove_participant("Charlie")  # Raises ValueError
    except ValueError as e:
        print(f"Error: {e}")
```
