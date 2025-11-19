"""
Generated Code Metadata:
========================
Original URL: https://locinews.com
Prompt: Write code to simulate a betting game for "Bầu Cua Bet88," incorporating the unique gameplay mechanics described on the website.
Generated: DETERMINISTIC_d71f5722c6de7836
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import sys
from enum import Enum

class DiceFace(Enum):
    FISH = "Fish"
    PRAWN = "Prawn"
    CRAB = "Crab"
    ROOSTER = "Rooster"
    GOURD = "Gourd"
    DEER = "Deer"

class BetType(Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    TRIPLE = "Triple"

class GameResult:
    def __init__(self, dice_results, payouts):
        self.dice_results = dice_results
        self.payouts = payouts

    def __str__(self):
        return f"Dice: {[face.value for face in self.dice_results]}, Payouts: {self.payouts}"

class Player:
    def __init__(self, name, initial_balance=1000):
        self.name = name
        self.balance = initial_balance
        self.bets = {}

    def place_bet(self, face, amount, bet_type=BetType.SINGLE):
        if amount <= 0:
            raise ValueError("Bet amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        
        key = (face, bet_type)
        if key in self.bets:
            self.bets[key] += amount
        else:
            self.bets[key] = amount
        
        self.balance -= amount

    def clear_bets(self):
        self.bets = {}

    def receive_winnings(self, amount):
        if amount < 0:
            raise ValueError("Winnings cannot be negative")
        self.balance += amount

class BauCuaGame:
    PAYOUT_RATES = {
        BetType.SINGLE: 1,
        BetType.DOUBLE: 2,
        BetType.TRIPLE: 3
    }

    def __init__(self):
        self.players = []
        self.current_bets = {}

    def add_player(self, player):
        self.players.append(player)

    def roll_dice(self):
        return [random.choice(list(DiceFace)) for _ in range(3)]

    def calculate_payouts(self, dice_results):
        payouts = {}
        face_counts = {face: dice_results.count(face) for face in DiceFace}

        for player in self.players:
            total_winnings = 0
            for (face, bet_type), amount in player.bets.items():
                count = face_counts.get(face, 0)
                
                if bet_type == BetType.SINGLE and count >= 1:
                    multiplier = self.PAYOUT_RATES[BetType.SINGLE] * count
                elif bet_type == BetType.DOUBLE and count >= 2:
                    multiplier = self.PAYOUT_RATES[BetType.DOUBLE]
                elif bet_type == BetType.TRIPLE and count == 3:
                    multiplier = self.PAYOUT_RATES[BetType.TRIPLE]
                else:
                    multiplier = 0
                
                total_winnings += amount * multiplier
            
            payouts[player.name] = total_winnings
        
        return payouts

    def play_round(self):
        dice_results = self.roll_dice()
        payouts = self.calculate_payouts(dice_results)

        # Distribute winnings
        for player in self.players:
            winnings = payouts.get(player.name, 0)
            player.receive_winnings(winnings)
            player.clear_bets()

        return GameResult(dice_results, payouts)

def main():
    try:
        game = BauCuaGame()
        
        # Create players
        player1 = Player("Alice", 1000)
        player2 = Player("Bob", 1500)
        game.add_player(player1)
        game.add_player(player2)

        # Place bets
        player1.place_bet(DiceFace.CRAB, 100, BetType.SINGLE)
        player1.place_bet(DiceFace.FISH, 50, BetType.DOUBLE)
        player2.place_bet(DiceFace.ROOSTER, 200, BetType.SINGLE)
        player2.place_bet(DiceFace.PRAWN, 100, BetType.TRIPLE)

        # Play round
        result = game.play_round()
        print(result)

        # Show player balances
        print(f"{player1.name}'s balance: {player1.balance}")
        print(f"{player2.name}'s balance: {player2.balance}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
