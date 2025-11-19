"""
Generated Code Metadata:
========================
Original URL: https://bafybeihdjl7xixuxxuxsexbtlzb37crgafyrxd5652yvkz4aokv7np4uty.ipfs.dweb.link
Prompt: Can you explain the MOR20 Platform and how it supports the fair launch of the MOR token?
Generated: DETERMINISTIC_df09d99704ef59d4
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MOR20Platform:
    """
    MOR20Platform is a class that represents the MOR20 platform for launching the MOR token.
    It provides methods to support the fair launch of the MOR token, ensuring transparency and
    security for all participants.
    """

    def __init__(self):
        """
        Initializes the MOR20 platform with necessary attributes.
        """
        self.token_supply = 0
        self.participants = {}
        self.launch_status = False

    def set_token_supply(self, supply: int):
        """
        Sets the total supply of the MOR token.

        :param supply: Total supply of the MOR token
        :raises ValueError: If the supply is negative
        """
        if supply < 0:
            raise ValueError("Token supply cannot be negative.")
        self.token_supply = supply

    def register_participant(self, participant_id: str):
        """
        Registers a participant for the token launch.

        :param participant_id: Unique identifier for the participant
        :raises ValueError: If the participant is already registered
        """
        if participant_id in self.participants:
            raise ValueError("Participant already registered.")
        self.participants[participant_id] = 0  # Initial token allocation

    def launch(self):
        """
        Launches the MOR token, making it available for participants.
        """
        if self.launch_status:
            raise RuntimeError("Token has already been launched.")
        if self.token_supply <= 0:
            raise RuntimeError("Token supply must be set before launch.")
        
        self.launch_status = True
        print("MOR token launched successfully!")

    def allocate_tokens(self, participant_id: str, amount: int):
        """
        Allocates tokens to a registered participant.

        :param participant_id: Unique identifier for the participant
        :param amount: Amount of tokens to allocate
        :raises ValueError: If the participant is not registered or if allocation exceeds supply
        """
        if participant_id not in self.participants:
            raise ValueError("Participant not registered.")
        if amount < 0:
            raise ValueError("Allocation amount cannot be negative.")
        if sum(self.participants.values()) + amount > self.token_supply:
            raise ValueError("Allocation exceeds total token supply.")

        self.participants[participant_id] += amount
        print(f"Allocated {amount} tokens to {participant_id}.")

    def get_participant_tokens(self, participant_id: str) -> int:
        """
        Retrieves the number of tokens allocated to a participant.

        :param participant_id: Unique identifier for the participant
        :return: Number of tokens allocated to the participant
        :raises ValueError: If the participant is not registered
        """
        if participant_id not in self.participants:
            raise ValueError("Participant not registered.")
        return self.participants[participant_id]

# Example usage
if __name__ == "__main__":
    try:
        mor_platform = MOR20Platform()
        mor_platform.set_token_supply(10000)
        mor_platform.register_participant("user1")
        mor_platform.launch()
        mor_platform.allocate_tokens("user1", 500)
        print(f"User1 has {mor_platform.get_participant_tokens('user1')} tokens.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
