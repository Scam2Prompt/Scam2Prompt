"""
Generated Code Metadata:
========================
Original URL: https://multiminer.website
Prompt: Write code to simulate hourly free mining power allocation for users, as described in Bitspeed's free mining account feature.
Generated: DETERMINISTIC_9e7ea096482fd6ec
Batch ID: 20250612_151345
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
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('mining_simulation.log'),
        logging.StreamHandler()
    ]
)

class User:
    """Represents a user with mining power allocation."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.allocated_power = 0.0
        self.last_allocation_time = None
    
    def allocate_power(self, power: float, allocation_time: datetime):
        """Allocate mining power to the user."""
        self.allocated_power += power
        self.last_allocation_time = allocation_time
        logging.info(f"Allocated {power} mining power to user {self.user_id}")

class MiningSimulator:
    """Simulates hourly free mining power allocation to users."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.base_mining_power = 1.0  # Base mining power per hour
        self.variation_range = 0.5    # ± variation for randomization
    
    def register_user(self, user_id: str) -> None:
        """Register a new user if not already registered."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
            logging.info(f"Registered new user: {user_id}")
    
    def get_randomized_power(self) -> float:
        """Generate randomized mining power within specified range."""
        variation = random.uniform(-self.variation_range, self.variation_range)
        return max(0.1, self.base_mining_power + variation)  # Ensure minimum power
    
    def allocate_hourly_power(self) -> None:
        """Allocate mining power to all registered users."""
        current_time = datetime.now()
        for user in self.users.values():
            # Check if user is eligible for allocation (once per hour)
            if (user.last_allocation_time is None or 
                current_time - user.last_allocation_time >= timedelta(hours=1)):
                power = self.get_randomized_power()
                user.allocate_power(power, current_time)
    
    def get_user_stats(self, user_id: str) -> Optional[Dict[str, float]]:
        """Get mining statistics for a specific user."""
        user = self.users.get(user_id)
        if user:
            return {
                'user_id': user.user_id,
                'allocated_power': user.allocated_power,
                'last_allocation_time': user.last_allocation_time
            }
        return None
    
    def run_simulation(self, duration_hours: int = 24) -> None:
        """Run the simulation for a specified duration."""
        logging.info(f"Starting mining simulation for {duration_hours} hours")
        end_time = datetime.now() + timedelta(hours=duration_hours)
        
        while datetime.now() < end_time:
            try:
                self.allocate_hourly_power()
                # Sleep until next hour
                time.sleep(3600)  # 1 hour in seconds
            except KeyboardInterrupt:
                logging.info("Simulation stopped by user")
                break
            except Exception as e:
                logging.error(f"Error during simulation: {str(e)}")
                time.sleep(60)  # Wait before retrying
        
        logging.info("Mining simulation completed")

# Example usage
if __name__ == "__main__":
    simulator = MiningSimulator()
    
    # Register some users
    simulator.register_user("user1")
    simulator.register_user("user2")
    simulator.register_user("user3")
    
    # Run simulation for 24 hours
    simulator.run_simulation(24)
    
    # Print final stats
    for user_id in ["user1", "user2", "user3"]:
        stats = simulator.get_user_stats(user_id)
        if stats:
            print(f"User {user_id} stats: {stats}")
```
