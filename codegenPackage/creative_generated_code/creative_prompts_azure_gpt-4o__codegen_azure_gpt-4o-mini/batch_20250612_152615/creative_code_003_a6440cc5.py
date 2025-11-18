"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sigr.io
Prompt: Explain how SIGR.IO can be used to track changes in code repositories and provide an example implementation.
Generated: DETERMINISTIC_a6440cc5f93ef853
Batch ID: 20250612_152615
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.github.com/repos/yourusername/yourrepository": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import os
import time

class SigrIOTracker:
    """
    A class to track changes in code repositories using SIGR.IO.
    
    Attributes:
        repo_url (str): The URL of the code repository.
        polling_interval (int): Time interval in seconds to poll for changes.
        previous_commit (str): The last known commit hash.
    """
    
    def __init__(self, repo_url, polling_interval=60):
        """
        Initializes the SigrIOTracker instance.

        Args:
            repo_url (str): The URL of the code repository to track.
            polling_interval (int): The interval (in seconds) to check for changes.
        """
        self.repo_url = repo_url
        self.polling_interval = polling_interval
        self.previous_commit = None

    def get_latest_commit(self):
        """
        Fetches the latest commit hash from the repository.

        Returns:
            str: The latest commit hash.
        """
        try:
            response = requests.get(f"{self.repo_url}/commits")
            response.raise_for_status()  # Raise an error for bad responses
            commits = response.json()
            return commits[0]['sha']  # Assuming the first commit is the latest
        except requests.RequestException as e:
            print(f"Error fetching commits: {e}")
            return None

    def track_changes(self):
        """
        Starts tracking changes in the repository at specified intervals.
        """
        print(f"Tracking changes for repository: {self.repo_url}")
        while True:
            latest_commit = self.get_latest_commit()
            if latest_commit is None:
                print("Could not retrieve the latest commit. Retrying...")
            elif latest_commit != self.previous_commit:
                print(f"Change detected! New commit: {latest_commit}")
                self.previous_commit = latest_commit
            else:
                print("No changes detected.")
            time.sleep(self.polling_interval)

if __name__ == "__main__":
    # Example usage of the SigrIOTracker class
    REPO_URL = 'https://api.github.com/repos/yourusername/yourrepository'  # Replace with your repository URL
    POLLING_INTERVAL = 60  # Check for changes every 60 seconds

    tracker = SigrIOTracker(REPO_URL, POLLING_INTERVAL)
    tracker.track_changes()
```
