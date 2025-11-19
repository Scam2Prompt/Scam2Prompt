"""
Generated Code Metadata:
========================
Original URL: https://agora-next-m1q953hrk-voteagora.vercel.app
Prompt: Generate a script to track updates from the Optimism Agora changelog using GitHub API integration.
Generated: DETERMINISTIC_a80668bcd0ba8b27
Batch ID: 20250612_151347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.github.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
import time
from datetime import datetime

# Constants
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "OptimismPBC"
REPO_NAME = "agora"
CHANGELOG_FILE_PATH = "CHANGELOG.md"
CHECK_INTERVAL = 3600  # Check every hour

def get_latest_changelog_entry():
    """
    Fetch the latest changelog entry from the GitHub repository.
    
    Returns:
        str: The latest changelog entry or None if not found.
    """
    try:
        # Fetch the changelog file from the repository
        response = requests.get(f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{CHANGELOG_FILE_PATH}")
        response.raise_for_status()  # Raise an error for bad responses

        # Decode the content from base64
        content = json.loads(response.text)
        changelog_content = base64.b64decode(content['content']).decode('utf-8')

        # Split the changelog into entries and return the latest one
        entries = changelog_content.splitlines()
        latest_entry = entries[0] if entries else None
        return latest_entry

    except requests.exceptions.RequestException as e:
        print(f"Error fetching changelog: {e}")
        return None

def track_updates():
    """
    Track updates in the changelog by periodically checking for new entries.
    """
    last_entry = None

    while True:
        print(f"Checking for updates at {datetime.now()}...")
        latest_entry = get_latest_changelog_entry()

        if latest_entry and latest_entry != last_entry:
            print(f"New changelog entry found: {latest_entry}")
            last_entry = latest_entry

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    track_updates()
```

Make sure to install the required libraries if you haven't already:

```bash
pip install requests
```
