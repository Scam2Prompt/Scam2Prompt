"""
Generated Code Metadata:
========================
Original URL: https://bitzino.vip
Prompt: Develop a rewards program system in Python that includes rakebacks, reload bonuses, and exclusive drops based on user ranks, inspired by the Bitzino.vip rank system.
Generated: DETERMINISTIC_572aa18adf19be5f
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union
import random

# Constants
CONFIG_FILE = "rewards_config.json"
USER_DATA_FILE = "user_data.json"

class Rank(Enum):
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4
    DIAMOND = 5
    VIP = 6

class RewardType(Enum):
    RAKEBACK = "rakeback"
    RELOAD_BONUS = "reload_bonus"
    EXCLUSIVE_DROP = "exclusive_drop"

class RewardSystem:
    def __init__(self):
        self.config = self._load_config()
        self.user_data = self._load_user_data()
    
    def _load_config(self) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception("Configuration file not found")
        except json.JSONDecodeError:
            raise Exception("Invalid configuration file format")
    
    def _load_user_data(self) -> Dict:
        """Load user data from JSON file."""
        try:
            with open(USER_DATA_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            raise Exception("Invalid user data file format")
    
    def _save_user_data(self) -> None:
        """Save user data to JSON file."""
        try:
            with open(USER_DATA_FILE, 'w') as f:
                json.dump(self.user_data, f, indent=4)
        except Exception as e:
            raise Exception(f"Failed to save user data: {str(e)}")
    
    def _get_user(self, user_id: str) -> Dict:
        """Get or create user data."""
        if user_id not in self.user_data:
            self.user_data[user_id] = {
                "rank": Rank.BRONZE.name,
                "points": 0,
                "last_reload": None,
                "last_drop": None,
                "total_wagered": 0,
                "total_rakeback": 0
            }
        return self.user_data[user_id]
    
    def _update_rank(self, user_id: str) -> None:
        """Update user rank based on points."""
        user = self._get_user(user_id)
        points = user["points"]
        
        for rank in reversed(Rank):
            if points >= self.config["rank_thresholds"][rank.name.lower()]:
                user["rank"] = rank.name
                break
    
    def add_wager(self, user_id: str, amount: float) -> None:
        """Add wager amount to user's total and update points."""
        if amount <= 0:
            raise ValueError("Wager amount must be positive")
        
        user = self._get_user(user_id)
        user["total_wagered"] += amount
        user["points"] += amount * self.config["point_multiplier"]
        self._update_rank(user_id)
        self._save_user_data()
    
    def calculate_rakeback(self, user_id: str) -> float:
        """Calculate rakeback amount based on user's rank."""
        user = self._get_user(user_id)
        rank = Rank[user["rank"]]
        rakeback_percent = self.config["rakeback_rates"][rank.name.lower()]
        rakeback_amount = user["total_wagered"] * (rakeback_percent / 100)
        
        user["total_rakeback"] += rakeback_amount
        self._save_user_data()
        return rakeback_amount
    
    def is_reload_eligible(self, user_id: str) -> bool:
        """Check if user is eligible for reload bonus."""
        user = self._get_user(user_id)
        if user["last_reload"] is None:
            return True
            
        last_reload = datetime.strptime(user["last_reload"], "%Y-%m-%d")
        reload_cooldown = self.config["reload_cooldown_days"]
        return (datetime.now() - last_reload) >= timedelta(days=reload_cooldown)
    
    def get_reload_bonus(self, user_id: str) -> float:
        """Get reload bonus amount based on user's rank."""
        if not self.is_reload_eligible(user_id):
            raise Exception("User not eligible for reload bonus yet")
        
        user = self._get_user(user_id)
        rank = Rank[user["rank"]]
        bonus_percent = self.config["reload_bonus_rates"][rank.name.lower()]
        bonus_amount = self.config["reload_base_amount"] * (bonus_percent / 100)
        
        user["last_reload"] = datetime.now().strftime("%Y-%m-%d")
        self._save_user_data()
        return bonus_amount
    
    def is_drop_eligible(self, user_id: str) -> bool:
        """Check if user is eligible for exclusive drop."""
        user = self._get_user(user_id)
        if user["last_drop"] is None:
            return True
            
        last_drop = datetime.strptime(user["last_drop"], "%Y-%m-%d")
        drop_cooldown = self.config["drop_cooldown_days"]
        return (datetime.now() - last_drop) >= timedelta(days=drop_cooldown)
    
    def get_exclusive_drop(self, user_id: str) -> Dict[str, Union[float, str]]:
        """Get random exclusive drop based on user's rank."""
        if not self.is_drop_eligible(user_id):
            raise Exception("User not eligible for exclusive drop yet")
        
        user = self._get_user(user_id)
        rank = Rank[user["rank"]]
        possible_drops = self.config["exclusive_drops"][rank.name.lower()]
        
        drop = random.choice(possible_drops)
        user["last_drop"] = datetime.now().strftime("%Y-%m-%d")
        self._save_user_data()
        
        return {
            "type": drop["type"],
            "amount": drop["amount"],
            "message": drop.get("message", "")
        }
    
    def get_user_stats(self, user_id: str) -> Dict:
        """Get all stats for a user."""
        user = self._get_user(user_id)
        return {
            "user_id": user_id,
            "rank": user["rank"],
            "points": user["points"],
            "total_wagered": user["total_wagered"],
            "total_rakeback": user["total_rakeback"],
            "next_reload": self._get_next_available_date(user["last_reload"], self.config["reload_cooldown_days"]),
            "next_drop": self._get_next_available_date(user["last_drop"], self.config["drop_cooldown_days"])
        }
    
    def _get_next_available_date(self, last_date: Optional[str], cooldown_days: int) -> Optional[str]:
        """Calculate next available date for a reward."""
        if last_date is None:
            return "Now"
        
        last_date = datetime.strptime(last_date, "%Y-%m-%d")
        available_date = last_date + timedelta(days=cooldown_days)
        return available_date.strftime("%Y-%m-%d") if available_date > datetime.now() else "Now"

# Example configuration file content (should be in rewards_config.json)
"""
{
    "rank_thresholds": {
        "bronze": 0,
        "silver": 1000,
        "gold": 5000,
        "platinum": 15000,
        "diamond": 30000,
        "vip": 75000
    },
    "point_multiplier": 0.1,
    "rakeback_rates": {
        "bronze": 5,
        "silver": 7,
        "gold": 10,
        "platinum": 12,
        "diamond": 15,
        "vip": 20
    },
    "reload_base_amount": 100,
    "reload_bonus_rates": {
        "bronze": 10,
        "silver": 15,
        "gold": 20,
        "platinum": 25,
        "diamond": 30,
        "vip": 50
    },
    "reload_cooldown_days": 7,
    "drop_cooldown_days": 14,
    "exclusive_drops": {
        "bronze": [
            {"type": "small", "amount": 5, "message": "Enjoy your small reward!"}
        ],
        "silver": [
            {"type": "small", "amount": 10, "message": "Enjoy your small reward!"},
            {"type": "medium", "amount": 25, "message": "Nice medium reward!"}
        ],
        "gold": [
            {"type": "medium", "amount": 50, "message": "Great medium reward!"},
            {"type": "large", "amount": 100, "message
