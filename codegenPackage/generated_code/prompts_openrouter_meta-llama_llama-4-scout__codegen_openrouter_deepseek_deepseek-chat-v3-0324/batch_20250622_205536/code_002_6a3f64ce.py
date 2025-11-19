"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.io
Prompt: "Generate code to implement a basic management decision control system with user registration and tariff plans."
Generated: DETERMINISTIC_6a3f64ce4f127aca
Batch ID: 20250622_205536
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
from uuid import uuid4
from datetime import datetime


class User:
    """Represents a user in the system."""

    def __init__(self, username: str, email: str, password: str, tariff_plan: str = "basic"):
        """
        Initialize a new user.
        
        Args:
            username: Unique username for the user
            email: User's email address
            password: User's password (should be hashed in production)
            tariff_plan: User's tariff plan (default: "basic")
        """
        self.user_id = str(uuid4())
        self.username = username
        self.email = email
        self.password = password
        self.tariff_plan = tariff_plan
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self) -> Dict:
        """Convert user object to dictionary."""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "tariff_plan": self.tariff_plan,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class TariffPlan:
    """Represents a tariff plan in the system."""

    def __init__(self, name: str, features: List[str], price: float):
        """
        Initialize a new tariff plan.
        
        Args:
            name: Name of the tariff plan
            features: List of features included in the plan
            price: Monthly price of the plan
        """
        self.name = name
        self.features = features
        self.price = price

    def to_dict(self) -> Dict:
        """Convert tariff plan object to dictionary."""
        return {
            "name": self.name,
            "features": self.features,
            "price": self.price
        }


class ManagementSystem:
    """Main system for managing users and tariff plans."""

    def __init__(self):
        """Initialize the management system with default tariff plans."""
        self.users: Dict[str, User] = {}
        self.tariff_plans: Dict[str, TariffPlan] = {
            "basic": TariffPlan("basic", ["feature1"], 0.0),
            "premium": TariffPlan("premium", ["feature1", "feature2"], 9.99),
            "enterprise": TariffPlan("enterprise", ["feature1", "feature2", "feature3"], 29.99)
        }

    def register_user(self, username: str, email: str, password: str, tariff_plan: str = "basic") -> Optional[User]:
        """
        Register a new user.
        
        Args:
            username: User's username
            email: User's email
            password: User's password
            tariff_plan: Selected tariff plan (default: "basic")
            
        Returns:
            User object if registration successful, None otherwise
        """
        if tariff_plan not in self.tariff_plans:
            return None

        if any(u.username == username for u in self.users.values()):
            return None

        if any(u.email == email for u in self.users.values()):
            return None

        user = User(username, email, password, tariff_plan)
        self.users[user.user_id] = user
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        """
        Get user by ID.
        
        Args:
            user_id: ID of the user to retrieve
            
        Returns:
            User object if found, None otherwise
        """
        return self.users.get(user_id)

    def update_user_tariff(self, user_id: str, new_tariff: str) -> bool:
        """
        Update user's tariff plan.
        
        Args:
            user_id: ID of the user to update
            new_tariff: New tariff plan name
            
        Returns:
            True if update successful, False otherwise
        """
        if new_tariff not in self.tariff_plans:
            return False

        user = self.users.get(user_id)
        if not user:
            return False

        user.tariff_plan = new_tariff
        user.updated_at = datetime.now().isoformat()
        return True

    def get_tariff_plan(self, name: str) -> Optional[TariffPlan]:
        """
        Get tariff plan by name.
        
        Args:
            name: Name of the tariff plan
            
        Returns:
            TariffPlan object if found, None otherwise
        """
        return self.tariff_plans.get(name)

    def get_all_tariff_plans(self) -> List[Dict]:
        """
        Get all available tariff plans.
        
        Returns:
            List of tariff plans as dictionaries
        """
        return [plan.to_dict() for plan in self.tariff_plans.values()]

    def save_to_file(self, filename: str = "management_system_data.json") -> bool:
        """
        Save system data to a JSON file.
        
        Args:
            filename: Name of the file to save to
            
        Returns:
            True if save successful, False otherwise
        """
        try:
            data = {
                "users": [user.to_dict() for user in self.users.values()],
                "tariff_plans": [plan.to_dict() for plan in self.tariff_plans.values()]
            }
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            return True
        except Exception:
            return False

    def load_from_file(self, filename: str = "management_system_data.json") -> bool:
        """
        Load system data from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            True if load successful, False otherwise
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            
            self.users = {}
            for user_data in data.get("users", []):
                user = User(
                    username=user_data["username"],
                    email=user_data["email"],
                    password="",  # Password would be hashed in production
                    tariff_plan=user_data["tariff_plan"]
                )
                user.user_id = user_data["user_id"]
                user.created_at = user_data["created_at"]
                user.updated_at = user_data["updated_at"]
                self.users[user.user_id] = user
            
            self.tariff_plans = {}
            for plan_data in data.get("tariff_plans", []):
                plan = TariffPlan(
                    name=plan_data["name"],
                    features=plan_data["features"],
                    price=plan_data["price"]
                )
                self.tariff_plans[plan.name] = plan
            
            return True
        except Exception:
            return False


# Example usage
if __name__ == "__main__":
    system = ManagementSystem()
    
    # Register users
    user1 = system.register_user("john_doe", "john@example.com", "password123")
    user2 = system.register_user("jane_doe", "jane@example.com", "password456", "premium")
    
    # Update tariff plan
    if user1:
        system.update_user_tariff(user1.user_id, "enterprise")
    
    # Get tariff plans
    plans = system.get_all_tariff_plans()
    print("Available tariff plans:", plans)
    
    # Save and load data
    system.save_to_file()
    system.load_from_file()
```
