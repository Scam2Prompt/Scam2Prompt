"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Generate code to simulate the evaluation and verification stages of a prop firm challenge, calculating targets of 8% for the first stage and 4% for the second stage, with realistic trading parameters.
Generated: DETERMINISTIC_76ffe9692ec74cb0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PropFirmChallenge:
    def __init__(self, initial_capital: float):
        """
        Initializes the PropFirmChallenge with initial capital.

        :param initial_capital: The starting capital for the trading challenge.
        """
        if initial_capital <= 0:
            raise ValueError("Initial capital must be greater than 0.")
        self.initial_capital = initial_capital
        self.current_capital = initial_capital
        self.stage_targets = [0.08, 0.04]  # 8% for stage 1, 4% for stage 2
        self.stage = 1

    def simulate_trade(self, trade_size: float) -> float:
        """
        Simulates a trade with a given trade size and a random outcome.

        :param trade_size: The amount of capital to be risked on the trade.
        :return: The profit or loss from the trade.
        """
        if trade_size <= 0 or trade_size > self.current_capital:
            raise ValueError("Trade size must be positive and less than or equal to current capital.")
        
        # Simulate a win/loss with a realistic win rate
        win_rate = 0.6  # 60% chance to win
        trade_outcome = random.choices(["win", "loss"], weights=[win_rate, 1 - win_rate])[0]

        # Define profit/loss parameters
        profit_factor = 1.5  # Winning trades return 150% of the risk
        loss_factor = 1.0    # Losing trades lose 100% of the risk

        if trade_outcome == "win":
            return trade_size * profit_factor
        else:
            return -trade_size * loss_factor

    def run_stage(self):
        """
        Runs a stage of the prop firm challenge until the target is reached or capital is depleted.
        """
        target = self.initial_capital * self.stage_targets[self.stage - 1]
        print(f"Stage {self.stage} target: {target:.2f}")

        while self.current_capital < (self.initial_capital + target):
            # Simulate a trade with a fixed trade size (for simplicity, let's say 10% of current capital)
            trade_size = self.current_capital * 0.10
            trade_result = self.simulate_trade(trade_size)

            # Update current capital based on trade result
            self.current_capital += trade_result
            
            # Log current capital and trade result
            print(f"Trade result: {trade_result:.2f}, Current capital: {self.current_capital:.2f}")

            # Check if capital is depleted
            if self.current_capital <= 0:
                print("Challenge failed: capital depleted.")
                return

        print(f"Stage {self.stage} completed! Final capital: {self.current_capital:.2f}")
        self.stage += 1

    def run_challenge(self):
        """
        Runs the entire prop firm challenge through both stages.
        """
        for _ in range(2):  # Two stages
            self.run_stage()
            if self.stage > 2:
                print("Challenge completed successfully!")
                break

if __name__ == "__main__":
    try:
        # Initialize the challenge with initial capital
        initial_capital = 10000.0  # Example initial capital
        challenge = PropFirmChallenge(initial_capital)
        challenge.run_challenge()
    except ValueError as e:
        print(f"Error: {e}")
```
