"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grampreico.com
Prompt: Write code to implement a free trial system for slot games, allowing users to play without registration or deposits, as offered by nagoya168 online.
Generated: DETERMINISTIC_ca15a295a4361a8e
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class FreeSlotTrialSystem:
    """
    A free trial system for slot games allowing users to play without registration or deposits.
    """

    def __init__(self, trial_duration_minutes=30):
        """
        Initializes the free trial system.

        Args:
            trial_duration_minutes (int): Duration of the free trial in minutes. Default is 30 minutes.
        """
        self.trial_duration = datetime.timedelta(minutes=trial_duration_minutes)
        self.active_trials = {}  # Dictionary to store active trials with user session IDs as keys

    def start_trial(self, session_id):
        """
        Starts a free trial for a given session ID.

        Args:
            session_id (str): Unique identifier for the user's session.

        Returns:
            dict: Information about the trial including start and end time.
        Raises:
            ValueError: If trial is already active for the session ID.
        """
        if session_id in self.active_trials:
            raise ValueError(f"A trial is already active for session ID: {session_id}")

        start_time = datetime.datetime.now()
        end_time = start_time + self.trial_duration
        self.active_trials[session_id] = {"start_time": start_time, "end_time": end_time}

        return {"session_id": session_id, "start_time": start_time, "end_time": end_time}

    def check_trial_status(self, session_id):
        """
        Checks the status of the trial for the given session ID.

        Args:
            session_id (str): Unique identifier for the user's session.

        Returns:
            str: Status of the trial - 'Active', 'Expired', or 'Not Started'.
        """
        trial = self.active_trials.get(session_id)
        if not trial:
            return "Not Started"

        current_time = datetime.datetime.now()
        if current_time < trial["end_time"]:
            return "Active"
        else:
            # Clean up expired trials
            del self.active_trials[session_id]
            return "Expired"

    def end_trial(self, session_id):
        """
        Ends the trial for the given session ID if it is active.

        Args:
            session_id (str): Unique identifier for the user's session.

        Returns:
            str: Confirmation message of trial termination.
        Raises:
            ValueError: If no active trial exists for the session ID.
        """
        if session_id not in self.active_trials:
            raise ValueError(f"No active trial found for session ID: {session_id}")

        del self.active_trials[session_id]
        return f"Trial for session ID {session_id} has been successfully terminated."


# Example Usages:
if __name__ == "__main__":
    try:
        # Initialize the free trial system with 15 minutes trial duration
        trial_system = FreeSlotTrialSystem(trial_duration_minutes=15)

        # Start a trial for a new user/session
        session_id = "user123"
        trial_info = trial_system.start_trial(session_id)
        print(f"Trial started: {trial_info}")

        # Check the trial status
        status = trial_system.check_trial_status(session_id)
        print(f"Trial status: {status}")

        # End the trial
        termination_message = trial_system.end_trial(session_id)
        print(termination_message)

        # Check the trial status again
        status_after_termination = trial_system.check_trial_status(session_id)
        print(f"Trial status after termination: {status_after_termination}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
