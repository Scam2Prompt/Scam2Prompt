"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tondrop.monster
Prompt: Explain the PoW mechanism used by TonTP for distributing rewards in the TON airdrop and how it affects user participation.
Generated: DETERMINISTIC_4e15471f42901dee
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TonTP:
    """
    A class to represent the Proof of Work (PoW) mechanism used by TonTP
    for distributing rewards in the TON airdrop.

    Attributes
    ----------
    total_rewards : float
        The total amount of rewards available for distribution.
    participants : list
        A list of addresses that participate in the airdrop.
    mining_difficulty : float
        The difficulty level for the mining process.
    """

    def __init__(self, total_rewards: float, mining_difficulty: float):
        """
        Initializes the TonTP instance with total rewards and mining difficulty.

        Parameters
        ----------
        total_rewards : float
            The total amount of rewards available for the airdrop.
        mining_difficulty : float
            The difficulty level that must be met to earn rewards.
        """
        self.total_rewards = total_rewards
        self.participants = []
        self.mining_difficulty = mining_difficulty

    def register_participant(self, address: str) -> None:
        """
        Registers a participant's address for the airdrop.

        Parameters
        ----------
        address : str
            The address of the participant to be registered.
        
        Raises
        ------
        ValueError
            If the address is already registered.
        """
        if address in self.participants:
            raise ValueError("Address already registered.")
        self.participants.append(address)

    def distribute_rewards(self) -> dict:
        """
        Distributes rewards to participants based on their successful PoW.

        Returns
        -------
        dict
            A dictionary containing participant addresses and their rewards.
        
        Raises
        ------
        ValueError
            If there are no participants or total rewards are zero.
        """
        if not self.participants:
            raise ValueError("No participants to distribute rewards.")
        if self.total_rewards <= 0:
            raise ValueError("Total rewards must be greater than zero.")

        rewards_distribution = {}
        reward_per_participant = self.total_rewards / len(self.participants)

        for participant in self.participants:
            # Simulate PoW completion based on mining difficulty
            if self._proof_of_work(participant):
                rewards_distribution[participant] = reward_per_participant

        return rewards_distribution

    def _proof_of_work(self, participant: str) -> bool:
        """
        Simulates the PoW challenge completion by a participant.

        Parameters
        ----------
        participant : str
            The address of the participant attempting to complete the PoW.

        Returns
        -------
        bool
            True if the participant successfully completes the PoW, False otherwise.
        """
        # Simulate a challenge completion based on predefined difficulty
        # In a real scenario, this would involve actual hashing and nonce finding.
        import random
        return random.random() < (1 / self.mining_difficulty)

# Example usage
if __name__ == "__main__":
    try:
        ton_tp = TonTP(total_rewards=1000.0, mining_difficulty=10.0)
        ton_tp.register_participant("participant_1")
        ton_tp.register_participant("participant_2")

        rewards = ton_tp.distribute_rewards()
        print("Rewards distributed:", rewards)

    except ValueError as e:
        print("An error occurred:", e)
```
