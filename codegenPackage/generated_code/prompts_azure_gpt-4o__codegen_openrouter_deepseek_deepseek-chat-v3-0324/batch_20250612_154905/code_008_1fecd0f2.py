"""
Generated Code Metadata:
========================
Original URL: https://miningbase.cloud
Prompt: Create a Python script to simulate free hashing power allocation for new users, similar to the MiningBase free GH/s feature.
Generated: DETERMINISTIC_1fecd0f2434b187c
Batch ID: 20250612_154905
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
from typing import Dict, List, Optional
from dataclasses import dataclass
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('hashing_power.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class User:
    """Represents a user with allocated hashing power."""
    user_id: str
    allocated_power: float  # in GH/s
    allocation_time: datetime
    expiration_time: datetime

class HashingPowerAllocator:
    """Manages allocation of free hashing power to users."""
    
    def __init__(
        self,
        base_power: float = 1.0,
        max_power: float = 10.0,
        allocation_duration: timedelta = timedelta(days=1),
        max_users: int = 1000
    ):
        """
        Initialize the hashing power allocator.
        
        Args:
            base_power: Base hashing power to allocate (in GH/s)
            max_power: Maximum hashing power that can be allocated (in GH/s)
            allocation_duration: Duration for which power is allocated
            max_users: Maximum number of users that can be allocated power
        """
        self.base_power = base_power
        self.max_power = max_power
        self.allocation_duration = allocation_duration
        self.max_users = max_users
        self.users: Dict[str, User] = {}
        
    def allocate_power(self, user_id: str) -> Optional[float]:
        """
        Allocate free hashing power to a new user.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            Allocated hashing power in GH/s or None if allocation failed
        """
        if user_id in self.users:
            logging.warning(f"User {user_id} already has allocated power")
            return None
            
        if len(self.users) >= self.max_users:
            logging.error("Maximum user capacity reached")
            return None
            
        try:
            # Calculate random bonus power (0-100% of base power)
            bonus_power = random.uniform(0, self.base_power)
            allocated_power = min(self.base_power + bonus_power, self.max_power)
            
            now = datetime.now()
            expiration_time = now + self.allocation_duration
            
            self.users[user_id] = User(
                user_id=user_id,
                allocated_power=allocated_power,
                allocation_time=now,
                expiration_time=expiration_time
            )
            
            logging.info(f"Allocated {allocated_power:.2f} GH/s to user {user_id}")
            return allocated_power
            
        except Exception as e:
            logging.error(f"Failed to allocate power to user {user_id}: {str(e)}")
            return None
    
    def get_user_power(self, user_id: str) -> Optional[float]:
        """
        Get the allocated hashing power for a user.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            Allocated hashing power in GH/s or None if not found/expired
        """
        user = self.users.get(user_id)
        if not user:
            return None
            
        if datetime.now() > user.expiration_time:
            self.users.pop(user_id)
            logging.info(f"Power allocation expired for user {user_id}")
            return None
            
        return user.allocated_power
    
    def cleanup_expired_users(self) -> int:
        """
        Clean up expired user allocations.
        
        Returns:
            Number of expired users removed
        """
        now = datetime.now()
        expired_users = [
            user_id for user_id, user in self.users.items()
            if now > user.expiration_time
        ]
        
        for user_id in expired_users:
            self.users.pop(user_id)
            
        if expired_users:
            logging.info(f"Cleaned up {len(expired_users)} expired users")
            
        return len(expired_users)
    
    def get_active_users(self) -> List[User]:
        """Return list of active users with allocated power."""
        self.cleanup_expired_users()
        return list(self.users.values())

def simulate_allocation(allocator: HashingPowerAllocator, num_users: int = 10):
    """Simulate hashing power allocation to multiple users."""
    for i in range(1, num_users + 1):
        user_id = f"user_{i}"
        power = allocator.allocate_power(user_id)
        if power:
            time.sleep(0.1)  # Simulate delay between allocations

if __name__ == "__main__":
    # Example usage
    try:
        allocator = HashingPowerAllocator(
            base_power=1.0,
            max_power=5.0,
            allocation_duration=timedelta(minutes=5),
            max_users=100
        )
        
        # Simulate allocations
        simulate_allocation(allocator, 5)
        
        # Check allocations
        for user in allocator.get_active_users():
            print(f"User {user.user_id} has {user.allocated_power:.2f} GH/s until {user.expiration_time}")
            
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
```
