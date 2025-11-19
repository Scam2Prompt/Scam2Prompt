"""
Generated Code Metadata:
========================
Original URL: https://thegraph.live
Prompt: Generate a Python script to calculate daily rewards based on the required business GRT levels for The Graph's incentive program.
Generated: DETERMINISTIC_e28b0171bb626d55
Batch ID: 20250612_155301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class DailyRewardCalculator:
    """
    A class to calculate daily rewards based on the required business GRT levels for The Graph's incentive program.
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the DailyRewardCalculator with configuration data.

        Args:
            config_path (Optional[str]): Path to a JSON configuration file. If None, uses default values.
        """
        self.grt_levels = {
            'low': 1000,
            'medium': 5000,
            'high': 10000
        }
        self.reward_rates = {
            'low': 0.01,
            'medium': 0.05,
            'high': 0.1
        }

        if config_path:
            self.load_config(config_path)

    def load_config(self, config_path: str) -> None:
        """
        Load configuration from a JSON file.

        Args:
            config_path (str): Path to the JSON configuration file.

        Raises:
            FileNotFoundError: If the config file doesn't exist.
            json.JSONDecodeError: If the config file is not valid JSON.
            KeyError: If required fields are missing in the config.
        """
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            
            self.grt_levels = config['grt_levels']
            self.reward_rates = config['reward_rates']
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in configuration file", doc="", pos=0)
        except KeyError as e:
            raise KeyError(f"Missing required configuration field: {e}")

    def calculate_daily_reward(self, grt_staked: float) -> float:
        """
        Calculate the daily reward based on the amount of GRT staked.

        Args:
            grt_staked (float): The amount of GRT staked by the participant.

        Returns:
            float: The daily reward in GRT.

        Raises:
            ValueError: If grt_staked is negative.
        """
        if grt_staked < 0:
            raise ValueError("GRT staked cannot be negative")

        if grt_staked >= self.grt_levels['high']:
            return grt_staked * self.reward_rates['high']
        elif grt_staked >= self.grt_levels['medium']:
            return grt_staked * self.reward_rates['medium']
        elif grt_staked >= self.grt_levels['low']:
            return grt_staked * self.reward_rates['low']
        else:
            return 0.0

    def calculate_rewards_for_multiple(self, participants: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate daily rewards for multiple participants.

        Args:
            participants (Dict[str, float]): Dictionary of participant names and their GRT staked.

        Returns:
            Dict[str, float]: Dictionary of participant names and their daily rewards.

        Raises:
            ValueError: If any participant has negative GRT staked.
        """
        results = {}
        for name, grt in participants.items():
            if grt < 0:
                raise ValueError(f"Participant {name} has negative GRT staked")
            results[name] = self.calculate_daily_reward(grt)
        return results

if __name__ == "__main__":
    # Example usage
    try:
        calculator = DailyRewardCalculator()
        
        # Single participant example
        grt_staked = 7500
        reward = calculator.calculate_daily_reward(grt_staked)
        print(f"Daily reward for {grt_staked} GRT staked: {reward:.2f} GRT")

        # Multiple participants example
        participants = {
            "Alice": 2000,
            "Bob": 6000,
            "Charlie": 12000,
            "Dana": 500
        }
        rewards = calculator.calculate_rewards_for_multiple(participants)
        print("\nDaily rewards for participants:")
        for name, reward in rewards.items():
            print(f"{name}: {reward:.2f} GRT")

    except Exception as e:
        print(f"An error occurred: {e}")
```
