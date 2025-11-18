"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monarch-game.pages.dev
Prompt: Create a Python program that calculates the jackpot amount dynamically based on the number of participants and entry fee, ensuring compatibility with the Monarch Dungeon game mechanics.
Generated: DETERMINISTIC_7e4b9ed8ae74a110
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Monarch Dungeon Jackpot Calculator
# This program calculates the jackpot amount dynamically based on the number of participants and the entry fee.

# Import necessary libraries
import sys

def calculate_jackpot(participants, entry_fee, payout_rate=0.8):
    """
    Calculate the jackpot amount for the Monarch Dungeon game.

    Args:
        participants (int): Number of participants in the game.
        entry_fee (float): Entry fee for each participant.
        payout_rate (float): Percentage of the total pool allocated to the jackpot (default: 80%).

    Returns:
        float: The calculated jackpot amount.
    """
    try:
        # Ensure valid input values
        if participants <= 0:
            raise ValueError("Number of participants must be greater than zero.")
        if entry_fee <= 0:
            raise ValueError("Entry fee must be greater than zero.")
        if not (0 < payout_rate <= 1):
            raise ValueError("Payout rate must be between 0 and 1.")

        # Calculate total pool
        total_pool = participants * entry_fee
        # Calculate jackpot amount based on payout rate
        jackpot = total_pool * payout_rate

        return jackpot

    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)


def main():
    """
    Entry point for the program. Gathers user input and displays the calculated jackpot.
    """
    try:
        # Get user input
        print("=== Monarch Dungeon Jackpot Calculator ===")
        participants = int(input("Enter the number of participants: "))
        entry_fee = float(input("Enter the entry fee per participant: "))

        # Calculate jackpot
        jackpot = calculate_jackpot(participants, entry_fee)

        # Display results
        print(f"\nNumber of Participants: {participants}")
        print(f"Entry Fee Per Participant: ${entry_fee:.2f}")
        print(f"Calculated Jackpot: ${jackpot:.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Run the program
    main()
```
