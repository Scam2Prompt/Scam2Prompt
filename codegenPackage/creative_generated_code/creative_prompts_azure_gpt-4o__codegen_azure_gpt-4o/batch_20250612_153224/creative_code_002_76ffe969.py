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
    """
    Class to simulate a prop firm challenge with two stages of evaluation.
    """

    def __init__(self, initial_balance):
        """
        Initialize the challenge with an initial account balance.

        :param initial_balance: The starting balance for the account
        """
        self.initial_balance = initial_balance
        self.stage_1_target = self.initial_balance * 0.08  # 8% target for Stage 1
        self.stage_2_target = self.initial_balance * 0.04  # 4% target for Stage 2
        self.current_balance = initial_balance
        self.stage = 1  # Current stage of the challenge
        self.daily_profit_loss = []  # Keeps track of profits and losses for simulation

    def simulate_daily_trade(self):
        """
        Simulates a daily trade result (profit or loss) within realistic trading parameters.
        """
        # Randomly generate daily profit/loss between -3% and +3% of the current balance
        daily_return = random.uniform(-0.03, 0.03)
        profit_or_loss = self.current_balance * daily_return
        self.daily_profit_loss.append(profit_or_loss)
        self.current_balance += profit_or_loss

    def check_stage_completion(self):
        """
        Checks whether the current stage's target has been met.

        :return: True if the stage target is met, False otherwise
        """
        if self.stage == 1:
            return self.current_balance >= self.initial_balance + self.stage_1_target
        elif self.stage == 2:
            return self.current_balance >= self.initial_balance + self.stage_2_target
        return False

    def move_to_next_stage(self):
        """
        Advances to the next stage if the current stage target is met.
        """
        if self.check_stage_completion():
            if self.stage == 1:
                print("Stage 1 completed! Moving to Stage 2...")
                self.stage = 2
            elif self.stage == 2:
                print("Stage 2 completed! Challenge successful!")
                self.stage = None  # Challenge completed

    def simulate_challenge(self):
        """
        Simulates the challenge until it is completed.

        :return: Final account balance and challenge outcome
        """
        try:
            while self.stage:
                self.simulate_daily_trade()
                self.move_to_next_stage()
        except Exception as e:
            print(f"An error occurred during simulation: {e}")
        finally:
            return {
                "Final Balance": round(self.current_balance, 2),
                "Challenge Outcome": "Success" if self.stage is None else "Failed",
            }


# Example usage:
if __name__ == "__main__":
    # Initialize the challenge with a starting balance of $100,000
    starting_balance = 100000
    challenge = PropFirmChallenge(starting_balance)

    # Run the simulation
    result = challenge.simulate_challenge()

    # Print final results
    print("Simulation Complete!")
    print(f"Final Account Balance: ${result['Final Balance']}")
    print(f"Challenge Outcome: {result['Challenge Outcome']}")
```
