"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```python
import requests
import json
import sys
import time

# GitHub API base URL
GITHUB_API_URL = "https://api.github.com"

# Repository details for the Optimism Agora changelog
OWNER = "ethereum-optimism"
REPO = "agora-changelog"

# GitHub Personal Access Token (replace with your token or use environment variables for better security)
GITHUB_TOKEN = "your_personal_access_token_here"

# Headers for GitHub API requests
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Function to fetch the latest changelog updates
def fetch_latest_updates():
    """
    Fetches the latest commits from the Optimism Agora changelog repository.
    Returns the list of commits or raises an exception if an error occurs.
    """
    url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/commits"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        return response.json()  # Return JSON response as a Python list
    except requests.exceptions.RequestException as e:
        print(f"Error fetching changelog updates: {e}", file=sys.stderr)
        return None

# Function to display updates in a human-readable format
def display_updates(commits):
    """
    Displays the fetched commits in a human-readable format.
    """
    if not commits:
        print("No updates found or an error occurred.")
        return

    print("\nLatest Updates from Optimism Agora Changelog:\n")
    for commit in commits:
        # Extract relevant fields
        commit_message = commit.get("commit", {}).get("message", "No commit message")
        commit_author = commit.get("commit", {}).get("author", {}).get("name", "Unknown author")
        commit_date = commit.get("commit", {}).get("author", {}).get("date", "Unknown date")
        commit_url = commit.get("html_url", "No URL")

        # Display the commit details
        print(f"- Commit Date: {commit_date}")
        print(f"  Author: {commit_author}")
        print(f"  Message: {commit_message}")
        print(f"  URL: {commit_url}\n")

# Main function to run the script
def main():
    """
    Main entry point for the script. Fetches and displays changelog updates.
    """
    print("Fetching updates from Optimism Agora changelog repository...")
    commits = fetch_latest_updates()  # Fetch the latest commits
    display_updates(commits)          # Display the fetched commits

# Entry point check
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by the user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```

Note: Replace the placeholder `your_personal_access_token_here` with your actual GitHub Personal Access Token. For security, it's recommended to store sensitive information like tokens in environment variables or a secrets manager.
