"""
Generated Code Metadata:
========================
Original URL: https://casinovlad.com
Prompt: "Generate a Python code snippet to implement a simple lottery game similar to those found on Cazino Vlad, including functionalities for ticket purchase and prize distribution."
Generated: DETERMINISTIC_ac8ddf20d10223df
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class LotteryGame:
    def __init__(self):
        self.tickets = {}  # Dictionary to store ticket purchases
        self.winning_numbers = []  # List to store winning numbers
        self.prize_pool = 1000  # Total prize pool for the lottery

    def purchase_ticket(self, player_name, numbers):
        """
        Allows a player to purchase a lottery ticket with selected numbers.
        
        :param player_name: Name of the player purchasing the ticket
        :param numbers: List of numbers chosen by the player (must be unique and within range)
        :raises ValueError: If numbers are not unique or out of range
        """
        if len(numbers) != 6 or len(set(numbers)) != 6 or any(n < 1 or n > 49 for n in numbers):
            raise ValueError("You must select 6 unique numbers between 1 and 49.")
        
        self.tickets[player_name] = numbers
        print(f"Ticket purchased successfully for {player_name}: {numbers}")

    def draw_winning_numbers(self):
        """
        Draws the winning numbers for the lottery.
        """
        self.winning_numbers = random.sample(range(1, 50), 6)
        print(f"Winning numbers drawn: {self.winning_numbers}")

    def check_winners(self):
        """
        Checks the tickets against the winning numbers and distributes prizes.
        """
        winners = {}
        for player, numbers in self.tickets.items():
            matches = set(numbers) & set(self.winning_numbers)
            if matches:
                winners[player] = matches
        
        if winners:
            for player, matches in winners.items():
                prize = self.calculate_prize(len(matches))
                print(f"{player} matched {len(matches)} numbers: {matches}. Prize: ${prize}")
        else:
            print("No winners this time.")

    def calculate_prize(self, match_count):
        """
        Calculates the prize based on the number of matches.
        
        :param match_count: Number of matches found
        :return: Prize amount
        """
        prize_distribution = {6: 500, 5: 300, 4: 100, 3: 50}
        return prize_distribution.get(match_count, 0)

def main():
    game = LotteryGame()
    
    # Example of purchasing tickets
    try:
        game.purchase_ticket("Alice", [5, 12, 23, 34, 45, 49])
        game.purchase_ticket("Bob", [1, 2, 3, 4, 5, 6])
        game.purchase_ticket("Charlie", [10, 20, 30, 40, 50, 60])  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")

    # Draw winning numbers
    game.draw_winning_numbers()
    
    # Check for winners
    game.check_winners()

if __name__ == "__main__":
    main()
```
