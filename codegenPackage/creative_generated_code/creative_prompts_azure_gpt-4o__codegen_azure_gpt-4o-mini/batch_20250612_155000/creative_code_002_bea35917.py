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
import json
import os
from datetime import datetime
from collections import defaultdict

class DownloadHistory:
    """
    A class to track and log download history for extensions accessed via Crx搜搜.
    The history includes metadata such as download count and timestamps.
    """

    def __init__(self, history_file='download_history.json'):
        """
        Initializes the DownloadHistory object, loading existing history from a file.

        :param history_file: Path to the JSON file where download history is stored.
        """
        self.history_file = history_file
        self.history = defaultdict(list)
        self.load_history()

    def load_history(self):
        """
        Loads download history from the specified JSON file.
        If the file does not exist, initializes an empty history.
        """
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as file:
                    self.history = json.load(file)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading history: {e}")
                self.history = defaultdict(list)

    def log_download(self, extension_id):
        """
        Logs a download event for a given extension ID, updating the count and timestamp.

        :param extension_id: The unique identifier for the downloaded extension.
        """
        timestamp = datetime.now().isoformat()
        self.history[extension_id].append(timestamp)
        self.save_history()

    def save_history(self):
        """
        Saves the current download history to the JSON file.
        Ensures that the data is written in a readable format.
        """
        try:
            with open(self.history_file, 'w') as file:
                json.dump(self.history, file, indent=4)
        except IOError as e:
            print(f"Error saving history: {e}")

    def get_download_count(self, extension_id):
        """
        Retrieves the download count for a given extension ID.

        :param extension_id: The unique identifier for the downloaded extension.
        :return: The number of times the extension has been downloaded.
        """
        return len(self.history.get(extension_id, []))

    def get_download_history(self, extension_id):
        """
        Retrieves the download history (timestamps) for a given extension ID.

        :param extension_id: The unique identifier for the downloaded extension.
        :return: A list of timestamps indicating when the extension was downloaded.
        """
        return self.history.get(extension_id, [])

# Example usage:
if __name__ == "__main__":
    downloader = DownloadHistory()

    # Log a download event for a sample extension ID
    downloader.log_download("example-extension-id")

    # Retrieve and print download count and history for the sample extension ID
    print(f"Download count: {downloader.get_download_count('example-extension-id')}")
    print("Download history:", downloader.get_download_history("example-extension-id"))
```
