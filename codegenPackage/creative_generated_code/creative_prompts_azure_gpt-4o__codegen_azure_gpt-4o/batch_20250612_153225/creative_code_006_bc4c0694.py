"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budbeeindia.com
Prompt: Create a Python function to schedule social media posts across platforms, referencing BudBee India's insights on traditional vs. digital marketing strategies.
Generated: DETERMINISTIC_bc4c069479dc88cf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Supported platforms for scheduling posts
SUPPORTED_PLATFORMS = ["Facebook", "Twitter", "Instagram", "LinkedIn"]

def schedule_post(platform, content, schedule_time):
    """
    Schedule a social media post for a specific platform.

    Args:
        platform (str): The social media platform to post on (e.g., 'Facebook', 'Twitter').
        content (str): The content of the post.
        schedule_time (datetime.datetime): The scheduled time for the post.

    Returns:
        dict: A dictionary containing the status and details of the scheduled post.

    Raises:
        ValueError: If the platform is not supported or the schedule time is invalid.
    """
    try:
        # Validate platform
        if platform not in SUPPORTED_PLATFORMS:
            raise ValueError(f"Unsupported platform. Supported platforms are: {SUPPORTED_PLATFORMS}")

        # Validate schedule time
        if not isinstance(schedule_time, datetime.datetime):
            raise ValueError("schedule_time must be a datetime object.")
        if schedule_time <= datetime.datetime.now():
            raise ValueError("Schedule time must be in the future.")

        # Log the scheduling action
        logging.info(f"Scheduling post on {platform} at {schedule_time}. Content: {content[:30]}...")

        # Simulate scheduling the post
        # In a real-world scenario, this would involve calling APIs of the respective platforms
        scheduled_post = {
            "platform": platform,
            "content": content,
            "schedule_time": schedule_time,
            "status": "Scheduled"
        }

        # Log success
        logging.info(f"Post scheduled successfully on {platform} at {schedule_time}.")
        return scheduled_post
    
    except Exception as e:
        # Log the error with details
        logging.error(f"Failed to schedule post. Error: {str(e)}")
        raise

# Example usage of the function
if __name__ == "__main__":
    try:
        # Define post details
        platform = "Twitter"
        content = "Traditional marketing focuses on offline activities. Digital marketing leverages online platforms for targeted outreach. Learn more from BudBee India's insights!"
        schedule_time = datetime.datetime.now() + datetime.timedelta(hours=1)

        # Schedule the post
        post = schedule_post(platform, content, schedule_time)
        print("Scheduled Post Details:", post)

    except Exception as e:
        print("Error:", str(e))
```
