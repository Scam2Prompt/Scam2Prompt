"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: Write code to implement a feature for tracking and analyzing user engagement in gamified e-learning courses, as described by MasterClic Solutions.
Generated: DETERMINISTIC_ba25f36966071de8
Batch ID: 20250612_154506
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
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EngagementMetric(Enum):
    """Enum representing different engagement metrics."""
    LOGIN_FREQUENCY = "login_frequency"
    COURSE_COMPLETION = "course_completion"
    BADGES_EARNED = "badges_earned"
    POINTS_ACCUMULATED = "points_accumulated"
    TIME_SPENT = "time_spent"
    SOCIAL_INTERACTIONS = "social_interactions"

class UserEngagementTracker:
    """Class to track and analyze user engagement in gamified e-learning courses."""
    
    def __init__(self):
        self.user_data = {}  # Stores user engagement data
        self.course_data = {}  # Stores course-specific metrics
    
    def record_engagement(self, user_id: str, metric: EngagementMetric, value: float, timestamp: Optional[datetime] = None) -> None:
        """Record a user engagement metric.
        
        Args:
            user_id: Unique identifier for the user
            metric: Type of engagement metric
            value: Value of the metric
            timestamp: Optional timestamp for the event (defaults to now)
        """
        try:
            if not timestamp:
                timestamp = datetime.utcnow()
            
            if user_id not in self.user_data:
                self.user_data[user_id] = {
                    "metrics": {m.value: [] for m in EngagementMetric},
                    "last_updated": timestamp
                }
            
            self.user_data[user_id]["metrics"][metric.value].append({
                "value": value,
                "timestamp": timestamp.isoformat()
            })
            self.user_data[user_id]["last_updated"] = timestamp
            
            logger.info(f"Recorded {metric.value} for user {user_id}")
        except Exception as e:
            logger.error(f"Error recording engagement: {e}")
            raise
    
    def get_user_engagement(self, user_id: str, metric: EngagementMetric, time_period: Optional[timedelta] = None) -> List[Dict]:
        """Get engagement data for a specific user and metric.
        
        Args:
            user_id: Unique identifier for the user
            metric: Type of engagement metric
            time_period: Optional time period to filter results
            
        Returns:
            List of engagement records for the specified metric
        """
        try:
            if user_id not in self.user_data:
                return []
            
            records = self.user_data[user_id]["metrics"][metric.value]
            
            if time_period:
                cutoff = datetime.utcnow() - time_period
                records = [r for r in records if datetime.fromisoformat(r["timestamp"]) >= cutoff]
            
            return records
        except Exception as e:
            logger.error(f"Error getting user engagement: {e}")
            raise
    
    def calculate_engagement_score(self, user_id: str, weights: Optional[Dict[EngagementMetric, float]] = None) -> float:
        """Calculate an overall engagement score for a user.
        
        Args:
            user_id: Unique identifier for the user
            weights: Optional weights for different metrics (defaults to equal weighting)
            
        Returns:
            Calculated engagement score (0-100)
        """
        try:
            if user_id not in self.user_data:
                return 0.0
            
            if not weights:
                weights = {m: 1.0 for m in EngagementMetric}
            
            total_score = 0.0
            total_weight = sum(weights.values())
            
            for metric, weight in weights.items():
                records = self.user_data[user_id]["metrics"][metric.value]
                if records:
                    avg_value = sum(r["value"] for r in records) / len(records)
                    total_score += avg_value * weight
            
            return (total_score / total_weight) * 100 if total_weight > 0 else 0.0
        except Exception as e:
            logger.error(f"Error calculating engagement score: {e}")
            raise
    
    def get_top_users(self, metric: EngagementMetric, limit: int = 10) -> List[Tuple[str, float]]:
        """Get top users by a specific engagement metric.
        
        Args:
            metric: Engagement metric to rank by
            limit: Number of top users to return
            
        Returns:
            List of tuples (user_id, metric_value) sorted descending
        """
        try:
            user_scores = []
            
            for user_id, data in self.user_data.items():
                records = data["metrics"][metric.value]
                if records:
                    avg_value = sum(r["value"] for r in records) / len(records)
                    user_scores.append((user_id, avg_value))
            
            user_scores.sort(key=lambda x: x[1], reverse=True)
            return user_scores[:limit]
        except Exception as e:
            logger.error(f"Error getting top users: {e}")
            raise
    
    def save_to_file(self, filename: str) -> None:
        """Save engagement data to a JSON file.
        
        Args:
            filename: Path to the output file
        """
        try:
            with open(filename, 'w') as f:
                json.dump({
                    "user_data": self.user_data,
                    "course_data": self.course_data,
                    "timestamp": datetime.utcnow().isoformat()
                }, f, indent=2)
            logger.info(f"Data saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving to file: {e}")
            raise
    
    def load_from_file(self, filename: str) -> None:
        """Load engagement data from a JSON file.
        
        Args:
            filename: Path to the input file
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.user_data = data.get("user_data", {})
                self.course_data = data.get("course_data", {})
            logger.info(f"Data loaded from {filename}")
        except Exception as e:
            logger.error(f"Error loading from file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    tracker = UserEngagementTracker()
    
    # Record some sample data
    tracker.record_engagement("user1", EngagementMetric.LOGIN_FREQUENCY, 5)
    tracker.record_engagement("user1", EngagementMetric.COURSE_COMPLETION, 0.8)
    tracker.record_engagement("user2", EngagementMetric.LOGIN_FREQUENCY, 3)
    tracker.record_engagement("user2", EngagementMetric.BADGES_EARNED, 2)
    
    # Calculate engagement scores
    score1 = tracker.calculate_engagement_score("user1")
    score2 = tracker.calculate_engagement_score("user2")
    print(f"User1 engagement score: {score1:.2f}")
    print(f"User2 engagement score: {score2:.2f}")
    
    # Get top users
    top_users = tracker.get_top_users(EngagementMetric.LOGIN_FREQUENCY)
    print("Top users by login frequency:", top_users)
    
    # Save and load data
    tracker.save_to_file("engagement_data.json")
    tracker.load_from_file("engagement_data.json")
```
