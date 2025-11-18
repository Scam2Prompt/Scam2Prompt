"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportify.club
Prompt: Generate code to implement a cloud DVR feature for a sports streaming service, allowing users to store up to 1000 hours of recorded content, as described on Sportify.Club.
Generated: DETERMINISTIC_ba2bd4aee6793d46
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os

class CloudDVR:
    MAX_RECORDING_HOURS = 1000
    MAX_RECORDING_SECONDS = MAX_RECORDING_HOURS * 3600

    def __init__(self, storage_path='./recordings'):
        """
        Initializes the CloudDVR with a specified storage path.
        """
        self.storage_path = storage_path
        self.recordings = []
        self.load_recordings()

    def load_recordings(self):
        """
        Loads existing recordings from a JSON file.
        """
        try:
            with open(os.path.join(self.storage_path, 'recordings.json'), 'r') as f:
                self.recordings = json.load(f)
        except FileNotFoundError:
            self.recordings = []
        except json.JSONDecodeError:
            print("Warning: Corrupted recordings data. Starting fresh.")
            self.recordings = []

    def save_recordings(self):
        """
        Saves the current recordings to a JSON file.
        """
        os.makedirs(self.storage_path, exist_ok=True)
        with open(os.path.join(self.storage_path, 'recordings.json'), 'w') as f:
            json.dump(self.recordings, f)

    def add_recording(self, title, duration):
        """
        Adds a new recording if the total duration does not exceed the limit.

        :param title: Title of the recording.
        :param duration: Duration of the recording in seconds.
        :raises ValueError: If total recording time exceeds the limit.
        """
        total_duration = sum(record['duration'] for record in self.recordings)

        if total_duration + duration > self.MAX_RECORDING_SECONDS:
            raise ValueError("Cannot add recording. Maximum recording limit reached.")

        recording = {
            'title': title,
            'duration': duration,
            'timestamp': datetime.datetime.now().isoformat()
        }
        self.recordings.append(recording)
        self.save_recordings()

    def list_recordings(self):
        """
        Lists all recordings with their titles and durations.
        """
        if not self.recordings:
            print("No recordings found.")
            return

        for recording in self.recordings:
            print(f"Title: {recording['title']}, Duration: {recording['duration']} seconds")

    def delete_recording(self, title):
        """
        Deletes a recording by title.

        :param title: Title of the recording to delete.
        :raises ValueError: If the recording is not found.
        """
        for recording in self.recordings:
            if recording['title'] == title:
                self.recordings.remove(recording)
                self.save_recordings()
                return
        raise ValueError(f"Recording with title '{title}' not found.")

if __name__ == "__main__":
    dvr = CloudDVR()

    # Example usage
    try:
        dvr.add_recording("Game Highlights", 3600)  # Adding a 1-hour recording
        dvr.add_recording("Post-Game Analysis", 1800)  # Adding a 30-minute recording
        dvr.list_recordings()

        dvr.delete_recording("Game Highlights")  # Deleting a recording
        dvr.list_recordings()
    except ValueError as e:
        print(e)
```
