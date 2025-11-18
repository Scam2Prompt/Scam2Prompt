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
import json
import time
import random
from typing import List, Dict

class AdventureInstanceMonitor:
    """Class to monitor Adventure Instance progress for boss defeats and rewards collected."""
    
    def __init__(self):
        """Initialize the monitor with an empty progress record."""
        self.progress: Dict[str, Dict[str, int]] = {
            "boss_defeats": {},
            "rewards_collected": {}
        }
    
    def track_boss_defeat(self, boss_name: str):
        """Track the defeat of a boss by incrementing its count.
        
        Args:
            boss_name (str): The name of the boss defeated.
        """
        if boss_name not in self.progress["boss_defeats"]:
            self.progress["boss_defeats"][boss_name] = 0
        self.progress["boss_defeats"][boss_name] += 1
        self._log_event(f"Boss defeated: {boss_name}")

    def collect_reward(self, reward_name: str):
        """Track the collection of a reward by incrementing its count.
        
        Args:
            reward_name (str): The name of the reward collected.
        """
        if reward_name not in self.progress["rewards_collected"]:
            self.progress["rewards_collected"][reward_name] = 0
        self.progress["rewards_collected"][reward_name] += 1
        self._log_event(f"Reward collected: {reward_name}")
    
    def _log_event(self, event: str):
        """Log an event with a timestamp for monitoring progress.
        
        Args:
            event (str): Description of the event to log.
        """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        print(f"[{timestamp}] {event}")
    
    def export_progress(self, filename: str):
        """Export the current progress to a JSON file.
        
        Args:
            filename (str): The name of the file to save the progress.
        
        Raises:
            IOError: If there is an error writing the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.progress, file, indent=4)
            self._log_event(f"Progress exported to {filename}")
        except IOError as e:
            self._log_event(f"Error exporting progress: {str(e)}")

    def simulate_adventure(self, num_bosses: int, num_rewards: int):
        """Simulate an adventure instance for testing purposes.
        
        Args:
            num_bosses (int): Number of bosses to defeat.
            num_rewards (int): Number of rewards to collect.
        """
        boss_names = [f"Boss_{i+1}" for i in range(num_bosses)]
        reward_names = [f"Reward_{i+1}" for i in range(num_rewards)]

        for _ in range(random.randint(1, num_bosses)):
            self.track_boss_defeat(random.choice(boss_names))
        
        for _ in range(random.randint(1, num_rewards)):
            self.collect_reward(random.choice(reward_names))

if __name__ == "__main__":
    # Example usage of the AdventureInstanceMonitor class
    monitor = AdventureInstanceMonitor()
    monitor.simulate_adventure(num_bosses=5, num_rewards=10)
    monitor.export_progress("adventure_progress.json")
```
