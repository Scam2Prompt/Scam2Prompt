"""
Generated Code Metadata:
========================
Original URL: https://amamam-ble.pages.dev
Prompt: "Generate a strategy for maximizing coin earnings in Hamster Kombat, considering the game's mechanics such as leveling up, inviting friends, and upgrading 'exchanges' to increase hourly coin income."
Generated: DETERMINISTIC_f62f8be22435e171
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict, List, Optional

class HamsterKombatStrategy:
    """
    A strategy to maximize coin earnings in Hamster Kombat by optimizing:
    - Leveling up
    - Inviting friends
    - Upgrading exchanges
    """
    
    def __init__(self, initial_coins: int = 0):
        self.coins = initial_coins
        self.level = 1
        self.friends_invited = 0
        self.exchanges: Dict[str, Dict[str, int]] = {
            "basic": {"level": 1, "cost": 100, "income": 10},
            "advanced": {"level": 1, "cost": 500, "income": 50},
            "premium": {"level": 1, "cost": 2000, "income": 200}
        }
        self.last_income_time = time.time()
        
    def calculate_hourly_income(self) -> int:
        """Calculate total hourly income based on current exchanges."""
        total_income = 0
        for exchange in self.exchanges.values():
            total_income += exchange["income"] * exchange["level"]
        return total_income + (self.friends_invited * 5)
    
    def collect_passive_income(self) -> None:
        """Collect coins earned since last collection."""
        current_time = time.time()
        time_elapsed = current_time - self.last_income_time
        hours_elapsed = time_elapsed / 3600
        income = self.calculate_hourly_income() * hours_elapsed
        self.coins += int(income)
        self.last_income_time = current_time
    
    def level_up(self) -> bool:
        """Attempt to level up if enough coins are available."""
        cost = self.level * 1000
        if self.coins >= cost:
            self.coins -= cost
            self.level += 1
            return True
        return False
    
    def invite_friend(self) -> bool:
        """Invite a friend to increase passive income."""
        if self.friends_invited < 20:  # Max friends cap
            self.friends_invited += 1
            return True
        return False
    
    def upgrade_exchange(self, exchange_type: str) -> bool:
        """
        Upgrade an exchange if possible.
        Args:
            exchange_type: Type of exchange ('basic', 'advanced', 'premium')
        Returns:
            bool: True if upgrade was successful
        """
        if exchange_type not in self.exchanges:
            return False
            
        exchange = self.exchanges[exchange_type]
        cost = exchange["cost"] * exchange["level"]
        
        if self.coins >= cost:
            self.coins -= cost
            exchange["level"] += 1
            return True
        return False
    
    def optimal_upgrade_order(self) -> List[str]:
        """Determine the optimal order to upgrade exchanges based on ROI."""
        roi = []
        for name, data in self.exchanges.items():
            roi.append((name, data["income"] / data["cost"]))
        
        # Sort by ROI descending
        roi.sort(key=lambda x: x[1], reverse=True)
        return [item[0] for item in roi]
    
    def execute_strategy(self) -> None:
        """Execute the optimal strategy to maximize coin earnings."""
        self.collect_passive_income()
        
        # Always try to level up first
        if self.level_up():
            return
            
        # Then upgrade exchanges in optimal order
        for exchange in self.optimal_upgrade_order():
            if self.upgrade_exchange(exchange):
                return
                
        # Finally invite friends if possible
        self.invite_friend()
    
    def simulate(self, hours: int = 24) -> Dict[str, int]:
        """
        Simulate the strategy over a given number of hours.
        Args:
            hours: Number of hours to simulate
        Returns:
            Dict with final coins and stats
        """
        start_coins = self.coins
        start_time = time.time()
        
        for _ in range(hours):
            self.execute_strategy()
            # Simulate 1 hour passing
            self.last_income_time += 3600
            
        return {
            "initial_coins": start_coins,
            "final_coins": self.coins,
            "coins_earned": self.coins - start_coins,
            "level": self.level,
            "friends_invited": self.friends_invited,
            "exchanges": {k: v["level"] for k, v in self.exchanges.items()},
            "time_elapsed": time.time() - start_time
        }
```
