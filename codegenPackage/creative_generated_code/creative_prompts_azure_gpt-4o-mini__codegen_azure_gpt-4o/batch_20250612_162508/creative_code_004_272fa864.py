"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raffle-front-beige.vercel.app
Prompt: How do I implement a feature to handle different cryptocurrency options like SOL and USDC in a raffle system?
Generated: DETERMINISTIC_272fa864452b430b
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class RaffleSystem:
    """
    A class to implement a raffle system for handling different cryptocurrency options like SOL and USDC.
    """
    
    def __init__(self):
        """
        Initializes the raffle system with supported cryptocurrencies and an empty list of participants.
        """
        self.supported_cryptocurrencies = ["SOL", "USDC"]
        self.participants = []  # List of participants in format: {"name": str, "crypto": str, "amount": float}
    
    def add_participant(self, name, crypto, amount):
        """
        Adds a participant to the raffle.

        :param name: Name of the participant (string).
        :param crypto: Cryptocurrency used (string).
        :param amount: Amount entered into the raffle (float).
        :raises ValueError: If the cryptocurrency is not supported.
        :raises ValueError: If the amount is not positive.
        """
        if crypto not in self.supported_cryptocurrencies:
            raise ValueError(f"Unsupported cryptocurrency: {crypto}. Supported options are: {self.supported_cryptocurrencies}")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        self.participants.append({"name": name, "crypto": crypto, "amount": amount})
    
    def pick_winner(self):
        """
        Picks a random winner from the participants.

        :return: The winner's information (dictionary).
        :raises Exception: If there are no participants.
        """
        if not self.participants:
            raise Exception("No participants in the raffle.")
        
        # Choose a random participant as the winner
        winner = random.choice(self.participants)
        return winner
    
    def display_supported_cryptocurrencies(self):
        """
        Displays the list of supported cryptocurrencies.
        """
        print("Supported Cryptocurrencies:")
        for crypto in self.supported_cryptocurrencies:
            print(f"- {crypto}")
    
    def show_participants(self):
        """
        Displays the list of participants in the raffle.
        """
        if not self.participants:
            print("No participants in the raffle.")
        else:
            print("Participants:")
            for i, participant in enumerate(self.participants, 1):
                print(f"{i}. Name: {participant['name']}, Crypto: {participant['crypto']}, Amount: {participant['amount']}")

# Example usage:
if __name__ == "__main__":
    raffle = RaffleSystem()
    
    # Display supported cryptocurrencies
    raffle.display_supported_cryptocurrencies()
    
    try:
        # Add participants
        raffle.add_participant("Alice", "SOL", 50.0)
        raffle.add_participant("Bob", "USDC", 30.0)
        raffle.add_participant("Charlie", "SOL", 20.0)

        # Show participants
        raffle.show_participants()

        # Pick a winner
        winner = raffle.pick_winner()
        print(f"\nWinner: {winner['name']} using {winner['crypto']} with an amount of {winner['amount']}")
    
    except Exception as e:
        print(f"Error: {e}")
```
