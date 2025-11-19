"""
Generated Code Metadata:
========================
Original URL: https://kossto.com
Prompt: Generate a Python script that utilizes the Kossto orthopedic memory foam coccyx seat cushion for tailbone pain relief in a home office setup.
Generated: DETERMINISTIC_80e9851aa88612a5
Batch ID: 20250612_161353
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
import os

class KosstoCushionMonitor:
    """
    A class to monitor and manage the Kossto orthopedic memory foam coccyx seat cushion usage.
    Helps track sitting duration, posture, and provides reminders for breaks.
    """
    
    def __init__(self, user_settings=None):
        """
        Initialize the cushion monitor with user settings.
        
        Args:
            user_settings (dict, optional): Dictionary containing user preferences. Defaults to None.
        """
        self.default_settings = {
            'max_sitting_duration': 50,  # minutes
            'break_duration': 10,       # minutes
            'posture_check_interval': 15,  # minutes
            'data_log_path': 'kossto_cushion_logs.json'
        }
        
        self.settings = {**self.default_settings, **(user_settings or {})}
        self.session_start = None
        self.last_posture_check = None
        self.usage_data = []
        
        # Ensure log directory exists
        os.makedirs(os.path.dirname(self.settings['data_log_path']), exist_ok=True)
        
    def start_session(self):
        """Start a new sitting session with the Kossto cushion."""
        if self.session_start is not None:
            print("Warning: Session already in progress. Use end_session() first.")
            return False
        
        self.session_start = datetime.now()
        self.last_posture_check = self.session_start
        print(f"Session started at {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}")
        return True
    
    def end_session(self):
        """End the current sitting session and log the data."""
        if self.session_start is None:
            print("No active session to end.")
            return False
        
        session_end = datetime.now()
        duration = (session_end - self.session_start).total_seconds() / 60  # in minutes
        
        session_data = {
            'start_time': self.session_start.strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': session_end.strftime('%Y-%m-%d %H:%M:%S'),
            'duration_minutes': round(duration, 2),
            'posture_checks': len(self.usage_data)
        }
        
        self._save_session_data(session_data)
        self.session_start = None
        self.last_posture_check = None
        print(f"Session ended. Duration: {round(duration, 2)} minutes")
        return True
    
    def check_posture(self):
        """Check and record posture during the session."""
        if self.session_start is None:
            print("No active session. Start a session first.")
            return False
        
        current_time = datetime.now()
        time_since_last_check = (current_time - self.last_posture_check).total_seconds() / 60
        
        if time_since_last_check < self.settings['posture_check_interval']:
            print(f"Next posture check in {round(self.settings['posture_check_interval'] - time_since_last_check, 1)} minutes")
            return False
        
        posture_data = {
            'timestamp': current_time.strftime('%Y-%m-%d %H:%M:%S'),
            'message': "Posture check: Ensure proper alignment with the coccyx cutout"
        }
        
        self.usage_data.append(posture_data)
        self.last_posture_check = current_time
        print("Posture checked and recorded. Remember to sit upright with proper lumbar support.")
        return True
    
    def check_break_needed(self):
        """Check if a break is needed based on sitting duration."""
        if self.session_start is None:
            return False
        
        current_duration = (datetime.now() - self.session_start).total_seconds() / 60
        if current_duration >= self.settings['max_sitting_duration']:
            print(f"Break needed! You've been sitting for {round(current_duration, 1)} minutes.")
            return True
        return False
    
    def _save_session_data(self, session_data):
        """Save session data to the log file."""
        try:
            existing_data = []
            if os.path.exists(self.settings['data_log_path']):
                with open(self.settings['data_log_path'], 'r') as f:
                    existing_data = json.load(f)
            
            existing_data.append(session_data)
            
            with open(self.settings['data_log_path'], 'w') as f:
                json.dump(existing_data, f, indent=2)
                
        except Exception as e:
            print(f"Error saving session data: {str(e)}")
    
    def get_usage_summary(self):
        """Retrieve and display summary of cushion usage."""
        if not os.path.exists(self.settings['data_log_path']):
            print("No usage data available yet.")
            return None
        
        try:
            with open(self.settings['data_log_path'], 'r') as f:
                data = json.load(f)
                
            total_sessions = len(data)
            total_duration = sum(session['duration_minutes'] for session in data)
            avg_duration = total_duration / total_sessions if total_sessions > 0 else 0
            
            summary = {
                'total_sessions': total_sessions,
                'total_duration_minutes': round(total_duration, 2),
                'average_duration_minutes': round(avg_duration, 2),
                'last_session': data[-1] if total_sessions > 0 else None
            }
            
            print("\nKossto Cushion Usage Summary:")
            print(f"Total Sessions: {summary['total_sessions']}")
            print(f"Total Sitting Time: {summary['total_duration_minutes']} minutes")
            print(f"Average Session: {summary['average_duration_minutes']} minutes")
            
            return summary
            
        except Exception as e:
            print(f"Error loading usage data: {str(e)}")
            return None


def main():
    """Main function to demonstrate the Kossto cushion monitoring."""
    # Initialize with custom settings
    settings = {
        'max_sitting_duration': 45,
        'break_duration': 5,
        'posture_check_interval': 20
    }
    
    monitor = KosstoCushionMonitor(settings)
    
    # Start a session
    monitor.start_session()
    
    try:
        # Simulate a work session with posture checks
        for _ in range(3):
            time.sleep(5)  # Simulate 5 minutes of work
            monitor.check_posture()
            
            if monitor.check_break_needed():
                print("Time to take a break and stretch!")
                break
                
    except KeyboardInterrupt:
        print("\nSession interrupted by user.")
    finally:
        # End the session
        monitor.end_session()
        monitor.get_usage_summary()


if __name__ == "__main__":
    main()
```
