"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: Generate code to simulate the evaluation and verification stages of a prop firm challenge, calculating targets of 8% for the first stage and 4% for the second stage, with realistic trading parameters.
Generated: DETERMINISTIC_76ffe9692ec74cb0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class PropFirmChallenge:
    def __init__(self, initial_balance, stage_one_target=0.08, stage_two_target=0.04):
        """
        Initialize the Prop Firm Challenge with the given parameters.

        :param initial_balance: The starting balance for the trading challenge.
        :param stage_one_target: The target profit percentage for stage one (default is 8%).
        :param stage_two_target: The target profit percentage for stage two (default is 4%).
        """
        self.initial_balance = initial_balance
        self.stage_one_target = stage_one_target
        self.stage_two_target = stage_two_target
        self.current_balance = initial_balance
        self.stage_one_completed = False
        self.stage_two_completed = False

    def simulate_trade(self):
        """
        Simulate a single trade with random profit or loss.

        :return: The profit or loss from the trade.
        """
        # Simulate a trade outcome with a random profit/loss between -2% and +2%
        trade_outcome = random.uniform(-0.02, 0.02)
        return self.current_balance * trade_outcome

    def evaluate_stage(self, stage):
        """
        Evaluate the specified stage of the challenge.

        :param stage: The stage to evaluate (1 or 2).
        :raises ValueError: If the stage is not 1 or 2.
        """
        if stage not in [1, 2]:
            raise ValueError("Stage must be either 1 or 2.")

        target = self.initial_balance * (self.stage_one_target if stage == 1 else self.stage_two_target)
        while not self.stage_one_completed and stage == 1:
            profit_loss = self.simulate_trade()
            self.current_balance += profit_loss
            print(f"Stage 1 Trade Outcome: {profit_loss:.2f}, Current Balance: {self.current_balance:.2f}")
            if self.current_balance >= self.initial_balance + target:
                self.stage_one_completed = True
                print("Stage 1 target achieved!")

        while not self.stage_two_completed and stage == 2:
            profit_loss = self.simulate_trade()
            self.current_balance += profit_loss
            print(f"Stage 2 Trade Outcome: {profit_loss:.2f}, Current Balance: {self.current_balance:.2f}")
            if self.current_balance >= self.initial_balance + target:
                self.stage_two_completed = True
                print("Stage 2 target achieved!")

    def run_challenge(self):
        """
        Run the entire prop firm challenge through both stages.
        """
        try:
            print("Starting Stage 1...")
            self.evaluate_stage(1)
            if self.stage_one_completed:
                print("Starting Stage 2...")
                self.evaluate_stage(2)
            else:
                print("Stage 1 not completed. Challenge failed.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    initial_balance = 10000  # Starting balance for the challenge
    challenge = PropFirmChallenge(initial_balance)
    challenge.run_challenge()
```
