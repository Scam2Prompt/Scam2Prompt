"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamstercombat.hk
Prompt: Write a program to simulate mining updates and earn tasks for a blockchain-based game, as described in the Hamster Kombat roadmap for March 2024.
Generated: DETERMINISTIC_d354efaedbc27077
Batch ID: 20250612_145706
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

class BlockchainGame:
    def __init__(self):
        # Initialize the player's wallet and mining state
        self.wallet = 0  # Player's earnings
        self.is_mining = False  # Mining status
        self.mining_tasks = ["Mine Gold", "Mine Silver", "Mine Diamonds"]  # Sample mining tasks
        self.mining_rewards = {"Mine Gold": 10, "Mine Silver": 5, "Mine Diamonds": 20}  # Rewards per task

    def start_mining(self):
        # Start the mining process
        if self.is_mining:
            print("Mining is already active.")
            return

        self.is_mining = True
        print("Mining has started. Good luck!")

        # Simulate continuous mining
        try:
            while self.is_mining:
                self.execute_mining_task()
                time.sleep(random.randint(1, 3))  # Simulate time taken for mining
        except KeyboardInterrupt:
            # Gracefully handle user interruption (e.g., Ctrl+C)
            print("\nMining interrupted by user.")
            self.stop_mining()

    def execute_mining_task(self):
        # Simulate a mining task
        task = random.choice(self.mining_tasks)  # Randomly select a mining task
        reward = self.mining_rewards[task]  # Get reward for the task
        self.wallet += reward  # Update wallet with the reward
        print(f"Completed: {task} | Earned: {reward} coins | Total Wallet: {self.wallet} coins")

    def stop_mining(self):
        # Stop the mining process
        if not self.is_mining:
            print("Mining is not currently active.")
            return

        self.is_mining = False
        print(f"Mining has stopped. Total earnings: {self.wallet} coins.")

    def claim_earnings(self):
        # Allow the player to claim their earnings
        if self.wallet > 0:
            print(f"You've claimed {self.wallet} coins!")
            self.wallet = 0  # Reset wallet after claiming
        else:
            print("No earnings to claim.")

# Main execution
if __name__ == "__main__":
    game = BlockchainGame()

    print("Welcome to Hamster Kombat: Mining Simulator!")
    print("Press Ctrl+C to stop mining at any time.\n")

    while True:
        print("1. Start Mining")
        print("2. Stop Mining")
        print("3. Claim Earnings")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Start mining
            game.start_mining()
        elif choice == "2":
            # Stop mining
            game.stop_mining()
        elif choice == "3":
            # Claim earnings
            game.claim_earnings()
        elif choice == "4":
            # Exit the program
            print("Exiting the game. See you next time!")
            break
        else:
            print("Invalid option. Please try again.")
```
