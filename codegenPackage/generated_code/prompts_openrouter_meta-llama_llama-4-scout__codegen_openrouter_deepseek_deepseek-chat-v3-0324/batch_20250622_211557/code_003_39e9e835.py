"""
Generated Code Metadata:
========================
Original URL: https://equipeleiafreitas.site
Prompt: Generate code to track and analyze user engagement for a gaming tool with 500 concurrent users.
Generated: DETERMINISTIC_39e9e835ec7b3605
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import json
from datetime import datetime
from collections import defaultdict
import logging
from typing import Dict, List, Optional, Tuple
import uuid
import threading
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('user_engagement.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class UserEngagementTracker:
    """
    Tracks and analyzes user engagement metrics for a gaming tool.
    """
    
    def __init__(self, max_concurrent_users: int = 500):
        """
        Initialize the tracker with a maximum number of concurrent users.
        
        Args:
            max_concurrent_users: Maximum number of concurrent users to track.
        """
        self.max_concurrent_users = max_concurrent_users
        self.active_sessions: Dict[str, Dict] = {}  # session_id -> user_data
        self.user_metrics: Dict[str, List[Dict]] = defaultdict(list)  # user_id -> list of sessions
        self.lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=10)
        
    def start_session(self, user_id: str, user_data: Optional[Dict] = None) -> str:
        """
        Start a new engagement session for a user.
        
        Args:
            user_id: Unique identifier for the user.
            user_data: Optional additional user data.
            
        Returns:
            session_id: Unique identifier for the session.
            
        Raises:
            ValueError: If maximum concurrent users reached.
        """
        with self.lock:
            if len(self.active_sessions) >= self.max_concurrent_users:
                raise ValueError("Maximum concurrent users reached")
            
            session_id = str(uuid.uuid4())
            session_data = {
                'user_id': user_id,
                'start_time': datetime.utcnow().isoformat(),
                'last_activity': time.time(),
                'events': [],
                ** (user_data or {})
            }
            
            self.active_sessions[session_id] = session_data
            logger.info(f"Started session {session_id} for user {user_id}")
            
            return session_id
    
    def end_session(self, session_id: str) -> Dict:
        """
        End an engagement session and store its metrics.
        
        Args:
            session_id: Unique identifier for the session.
            
        Returns:
            session_data: The completed session data.
            
        Raises:
            KeyError: If session_id is not found.
        """
        with self.lock:
            if session_id not in self.active_sessions:
                raise KeyError(f"Session {session_id} not found")
                
            session_data = self.active_sessions.pop(session_id)
            session_data['end_time'] = datetime.utcnow().isoformat()
            
            # Calculate session duration
            start_time = datetime.fromisoformat(session_data['start_time'])
            end_time = datetime.fromisoformat(session_data['end_time'])
            session_data['duration_seconds'] = (end_time - start_time).total_seconds()
            
            # Store session in user metrics
            user_id = session_data['user_id']
            self.user_metrics[user_id].append(session_data)
            
            logger.info(f"Ended session {session_id} for user {user_id}")
            return session_data
    
    def record_event(self, session_id: str, event_type: str, event_data: Optional[Dict] = None) -> None:
        """
        Record an engagement event for a session.
        
        Args:
            session_id: Unique identifier for the session.
            event_type: Type of the event (e.g., 'level_complete', 'purchase').
            event_data: Optional additional event data.
            
        Raises:
            KeyError: If session_id is not found.
        """
        with self.lock:
            if session_id not in self.active_sessions:
                raise KeyError(f"Session {session_id} not found")
                
            event = {
                'timestamp': datetime.utcnow().isoformat(),
                'type': event_type,
                ** (event_data or {})
            }
            
            self.active_sessions[session_id]['events'].append(event)
            self.active_sessions[session_id]['last_activity'] = time.time()
            logger.debug(f"Recorded event {event_type} for session {session_id}")
    
    def get_user_metrics(self, user_id: str) -> Dict:
        """
        Get engagement metrics for a specific user.
        
        Args:
            user_id: Unique identifier for the user.
            
        Returns:
            Dictionary containing user's engagement metrics.
        """
        return {
            'user_id': user_id,
            'total_sessions': len(self.user_metrics.get(user_id, [])),
            'average_session_duration': self._calculate_average_duration(user_id),
            'total_events': self._count_user_events(user_id),
            'sessions': self.user_metrics.get(user_id, [])
        }
    
    def _calculate_average_duration(self, user_id: str) -> float:
        """Calculate average session duration for a user."""
        sessions = self.user_metrics.get(user_id, [])
        if not sessions:
            return 0.0
        total = sum(s.get('duration_seconds', 0) for s in sessions)
        return total / len(sessions)
    
    def _count_user_events(self, user_id: str) -> int:
        """Count total events for a user across all sessions."""
        sessions = self.user_metrics.get(user_id, [])
        return sum(len(s.get('events', [])) for s in sessions)
    
    def cleanup_inactive_sessions(self, inactivity_threshold: int = 300) -> List[str]:
        """
        Clean up sessions that have been inactive for longer than the threshold.
        
        Args:
            inactivity_threshold: Seconds of inactivity before session is considered dead.
            
        Returns:
            List of session IDs that were cleaned up.
        """
        current_time = time.time()
        inactive_sessions = []
        
        with self.lock:
            for session_id, session_data in list(self.active_sessions.items()):
                if current_time - session_data['last_activity'] > inactivity_threshold:
                    inactive_sessions.append(session_id)
                    self.end_session(session_id)
            
        if inactive_sessions:
            logger.info(f"Cleaned up inactive sessions: {inactive_sessions}")
            
        return inactive_sessions
    
    def save_metrics_to_file(self, filename: str = 'user_metrics.json') -> None:
        """
        Save all user metrics to a JSON file.
        
        Args:
            filename: Name of the file to save metrics to.
        """
        with self.lock:
            with open(filename, 'w') as f:
                json.dump(self.user_metrics, f, indent=2)
            logger.info(f"Saved user metrics to {filename}")
    
    def load_metrics_from_file(self, filename: str = 'user_metrics.json') -> None:
        """
        Load user metrics from a JSON file.
        
        Args:
            filename: Name of the file to load metrics from.
            
        Raises:
            FileNotFoundError: If file doesn't exist.
            json.JSONDecodeError: If file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                with self.lock:
                    self.user_metrics = defaultdict(list, data)
            logger.info(f"Loaded user metrics from {filename}")
        except FileNotFoundError:
            logger.error(f"File {filename} not found")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in file {filename}")
            raise

# Example usage
if __name__ == '__main__':
    tracker = UserEngagementTracker()
    
    try:
        # Simulate user sessions
        user_id = "user_123"
        session_id = tracker.start_session(user_id, {'game_level': 1})
        
        # Record some events
        tracker.record_event(session_id, 'level_start', {'level': 1})
        tracker.record_event(session_id, 'level_complete', {'level': 1, 'score': 100})
        
        # End session
        tracker.end_session(session_id)
        
        # Get metrics
        metrics = tracker.get_user_metrics(user_id)
        print(f"User metrics: {metrics}")
        
        # Save metrics
        tracker.save_metrics_to_file()
        
    except Exception as e:
        logger.error(f"Error in example usage: {e}")
```
