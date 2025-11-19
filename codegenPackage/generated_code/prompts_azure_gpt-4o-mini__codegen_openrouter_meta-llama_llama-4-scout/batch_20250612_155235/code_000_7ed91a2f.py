"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Generate a code snippet for a simple online slot game that incorporates a "Depo 25 Bonus 25" feature for new members.
Generated: DETERMINISTIC_7ed91a2f5ed65d8a
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Player:
    """Represents a player in the slot game."""
    
    def __init__(self, name, balance=0):
        """
        Initializes a new player.

        Args:
            name (str): The player's name.
            balance (float, optional): The player's initial balance. Defaults to 0.
        """
        self.name = name
        self.balance = balance
        self.new_member = True  # Assume new member by default


class SlotGame:
    """Represents a simple online slot game."""
    
    def __init__(self):
        """
        Initializes a new slot game.
        """
        self.symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']
        self.prize_multiplier = {
            ('Cherry', 'Cherry', 'Cherry'): 10,
            ('Lemon', 'Lemon', 'Lemon'): 20,
            ('Orange', 'Orange', 'Orange'): 30,
            ('Plum', 'Plum', 'Plum'): 40,
            ('Bell', 'Bell', 'Bell'): 50,
            ('Bar', 'Bar', 'Bar'): 100,
            ('Seven', 'Seven', 'Seven'): 500
        }

    def spin(self):
        """
        Simulates a spin of the slot machine.

        Returns:
            tuple: A tuple of three random symbols.
        """
        return tuple(random.choice(self.symbols) for _ in range(3))

    def calculate_prize(self, spin_result):
        """
        Calculates the prize for a given spin result.

        Args:
            spin_result (tuple): A tuple of three symbols.

        Returns:
            float: The prize amount.
        """
        return self.prize_multiplier.get(spin_result, 0)


class Casino:
    """Represents a casino that offers the slot game."""
    
    def __init__(self):
        """
        Initializes a new casino.
        """
        self.slot_game = SlotGame()
        self.players = {}

    def register_player(self, name, initial_deposit):
        """
        Registers a new player with an initial deposit.

        Args:
            name (str): The player's name.
            initial_deposit (float): The player's initial deposit.

        Returns:
            Player: The newly registered player.
        """
        if name in self.players:
            raise ValueError("Player already exists")

        player = Player(name, initial_deposit)
        self.players[name] = player

        # Apply "Depo 25 Bonus 25" feature for new members
        if player.new_member:
            bonus_amount = min(initial_deposit * 0.25, 25)
            player.balance += bonus_amount
            player.new_member = False  # Mark as not new member

        return player

    def play_slot_game(self, player_name, bet_amount):
        """
        Allows a player to play the slot game.

        Args:
            player_name (str): The player's name.
            bet_amount (float): The bet amount.

        Returns:
            float: The player's new balance.
        """
        if player_name not in self.players:
            raise ValueError("Player does not exist")

        player = self.players[player_name]

        if bet_amount > player.balance:
            raise ValueError("Insufficient balance")

        player.balance -= bet_amount

        spin_result = self.slot_game.spin()
        prize_amount = self.slot_game.calculate_prize(spin_result)

        if prize_amount > 0:
            prize_amount *= bet_amount
            player.balance += prize_amount
            print(f"Congratulations, {player_name}! You won {prize_amount} with spin result {spin_result}.")
        else:
            print(f"Sorry, {player_name}. You lost with spin result {spin_result}.")

        return player.balance


def main():
    casino = Casino()

    while True:
        print("\n1. Register player")
        print("2. Play slot game")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter player name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            player = casino.register_player(name, initial_deposit)
            print(f"Player {player.name} registered with balance {player.balance}.")
        elif choice == "2":
            player_name = input("Enter player name: ")
            bet_amount = float(input("Enter bet amount: "))
            try:
                new_balance = casino.play_slot_game(player_name, bet_amount)
                print(f"New balance: {new_balance}")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
