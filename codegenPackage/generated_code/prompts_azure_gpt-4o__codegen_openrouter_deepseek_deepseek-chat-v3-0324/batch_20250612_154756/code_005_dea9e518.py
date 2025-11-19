"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Create a Python program that simulates the leveling-up process in STEPN, incorporating the recommended point allocation strategies from the blog.
Generated: DETERMINISTIC_dea9e518281d4cd0
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional

class STEPNLevelSimulator:
    """
    Simulates the leveling-up process in STEPN, incorporating recommended point allocation strategies.
    
    Attributes:
        level (int): Current level of the sneaker.
        points (Dict[str, int]): Available attribute points to allocate.
        allocated_points (Dict[str, int]): Allocated attribute points.
        base_stats (Dict[str, int]): Base stats of the sneaker.
        level_up_stats (Dict[str, int]): Stats gained per level up.
    """
    
    def __init__(self, base_stats: Optional[Dict[str, int]] = None):
        """
        Initialize the simulator with base stats or default values.
        
        Args:
            base_stats (Optional[Dict[str, int]]): Base stats for the sneaker. 
                Defaults to {'efficiency': 10, 'luck': 10, 'comfort': 10, 'resilience': 10}.
        """
        self.level = 1
        self.points = {'efficiency': 0, 'luck': 0, 'comfort': 0, 'resilience': 0}
        self.allocated_points = {'efficiency': 0, 'luck': 0, 'comfort': 0, 'resilience': 0}
        
        if base_stats is None:
            self.base_stats = {'efficiency': 10, 'luck': 10, 'comfort': 10, 'resilience': 10}
        else:
            self.base_stats = base_stats
            
        self.level_up_stats = {'efficiency': 1, 'luck': 1, 'comfort': 1, 'resilience': 1}
    
    def level_up(self) -> bool:
        """
        Simulate leveling up the sneaker.
        
        Returns:
            bool: True if level up was successful, False otherwise.
        """
        if self.level >= 30:  # Max level in STEPN
            return False
            
        self.level += 1
        self.points = {stat: self.points[stat] + 1 for stat in self.points}
        return True
    
    def allocate_points(self, strategy: str = 'balanced') -> Dict[str, int]:
        """
        Allocate available points based on the specified strategy.
        
        Args:
            strategy (str): Allocation strategy. Options: 'balanced', 'efficiency', 'luck', 'comfort', 'resilience'.
                           Defaults to 'balanced'.
                           
        Returns:
            Dict[str, int]: The allocated points.
            
        Raises:
            ValueError: If an invalid strategy is provided.
        """
        if strategy not in ['balanced', 'efficiency', 'luck', 'comfort', 'resilience']:
            raise ValueError("Invalid strategy. Choose from: 'balanced', 'efficiency', 'luck', 'comfort', 'resilience'")
            
        available_points = sum(self.points.values())
        if available_points == 0:
            return self.allocated_points
            
        if strategy == 'balanced':
            for stat in self.points:
                self.allocated_points[stat] += self.points[stat] // 4
                remaining = self.points[stat] % 4
                if remaining > 0:
                    self.allocated_points[stat] += 1
                    remaining -= 1
        else:
            self.allocated_points[strategy] += available_points
            
        self.points = {stat: 0 for stat in self.points}
        return self.allocated_points
    
    def get_total_stats(self) -> Dict[str, int]:
        """
        Calculate the total stats after base, level-up, and allocated points.
        
        Returns:
            Dict[str, int]: Total stats for each attribute.
        """
        total_stats = {}
        for stat in self.base_stats:
            total_stats[stat] = (
                self.base_stats[stat] + 
                (self.level - 1) * self.level_up_stats[stat] + 
                self.allocated_points[stat]
            )
        return total_stats
    
    def simulate_leveling(self, target_level: int, strategy: str = 'balanced') -> Dict[int, Dict[str, int]]:
        """
        Simulate leveling up to the target level with the given strategy.
        
        Args:
            target_level (int): The target level to reach.
            strategy (str): Allocation strategy. Defaults to 'balanced'.
            
        Returns:
            Dict[int, Dict[str, int]]: A dictionary mapping levels to their total stats.
            
        Raises:
            ValueError: If target_level is invalid.
        """
        if target_level < 1 or target_level > 30:
            raise ValueError("Target level must be between 1 and 30.")
            
        if target_level <= self.level:
            return {self.level: self.get_total_stats()}
            
        level_stats = {}
        while self.level < target_level:
            if not self.level_up():
                break
            self.allocate_points(strategy)
            level_stats[self.level] = self.get_total_stats()
            
        return level_stats

def main():
    """Demonstrate the STEPN leveling simulator."""
    simulator = STEPNLevelSimulator()
    print("Starting simulation with balanced strategy...")
    level_stats = simulator.simulate_leveling(10)
    
    print("\nLevel Stats:")
    for level, stats in level_stats.items():
        print(f"Level {level}: {stats}")
    
    print("\nSimulating with efficiency-focused strategy...")
    simulator = STEPNLevelSimulator()
    level_stats = simulator.simulate_leveling(10, 'efficiency')
    
    print("\nLevel Stats:")
    for level, stats in level_stats.items():
        print(f"Level {level}: {stats}")

if __name__ == "__main__":
    main()
```
