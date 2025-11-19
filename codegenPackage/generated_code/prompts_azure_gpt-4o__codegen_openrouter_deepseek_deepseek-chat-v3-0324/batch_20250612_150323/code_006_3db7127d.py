"""
Generated Code Metadata:
========================
Original URL: https://web3inbox.com
Prompt: Write a script to implement spam and rate limit protections for Web3Inbox notifications using WalletConnect's Notify API.
Generated: DETERMINISTIC_3db7127dbc7b6dcf
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import redis
from fastapi import HTTPException, Request
from pydantic import BaseModel

# Configuration
class RateLimitConfig(BaseModel):
    window_seconds: int = 60  # Time window in seconds
    max_requests: int = 10   # Max requests allowed in the window
    spam_threshold: int = 5  # Minimum time between notifications in seconds

# Redis client setup
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

class NotificationProtection:
    def __init__(self, config: RateLimitConfig):
        self.config = config

    async def check_rate_limit(self, user_id: str) -> bool:
        """
        Check if user has exceeded rate limit
        Returns True if allowed, False if rate limited
        """
        key = f"rate_limit:{user_id}"
        current_time = datetime.now().timestamp()
        window_start = current_time - self.config.window_seconds

        # Remove old timestamps
        redis_client.zremrangebyscore(key, 0, window_start)

        # Count requests in current window
        request_count = redis_client.zcard(key)
        if request_count >= self.config.max_requests:
            return False

        # Add current request timestamp
        redis_client.zadd(key, {str(current_time): current_time})
        redis_client.expire(key, self.config.window_seconds)
        return True

    async def check_spam_protection(self, user_id: str, notification_id: str) -> bool:
        """
        Check if notification is considered spam
        Returns True if allowed, False if spam
        """
        spam_key = f"spam_protection:{user_id}"
        last_notification_time = redis_client.get(spam_key)

        if last_notification_time:
            last_time = float(last_notification_time)
            current_time = datetime.now().timestamp()
            if current_time - last_time < self.config.spam_threshold:
                return False

        # Update last notification time
        redis_client.set(spam_key, str(datetime.now().timestamp()))
        redis_client.expire(spam_key, self.config.spam_threshold)
        return True

    async def protect_notification(
        self,
        user_id: str,
        notification_id: str,
        request: Optional[Request] = None
    ) -> None:
        """
        Combined protection check for rate limiting and spam
        Raises HTTPException if protections are triggered
        """
        # Check rate limit
        if not await self.check_rate_limit(user_id):
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Please try again later."
            )

        # Check spam protection
        if not await self.check_spam_protection(user_id, notification_id):
            raise HTTPException(
                status_code=429,
                detail="Notification frequency too high. Please wait before sending another."
            )

# Example usage
if __name__ == "__main__":
    # Initialize with default config
    protection = NotificationProtection(RateLimitConfig())

    # Mock user and notification
    user_id = "user123"
    notification_id = "notif456"

    # Test rate limit
    for i in range(12):
        try:
            protection.protect_notification(user_id, notification_id)
            print(f"Notification {i+1}: Allowed")
        except HTTPException as e:
            print(f"Notification {i+1}: {e.detail}")

    # Test spam protection
    try:
        protection.protect_notification(user_id, notification_id)
        print("First notification: Allowed")
        protection.protect_notification(user_id, notification_id)
        print("Second notification: Allowed")
    except HTTPException as e:
        print(f"Second notification: {e.detail}")
```
