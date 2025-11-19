"""
Generated Code Metadata:
========================
Original URL: https://hamstercombat.hk
Prompt: Write a program to simulate mining updates and earn tasks for a blockchain-based game, as described in the Hamster Kombat roadmap for March 2024.
Generated: DETERMINISTIC_d354efaedbc27077
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import logging
from typing import List, Dict

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Task:
    """Class representing a mining task in the blockchain-based game."""
    
    def __init__(self, task_id: int, reward: int):
        self.task_id = task_id
        self.reward = reward
        self.completed = False

    def complete_task(self):
        """Mark the task as completed."""
        self.completed = True
        logging.info(f"Task {self.task_id} completed with reward: {self.reward}")

class Miner:
    """Class representing a miner in the game."""
    
    def __init__(self, miner_id: int):
        self.miner_id = miner_id
        self.tasks: List[Task] = []

    def generate_task(self) -> Task:
        """Generate a new mining task with a random reward."""
        task_id = len(self.tasks) + 1
        reward = random.randint(10, 100)  # Random reward between 10 and 100
        new_task = Task(task_id, reward)
        self.tasks.append(new_task)
        logging.info(f"Miner {self.miner_id} generated task {task_id} with reward: {reward}")
        return new_task

    def complete_task(self, task_id: int):
        """Complete a task by its ID."""
        for task in self.tasks:
            if task.task_id == task_id and not task.completed:
                task.complete_task()
                return
        logging.warning(f"Task {task_id} not found or already completed.")

class Game:
    """Class representing the game that manages miners and tasks."""
    
    def __init__(self):
        self.miners: Dict[int, Miner] = {}
        self.task_generation_interval = 5  # Time in seconds between task generations

    def add_miner(self, miner_id: int):
        """Add a new miner to the game."""
        if miner_id not in self.miners:
            self.miners[miner_id] = Miner(miner_id)
            logging.info(f"Miner {miner_id} added to the game.")
        else:
            logging.warning(f"Miner {miner_id} already exists.")

    def start_mining(self):
        """Start the mining process for all miners."""
        try:
            while True:
                for miner in self.miners.values():
                    miner.generate_task()
                time.sleep(self.task_generation_interval)
        except KeyboardInterrupt:
            logging.info("Mining process stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred during mining: {e}")

if __name__ == "__main__":
    # Initialize the game
    game = Game()
    
    # Add miners to the game
    game.add_miner(1)
    game.add_miner(2)

    # Start the mining process
    game.start_mining()
```
