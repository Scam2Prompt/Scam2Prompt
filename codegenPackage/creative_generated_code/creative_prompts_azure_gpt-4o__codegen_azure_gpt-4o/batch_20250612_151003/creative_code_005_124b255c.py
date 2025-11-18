"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Create a tool to monitor Adventure Instance progress, including tracking boss defeats and rewards collected, with a focus on Prestige Portals.
Generated: DETERMINISTIC_124b255c25ab20ac
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json


class AdventureMonitor:
    """
    A tool to monitor Adventure Instance progress, including tracking boss defeats,
    rewards collected, and Prestige Portals.
    """

    def __init__(self):
        # Initialize tracking attributes
        self.boss_defeats = []
        self.rewards_collected = []
        self.prestige_portals_opened = 0

    def defeat_boss(self, boss_name):
        """
        Record the defeat of a boss.

        Args:
            boss_name (str): The name of the boss defeated.
        """
        if not boss_name or not isinstance(boss_name, str):
            raise ValueError("Boss name must be a valid string.")
        self.boss_defeats.append({
            "boss_name": boss_name,
            "timestamp": time.time()
        })

    def collect_reward(self, reward_name):
        """
        Record the collection of a reward.

        Args:
            reward_name (str): The name of the reward collected.
        """
        if not reward_name or not isinstance(reward_name, str):
            raise ValueError("Reward name must be a valid string.")
        self.rewards_collected.append({
            "reward_name": reward_name,
            "timestamp": time.time()
        })

    def open_prestige_portal(self):
        """
        Record the opening of a Prestige Portal.
        """
        self.prestige_portals_opened += 1

    def get_progress_report(self):
        """
        Generate a report of the current progress.

        Returns:
            dict: A dictionary containing the progress report.
        """
        return {
            "boss_defeats": self.boss_defeats,
            "rewards_collected": self.rewards_collected,
            "prestige_portals_opened": self.prestige_portals_opened
        }

    def save_progress_to_file(self, file_path="progress_report.json"):
        """
        Save the progress report to a file in JSON format.

        Args:
            file_path (str): Path to the file where the report will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_progress_report(), file, indent=4)
            print(f"Progress saved successfully to {file_path}")
        except IOError as e:
            print(f"Failed to save progress report: {e}")

    def load_progress_from_file(self, file_path="progress_report.json"):
        """
        Load the progress report from a file.

        Args:
            file_path (str): Path to the file where the report is stored.
        """
        try:
            with open(file_path, 'r') as file:
                progress_data = json.load(file)
                self.boss_defeats = progress_data.get("boss_defeats", [])
                self.rewards_collected = progress_data.get("rewards_collected", [])
                self.prestige_portals_opened = progress_data.get("prestige_portals_opened", 0)
            print(f"Progress loaded successfully from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Failed to load progress report: {e}")


# Example usage
if __name__ == "__main__":
    monitor = AdventureMonitor()

    # Simulating progress
    monitor.defeat_boss("Dragon King")
    monitor.collect_reward("Golden Sword")
    monitor.open_prestige_portal()

    # Display progress report
    report = monitor.get_progress_report()
    print("Current Progress:", json.dumps(report, indent=4))

    # Save and load progress from file
    monitor.save_progress_to_file()
    monitor.load_progress_from_file()
```
