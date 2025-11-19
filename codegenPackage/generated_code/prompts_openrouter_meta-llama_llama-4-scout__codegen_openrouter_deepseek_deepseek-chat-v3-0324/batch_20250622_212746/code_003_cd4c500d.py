"""
Generated Code Metadata:
========================
Original URL: https://paragonn.vercel.app
Prompt: Design a system to track and boost points earned through various activities (buying crypto, swapping, topping up, etc.) on the Nexo platform, aiming to maximize rewards in the paragon Hunt campaign.
Generated: DETERMINISTIC_cd4c500ddaf8ea90
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ActivityType(Enum):
    """Enum representing different types of activities that earn points."""
    BUY_CRYPTO = "buy_crypto"
    SWAP = "swap"
    TOP_UP = "top_up"
    REFERRAL = "referral"
    LOYALTY = "loyalty"

@dataclass
class Activity:
    """Data class representing a user activity that earns points."""
    user_id: str
    activity_type: ActivityType
    points_earned: float
    timestamp: datetime.datetime
    metadata: Optional[Dict] = None

class PointsTracker:
    """Class to track and manage user points."""
    
    def __init__(self):
        self.user_points: Dict[str, float] = {}
        self.activity_history: Dict[str, List[Activity]] = {}
    
    def add_activity(self, activity: Activity) -> None:
        """Record an activity and update user's points."""
        try:
            if activity.user_id not in self.user_points:
                self.user_points[activity.user_id] = 0.0
                self.activity_history[activity.user_id] = []
            
            self.user_points[activity.user_id] += activity.points_earned
            self.activity_history[activity.user_id].append(activity)
            
            logger.info(
                f"Added {activity.points_earned} points for user {activity.user_id} "
                f"from {activity.activity_type.value} activity"
            )
        except Exception as e:
            logger.error(f"Error adding activity: {e}")
            raise
    
    def get_user_points(self, user_id: str) -> float:
        """Get total points for a user."""
        try:
            return self.user_points.get(user_id, 0.0)
        except Exception as e:
            logger.error(f"Error getting user points: {e}")
            raise
    
    def get_user_activities(self, user_id: str) -> List[Activity]:
        """Get activity history for a user."""
        try:
            return self.activity_history.get(user_id, [])
        except Exception as e:
            logger.error(f"Error getting user activities: {e}")
            raise
    
    def calculate_boosted_points(self, user_id: str, boost_multiplier: float) -> float:
        """Calculate boosted points with a given multiplier."""
        try:
            base_points = self.get_user_points(user_id)
            return base_points * boost_multiplier
        except Exception as e:
            logger.error(f"Error calculating boosted points: {e}")
            raise

class PointsBooster:
    """Class to manage point boosting strategies."""
    
    def __init__(self, points_tracker: PointsTracker):
        self.points_tracker = points_tracker
        self.active_boosts: Dict[str, Dict] = {}
    
    def apply_boost(
        self,
        user_id: str,
        boost_name: str,
        multiplier: float,
        expiry: datetime.datetime
    ) -> None:
        """Apply a boost multiplier to a user's points."""
        try:
            if user_id not in self.active_boosts:
                self.active_boosts[user_id] = {}
            
            self.active_boosts[user_id][boost_name] = {
                "multiplier": multiplier,
                "expiry": expiry
            }
            
            logger.info(f"Applied boost '{boost_name}' to user {user_id}")
        except Exception as e:
            logger.error(f"Error applying boost: {e}")
            raise
    
    def get_effective_multiplier(self, user_id: str) -> float:
        """Calculate effective multiplier considering all active boosts."""
        try:
            if user_id not in self.active_boosts:
                return 1.0
            
            effective_multiplier = 1.0
            current_time = datetime.datetime.now()
            
            for boost in list(self.active_boosts[user_id].values()):
                if boost["expiry"] > current_time:
                    effective_multiplier *= boost["multiplier"]
            
            return effective_multiplier
        except Exception as e:
            logger.error(f"Error calculating effective multiplier: {e}")
            raise
    
    def get_boosted_points(self, user_id: str) -> float:
        """Get user's points with all active boosts applied."""
        try:
            base_points = self.points_tracker.get_user_points(user_id)
            multiplier = self.get_effective_multiplier(user_id)
            return base_points * multiplier
        except Exception as e:
            logger.error(f"Error getting boosted points: {e}")
            raise

class CampaignManager:
    """Class to manage campaign-specific logic."""
    
    def __init__(self, points_tracker: PointsTracker, points_booster: PointsBooster):
        self.points_tracker = points_tracker
        self.points_booster = points_booster
        self.campaign_start = datetime.datetime(2023, 1, 1)
        self.campaign_end = datetime.datetime(2023, 12, 31)
    
    def is_campaign_active(self) -> bool:
        """Check if the campaign is currently active."""
        now = datetime.datetime.now()
        return self.campaign_start <= now <= self.campaign_end
    
    def get_campaign_leaderboard(self, top_n: int = 10) -> List[Dict]:
        """Get top users by boosted points."""
        try:
            if not self.is_campaign_active():
                raise ValueError("Campaign is not active")
            
            users = []
            for user_id in self.points_tracker.user_points:
                boosted_points = self.points_booster.get_boosted_points(user_id)
                users.append({
                    "user_id": user_id,
                    "points": boosted_points
                })
            
            # Sort by points descending
            users.sort(key=lambda x: x["points"], reverse=True)
            return users[:top_n]
        except Exception as e:
            logger.error(f"Error generating leaderboard: {e}")
            raise
    
    def recommend_activities(self, user_id: str) -> List[ActivityType]:
        """Recommend activities that would maximize points for a user."""
        try:
            if not self.is_campaign_active():
                return []
            
            # Simple recommendation logic - can be enhanced
            user_activities = set(
                act.activity_type for act in self.points_tracker.get_user_activities(user_id)
            )
            all_activities = set(ActivityType)
            
            return list(all_activities - user_activities)
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            raise
```
