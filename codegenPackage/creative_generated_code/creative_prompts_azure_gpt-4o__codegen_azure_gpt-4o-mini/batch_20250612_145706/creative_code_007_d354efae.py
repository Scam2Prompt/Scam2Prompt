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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MiningTask:
    """
    A class representing a mining task in the blockchain-based game.
    """
    def __init__(self, task_id: int, reward: float):
        self.task_id = task_id  # Unique identifier for the task
        self.reward = reward      # Reward for completing the mining task

    def __repr__(self):
        return f"MiningTask(id={self.task_id}, reward={self.reward})"


class Miner:
    """
    A class representing a miner in the game.
    """
    def __init__(self, name: str):
        self.name = name          # Name of the miner
        self.balance = 0.0       # Initial balance
        self.tasks_completed = [] # List of completed tasks

    def complete_task(self, task: MiningTask) -> None:
        """
        Simulate the completion of a mining task.
        :param task: The mining task to be completed.
        """
        logging.info(f"{self.name} is completing task {task.task_id}...")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate time taken to complete the task
        self.balance += task.reward
        self.tasks_completed.append(task)
        logging.info(f"{self.name} completed task {task.task_id} and earned {task.reward}. Current balance: {self.balance}")


class MiningSimulator:
    """
    A class to simulate the mining process.
    """
    def __init__(self):
        self.tasks = []  # List of available mining tasks

    def generate_tasks(self, num_tasks: int) -> None:
        """
        Generates a list of mining tasks.
        :param num_tasks: Number of tasks to generate.
        """
        self.tasks = [MiningTask(task_id=i, reward=random.uniform(1, 10)) for i in range(num_tasks)]
        logging.info(f"Generated {num_tasks} mining tasks.")

    def start_mining(self, miner: Miner) -> None:
        """
        Simulate the mining process for the given miner.
        :param miner: The miner who will complete the tasks.
        """
        if not self.tasks:
            logging.error("No tasks available to mine.")
            return

        for task in self.tasks:
            miner.complete_task(task)

        logging.info(f"{miner.name} finished mining. Total balance: {miner.balance}")


def main():
    """
    Main function to run the mining simulation.
    """
    try:
        # Create a miner
        miner_name = "HamsterMiner"
        miner = Miner(name=miner_name)

        # Create a mining simulator and generate tasks
        simulator = MiningSimulator()
        simulator.generate_tasks(num_tasks=5)

        # Start the mining process
        simulator.start_mining(miner)

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
