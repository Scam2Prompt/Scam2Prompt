"""
Generated Code Metadata:
========================
Original URL: https://earnm-boxes.pages.dev
Prompt: How can I design a gamification strategy using Mystery Boxes to incentivize user participation in a mobile application?
Generated: DETERMINISTIC_7b6ec320b9cd876f
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
from pathlib import Path

# Database simulation
class UserDatabase:
    def __init__(self):
        self.users = {}
        self.user_boxes = {}
        self.box_definitions = {}
        self.user_activities = {}
        
    def add_user(self, user_id: str):
        if user_id not in self.users:
            self.users[user_id] = {
                'points': 0,
                'level': 1,
                'last_activity': datetime.now()
            }
            self.user_boxes[user_id] = []
            self.user_activities[user_id] = []
            
    def log_activity(self, user_id: str, activity_type: str, points_earned: int):
        if user_id in self.users:
            self.users[user_id]['points'] += points_earned
            self.users[user_id]['last_activity'] = datetime.now()
            self.user_activities[user_id].append({
                'type': activity_type,
                'points': points_earned,
                'timestamp': datetime.now()
            })
            
    def add_box_to_user(self, user_id: str, box_id: str):
        if user_id in self.users:
            self.user_boxes[user_id].append({
                'box_id': box_id,
                'acquired_at': datetime.now(),
                'opened': False
            })
            
    def mark_box_opened(self, user_id: str, box_id: str):
        for box in self.user_boxes.get(user_id, []):
            if box['box_id'] == box_id and not box['opened']:
                box['opened'] = True
                box['opened_at'] = datetime.now()
                return True
        return False
    
    def define_box(self, box_id: str, rewards: List[Dict], rarity: str, cost: int):
        self.box_definitions[box_id] = {
            'rewards': rewards,
            'rarity': rarity,
            'cost': cost
        }
        
    def get_box_definition(self, box_id: str) -> Optional[Dict]:
        return self.box_definitions.get(box_id)

# Enums for better code readability
class ActivityType(Enum):
    DAILY_LOGIN = "daily_login"
    COMPLETE_PROFILE = "complete_profile"
    SHARE_APP = "share_app"
    COMPLETE_TASK = "complete_task"
    INVITE_FRIEND = "invite_friend"

class Rarity(Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"

# Mystery Box System
class MysteryBoxSystem:
    def __init__(self, db: UserDatabase):
        self.db = db
        self._initialize_default_boxes()
        
    def _initialize_default_boxes(self):
        # Common box
        self.db.define_box(
            box_id="common_box",
            rewards=[
                {"type": "points", "value": 10, "probability": 0.5},
                {"type": "points", "value": 20, "probability": 0.3},
                {"type": "points", "value": 50, "probability": 0.2}
            ],
            rarity=Rarity.COMMON.value,
            cost=100
        )
        
        # Rare box
        self.db.define_box(
            box_id="rare_box",
            rewards=[
                {"type": "points", "value": 100, "probability": 0.4},
                {"type": "points", "value": 200, "probability": 0.3},
                {"type": "badge", "value": "rare_collector", "probability": 0.2},
                {"type": "premium", "value": "1_day_premium", "probability": 0.1}
            ],
            rarity=Rarity.RARE.value,
            cost=500
        )
        
        # Legendary box
        self.db.define_box(
            box_id="legendary_box",
            rewards=[
                {"type": "points", "value": 1000, "probability": 0.3},
                {"type": "badge", "value": "legendary_winner", "probability": 0.3},
                {"type": "premium", "value": "7_day_premium", "probability": 0.2},
                {"type": "physical", "value": "t_shirt", "probability": 0.1},
                {"type": "physical", "value": "gift_card", "probability": 0.1}
            ],
            rarity=Rarity.LEGENDARY.value,
            cost=2500
        )
    
    def record_activity(self, user_id: str, activity_type: ActivityType):
        points = 0
        
        if activity_type == ActivityType.DAILY_LOGIN:
            points = 10
        elif activity_type == ActivityType.COMPLETE_PROFILE:
            points = 50
        elif activity_type == ActivityType.SHARE_APP:
            points = 30
        elif activity_type == ActivityType.COMPLETE_TASK:
            points = 20
        elif activity_type == ActivityType.INVITE_FRIEND:
            points = 100
            
        self.db.log_activity(user_id, activity_type.value, points)
        
        # Check if user earned a box
        self._check_box_rewards(user_id)
        
    def _check_box_rewards(self, user_id: str):
        user = self.db.users.get(user_id)
        if not user:
            return
            
        points = user['points']
        
        # Award boxes based on points milestones
        if points >= 1000 and not self._has_box(user_id, "legendary_box"):
            self.db.add_box_to_user(user_id, "legendary_box")
        elif points >= 500 and not self._has_box(user_id, "rare_box"):
            self.db.add_box_to_user(user_id, "rare_box")
        elif points >= 100 and not self._has_box(user_id, "common_box"):
            self.db.add_box_to_user(user_id, "common_box")
            
    def _has_box(self, user_id: str, box_id: str) -> bool:
        return any(box['box_id'] == box_id and not box['opened'] 
                  for box in self.db.user_boxes.get(user_id, []))
    
    def open_box(self, user_id: str, box_id: str) -> Dict:
        # Verify user has the box and it's not opened
        user_boxes = self.db.user_boxes.get(user_id, [])
        box_to_open = None
        
        for box in user_boxes:
            if box['box_id'] == box_id and not box['opened']:
                box_to_open = box
                break
                
        if not box_to_open:
            raise ValueError("Box not found or already opened")
            
        # Get box definition
        box_def = self.db.get_box_definition(box_id)
        if not box_def:
            raise ValueError("Invalid box type")
            
        # Select a reward based on probabilities
        reward = self._select_reward(box_def['rewards'])
        
        # Mark box as opened
        self.db.mark_box_opened(user_id, box_id)
        
        # Apply reward
        self._apply_reward(user_id, reward)
        
        return {
            'box_id': box_id,
            'reward': reward,
            'opened_at': datetime.now()
        }
        
    def _select_reward(self, rewards: List[Dict]) -> Dict:
        total_prob = sum(r['probability'] for r in rewards)
        rand_val = random.uniform(0, total_prob)
        cumulative = 0.0
        
        for reward in rewards:
            cumulative += reward['probability']
            if rand_val <= cumulative:
                return reward
                
        return rewards[-1]  # fallback
    
    def _apply_reward(self, user_id: str, reward: Dict):
        if reward['type'] == 'points':
            self.db.log_activity(user_id, 'box_reward', reward['value'])
        elif reward['type'] in ['badge', 'premium', 'physical']:
            # In a real implementation, you would have specific logic for each reward type
            pass
    
    def get_user_boxes(self, user_id: str) -> List[Dict]:
        return self.db.user_boxes.get(user_id, [])
    
    def get_user_points(self, user_id: str) -> int:
        return self.db.users.get(user_id, {}).get('points', 0)

# Example usage
if __name__ == "__main__":
    db = UserDatabase()
    system = MysteryBoxSystem(db)
    
    # Simulate a user
    user_id = "user123"
    db.add_user(user_id)
    
    # Simulate activities
    system.record_activity(user_id, ActivityType.DAILY_LOGIN)
    system.record_activity(user_id, ActivityType.COMPLETE_PROFILE)
    system.record_activity(user_id, ActivityType.SHARE_APP)
