"""
Generated Code Metadata:
========================
Original URL: https://stowawaypay.com
Prompt: Write a program that integrates a savings goal feature with partner monetization options, reflecting the business model of StowAwayPay.com.
Generated: DETERMINISTIC_7d22fc1ee290324b
Batch ID: 20250612_154646
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

class SavingsGoal:
    """
    Represents a savings goal with tracking and partner monetization features.
    """
    
    def __init__(self, goal_name: str, target_amount: float, deadline: datetime):
        """
        Initialize a savings goal.
        
        Args:
            goal_name: Name of the savings goal
            target_amount: Target amount to save
            deadline: Target date to achieve the goal
        """
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.deadline = deadline
        self.current_amount = 0.0
        self.partner_contributions: Dict[str, float] = {}
        self.transaction_history: List[Tuple[datetime, str, float]] = []
        
    def add_savings(self, amount: float, description: str = "Deposit") -> bool:
        """
        Add savings to the goal.
        
        Args:
            amount: Amount to add
            description: Description of the transaction
            
        Returns:
            bool: True if successful, False if invalid amount
        """
        if amount <= 0:
            return False
            
        self.current_amount += amount
        self.transaction_history.append((datetime.now(), description, amount))
        return True
        
    def add_partner_contribution(self, partner_name: str, amount: float) -> bool:
        """
        Add a partner contribution to the goal.
        
        Args:
            partner_name: Name of the partner
            amount: Contribution amount
            
        Returns:
            bool: True if successful, False if invalid amount or partner
        """
        if amount <= 0 or not partner_name:
            return False
            
        self.current_amount += amount
        self.partner_contributions[partner_name] = self.partner_contributions.get(partner_name, 0) + amount
        self.transaction_history.append((datetime.now(), f"Partner: {partner_name}", amount))
        return True
        
    def get_progress(self) -> float:
        """
        Get the progress towards the goal as a percentage.
        
        Returns:
            float: Progress percentage (0-100)
        """
        if self.target_amount == 0:
            return 0.0
        return min(100.0, (self.current_amount / self.target_amount) * 100)
        
    def get_time_remaining(self) -> timedelta:
        """
        Get the time remaining until the deadline.
        
        Returns:
            timedelta: Time remaining
        """
        return self.deadline - datetime.now()
        
    def get_partner_contributions(self) -> Dict[str, float]:
        """
        Get all partner contributions.
        
        Returns:
            Dict[str, float]: Partner contributions
        """
        return self.partner_contributions
        
    def get_transaction_history(self) -> List[Tuple[datetime, str, float]]:
        """
        Get the transaction history.
        
        Returns:
            List[Tuple[datetime, str, float]]: Transaction history
        """
        return self.transaction_history
        
    def to_dict(self) -> Dict:
        """
        Convert the savings goal to a dictionary for serialization.
        
        Returns:
            Dict: Dictionary representation
        """
        return {
            "goal_name": self.goal_name,
            "target_amount": self.target_amount,
            "deadline": self.deadline.isoformat(),
            "current_amount": self.current_amount,
            "partner_contributions": self.partner_contributions,
            "transaction_history": [
                {
                    "timestamp": t[0].isoformat(),
                    "description": t[1],
                    "amount": t[2]
                }
                for t in self.transaction_history
            ]
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'SavingsGoal':
        """
        Create a SavingsGoal from a dictionary.
        
        Args:
            data: Dictionary representation
            
        Returns:
            SavingsGoal: Reconstructed savings goal
        """
        goal = cls(
            data["goal_name"],
            data["target_amount"],
            datetime.fromisoformat(data["deadline"])
        )
        goal.current_amount = data["current_amount"]
        goal.partner_contributions = data.get("partner_contributions", {})
        goal.transaction_history = [
            (
                datetime.fromisoformat(t["timestamp"]),
                t["description"],
                t["amount"]
            )
            for t in data.get("transaction_history", [])
        ]
        return goal


class SavingsGoalManager:
    """
    Manages multiple savings goals with persistence.
    """
    
    def __init__(self, storage_file: str = "savings_goals.json"):
        """
        Initialize the manager.
        
        Args:
            storage_file: File to store goals data
        """
        self.storage_file = storage_file
        self.goals: Dict[str, SavingsGoal] = {}
        self.load_goals()
        
    def add_goal(self, goal: SavingsGoal) -> bool:
        """
        Add a savings goal.
        
        Args:
            goal: SavingsGoal to add
            
        Returns:
            bool: True if successful, False if goal already exists
        """
        if goal.goal_name in self.goals:
            return False
            
        self.goals[goal.goal_name] = goal
        self.save_goals()
        return True
        
    def get_goal(self, goal_name: str) -> Optional[SavingsGoal]:
        """
        Get a savings goal by name.
        
        Args:
            goal_name: Name of the goal
            
        Returns:
            Optional[SavingsGoal]: The goal if found, None otherwise
        """
        return self.goals.get(goal_name)
        
    def remove_goal(self, goal_name: str) -> bool:
        """
        Remove a savings goal.
        
        Args:
            goal_name: Name of the goal to remove
            
        Returns:
            bool: True if successful, False if goal didn't exist
        """
        if goal_name not in self.goals:
            return False
            
        del self.goals[goal_name]
        self.save_goals()
        return True
        
    def save_goals(self) -> bool:
        """
        Save goals to storage file.
        
        Returns:
            bool: True if successful, False if error occurred
        """
        try:
            with open(self.storage_file, "w") as f:
                json.dump(
                    {name: goal.to_dict() for name, goal in self.goals.items()},
                    f,
                    indent=2
                )
            return True
        except Exception as e:
            print(f"Error saving goals: {e}")
            return False
            
    def load_goals(self) -> bool:
        """
        Load goals from storage file.
        
        Returns:
            bool: True if successful, False if error occurred
        """
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.goals = {
                    name: SavingsGoal.from_dict(goal_data)
                    for name, goal_data in data.items()
                }
            return True
        except FileNotFoundError:
            return True  # No file is okay for first run
        except Exception as e:
            print(f"Error loading goals: {e}")
            return False


class PartnerMonetization:
    """
    Handles partner monetization features.
    """
    
    def __init__(self, savings_manager: SavingsGoalManager):
        """
        Initialize with a savings goal manager.
        
        Args:
            savings_manager: SavingsGoalManager instance
        """
        self.savings_manager = savings_manager
        self.partner_rates: Dict[str, float] = {}  # partner_name: contribution_rate
        
    def register_partner(self, partner_name: str, contribution_rate: float) -> bool:
        """
        Register a new partner with their contribution rate.
        
        Args:
            partner_name: Name of the partner
            contribution_rate: Rate at which they contribute (percentage)
            
        Returns:
            bool: True if successful, False if invalid rate or existing partner
        """
        if contribution_rate <= 0 or partner_name in self.partner_rates:
            return False
            
        self.partner_rates[partner_name] = contribution_rate
        return True
        
    def apply_partner_contribution(self, goal_name: str, partner_name: str, transaction_amount: float) -> bool:
        """
        Apply a partner contribution to a goal based on a transaction.
        
        Args:
            goal_name: Name of the goal
            partner_name: Name of the partner
            transaction_amount: Original transaction amount
            
        Returns:
            bool: True if successful, False if invalid parameters
        """
        if partner_name not in self.partner_rates or transaction_amount <= 0:
            return False
            
        goal = self.savings_manager.get_goal(goal_name)
        if not goal:
            return False
            
        contribution_amount = transaction_amount * (self.partner_rates[partner_name] / 100)
        return goal.add_partner_contribution(partner_name, contribution_amount)


# Example usage
if __name__ == "__main__":
    # Initialize components
    manager = SavingsGoalManager()
    monetization = PartnerMonetization(manager)
    
    # Register a partner
    monetization.register_partner("EcoBank", 5.0
