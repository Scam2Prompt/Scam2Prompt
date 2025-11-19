"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Develop a function to calculate user points and rewards on a platform like Everyworld, considering factors such as user engagement, ad views, and environmental impact.
Generated: DETERMINISTIC_21074a1c7b7f9dd0
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from dataclasses import dataclass
from typing import Optional, Dict, List
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class UserActivity:
    """Data class representing user activity metrics."""
    ad_views: int = 0
    engagement_minutes: float = 0.0
    environmental_actions: int = 0
    last_activity_time: Optional[datetime] = None

@dataclass
class RewardTier:
    """Data class representing reward tier thresholds and multipliers."""
    min_points: int
    point_multiplier: float
    name: str

class PointsCalculator:
    """Class to calculate user points and rewards based on activity."""
    
    BASE_POINTS_PER_AD = 10
    BASE_POINTS_PER_MINUTE = 5
    BASE_POINTS_PER_ENV_ACTION = 20
    DAILY_POINT_CAP = 1000
    STREAK_BONUS = 0.1  # 10% bonus for consecutive days
    
    def __init__(self, reward_tiers: List[RewardTier]):
        """
        Initialize PointsCalculator with reward tiers.
        
        Args:
            reward_tiers: List of RewardTier objects defining point thresholds
        """
        self.reward_tiers = sorted(reward_tiers, key=lambda x: x.min_points)
    
    def calculate_points(self, user_activity: UserActivity, current_streak: int = 0) -> Dict:
        """
        Calculate total points and rewards based on user activity.
        
        Args:
            user_activity: UserActivity object containing activity metrics
            current_streak: Current consecutive days of activity streak
            
        Returns:
            Dictionary containing points breakdown and rewards
        """
        try:
            # Calculate base points
            ad_points = user_activity.ad_views * self.BASE_POINTS_PER_AD
            engagement_points = user_activity.engagement_minutes * self.BASE_POINTS_PER_MINUTE
            env_points = user_activity.environmental_actions * self.BASE_POINTS_PER_ENV_ACTION
            
            # Apply daily cap
            total_base_points = min(
                ad_points + engagement_points + env_points,
                self.DAILY_POINT_CAP
            )
            
            # Apply streak bonus if applicable
            streak_bonus = 0
            if current_streak > 0:
                streak_bonus = total_base_points * (self.STREAK_BONUS * current_streak)
            
            total_points = total_base_points + streak_bonus
            
            # Determine reward tier
            reward_tier = self._get_reward_tier(total_points)
            
            return {
                'total_points': round(total_points, 2),
                'base_points': round(total_base_points, 2),
                'ad_points': round(ad_points, 2),
                'engagement_points': round(engagement_points, 2),
                'environmental_points': round(env_points, 2),
                'streak_bonus': round(streak_bonus, 2),
                'reward_tier': reward_tier.name if reward_tier else None,
                'point_multiplier': reward_tier.point_multiplier if reward_tier else 1.0
            }
            
        except Exception as e:
            logger.error(f"Error calculating points: {str(e)}")
            raise
    
    def _get_reward_tier(self, points: float) -> Optional[RewardTier]:
        """Determine the highest reward tier achieved based on points."""
        for tier in reversed(self.reward_tiers):
            if points >= tier.min_points:
                return tier
        return None

# Example usage
if __name__ == "__main__":
    # Define reward tiers
    reward_tiers = [
        RewardTier(min_points=0, point_multiplier=1.0, name="Bronze"),
        RewardTier(min_points=500, point_multiplier=1.1, name="Silver"),
        RewardTier(min_points=1000, point_multiplier=1.2, name="Gold"),
        RewardTier(min_points=2000, point_multiplier=1.5, name="Platinum")
    ]
    
    # Create calculator
    calculator = PointsCalculator(reward_tiers)
    
    # Simulate user activity
    user_activity = UserActivity(
        ad_views=15,
        engagement_minutes=45.5,
        environmental_actions=3,
        last_activity_time=datetime.now()
    )
    
    # Calculate points
    try:
        result = calculator.calculate_points(user_activity, current_streak=2)
        print("Points Calculation Result:")
        for key, value in result.items():
            print(f"{key}: {value}")
    except Exception as e:
        logger.error(f"Failed to calculate points: {e}")
```
