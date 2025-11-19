"""
Generated Code Metadata:
========================
Original URL: https://equipethaianealquimim.site
Prompt: Create a script that tracks online users of a signal generation tool and outputs real-time statistics, similar to the functionality described for 500 players.
Generated: DETERMINISTIC_6e35c38ed9b8fb55
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from collections import defaultdict
from datetime import datetime, timedelta
import threading
import logging
from typing import Dict, List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('user_tracker.log'),
        logging.StreamHandler()
    ]
)

class UserTracker:
    """
    A class to track online users and generate real-time statistics.
    """
    
    def __init__(self):
        """Initialize the UserTracker with empty data structures."""
        self.online_users = set()
        self.user_sessions = defaultdict(list)
        self.lock = threading.Lock()
        self.running = False
        self.stats_interval = 60  # seconds
        
    def add_user(self, user_id: str) -> None:
        """
        Add a user to the online users set and record their session start time.
        
        Args:
            user_id: Unique identifier for the user.
        """
        with self.lock:
            if user_id not in self.online_users:
                self.online_users.add(user_id)
                self.user_sessions[user_id].append(datetime.now())
                logging.info(f"User {user_id} came online")
    
    def remove_user(self, user_id: str) -> None:
        """
        Remove a user from the online users set and record their session end time.
        
        Args:
            user_id: Unique identifier for the user.
        """
        with self.lock:
            if user_id in self.online_users:
                self.online_users.remove(user_id)
                if self.user_sessions[user_id]:
                    last_session = self.user_sessions[user_id][-1]
                    duration = (datetime.now() - last_session).total_seconds()
                    logging.info(f"User {user_id} went offline after {duration:.2f} seconds")
    
    def get_online_count(self) -> int:
        """
        Get the current number of online users.
        
        Returns:
            int: Number of online users.
        """
        with self.lock:
            return len(self.online_users)
    
    def get_user_sessions(self, user_id: str) -> List[Tuple[datetime, datetime]]:
        """
        Get all sessions for a specific user.
        
        Args:
            user_id: Unique identifier for the user.
            
        Returns:
            List of tuples with (start_time, end_time) for each session.
        """
        with self.lock:
            sessions = []
            timestamps = self.user_sessions.get(user_id, [])
            for i in range(0, len(timestamps), 2):
                start = timestamps[i]
                end = timestamps[i+1] if i+1 < len(timestamps) else None
                sessions.append((start, end))
            return sessions
    
    def generate_stats(self) -> Dict[str, float]:
        """
        Generate statistics about user activity.
        
        Returns:
            Dictionary containing various statistics.
        """
        with self.lock:
            stats = {
                'online_users': len(self.online_users),
                'total_sessions': sum(len(sessions) // 2 for sessions in self.user_sessions.values()),
                'avg_session_duration': 0,
                'max_concurrent': 0
            }
            
            # Calculate average session duration
            total_duration = 0
            session_count = 0
            for sessions in self.user_sessions.values():
                for i in range(0, len(sessions), 2):
                    if i+1 < len(sessions):
                        duration = (sessions[i+1] - sessions[i]).total_seconds()
                        total_duration += duration
                        session_count += 1
            
            if session_count > 0:
                stats['avg_session_duration'] = total_duration / session_count
            
            return stats
    
    def stats_loop(self) -> None:
        """Periodically log statistics while the tracker is running."""
        while self.running:
            stats = self.generate_stats()
            logging.info(f"Current stats: {stats}")
            time.sleep(self.stats_interval)
    
    def start(self) -> None:
        """Start the user tracker and statistics thread."""
        self.running = True
        threading.Thread(target=self.stats_loop, daemon=True).start()
        logging.info("User tracker started")
    
    def stop(self) -> None:
        """Stop the user tracker and statistics thread."""
        self.running = False
        logging.info("User tracker stopped")

def simulate_users(tracker: UserTracker, num_users: int = 500) -> None:
    """
    Simulate user activity for testing purposes.
    
    Args:
        tracker: UserTracker instance
        num_users: Number of users to simulate
    """
    user_ids = [f"user_{i}" for i in range(1, num_users + 1)]
    
    while tracker.running:
        # Randomly add or remove users
        user_id = random.choice(user_ids)
        if user_id in tracker.online_users:
            tracker.remove_user(user_id)
        else:
            tracker.add_user(user_id)
        
        # Random delay between actions
        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    try:
        tracker = UserTracker()
        tracker.start()
        
        # Start simulation in a separate thread
        simulation_thread = threading.Thread(
            target=simulate_users,
            args=(tracker, 500),
            daemon=True
        )
        simulation_thread.start()
        
        # Keep main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        tracker.stop()
        logging.info("Shutting down...")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        tracker.stop()
```
