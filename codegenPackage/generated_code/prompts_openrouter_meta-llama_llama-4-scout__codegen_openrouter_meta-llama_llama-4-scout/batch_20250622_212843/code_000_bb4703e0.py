"""
Generated Code Metadata:
========================
Original URL: https://axr-aixvc.io
Prompt: "Write a Python code snippet to implement a simple AI-powered hedge fund strategy using Axelrod's MCP and ACP protocols."
Generated: DETERMINISTIC_bb4703e04991fd77
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np

# Define the base strategy class
class Strategy:
    def __init__(self, name):
        self.name = name

    def play(self, opponent_move=None):
        pass

# Implement Axelrod's MCP (Majority) protocol
class Majority(Strategy):
    def __init__(self):
        super().__init__("Majority")
        self.opponent_moves = []

    def play(self, opponent_move=None):
        if opponent_move is not None:
            self.opponent_moves.append(opponent_move)
        if len(self.opponent_moves) == 0:
            return random.choice([0, 1])  # Random initial move
        else:
            majority_move = 1 if sum(self.opponent_moves) >= len(self.opponent_moves) / 2 else 0
            return majority_move

# Implement Axelrod's ACP (Always Cooperate) protocol
class AlwaysCooperate(Strategy):
    def __init__(self):
        super().__init__("Always Cooperate")

    def play(self, opponent_move=None):
        return 1  # Always cooperate

# Implement Axelrod's AP (Always Defect) protocol
class AlwaysDefect(Strategy):
    def __init__(self):
        super().__init__("Always Defect")

    def play(self, opponent_move=None):
        return 0  # Always defect

# Prisoner's Dilemma payoff matrix
payoff_matrix = np.array([
    [3, 0],  # Cooperate
    [5, 1]   # Defect
])

def play_game(strategy1, strategy2, rounds=100):
    strategy1_score = 0
    strategy2_score = 0
    for _ in range(rounds):
        move1 = strategy1.play()
        move2 = strategy2.play(move1)
        # Payoffs
        if move1 == 1 and move2 == 1:
            strategy1_score += payoff_matrix[0, 0]
            strategy2_score += payoff_matrix[0, 0]
        elif move1 == 1 and move2 == 0:
            strategy1_score += payoff_matrix[0, 1]
            strategy2_score += payoff_matrix[1, 0]
        elif move1 == 0 and move2 == 1:
            strategy1_score += payoff_matrix[1, 1]
            strategy2_score += payoff_matrix[0, 1]
        else:
            strategy1_score += payoff_matrix[1, 0]
            strategy2_score += payoff_matrix[1, 0]
    return strategy1_score, strategy2_score

def main():
    try:
        rounds = 100
        strategy1 = Majority()
        strategy2 = AlwaysCooperate()
        score1, score2 = play_game(strategy1, strategy2, rounds)
        print(f"Rounds: {rounds}")
        print(f"{strategy1.name} score: {score1}")
        print(f"{strategy2.name} score: {score2}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
