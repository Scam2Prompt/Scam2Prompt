"""
Generated Code Metadata:
========================
Original URL: https://geokukt.cn
Prompt: Write code to implement a "Move to Earn" concept, integrating token rewards for physical activities as described in the 欧易官网 content.
Generated: DETERMINISTIC_af1306a8b76b445b
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import hashlib
from typing import Dict, Optional
from datetime import datetime, timedelta
from enum import Enum

# Database mock for demonstration purposes
class Database:
    def __init__(self):
        self.users = {}
        self.activities = []
        self.token_balances = {}

    def get_user(self, user_id: str) -> Optional[Dict]:
        return self.users.get(user_id)

    def create_user(self, user_data: Dict) -> Dict:
        user_id = hashlib.sha256(user_data['email'].encode()).hexdigest()[:16]
        self.users[user_id] = {**user_data, 'id': user_id}
        self.token_balances[user_id] = 0
        return self.users[user_id]

    def log_activity(self, activity_data: Dict) -> Dict:
        activity_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
        activity = {**activity_data, 'id': activity_id, 'timestamp': datetime.utcnow()}
        self.activities.append(activity)
        return activity

    def update_token_balance(self, user_id: str, amount: float) -> float:
        if user_id not in self.token_balances:
            self.token_balances[user_id] = 0
        self.token_balances[user_id] += amount
        return self.token_balances[user_id]

class ActivityType(Enum):
    WALKING = "walking"
    RUNNING = "running"
    CYCLING = "cycling"
    SWIMMING = "swimming"

class TokenRewardSystem:
    def __init__(self, db: Database):
        self.db = db
        self.reward_rates = {
            ActivityType.WALKING: 0.1,   # tokens per minute
            ActivityType.RUNNING: 0.2,
            ActivityType.CYCLING: 0.15,
            ActivityType.SWIMMING: 0.18
        }
        self.minimum_activity_duration = 5  # minutes
        self.maximum_daily_reward = 100     # tokens per day

    def calculate_reward(self, activity_type: ActivityType, duration_minutes: float) -> float:
        if duration_minutes < self.minimum_activity_duration:
            return 0
        
        reward = self.reward_rates[activity_type] * duration_minutes
        return min(reward, self.maximum_daily_reward)

    def get_daily_rewards(self, user_id: str, date: datetime = None) -> float:
        if date is None:
            date = datetime.utcnow().date()
        
        start_of_day = datetime.combine(date, datetime.min.time())
        end_of_day = start_of_day + timedelta(days=1)
        
        user_activities = [
            a for a in self.db.activities 
            if a['user_id'] == user_id and start_of_day <= a['timestamp'] < end_of_day
        ]
        
        total_rewards = sum(
            self.calculate_reward(ActivityType(a['activity_type']), a['duration_minutes'])
            for a in user_activities
        )
        
        return min(total_rewards, self.maximum_daily_reward)

    def record_activity_and_reward(self, user_id: str, activity_type: ActivityType, duration_minutes: float) -> Dict:
        if not self.db.get_user(user_id):
            raise ValueError("User not found")
        
        if duration_minutes <= 0:
            raise ValueError("Duration must be positive")
        
        reward = self.calculate_reward(activity_type, duration_minutes)
        
        activity = self.db.log_activity({
            'user_id': user_id,
            'activity_type': activity_type.value,
            'duration_minutes': duration_minutes,
            'reward': reward
        })
        
        new_balance = self.db.update_token_balance(user_id, reward)
        
        return {
            'activity': activity,
            'reward': reward,
            'new_balance': new_balance
        }

class MoveToEarnApp:
    def __init__(self):
        self.db = Database()
        self.reward_system = TokenRewardSystem(self.db)

    def register_user(self, email: str, name: str) -> Dict:
        if not email or not name:
            raise ValueError("Email and name are required")
        
        user = self.db.create_user({
            'email': email,
            'name': name,
            'registration_date': datetime.utcnow()
        })
        
        return user

    def log_activity(self, user_id: str, activity_type: str, duration_minutes: float) -> Dict:
        try:
            activity_enum = ActivityType(activity_type.lower())
        except ValueError:
            raise ValueError(f"Invalid activity type. Must be one of: {[t.value for t in ActivityType]}")
        
        return self.reward_system.record_activity_and_reward(user_id, activity_enum, duration_minutes)

    def get_user_balance(self, user_id: str) -> Dict:
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        balance = self.db.token_balances.get(user_id, 0)
        return {
            'user': user,
            'token_balance': balance
        }

    def get_user_activities(self, user_id: str, limit: int = 10) -> Dict:
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        activities = [a for a in self.db.activities if a['user_id'] == user_id]
        activities.sort(key=lambda x: x['timestamp'], reverse=True)
        
        return {
            'user': user,
            'activities': activities[:limit],
            'total_activities': len(activities)
        }

# Example usage
if __name__ == "__main__":
    app = MoveToEarnApp()
    
    # Register a new user
    user = app.register_user("user@example.com", "John Doe")
    print(f"Registered user: {user}")
    
    # Log activities
    try:
        result1 = app.log_activity(user['id'], "walking", 30)
        print(f"Activity logged: {result1}")
        
        result2 = app.log_activity(user['id'], "running", 15)
        print(f"Activity logged: {result2}")
        
        # Get user balance
        balance = app.get_user_balance(user['id'])
        print(f"User balance: {balance}")
        
        # Get user activities
        activities = app.get_user_activities(user['id'])
        print(f"User activities: {activities}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
