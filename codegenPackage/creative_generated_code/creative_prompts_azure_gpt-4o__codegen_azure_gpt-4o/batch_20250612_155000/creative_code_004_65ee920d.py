"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethminer.world
Prompt: Create a program that simulates ETHMiner's "auto mining 24/7" feature, including a visualization of mining progress and daily payouts for different plans.
Generated: DETERMINISTIC_65ee920da670c069
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class ETHMinerSimulator:
    """
    A class to simulate ETH mining with auto-mining functionality,
    mining progress visualization, and daily payouts for different plans.
    """

    def __init__(self):
        # Define mining plans and their respective payouts per day (ETH)
        self.plans = {
            "Basic": 0.01,   # 0.01 ETH/day
            "Standard": 0.05, # 0.05 ETH/day
            "Premium": 0.10   # 0.1 ETH/day
        }
        # Initialize mining progress and mined ETH
        self.mining_progress = 0.0
        self.mined_eth = 0.0

    def visualize_mining_progress(self):
        """
        Visualize the mining progress as a percentage.
        """
        progress_bar = "#" * int(self.mining_progress // 2)  # Create a progress bar
        print(f"Mining Progress: [{progress_bar:<50}] {self.mining_progress:.2f}%")

    def simulate_mining(self, plan):
        """
        Simulates mining for a single day with the selected plan.
        :param plan: The chosen mining plan ('Basic', 'Standard', 'Premium')
        """
        if plan not in self.plans:
            raise ValueError(f"Invalid plan selected: {plan}. Available plans: {list(self.plans.keys())}")

        print(f"\nStarting mining with the '{plan}' plan...")
        daily_payout = self.plans[plan]  # ETH payout per day
        self.mining_progress = 0.0  # Reset daily progress

        for _ in range(100):  # Simulate progress in 100 steps
            time.sleep(0.1)  # Simulated delay
            self.mining_progress += random.uniform(0.5, 1.0)  # Random progress increment
            self.mining_progress = min(self.mining_progress, 100.0)  # Cap progress to 100%
            self.visualize_mining_progress()

        self.mined_eth += daily_payout  # Add daily payout to total mined ETH
        print(f"\nMining completed for the day. Earned {daily_payout:.2f} ETH.")
        print(f"Total mined ETH: {self.mined_eth:.2f}")

    def start_auto_mining(self, plan, days):
        """
        Start auto-mining for a given number of days with the chosen plan.
        :param plan: The chosen mining plan ('Basic', 'Standard', 'Premium')
        :param days: Number of days to mine
        """
        print(f"Starting auto-mining with the '{plan}' plan for {days} days...\n")

        for day in range(1, days + 1):
            print(f"Day {day} of {days}")
            try:
                self.simulate_mining(plan)
            except ValueError as e:
                print(f"Error during mining: {e}")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
                break

        print("\nAuto-mining session completed.")
        print(f"Total ETH mined: {self.mined_eth:.2f}")


if __name__ == "__main__":
    # Create an instance of the ETHMiner simulator
    miner = ETHMinerSimulator()

    # Prompt the user for input
    print("Welcome to ETHMiner Simulator!")
    print("Available plans:")
    for plan, payout in miner.plans.items():
        print(f"- {plan}: {payout:.2f} ETH/day")

    try:
        selected_plan = input("Select a plan (Basic, Standard, Premium): ").strip()
        number_of_days = int(input("Enter the number of days to mine: "))

        # Start auto-mining
        miner.start_auto_mining(selected_plan, number_of_days)
    except ValueError:
        print("Invalid input. Please enter valid plan and number of days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

```
