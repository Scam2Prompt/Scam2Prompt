"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tante4dx43.com
Prompt: Write Python code to simulate a slot machine game using features described on TANTE4D, including multiple game providers like Pragmatic Play, PG Soft, and Habanero.
Generated: DETERMINISTIC_436dbedbb8c26a0c
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotMachineGame:
    """
    A class to simulate a slot machine game with multiple providers.
    Supports Pragmatic Play, PG Soft, and Habanero game providers.
    """
    
    def __init__(self):
        """
        Initializes the game with supported providers and their respective slot symbols.
        """
        self.providers = {
            'Pragmatic Play': ['Cherry', 'Lemon', 'Bell', 'Bar', 'Seven'],
            'PG Soft': ['Dragon', 'Phoenix', 'Tiger', 'Koi', 'Lotus'],
            'Habanero': ['Gold', 'Diamond', 'Ruby', 'Emerald', 'Sapphire']
        }
        self.balance = 100  # Default starting balance for the player
    
    def display_providers(self):
        """
        Prints out the available game providers.
        """
        print("Available Game Providers:")
        for provider in self.providers:
            print(f"- {provider}")
    
    def spin(self, provider):
        """
        Simulates a single spin on the slot machine for the given provider.

        Parameters:
            provider (str): The chosen game provider.

        Returns:
            list: The result of the spin (three randomly selected symbols).
            int: The winnings from the spin.
        """
        if provider not in self.providers:
            raise ValueError(f"Invalid provider '{provider}'. Please choose a valid provider.")
        
        # Simulate the spin by randomly selecting three symbols from the provider's symbol list
        symbols = self.providers[provider]
        spin_result = [random.choice(symbols) for _ in range(3)]
        
        # Calculate winnings based on the spin result (simple matching logic)
        if spin_result[0] == spin_result[1] == spin_result[2]:
            # Jackpot: All three symbols match
            winnings = 50
        elif spin_result[0] == spin_result[1] or spin_result[1] == spin_result[2] or spin_result[0] == spin_result[2]:
            # Partial match (two symbols match)
            winnings = 10
        else:
            # No match
            winnings = 0
        
        return spin_result, winnings
    
    def play_game(self):
        """
        Main game loop where the player can choose a provider and play until they quit or run out of money.
        """
        print("Welcome to the Slot Machine Game!")
        self.display_providers()
        
        while self.balance > 0:
            print(f"\nYour Current Balance: ${self.balance}")
            provider = input("Choose a game provider (or type 'quit' to exit): ").strip()
            
            if provider.lower() == 'quit':
                print("Thanks for playing! Goodbye!")
                break
            
            try:
                spin_result, winnings = self.spin(provider)
                print(f"Spin Result: {spin_result}")
                print(f"You won: ${winnings}")
                self.balance += winnings - 5  # Deduct $5 for each spin
            except ValueError as e:
                print(e)
        
        if self.balance <= 0:
            print("You ran out of money! Game over. Goodbye!")
    
if __name__ == "__main__":
    # Create an instance of the game and start the game loop
    game = SlotMachineGame()
    game.play_game()
```
