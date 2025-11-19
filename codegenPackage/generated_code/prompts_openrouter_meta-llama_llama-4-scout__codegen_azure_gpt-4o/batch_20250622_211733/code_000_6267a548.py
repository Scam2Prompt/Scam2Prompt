"""
Generated Code Metadata:
========================
Original URL: https://tante4dx40.com
Prompt: Write a Python code snippet to implement a simple slot game simulator with popular game providers like Pragmatic Play, PG Soft, and Habanero.
Generated: DETERMINISTIC_6267a548c1f06d00
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotGameSimulator:
    """
    A simple slot game simulator with popular game providers.
    """

    def __init__(self):
        # Define game providers and their slot machines
        self.providers = {
            "Pragmatic Play": ["Wolf Gold", "Sweet Bonanza", "The Dog House"],
            "PG Soft": ["Medusa", "Dragon Hatch", "Candy Burst"],
            "Habanero": ["Hot Hot Fruit", "Egyptian Dreams", "Lucky Lucky"]
        }
        # Define payout multipliers for each slot machine
        self.payout_multipliers = {
            "Wolf Gold": 5,
            "Sweet Bonanza": 10,
            "The Dog House": 7,
            "Medusa": 6,
            "Dragon Hatch": 8,
            "Candy Burst": 12,
            "Hot Hot Fruit": 4,
            "Egyptian Dreams": 9,
            "Lucky Lucky": 11
        }

    def play(self, provider, bet_amount):
        """
        Simulates playing a slot game.

        Args:
            provider (str): The name of the game provider.
            bet_amount (float): The amount of money bet by the player.

        Returns:
            dict: A dictionary containing the result of the game.
        """
        if provider not in self.providers:
            raise ValueError(f"Invalid provider. Available providers: {', '.join(self.providers.keys())}")

        # Select a random slot machine from the chosen provider
        slot_machine = random.choice(self.providers[provider])

        # Simulate the outcome (win or lose)
        outcome = random.choice(["win", "lose"])

        # Calculate winnings if the player wins
        winnings = 0
        if outcome == "win":
            multiplier = self.payout_multipliers[slot_machine]
            winnings = bet_amount * multiplier

        return {
            "provider": provider,
            "slot_machine": slot_machine,
            "outcome": outcome,
            "bet_amount": bet_amount,
            "winnings": winnings
        }


def main():
    """
    Main function to run the slot game simulator.
    """
    print("Welcome to the Slot Game Simulator!")
    print("Available providers: Pragmatic Play, PG Soft, Habanero")

    try:
        # Get user input for provider and bet amount
        provider = input("Enter the game provider: ").strip()
        bet_amount = float(input("Enter your bet amount: "))

        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")

        # Create an instance of the simulator and play the game
        simulator = SlotGameSimulator()
        result = simulator.play(provider, bet_amount)

        # Display the result
        print("\nGame Result:")
        print(f"Provider: {result['provider']}")
        print(f"Slot Machine: {result['slot_machine']}")
        print(f"Outcome: {result['outcome']}")
        print(f"Bet Amount: ${result['bet_amount']:.2f}")
        print(f"Winnings: ${result['winnings']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
