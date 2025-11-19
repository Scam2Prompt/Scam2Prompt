"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatime.pro
Prompt: Develop a function that simulates the "internal time management" technique described by A. Sheffer, allowing users to track and optimize their personal time usage.
Generated: DETERMINISTIC_6776b63bbb94679b
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class TimeManagementTracker:
    """
    A class to track and optimize personal time usage.
    """

    def __init__(self):
        """
        Initializes the TimeManagementTracker with an empty list of sessions.
        """
        self.sessions = []

    def start_session(self, task_name: str):
        """
        Starts a new time tracking session for a given task.
        
        Args:
            task_name (str): The name of the task being tracked.
        """
        start_time = datetime.now()
        self.sessions.append({'task': task_name, 'start': start_time})
        print(f"Started tracking for task: '{task_name}' at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def end_session(self):
        """
        Ends the most recent time tracking session.
        Raises an error if no session is currently active.
        """
        if not self.sessions:
            raise RuntimeError("No active session to end.")
        
        end_time = datetime.now()
        last_session = self.sessions[-1]
        last_session['end'] = end_time
        last_session['duration'] = (end_time - last_session['start']).total_seconds()
        print(f"Ended tracking for task: '{last_session['task']}' at {end_time.strftime('%Y-%m-%d %H:%M:%S')}, Duration: {last_session['duration']} seconds")

    def get_report(self):
        """
        Generates a report of all tracked sessions.
        
        Returns:
            list: A summary of the tracked sessions, including task names, start/end times, and duration.
        """
        report = []
        for session in self.sessions:
            task_report = {
                'Task': session['task'],
                'Start Time': session['start'].strftime('%Y-%m-%d %H:%M:%S'),
                'End Time': session.get('end', 'Ongoing').strftime('%Y-%m-%d %H:%M:%S') if 'end' in session else 'Ongoing',
                'Duration (seconds)': session.get('duration', 'N/A')
            }
            report.append(task_report)
        
        return report

    def optimize_time(self):
        """
        Analyzes the sessions and provides suggestions to optimize time usage.
        
        Returns:
            str: Suggestions based on time tracking data.
        """
        total_duration = sum(session.get('duration', 0) for session in self.sessions if 'duration' in session)
        task_counts = {}
        
        for session in self.sessions:
            task = session['task']
            task_counts[task] = task_counts.get(task, 0) + 1
        
        suggestions = []
        for task, count in task_counts.items():
            avg_time = total_duration / count if count > 0 else 0
            suggestions.append(f"Task '{task}' was performed {count} times with an average duration of {avg_time:.2f} seconds.")
        
        return "\n".join(suggestions)

# Example usage:
if __name__ == "__main__":
    try:
        tracker = TimeManagementTracker()
        tracker.start_session("Writing Code")
        time.sleep(2)  # Simulate time spent on task
        tracker.end_session()
        
        tracker.start_session("Reviewing Code")
        time.sleep(3)  # Simulate time spent on task
        tracker.end_session()
        
        report = tracker.get_report()
        for entry in report:
            print(entry)
        
        print(tracker.optimize_time())
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
