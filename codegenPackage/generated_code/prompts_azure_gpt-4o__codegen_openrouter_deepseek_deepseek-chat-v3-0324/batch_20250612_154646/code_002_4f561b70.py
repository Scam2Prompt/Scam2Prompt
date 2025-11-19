"""
Generated Code Metadata:
========================
Original URL: https://stowawaypay.com
Prompt: Develop a Python script that simulates the savings process outlined on StowAwayPay.com, including goal setting, progress tracking, and automatic reward delivery upon goal completion.
Generated: DETERMINISTIC_4f561b700202dfc2
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
import random
import time
from datetime import datetime, timedelta
from typing import Dict, Optional, List

class SavingsGoal:
    """Represents a savings goal with tracking functionality."""
    
    def __init__(self, name: str, target_amount: float, deadline: datetime):
        """
        Initialize a savings goal.
        
        Args:
            name: Name of the savings goal
            target_amount: Target amount to save
            deadline: Deadline to reach the goal
        """
        self.name = name
        self.target_amount = target_amount
        self.deadline = deadline
        self.current_amount = 0.0
        self.completed = False
        self.created_at = datetime.now()
        self.rewards = []
        
    def add_contribution(self, amount: float) -> bool:
        """
        Add a contribution to the savings goal.
        
        Args:
            amount: Amount to contribute
            
        Returns:
            bool: True if goal is completed after this contribution
        """
        if self.completed:
            raise ValueError("Goal already completed")
            
        self.current_amount += amount
        
        if self.current_amount >= self.target_amount:
            self.completed = True
            return True
        return False
    
    def get_progress(self) -> Dict:
        """
        Get progress information about the goal.
        
        Returns:
            Dict: Progress information including percentage, days remaining, etc.
        """
        progress_percent = (self.current_amount / self.target_amount) * 100
        days_remaining = (self.deadline - datetime.now()).days
        
        return {
            "name": self.name,
            "target": self.target_amount,
            "current": self.current_amount,
            "progress": min(progress_percent, 100),
            "days_remaining": max(days_remaining, 0),
            "completed": self.completed,
            "deadline": self.deadline.isoformat()
        }
    
    def add_reward(self, reward: str) -> None:
        """Add a reward to be delivered upon goal completion."""
        self.rewards.append(reward)

class SavingsSimulator:
    """Simulates the savings process with goal tracking and rewards."""
    
    def __init__(self):
        """Initialize the savings simulator."""
        self.goals: Dict[str, SavingsGoal] = {}
        self.reward_options = [
            "Amazon Gift Card",
            "Movie Tickets",
            "Coffee Voucher",
            "Charity Donation in Your Name",
            "Custom Reward"
        ]
        
    def create_goal(self, name: str, target_amount: float, deadline_days: int) -> SavingsGoal:
        """
        Create a new savings goal.
        
        Args:
            name: Name of the goal
            target_amount: Target amount to save
            deadline_days: Number of days until deadline
            
        Returns:
            SavingsGoal: The created goal object
        """
        if name in self.goals:
            raise ValueError("Goal with this name already exists")
            
        deadline = datetime.now() + timedelta(days=deadline_days)
        goal = SavingsGoal(name, target_amount, deadline)
        self.goals[name] = goal
        
        # Automatically add a random reward
        reward = random.choice(self.reward_options)
        goal.add_reward(reward)
        
        return goal
    
    def contribute(self, goal_name: str, amount: float) -> Optional[Dict]:
        """
        Contribute to a savings goal.
        
        Args:
            goal_name: Name of the goal to contribute to
            amount: Amount to contribute
            
        Returns:
            Optional[Dict]: Reward information if goal completed, None otherwise
        """
        if goal_name not in self.goals:
            raise ValueError("Goal not found")
            
        goal = self.goals[goal_name]
        completed = goal.add_contribution(amount)
        
        if completed:
            return {
                "message": f"Congratulations! You've reached your goal: {goal_name}",
                "rewards": goal.rewards
            }
        return None
    
    def get_goal_progress(self, goal_name: str) -> Dict:
        """
        Get progress information for a goal.
        
        Args:
            goal_name: Name of the goal
            
        Returns:
            Dict: Progress information
        """
        if goal_name not in self.goals:
            raise ValueError("Goal not found")
        return self.goals[goal_name].get_progress()
    
    def list_goals(self) -> List[Dict]:
        """
        List all savings goals with their progress.
        
        Returns:
            List[Dict]: List of goal progress information
        """
        return [goal.get_progress() for goal in self.goals.values()]
    
    def save_to_file(self, filename: str = "savings_goals.json") -> None:
        """
        Save goals to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        data = {
            "goals": [
                {
                    "name": goal.name,
                    "target_amount": goal.target_amount,
                    "current_amount": goal.current_amount,
                    "deadline": goal.deadline.isoformat(),
                    "completed": goal.completed,
                    "rewards": goal.rewards,
                    "created_at": goal.created_at.isoformat()
                }
                for goal in self.goals.values()
            ]
        }
        
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str = "savings_goals.json") -> None:
        """
        Load goals from a JSON file.
        
        Args:
            filename: Name of the file to load from
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                
            self.goals = {}
            for goal_data in data["goals"]:
                goal = SavingsGoal(
                    name=goal_data["name"],
                    target_amount=goal_data["target_amount"],
                    deadline=datetime.fromisoformat(goal_data["deadline"])
                )
                goal.current_amount = goal_data["current_amount"]
                goal.completed = goal_data["completed"]
                goal.rewards = goal_data["rewards"]
                goal.created_at = datetime.fromisoformat(goal_data["created_at"])
                self.goals[goal.name] = goal
                
        except FileNotFoundError:
            print("No saved goals found. Starting fresh.")
        except json.JSONDecodeError:
            print("Error reading saved goals file. Starting fresh.")

def main():
    """Main function to demonstrate the savings simulator."""
    simulator = SavingsSimulator()
    simulator.load_from_file()
    
    while True:
        print("\nStowAwayPay Savings Simulator")
        print("1. Create new savings goal")
        print("2. Contribute to a goal")
        print("3. View goal progress")
        print("4. List all goals")
        print("5. Save and exit")
        
        choice = input("Enter your choice (1-5): ")
        
        try:
            if choice == "1":
                name = input("Enter goal name: ")
                target = float(input("Enter target amount: "))
                days = int(input("Enter number of days to reach goal: "))
                goal = simulator.create_goal(name, target, days)
                print(f"Goal '{name}' created with target ${target:.2f} in {days} days")
                
            elif choice == "2":
                name = input("Enter goal name: ")
                amount = float(input("Enter contribution amount: "))
                result = simulator.contribute(name, amount)
                if result:
                    print(result["message"])
                    print("Your rewards:")
                    for reward in result["rewards"]:
                        print(f"- {reward}")
                else:
                    print(f"Contribution of ${amount:.2f} added to '{name}'")
                    
            elif choice == "3":
                name = input("Enter goal name: ")
                progress = simulator.get_goal_progress(name)
                print(f"\nGoal: {progress['name']}")
                print(f"Target: ${progress['target']:.2f}")
                print(f"Current: ${progress['current']:.2f}")
                print(f"Progress: {progress['progress']:.1f}%")
                print(f"Days remaining: {progress['days_remaining']}")
                print(f"Status: {'Completed' if progress['completed'] else 'In progress'}")
                
            elif choice == "4":
                goals = simulator.list_goals()
                print("\nAll Savings Goals:")
                for goal in goals:
                    status = "✓" if goal["completed"] else " "
                    print(f"[{status}] {goal['name']}: ${goal['current']:.2f}/${goal['target']:.2f} ({goal['progress']:.1f}%)")
                    
            elif choice == "5":
                simulator.save_to_file()
                print("Goals saved. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1-5.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
