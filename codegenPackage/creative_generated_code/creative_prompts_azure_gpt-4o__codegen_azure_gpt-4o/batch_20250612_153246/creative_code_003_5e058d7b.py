"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blogdotrabalhadordigital.com
Prompt: Provide a Python script to simulate gameplay for a table game offered by Pelangi189, including random win/loss outcomes and bonus triggers.
Generated: DETERMINISTIC_5e058d7be04595b3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class TableGameSimulator:
    """
    A class to simulate gameplay for a table game with random win/loss outcomes
    and bonus triggers.
    """

    def __init__(self, player_name, rounds=10):
        """
        Initializes the table game simulator.
        
        :param player_name: Name of the player
        :param rounds: Number of rounds to simulate gameplay (default is 10)
        """
        self.player_name = player_name
        self.rounds = rounds
        self.total_wins = 0
        self.total_losses = 0
        self.total_bonus = 0

    def simulate_round(self, round_number):
        """
        Simulates a single round of the table game.
        
        :param round_number: The current round number
        :return: A dictionary with the result of the round
        """
        result = random.choice(['WIN', 'LOSS'])  # Randomly determine win or loss
        bonus_triggered = random.random() < 0.2  # 20% chance of triggering a bonus
        
        if result == 'WIN':
            self.total_wins += 1
        else:
            self.total_losses += 1

        if bonus_triggered:
            bonus_amount = random.randint(10, 100)  # Random bonus between 10 and 100
            self.total_bonus += bonus_amount
        else:
            bonus_amount = 0

        return {
            'round_number': round_number,
            'result': result,
            'bonus_triggered': bonus_triggered,
            'bonus_amount': bonus_amount
        }

    def simulate_gameplay(self):
        """
        Simulates multiple rounds of table gameplay.
        """
        print(f"Starting gameplay simulation for {self.player_name}...\n")
        time.sleep(1)

        for round_number in range(1, self.rounds + 1):
            round_result = self.simulate_round(round_number)
            print(f"Round {round_result['round_number']}: Result = {round_result['result']}, "
                  f"Bonus Triggered = {round_result['bonus_triggered']}, "
                  f"Bonus Amount = {round_result['bonus_amount']}")
            time.sleep(0.5)

        print("\nGameplay simulation completed!")
        print(f"Total Wins: {self.total_wins}")
        print(f"Total Losses: {self.total_losses}")
        print(f"Total Bonus Awarded: {self.total_bonus}")

    def run(self):
        """
        Entry point to start the simulation.
        Includes error handling to ensure smooth execution.
        """
        try:
            self.simulate_gameplay()
        except Exception as e:
            print(f"An unexpected error occurred during gameplay simulation: {e}")


if __name__ == "__main__":
    # Example usage:
    player_name = input("Enter player name: ").strip()
    try:
        rounds = int(input("Enter number of rounds to play: "))
        if rounds <= 0:
            raise ValueError("Number of rounds must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input for rounds: {e}. Defaulting to 10 rounds.")
        rounds = 10
    
    game_simulator = TableGameSimulator(player_name, rounds)
    game_simulator.run()
```
