"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappbay-bnbchain-org.pages.dev
Prompt: Write a Python script that tracks the completion of tasks for minting the 4YA NFT as described on the DappBay site.
Generated: DETERMINISTIC_3b9adcb593f2677b
Batch ID: 20250612_163958
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dappbay.com/tasks": {
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
import json
import logging
import requests
from datetime import datetime

# Setting up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TaskTracker:
    """
    Class to track the completion of tasks for minting the 4YA NFT.
    """

    def __init__(self, api_url):
        """
        Initializes the TaskTracker with the given API URL.

        Parameters:
        api_url (str): The URL of the API to fetch task data.
        """
        self.api_url = api_url
        self.tasks = []

    def fetch_tasks(self):
        """
        Fetches tasks from the API and stores them in the tasks list.
        Raises an exception if the request fails.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            self.tasks = response.json()  # Assuming the API returns a JSON array of tasks
            logging.info("Tasks successfully fetched from API.")
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")

    def display_tasks(self):
        """
        Displays the list of tasks and their completion status.
        """
        if not self.tasks:
            logging.warning("No tasks available to display.")
            return

        logging.info("Current tasks and their completion statuses:")
        for task in self.tasks:
            task_name = task.get('name', 'Unnamed Task')
            completed = task.get('completed', False)
            completion_status = "Completed" if completed else "Not Completed"
            logging.info(f"Task: {task_name}, Status: {completion_status}")

    def mark_task_completed(self, task_name):
        """
        Marks a task as completed by updating it in the tasks list.

        Parameters:
        task_name (str): The name of the task to mark as completed.
        """
        for task in self.tasks:
            if task.get('name') == task_name:
                task['completed'] = True
                logging.info(f"Task '{task_name}' marked as completed.")
                return
        logging.warning(f"Task '{task_name}' not found.")

def main():
    """
    Main function to run the task tracker.
    """
    api_url = "https://api.dappbay.com/tasks"  # Replace with the actual API URL
    tracker = TaskTracker(api_url)

    # Fetch tasks from the API
    tracker.fetch_tasks()

    # Display fetched tasks
    tracker.display_tasks()

    # Example of marking a task as completed
    tracker.mark_task_completed("Mint 4YA NFT")  # Replace with actual task name

    # Display tasks again to see updated status
    tracker.display_tasks()

if __name__ == "__main__":
    main()
```
