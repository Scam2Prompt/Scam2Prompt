"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crxsoso.com
Prompt: Create a function to track and log download history for extensions accessed via Crx搜搜, including metadata like download count and timestamps.
Generated: DETERMINISTIC_bea35917a91c1610
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

class DownloadHistoryTracker:
    def __init__(self, log_file='download_history.json'):
        """
        Initializes the tracker with a log file to store download history.

        :param log_file: The path to the JSON file used to store download history.
        """
        self.log_file = log_file
        self._initialize_log_file()

    def _initialize_log_file(self):
        """
        Ensures the log file exists and initializes it if it does not.
        """
        if not os.path.exists(self.log_file):
            # Create an empty JSON structure if log file doesn't exist
            with open(self.log_file, 'w') as file:
                json.dump({}, file)

    def log_download(self, extension_name):
        """
        Logs a download event for a given extension.

        :param extension_name: The name of the extension being downloaded.
        """
        try:
            # Read the existing log file
            with open(self.log_file, 'r') as file:
                data = json.load(file)

            # Get current timestamp
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Update extension metadata
            if extension_name in data:
                data[extension_name]['download_count'] += 1
                data[extension_name]['timestamps'].append(current_time)
            else:
                data[extension_name] = {
                    'download_count': 1,
                    'timestamps': [current_time]
                }

            # Write updated data back to log file
            with open(self.log_file, 'w') as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            # Handle any file or JSON errors gracefully
            print(f"Error logging download: {e}")

    def get_download_history(self):
        """
        Retrieves the download history from the log file.

        :return: A dictionary containing the download history.
        """
        try:
            with open(self.log_file, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error retrieving download history: {e}")
            return {}

# Example usage:
if __name__ == "__main__":
    tracker = DownloadHistoryTracker()

    # Log downloads
    tracker.log_download('ExtensionA')
    tracker.log_download('ExtensionB')
    tracker.log_download('ExtensionA')  # Log a second download for ExtensionA

    # Retrieve and print download history
    history = tracker.get_download_history()
    print(json.dumps(history, indent=4))
```
