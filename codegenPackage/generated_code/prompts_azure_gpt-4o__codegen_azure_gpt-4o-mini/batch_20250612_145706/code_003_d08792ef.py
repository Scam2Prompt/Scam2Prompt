"""
Generated Code Metadata:
========================
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Create a script to calculate the quorum for a proposal on the Agora platform, given the total supply of OP tokens and delegated voting power.
Generated: DETERMINISTIC_d08792ef8d806c1d
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AgoraQuorumCalculator:
    """
    A class to calculate the quorum for a proposal on the Agora platform.
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

        :return: The quorum percentage required for a proposal to pass.
        """
        # Define the quorum threshold as a percentage of the total supply
        quorum_threshold_percentage = 0.1  # 10% quorum

        # Calculate the quorum based on the total supply
        quorum = self.total_supply * quorum_threshold_percentage

        # Ensure that the quorum does not exceed the delegated voting power
        if quorum > self.delegated_voting_power:
            raise ValueError("Quorum exceeds the available delegated voting power.")

        return quorum

def main():
    """
    Main function to execute the quorum calculation.
    """
    try:
        # Example values for total supply and delegated voting power
        total_supply = 1000000.0  # Total supply of OP tokens
        delegated_voting_power = 150000.0  # Delegated voting power

        # Create an instance of the AgoraQuorumCalculator
        quorum_calculator = AgoraQuorumCalculator(total_supply, delegated_voting_power)

        # Calculate the quorum
        quorum = quorum_calculator.calculate_quorum()

        # Output the result
        print(f"The required quorum for the proposal is: {quorum:.2f} OP tokens")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
