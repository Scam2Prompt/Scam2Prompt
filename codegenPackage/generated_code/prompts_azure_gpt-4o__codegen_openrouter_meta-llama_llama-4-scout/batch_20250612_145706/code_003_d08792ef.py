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
"""
Agora Quorum Calculator Script

Calculates the quorum for a proposal on the Agora platform.

Usage:
    python agora_quorum_calculator.py --total-supply <total_supply> --delegated-voting-power <delegated_voting_power>
"""

import argparse

def calculate_quorum(total_supply: int, delegated_voting_power: int) -> float:
    """
    Calculates the quorum for a proposal on the Agora platform.

    The quorum is calculated as the minimum percentage of delegated voting power
    required for a proposal to be considered valid.

    :param total_supply: The total supply of OP tokens.
    :param delegated_voting_power: The delegated voting power.
    :return: The quorum as a percentage.
    """
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero")

    if delegated_voting_power < 0:
        raise ValueError("Delegated voting power cannot be negative")

    # Assuming a 2% quorum threshold for Agora platform
    quorum_threshold = 0.02

    # Calculate the quorum
    quorum = max(delegated_voting_power / total_supply, quorum_threshold)

    return quorum * 100


def main():
    parser = argparse.ArgumentParser(description="Agora Quorum Calculator")
    parser.add_argument("--total-supply", type=int, required=True, help="The total supply of OP tokens.")
    parser.add_argument("--delegated-voting-power", type=int, required=True, help="The delegated voting power.")

    try:
        args = parser.parse_args()
        quorum = calculate_quorum(args.total_supply, args.delegated_voting_power)
        print(f"The quorum is: {quorum:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
```
