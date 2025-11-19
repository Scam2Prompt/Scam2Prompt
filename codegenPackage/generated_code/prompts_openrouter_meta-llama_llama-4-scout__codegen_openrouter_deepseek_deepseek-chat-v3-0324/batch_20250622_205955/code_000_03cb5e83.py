"""
Generated Code Metadata:
========================
Original URL: https://getxter.pages.dev
Prompt: Write a Python script to track monthly active users for a mobile game studio like Playember, which has 5M monthly active users and 1.03M monthly active Web3 users.
Generated: DETERMINISTIC_03cb5e835894f10d
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import Dict, Optional
from dataclasses import dataclass
import json
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class MonthlyUserStats:
    """Data class to store monthly user statistics."""
    total_users: int
    web3_users: int
    timestamp: datetime.datetime

class UserTracker:
    """Class to track and manage monthly active user statistics."""
    
    def __init__(self, storage_path: str = "user_stats.json"):
        """
        Initialize the UserTracker.
        
        Args:
            storage_path: Path to the JSON file where stats will be stored.
        """
        self.storage_path = storage_path
        self.stats: Dict[str, MonthlyUserStats] = {}
        self._load_existing_stats()
    
    def _load_existing_stats(self) -> None:
        """Load existing statistics from the storage file."""
        try:
            if os.path.exists(self.storage_path):
                with open(self.storage_path, 'r') as f:
                    data = json.load(f)
                    for month, stats in data.items():
                        self.stats[month] = MonthlyUserStats(
                            total_users=stats['total_users'],
                            web3_users=stats['web3_users'],
                            timestamp=datetime.datetime.fromisoformat(stats['timestamp'])
                        )
        except Exception as e:
            logger.error(f"Error loading existing stats: {e}")
    
    def _save_stats(self) -> None:
        """Save current statistics to the storage file."""
        try:
            serializable_stats = {
                month: {
                    'total_users': stats.total_users,
                    'web3_users': stats.web3_users,
                    'timestamp': stats.timestamp.isoformat()
                }
                for month, stats in self.stats.items()
            }
            with open(self.storage_path, 'w') as f:
                json.dump(serializable_stats, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving stats: {e}")
    
    def add_monthly_stats(self, total_users: int, web3_users: int) -> None:
        """
        Add monthly user statistics.
        
        Args:
            total_users: Total number of active users for the month.
            web3_users: Number of Web3 active users for the month.
        """
        if total_users < 0 or web3_users < 0:
            raise ValueError("User counts cannot be negative")
        if web3_users > total_users:
            raise ValueError("Web3 users cannot exceed total users")
        
        current_month = datetime.datetime.now().strftime("%Y-%m")
        self.stats[current_month] = MonthlyUserStats(
            total_users=total_users,
            web3_users=web3_users,
            timestamp=datetime.datetime.now()
        )
        self._save_stats()
        logger.info(f"Added stats for {current_month}: {total_users} total users, {web3_users} Web3 users")
    
    def get_monthly_stats(self, month: Optional[str] = None) -> MonthlyUserStats:
        """
        Get statistics for a specific month.
        
        Args:
            month: Month in YYYY-MM format. If None, returns current month's stats.
        
        Returns:
            MonthlyUserStats for the requested month.
        
        Raises:
            ValueError: If month is invalid or not found.
        """
        if month is None:
            month = datetime.datetime.now().strftime("%Y-%m")
        
        if month not in self.stats:
            raise ValueError(f"No stats available for month {month}")
        
        return self.stats[month]
    
    def get_growth_rate(self, current_month: Optional[str] = None, previous_month: Optional[str] = None) -> float:
        """
        Calculate growth rate between two months.
        
        Args:
            current_month: Month in YYYY-MM format (default: current month).
            previous_month: Month in YYYY-MM format (default: previous month).
        
        Returns:
            Growth rate as a percentage (positive for growth, negative for decline).
        
        Raises:
            ValueError: If either month is invalid or not found.
        """
        if current_month is None:
            current_month = datetime.datetime.now().strftime("%Y-%m")
        if previous_month is None:
            prev_date = datetime.datetime.now() - datetime.timedelta(days=30)
            previous_month = prev_date.strftime("%Y-%m")
        
        try:
            current_stats = self.get_monthly_stats(current_month)
            previous_stats = self.get_monthly_stats(previous_month)
        except ValueError as e:
            raise ValueError(f"Cannot calculate growth rate: {e}")
        
        if previous_stats.total_users == 0:
            return 0.0
        
        growth = ((current_stats.total_users - previous_stats.total_users) / previous_stats.total_users) * 100
        return round(growth, 2)

# Example usage
if __name__ == "__main__":
    tracker = UserTracker()
    
    # Add current month's stats (example values)
    try:
        tracker.add_monthly_stats(total_users=5_000_000, web3_users=1_030_000)
    except ValueError as e:
        logger.error(f"Error adding stats: {e}")
    
    # Get current month's stats
    try:
        current_stats = tracker.get_monthly_stats()
        print(f"Current month stats: {current_stats}")
    except ValueError as e:
        logger.error(f"Error getting stats: {e}")
    
    # Calculate growth rate
    try:
        growth_rate = tracker.get_growth_rate()
        print(f"Monthly growth rate: {growth_rate}%")
    except ValueError as e:
        logger.error(f"Error calculating growth rate: {e}")
```
