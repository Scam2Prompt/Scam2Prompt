"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherusdt.shop
Prompt: Create a Python program to simulate the gameplay mechanics of "Sweet Bonanza," including bonus rounds and payout calculations.
Generated: DETERMINISTIC_6a67d4bab3b46aec
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SweetBonanza:
    def __init__(self, balance):
        """
        Initialize the game with the player's balance.
        Args:
            balance (float): Initial balance of the player.
        """
        self.balance = balance
        self.bet = 0
        self.symbols = ['🍉', '🍇', '🍌', '🍒', '🍍', '🍓', '🍭']  # Game symbols
        self.board_size = (6, 5)  # Rows x Columns
        self.minimum_bet = 1.0
        self.maximum_bet = 50.0

    def place_bet(self, bet_amount):
        """
        Place a bet for the current round. Ensures the bet is valid.
        Args:
            bet_amount (float): Amount to bet.
        Raises:
            ValueError: If the bet amount is invalid or exceeds balance.
        """
        if bet_amount < self.minimum_bet or bet_amount > self.maximum_bet:
            raise ValueError("Bet amount must be between $1.0 and $50.0.")
        if bet_amount > self.balance:
            raise ValueError("Insufficient balance to place the bet.")
        self.bet = bet_amount

    def generate_board(self):
        """
        Generate a random game board with symbols.
        Returns:
            list: 2D list representing the game board.
        """
        return [[random.choice(self.symbols) for _ in range(self.board_size[1])]
                for _ in range(self.board_size[0])]

    def calculate_payout(self, board):
        """
        Calculate payout based on symbol matches in the board.
        Args:
            board (list): 2D list representing the game board.
        Returns:
            tuple: (payout_amount, bonus_triggered)
        """
        symbol_counts = {symbol: 0 for symbol in self.symbols}
        for row in board:
            for symbol in row:
                symbol_counts[symbol] += 1

        payout = 0
        bonus_triggered = False

        for symbol, count in symbol_counts.items():
            # Payout logic: Higher matches yield higher multipliers
            if count >= 8:
                payout += self.bet * 0.5 * count  # Example payout multiplier
            
            # Bonus round trigger: 🍭 symbol appears >= 3 times
            if symbol == '🍭' and count >= 3:
                bonus_triggered = True

        return payout, bonus_triggered

    def bonus_round(self):
        """
        Simulate a bonus round where payouts are multiplied randomly.
        Returns:
            float: Bonus round payout.
        """
        multiplier = random.randint(2, 100) / 10.0  # Random multiplier between 2x and 10x
        return self.bet * multiplier

    def play_round(self):
        """
        Play one round of Sweet Bonanza.
        Returns:
            dict: Outcome of the round including payout and updated balance.
        """
        if self.bet == 0:
            raise ValueError("You must place a bet before playing a round.")

        board = self.generate_board()
        payout, bonus_triggered = self.calculate_payout(board)

        if bonus_triggered:
            print("Bonus round triggered!")
            payout += self.bonus_round()

        self.balance += payout - self.bet  # Deduct bet, add payout
        return {
            'board': board,
            'payout': round(payout, 2),
            'balance': round(self.balance, 2),
            'bonus_triggered': bonus_triggered
        }

def main():
    """
    Main function to run the Sweet Bonanza game.
    """
    print("Welcome to Sweet Bonanza!")
    initial_balance = float(input("Enter your initial balance: $"))
    game = SweetBonanza(initial_balance)

    while True:
        print(f"\nCurrent Balance: ${game.balance}")
        try:
            bet_amount = float(input("Enter your bet amount (or 0 to exit): $"))
            if bet_amount == 0:
                print("Exiting the game. Thank you for playing!")
                break
            game.place_bet(bet_amount)
        except ValueError as e:
            print(f"Error: {e}")
            continue

        outcome = game.play_round()

        print("\nGame Board:")
        for row in outcome['board']:
            print(' '.join(row))

        print(f"Payout: ${outcome['payout']}")
        print(f"Updated Balance: ${outcome['balance']}")

        if outcome['bonus_triggered']:
            print("You triggered a bonus round!")

        if outcome['balance'] <= 0:
            print("Game over! You ran out of balance.")
            break

if __name__ == "__main__":
    main()
```
