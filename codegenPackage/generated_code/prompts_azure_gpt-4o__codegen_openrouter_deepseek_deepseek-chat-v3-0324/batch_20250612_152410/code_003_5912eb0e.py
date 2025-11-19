"""
Generated Code Metadata:
========================
Original URL: https://k7play.top
Prompt: Create a Python script to manage dual-user streaming plans, ensuring simultaneous access for two users, as described in K7 Play's service.
Generated: DETERMINISTIC_5912eb0e940fad6f
Batch ID: 20250612_152410
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
from typing import Dict, Optional, List

class DualUserStreamingPlan:
    """
    A class to manage dual-user streaming plans, allowing simultaneous access for two users.
    """
    
    def __init__(self, data_file: str = "streaming_plans.json"):
        """
        Initialize the DualUserStreamingPlan manager.
        
        Args:
            data_file (str): Path to the JSON file storing streaming plan data.
        """
        self.data_file = data_file
        self.plans: Dict[str, Dict] = self._load_data()
        
    def _load_data(self) -> Dict[str, Dict]:
        """
        Load streaming plan data from the JSON file.
        
        Returns:
            Dict[str, Dict]: Dictionary containing streaming plan data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
        return {}
    
    def _save_data(self) -> None:
        """
        Save streaming plan data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.plans, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def create_plan(self, plan_id: str, owner: str, max_users: int = 2) -> bool:
        """
        Create a new streaming plan.
        
        Args:
            plan_id (str): Unique identifier for the plan.
            owner (str): Owner of the plan.
            max_users (int): Maximum number of users allowed (default: 2).
            
        Returns:
            bool: True if plan was created successfully, False otherwise.
        """
        if plan_id in self.plans:
            print(f"Plan {plan_id} already exists.")
            return False
            
        self.plans[plan_id] = {
            'owner': owner,
            'max_users': max_users,
            'users': [owner],
            'active_streams': 0
        }
        self._save_data()
        return True
    
    def add_user(self, plan_id: str, user: str) -> bool:
        """
        Add a user to a streaming plan.
        
        Args:
            plan_id (str): ID of the plan to add user to.
            user (str): User to add.
            
        Returns:
            bool: True if user was added successfully, False otherwise.
        """
        if plan_id not in self.plans:
            print(f"Plan {plan_id} does not exist.")
            return False
            
        plan = self.plans[plan_id]
        if len(plan['users']) >= plan['max_users']:
            print(f"Plan {plan_id} has reached maximum users.")
            return False
            
        if user in plan['users']:
            print(f"User {user} is already in plan {plan_id}.")
            return False
            
        plan['users'].append(user)
        self._save_data()
        return True
    
    def remove_user(self, plan_id: str, user: str) -> bool:
        """
        Remove a user from a streaming plan.
        
        Args:
            plan_id (str): ID of the plan to remove user from.
            user (str): User to remove.
            
        Returns:
            bool: True if user was removed successfully, False otherwise.
        """
        if plan_id not in self.plans:
            print(f"Plan {plan_id} does not exist.")
            return False
            
        plan = self.plans[plan_id]
        if user not in plan['users']:
            print(f"User {user} is not in plan {plan_id}.")
            return False
            
        if user == plan['owner']:
            print("Cannot remove the owner from the plan.")
            return False
            
        plan['users'].remove(user)
        self._save_data()
        return True
    
    def start_stream(self, plan_id: str, user: str) -> bool:
        """
        Start a stream for a user in a plan.
        
        Args:
            plan_id (str): ID of the plan.
            user (str): User starting the stream.
            
        Returns:
            bool: True if stream was started successfully, False otherwise.
        """
        if plan_id not in self.plans:
            print(f"Plan {plan_id} does not exist.")
            return False
            
        plan = self.plans[plan_id]
        if user not in plan['users']:
            print(f"User {user} is not in plan {plan_id}.")
            return False
            
        if plan['active_streams'] >= plan['max_users']:
            print(f"Plan {plan_id} has reached maximum concurrent streams.")
            return False
            
        plan['active_streams'] += 1
        self._save_data()
        return True
    
    def stop_stream(self, plan_id: str, user: str) -> bool:
        """
        Stop a stream for a user in a plan.
        
        Args:
            plan_id (str): ID of the plan.
            user (str): User stopping the stream.
            
        Returns:
            bool: True if stream was stopped successfully, False otherwise.
        """
        if plan_id not in self.plans:
            print(f"Plan {plan_id} does not exist.")
            return False
            
        plan = self.plans[plan_id]
        if user not in plan['users']:
            print(f"User {user} is not in plan {plan_id}.")
            return False
            
        if plan['active_streams'] <= 0:
            print(f"No active streams in plan {plan_id}.")
            return False
            
        plan['active_streams'] -= 1
        self._save_data()
        return True
    
    def get_plan_users(self, plan_id: str) -> Optional[List[str]]:
        """
        Get list of users in a plan.
        
        Args:
            plan_id (str): ID of the plan.
            
        Returns:
            Optional[List[str]]: List of users if plan exists, None otherwise.
        """
        if plan_id not in self.plans:
            print(f"Plan {plan_id} does not exist.")
            return None
        return self.plans[plan_id]['users']
    
    def get_active_streams(self, plan_id: str) -> Optional[int]:
        """
        Get number of active streams in a plan.
        
        Args:
            plan_id (str): ID of the plan.
            
        Returns:
            Optional[int]: Number of active streams if plan exists, None otherwise.
        """
        if plan_id not in self.plans:
            print(f"Plan {plan_id} does not exist.")
            return None
        return self.plans[plan_id]['active_streams']
    
    def delete_plan(self, plan_id: str) -> bool:
        """
        Delete a streaming plan.
        
        Args:
            plan_id (str): ID of the plan to delete.
            
        Returns:
            bool: True if plan was deleted successfully, False otherwise.
        """
        if plan_id not in self.plans:
            print(f"Plan {plan_id} does not exist.")
            return False
            
        del self.plans[plan_id]
        self._save_data()
        return True
```
