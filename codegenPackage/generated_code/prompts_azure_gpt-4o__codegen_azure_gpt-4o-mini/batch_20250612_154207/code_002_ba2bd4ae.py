"""
Generated Code Metadata:
========================
Original URL: https://sportify.club
Prompt: Generate code to implement a cloud DVR feature for a sports streaming service, allowing users to store up to 1000 hours of recorded content, as described on Sportify.Club.
Generated: DETERMINISTIC_ba2bd4aee6793d46
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Recording:
    """Class representing a single recording."""
    
    def __init__(self, title: str, duration: int, recorded_at: datetime.datetime):
        """
        Initialize a new recording.

        :param title: Title of the recorded content.
        :param duration: Duration of the recording in minutes.
        :param recorded_at: Timestamp when the recording was made.
        """
        self.title = title
        self.duration = duration  # Duration in minutes
        self.recorded_at = recorded_at

    def __str__(self):
        return f"{self.title} ({self.duration} min) - Recorded at {self.recorded_at}"

class CloudDVR:
    """Class representing a cloud DVR for storing recordings."""
    
    MAX_STORAGE_HOURS = 1000  # Maximum storage in hours
    MAX_STORAGE_MINUTES = MAX_STORAGE_HOURS * 60  # Convert hours to minutes

    def __init__(self):
        """Initialize the CloudDVR with an empty list of recordings."""
        self.recordings: List[Recording] = []
        self.total_storage_used: int = 0  # Total storage used in minutes

    def add_recording(self, title: str, duration: int) -> None:
        """
        Add a new recording to the DVR.

        :param title: Title of the recording.
        :param duration: Duration of the recording in minutes.
        :raises ValueError: If the duration is negative or if adding the recording exceeds storage limits.
        """
        if duration < 0:
            raise ValueError("Duration must be a non-negative integer.")
        
        if self.total_storage_used + duration > self.MAX_STORAGE_MINUTES:
            raise ValueError("Cannot add recording: storage limit exceeded.")

        recorded_at = datetime.datetime.now()
        new_recording = Recording(title, duration, recorded_at)
        self.recordings.append(new_recording)
        self.total_storage_used += duration
        print(f"Recording added: {new_recording}")

    def delete_recording(self, title: str) -> None:
        """
        Delete a recording from the DVR by title.

        :param title: Title of the recording to delete.
        :raises ValueError: If the recording is not found.
        """
        for recording in self.recordings:
            if recording.title == title:
                self.recordings.remove(recording)
                self.total_storage_used -= recording.duration
                print(f"Recording deleted: {recording}")
                return
        raise ValueError("Recording not found.")

    def list_recordings(self) -> List[str]:
        """
        List all recordings in the DVR.

        :return: A list of strings representing the recordings.
        """
        return [str(recording) for recording in self.recordings]

    def get_storage_status(self) -> str:
        """
        Get the current storage status of the DVR.

        :return: A string indicating the total storage used and remaining.
        """
        remaining_minutes = self.MAX_STORAGE_MINUTES - self.total_storage_used
        return f"Storage used: {self.total_storage_used} min, Remaining: {remaining_minutes} min"

# Example usage
if __name__ == "__main__":
    dvr = CloudDVR()
    
    try:
        dvr.add_recording("Championship Game", 120)
        dvr.add_recording("Finals Highlights", 90)
        print(dvr.list_recordings())
        print(dvr.get_storage_status())
        
        dvr.delete_recording("Championship Game")
        print(dvr.list_recordings())
        print(dvr.get_storage_status())
        
    except ValueError as e:
        print(f"Error: {e}")
```
