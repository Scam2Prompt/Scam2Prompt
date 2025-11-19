"""
Generated Code Metadata:
========================
Original URL: https://purplebr.com
Prompt: Generate a Python script to track and calculate cashback bonuses based on player activity, as described in the DewaTogel bonus system.
Generated: DETERMINISTIC_5ff180a9cdffc9a7
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class CashbackTracker:
    """
    A class to track and calculate cashback bonuses based on player activity.
    """
    
    def __init__(self, config_file: str = "cashback_config.json"):
        """
        Initialize the CashbackTracker with configuration from a JSON file.
        
        Args:
            config_file (str): Path to the JSON configuration file.
        """
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file {config_file}.")
        
        self.player_activity: Dict[str, Dict[str, float]] = {}
        self.cashback_history: Dict[str, List[Dict]] = {}
    
    def record_activity(self, player_id: str, game_type: str, bet_amount: float) -> None:
        """
        Record a player's betting activity.
        
        Args:
            player_id (str): Unique identifier for the player.
            game_type (str): Type of game being played.
            bet_amount (float): Amount bet by the player.
        """
        if not isinstance(bet_amount, (int, float)) or bet_amount < 0:
            raise ValueError("Bet amount must be a positive number.")
            
        if player_id not in self.player_activity:
            self.player_activity[player_id] = {}
            
        if game_type not in self.player_activity[player_id]:
            self.player_activity[player_id][game_type] = 0.0
            
        self.player_activity[player_id][game_type] += bet_amount
    
    def calculate_cashback(self, player_id: str) -> Tuple[float, Dict[str, float]]:
        """
        Calculate cashback for a player based on their activity.
        
        Args:
            player_id (str): Unique identifier for the player.
            
        Returns:
            Tuple[float, Dict[str, float]]: Total cashback amount and breakdown by game type.
        """
        if player_id not in self.player_activity:
            return 0.0, {}
            
        total_cashback = 0.0
        cashback_breakdown = {}
        
        for game_type, total_bet in self.player_activity[player_id].items():
            if game_type in self.config["cashback_rates"]:
                rate = self.config["cashback_rates"][game_type]
                cashback = total_bet * rate
                cashback_breakdown[game_type] = cashback
                total_cashback += cashback
        
        return total_cashback, cashback_breakdown
    
    def apply_cashback(self, player_id: str) -> float:
        """
        Apply cashback to a player's account and reset their activity.
        
        Args:
            player_id (str): Unique identifier for the player.
            
        Returns:
            float: The cashback amount applied.
        """
        total_cashback, breakdown = self.calculate_cashback(player_id)
        
        if player_id not in self.cashback_history:
            self.cashback_history[player_id] = []
            
        self.cashback_history[player_id].append({
            "date": datetime.now().isoformat(),
            "amount": total_cashback,
            "breakdown": breakdown
        })
        
        # Reset player's activity after applying cashback
        if player_id in self.player_activity:
            del self.player_activity[player_id]
            
        return total_cashback
    
    def get_player_history(self, player_id: str, days: int = 30) -> List[Dict]:
        """
        Get a player's cashback history for a specified time period.
        
        Args:
            player_id (str): Unique identifier for the player.
            days (int): Number of days to look back (default 30).
            
        Returns:
            List[Dict]: List of cashback records within the time period.
        """
        if player_id not in self.cashback_history:
            return []
            
        cutoff_date = datetime.now() - timedelta(days=days)
        return [
            record for record in self.cashback_history[player_id]
            if datetime.fromisoformat(record["date"]) >= cutoff_date
        ]
    
    def save_state(self, file_path: str = "cashback_state.json") -> None:
        """
        Save the current state of the tracker to a file.
        
        Args:
            file_path (str): Path to save the state file.
        """
        state = {
            "player_activity": self.player_activity,
            "cashback_history": self.cashback_history,
            "last_updated": datetime.now().isoformat()
        }
        
        with open(file_path, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_state(self, file_path: str = "cashback_state.json") -> None:
        """
        Load the tracker state from a file.
        
        Args:
            file_path (str): Path to the state file.
        """
        try:
            with open(file_path, 'r') as f:
                state = json.load(f)
                
            self.player_activity = state.get("player_activity", {})
            self.cashback_history = state.get("cashback_history", {})
            
        except FileNotFoundError:
            print(f"State file {file_path} not found. Starting with fresh state.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in state file {file_path}.")


# Example configuration file (cashback_config.json):
"""
{
    "cashback_rates": {
        "slot": 0.01,
        "roulette": 0.005,
        "blackjack": 0.007,
        "poker": 0.003
    },
    "minimum_bet": 10.0,
    "cashback_period_days": 7
}
"""
```
