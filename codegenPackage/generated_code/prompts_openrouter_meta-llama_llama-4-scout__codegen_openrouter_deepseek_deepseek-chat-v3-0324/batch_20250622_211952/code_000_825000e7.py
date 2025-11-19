"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: "Write a Python script to track and convert daily steps into Energy and KI Tokens in a move-to-earn game like Genopets."
Generated: DETERMINISTIC_825000e701337cf0
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple

# Constants
STEPS_TO_ENERGY_RATIO = 1000  # 1000 steps = 1 Energy
ENERGY_TO_TOKEN_RATIO = 10    # 10 Energy = 1 KI Token
DAILY_ENERGY_CAP = 20         # Max Energy that can be earned per day
DATA_FILE = "user_data.json"  # File to store user data

class StepTracker:
    """
    A class to track daily steps, convert them to Energy and KI Tokens,
    and manage user data persistence.
    """
    
    def __init__(self):
        self.user_data = self._load_user_data()
    
    def _load_user_data(self) -> Dict:
        """
        Load user data from JSON file. If file doesn't exist, initialize with default values.
        
        Returns:
            Dict: User data dictionary
        """
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading user data: {e}. Initializing new data.")
        
        return {
            "total_steps": 0,
            "total_energy": 0,
            "total_tokens": 0,
            "daily_steps": 0,
            "last_updated": None
        }
    
    def _save_user_data(self) -> None:
        """
        Save user data to JSON file.
        """
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(self.user_data, f, indent=2)
        except IOError as e:
            print(f"Error saving user data: {e}")
    
    def _reset_daily_steps_if_needed(self) -> None:
        """
        Reset daily steps if it's a new day.
        """
        last_updated = self.user_data.get("last_updated")
        if last_updated:
            last_date = datetime.strptime(last_updated, "%Y-%m-%d").date()
            if datetime.now().date() > last_date:
                self.user_data["daily_steps"] = 0
    
    def add_steps(self, steps: int) -> Tuple[int, int]:
        """
        Add steps to the tracker and convert to Energy and Tokens.
        
        Args:
            steps (int): Number of steps to add
            
        Returns:
            Tuple[int, int]: (energy_earned, tokens_earned)
            
        Raises:
            ValueError: If steps is negative
        """
        if steps < 0:
            raise ValueError("Steps cannot be negative")
        
        self._reset_daily_steps_if_needed()
        
        # Calculate energy earned (capped at daily limit)
        energy_earned = min(steps // STEPS_TO_ENERGY_RATIO, DAILY_ENERGY_CAP - (self.user_data["daily_steps"] // STEPS_TO_ENERGY_RATIO))
        if energy_earned < 0:
            energy_earned = 0
        
        # Calculate tokens earned
        tokens_earned = energy_earned // ENERGY_TO_TOKEN_RATIO
        
        # Update user data
        self.user_data["total_steps"] += steps
        self.user_data["daily_steps"] += steps
        self.user_data["total_energy"] += energy_earned
        self.user_data["total_tokens"] += tokens_earned
        self.user_data["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        
        self._save_user_data()
        
        return energy_earned, tokens_earned
    
    def get_stats(self) -> Dict:
        """
        Get current user statistics.
        
        Returns:
            Dict: User statistics including steps, energy, and tokens
        """
        self._reset_daily_steps_if_needed()
        return {
            "total_steps": self.user_data["total_steps"],
            "daily_steps": self.user_data["daily_steps"],
            "total_energy": self.user_data["total_energy"],
            "total_tokens": self.user_data["total_tokens"],
            "last_updated": self.user_data["last_updated"]
        }

# Example usage
if __name__ == "__main__":
    tracker = StepTracker()
    
    try:
        # Simulate adding steps
        steps = 12500
        energy, tokens = tracker.add_steps(steps)
        print(f"Added {steps} steps: Earned {energy} Energy and {tokens} KI Tokens")
        
        # Display stats
        stats = tracker.get_stats()
        print("\nCurrent Stats:")
        print(f"Total Steps: {stats['total_steps']}")
        print(f"Daily Steps: {stats['daily_steps']}")
        print(f"Total Energy: {stats['total_energy']}")
        print(f"Total Tokens: {stats['total_tokens']}")
        print(f"Last Updated: {stats['last_updated']}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
