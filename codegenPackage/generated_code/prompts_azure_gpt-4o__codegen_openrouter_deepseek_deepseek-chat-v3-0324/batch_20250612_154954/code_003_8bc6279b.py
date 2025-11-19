"""
Generated Code Metadata:
========================
Original URL: https://cmdsa.com
Prompt: Provide examples of how to use CMD's digital monitoring system for tracking user activity across multiple channels.
Generated: DETERMINISTIC_8bc6279beb009277
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ChannelType(Enum):
    """Enum representing different digital channels."""
    WEB = "web"
    MOBILE = "mobile"
    SOCIAL = "social"
    EMAIL = "email"
    SMS = "sms"

class UserActivity:
    """Class to represent user activity across channels."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.activities: List[Dict] = []
    
    def add_activity(
        self,
        channel: ChannelType,
        action: str,
        timestamp: Optional[datetime] = None,
        metadata: Optional[Dict] = None
    ) -> None:
        """Record a user activity.
        
        Args:
            channel: The channel where activity occurred
            action: Description of the activity
            timestamp: When the activity occurred (defaults to now)
            metadata: Additional context about the activity
        """
        try:
            activity = {
                "channel": channel.value,
                "action": action,
                "timestamp": timestamp or datetime.utcnow(),
                "metadata": metadata or {}
            }
            self.activities.append(activity)
            logger.info(f"Activity recorded for user {self.user_id}")
        except Exception as e:
            logger.error(f"Failed to record activity: {str(e)}")
            raise
    
    def get_activities_by_channel(self, channel: ChannelType) -> List[Dict]:
        """Get all activities for a specific channel.
        
        Args:
            channel: The channel to filter by
            
        Returns:
            List of matching activities
        """
        return [act for act in self.activities if act["channel"] == channel.value]

class DigitalMonitoringSystem:
    """Main class for the digital monitoring system."""
    
    def __init__(self):
        self.users: Dict[str, UserActivity] = {}
    
    def track_user_activity(
        self,
        user_id: str,
        channel: ChannelType,
        action: str,
        **kwargs
    ) -> None:
        """Track a user activity across channels.
        
        Args:
            user_id: Unique identifier for the user
            channel: Channel where activity occurred
            action: Description of the activity
            kwargs: Additional arguments (timestamp, metadata)
        """
        try:
            if user_id not in self.users:
                self.users[user_id] = UserActivity(user_id)
            
            self.users[user_id].add_activity(channel, action, **kwargs)
        except Exception as e:
            logger.error(f"Tracking failed for user {user_id}: {str(e)}")
            raise
    
    def get_user_activities(self, user_id: str) -> List[Dict]:
        """Get all activities for a user.
        
        Args:
            user_id: User to retrieve activities for
            
        Returns:
            List of all user activities
        """
        if user_id not in self.users:
            logger.warning(f"No activities found for user {user_id}")
            return []
        return self.users[user_id].activities
    
    def get_channel_activities(self, channel: ChannelType) -> List[Dict]:
        """Get all activities across users for a specific channel.
        
        Args:
            channel: Channel to filter by
            
        Returns:
            List of all activities on the specified channel
        """
        activities = []
        for user in self.users.values():
            activities.extend(user.get_activities_by_channel(channel))
        return activities

# Example usage
if __name__ == "__main__":
    # Initialize monitoring system
    monitor = DigitalMonitoringSystem()
    
    # Track some activities
    monitor.track_user_activity(
        "user123",
        ChannelType.WEB,
        "page_view",
        metadata={"page": "homepage"}
    )
    
    monitor.track_user_activity(
        "user123",
        ChannelType.MOBILE,
        "app_open",
        timestamp=datetime(2023, 1, 15, 10, 30)
    )
    
    monitor.track_user_activity(
        "user456",
        ChannelType.SOCIAL,
        "post_like",
        metadata={"platform": "twitter", "post_id": "abc123"}
    )
    
    # Retrieve activities
    print("User 123 activities:", monitor.get_user_activities("user123"))
    print("Social channel activities:", monitor.get_channel_activities(ChannelType.SOCIAL))
```
