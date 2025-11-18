"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Write code to implement a notification system that alerts healthcare professionals about new job openings matching their profile in real-time.
Generated: DETERMINISTIC_17a7990c4c2ce192
Batch ID: 20250612_153224
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
import threading
import time
from typing import List, Dict, Callable


class NotificationSystem:
    """
    A notification system for alerting healthcare professionals about new job openings matching their profile.
    """

    def __init__(self):
        """
        Initialize the notification system with empty job postings and user subscriptions.
        """
        self.job_postings = []  # List to store job postings
        self.subscriptions = {}  # Dictionary to store user subscriptions
        self.lock = threading.Lock()  # Thread lock for safe concurrency

    def subscribe_user(self, user_id: str, profile_keywords: List[str], callback: Callable[[Dict], None]):
        """
        Subscribe a healthcare professional to receive notifications for job openings matching their profile.

        Args:
            user_id (str): Unique identifier for the user.
            profile_keywords (List[str]): Keywords describing the user's professional profile.
            callback (Callable[[Dict], None]): Function to call when a matching job is found.
        """
        with self.lock:
            self.subscriptions[user_id] = {
                "keywords": profile_keywords,
                "callback": callback
            }
            print(f"User {user_id} successfully subscribed.")

    def add_job_posting(self, job_id: str, job_title: str, job_description: str, job_location: str):
        """
        Add a new job posting to the system.

        Args:
            job_id (str): Unique identifier for the job.
            job_title (str): Title of the job.
            job_description (str): Description of the job.
            job_location (str): Location of the job.
        """
        job = {
            "job_id": job_id,
            "job_title": job_title,
            "job_description": job_description,
            "job_location": job_location,
            "timestamp": datetime.datetime.now().isoformat()
        }
        with self.lock:
            self.job_postings.append(job)
            print(f"Job posting {job_id} added.")
            self.notify_users(job)

    def notify_users(self, job: Dict):
        """
        Notify subscribed users about a new job posting if it matches their profile.

        Args:
            job (Dict): A dictionary representing the job posting.
        """
        for user_id, subscription in self.subscriptions.items():
            keywords = subscription["keywords"]
            callback = subscription["callback"]

            # Check if job description or title contains any of the profile keywords
            if any(keyword.lower() in (job["job_description"] + job["job_title"]).lower() for keyword in keywords):
                try:
                    callback(job)
                except Exception as e:
                    print(f"Error notifying user {user_id}: {e}")

    def fetch_job_postings(self) -> List[Dict]:
        """
        Fetch all job postings in the system.

        Returns:
            List[Dict]: A list of job postings.
        """
        with self.lock:
            return self.job_postings.copy()


# Example usage
def example_callback(job):
    """
    A sample callback function to simulate user notification.
    
    Args:
        job (Dict): The job posting details.
    """
    print(f"Notification received! New job posted: {json.dumps(job, indent=2)}")


def main():
    """
    Main function to demonstrate the notification system in action.
    """
    # Create the notification system
    system = NotificationSystem()

    # Subscribe users
    system.subscribe_user(
        user_id="user_1",
        profile_keywords=["nurse", "healthcare", "hospital"],
        callback=example_callback
    )
    system.subscribe_user(
        user_id="user_2",
        profile_keywords=["doctor", "surgeon"],
        callback=example_callback
    )

    # Add job postings
    system.add_job_posting(
        job_id="job_101",
        job_title="Nurse Position Available",
        job_description="Looking for experienced nurses to join our hospital.",
        job_location="New York"
    )

    system.add_job_posting(
        job_id="job_102",
        job_title="Surgeon Needed",
        job_description="Seeking skilled surgeons for a private healthcare facility in LA.",
        job_location="Los Angeles"
    )

    # Fetch all job postings
    print("All job postings:")
    for job in system.fetch_job_postings():
        print(json.dumps(job, indent=2))


if __name__ == "__main__":
    # Run the main function in a separate thread (simulates real-time behavior)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
```
