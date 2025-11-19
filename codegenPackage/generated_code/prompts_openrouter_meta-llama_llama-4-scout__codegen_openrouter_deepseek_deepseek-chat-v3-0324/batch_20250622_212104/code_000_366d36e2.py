"""
Generated Code Metadata:
========================
Original URL: https://stowawaypay.com
Prompt: Write a Python code snippet to implement a savings goal tracker for non-bank customers, incorporating automated rewards and discounts for achieving specific goals.
Generated: DETERMINISTIC_366d36e2d74ef4fb
Batch ID: 20250622_212104
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
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class SavingsGoalTracker:
    """
    A savings goal tracker for non-bank customers with automated rewards and discounts.
    
    Attributes:
        goals_file (str): Path to the JSON file storing goals data.
        rewards (Dict[str, float]): Dictionary mapping goal names to reward percentages.
    """
    
    def __init__(self, goals_file: str = "savings_goals.json"):
        """
        Initialize the tracker with a goals file and predefined rewards.
        
        Args:
            goals_file (str): Path to the JSON file for storing goals data.
        """
        self.goals_file = goals_file
        self.rewards = {
            "emergency_fund": 0.05,  # 5% reward
            "vacation": 0.03,       # 3% reward
            "education": 0.07,      # 7% reward
            "retirement": 0.1       # 10% reward
        }
        self._ensure_goals_file_exists()
    
    def _ensure_goals_file_exists(self) -> None:
        """Ensure the goals file exists; create it if it doesn't."""
        if not os.path.exists(self.goals_file):
            with open(self.goals_file, 'w') as f:
                json.dump([], f)
    
    def _load_goals(self) -> List[Dict]:
        """Load goals from the JSON file."""
        try:
            with open(self.goals_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load goals: {e}")
    
    def _save_goals(self, goals: List[Dict]) -> None:
        """Save goals to the JSON file."""
        try:
            with open(self.goals_file, 'w') as f:
                json.dump(goals, f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Failed to save goals: {e}")
    
    def create_goal(self, name: str, target_amount: float, deadline: str) -> Dict:
        """
        Create a new savings goal.
        
        Args:
            name (str): Name of the goal.
            target_amount (float): Target amount to save.
            deadline (str): Deadline in YYYY-MM-DD format.
            
        Returns:
            Dict: The created goal.
            
        Raises:
            ValueError: If the goal name already exists or deadline is invalid.
        """
        goals = self._load_goals()
        if any(goal['name'] == name for goal in goals):
            raise ValueError(f"Goal '{name}' already exists.")
        
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid deadline format. Use YYYY-MM-DD.")
        
        goal = {
            "name": name,
            "target_amount": target_amount,
            "current_amount": 0.0,
            "deadline": deadline,
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "achieved": False
        }
        
        goals.append(goal)
        self._save_goals(goals)
        return goal
    
    def add_to_goal(self, name: str, amount: float) -> Tuple[Dict, Optional[float]]:
        """
        Add money to a savings goal and check for achievement.
        
        Args:
            name (str): Name of the goal.
            amount (float): Amount to add.
            
        Returns:
            Tuple[Dict, Optional[float]]: Updated goal and reward amount (if achieved).
            
        Raises:
            ValueError: If the goal doesn't exist or amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        goals = self._load_goals()
        goal_index = next((i for i, g in enumerate(goals) if g['name'] == name), None)
        
        if goal_index is None:
            raise ValueError(f"Goal '{name}' not found.")
        
        goal = goals[goal_index]
        if goal['achieved']:
            raise ValueError(f"Goal '{name}' has already been achieved.")
        
        goal['current_amount'] += amount
        
        reward = None
        if goal['current_amount'] >= goal['target_amount']:
            goal['achieved'] = True
            goal['achieved_at'] = datetime.now().strftime("%Y-%m-%d")
            reward = goal['current_amount'] * self.rewards.get(name, 0.0)
        
        goals[goal_index] = goal
        self._save_goals(goals)
        return goal, reward
    
    def get_goal(self, name: str) -> Dict:
        """
        Retrieve a goal by name.
        
        Args:
            name (str): Name of the goal.
            
        Returns:
            Dict: The goal data.
            
        Raises:
            ValueError: If the goal doesn't exist.
        """
        goals = self._load_goals()
        goal = next((g for g in goals if g['name'] == name), None)
        if goal is None:
            raise ValueError(f"Goal '{name}' not found.")
        return goal
    
    def list_goals(self) -> List[Dict]:
        """
        List all savings goals.
        
        Returns:
            List[Dict]: List of all goals.
        """
        return self._load_goals()
    
    def delete_goal(self, name: str) -> None:
        """
        Delete a savings goal.
        
        Args:
            name (str): Name of the goal to delete.
            
        Raises:
            ValueError: If the goal doesn't exist.
        """
        goals = self._load_goals()
        goals = [g for g in goals if g['name'] != name]
        
        if len(goals) == len(self._load_goals()):
            raise ValueError(f"Goal '{name}' not found.")
        
        self._save_goals(goals)
```
