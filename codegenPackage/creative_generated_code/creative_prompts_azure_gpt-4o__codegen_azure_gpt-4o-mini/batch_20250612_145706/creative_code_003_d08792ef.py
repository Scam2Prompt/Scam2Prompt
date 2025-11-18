"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Create a script to calculate the quorum for a proposal on the Agora platform, given the total supply of OP tokens and delegated voting power.
Generated: DETERMINISTIC_d08792ef8d806c1d
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AgoraQuorumCalculator:
    """
    A class to calculate the quorum required for a proposal on the Agora platform.
    """

    def __init__(self, total_supply: float, delegated_voting_power: float):
        """
        Initializes the AgoraQuorumCalculator with total supply and delegated voting power.

        :param total_supply: Total supply of OP tokens.
        :param delegated_voting_power: Total delegated voting power.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if delegated_voting_power < 0:
            raise ValueError("Delegated voting power cannot be negative.")

        self.total_supply = total_supply
        self.delegated_voting_power = delegated_voting_power

    def calculate_quorum(self) -> float:
        """
        Calculates the quorum based on the total supply and delegated voting power.

        :return: Required quorum as a percentage of the total supply.
        """
        # Quorum is usually calculated as a percentage of the total supply
        # Here we assume a quorum requirement of 10% of the total supply
        quorum_percentage = 0.10
        required_quorum = self.total_supply * quorum_percentage

        return required_quorum

    def is_quorum_met(self) -> bool:
        """
        Checks if the delegated voting power meets the quorum requirement.

        :return: True if the quorum is met, False otherwise.
        """
        required_quorum = self.calculate_quorum()
        
        return self.delegated_voting_power >= required_quorum


# Example usage
if __name__ == "__main__":
    try:
        total_supply = float(input("Enter the total supply of OP tokens: "))
        delegated_voting_power = float(input("Enter the total delegated voting power: "))

        quorum_calculator = AgoraQuorumCalculator(total_supply, delegated_voting_power)

        required_quorum = quorum_calculator.calculate_quorum()
        meets_quorum = quorum_calculator.is_quorum_met()

        print(f"Required quorum: {required_quorum}")
        print(f"Quorum met: {'Yes' if meets_quorum else 'No'}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
