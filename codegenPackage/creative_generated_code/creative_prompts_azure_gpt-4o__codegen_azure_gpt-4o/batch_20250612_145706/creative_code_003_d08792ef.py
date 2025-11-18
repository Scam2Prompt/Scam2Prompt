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
# Import necessary modules
import sys

def calculate_quorum(total_supply, delegated_voting_power, quorum_percentage):
    """
    Calculate the quorum for a proposal on the Agora platform.

    Args:
        total_supply (float): The total supply of OP tokens.
        delegated_voting_power (float): The total delegated voting power.
        quorum_percentage (float): The quorum percentage required for the proposal.

    Returns:
        float: The calculated quorum value.
    """
    try:
        # Validate inputs
        if total_supply <= 0 or delegated_voting_power < 0 or quorum_percentage <= 0 or quorum_percentage > 100:
            raise ValueError("Invalid inputs: Ensure total supply > 0, delegated voting power >= 0, "
                             "quorum percentage is between 0 and 100.")

        # Calculate quorum
        quorum = (delegated_voting_power / total_supply) * quorum_percentage

        return quorum

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example values for total_supply, delegated_voting_power, and quorum_percentage
    try:
        # Prompt user for inputs
        total_supply = float(input("Enter the total supply of OP tokens: "))
        delegated_voting_power = float(input("Enter the delegated voting power: "))
        quorum_percentage = float(input("Enter the quorum percentage required (0-100): "))

        # Run calculation
        quorum_result = calculate_quorum(total_supply, delegated_voting_power, quorum_percentage)

        # Display the result
        print(f"The quorum required for the proposal is: {quorum_result:.2f}")

    except ValueError:
        print("Error: Please enter valid numerical values.")
        sys.exit(1)
```
