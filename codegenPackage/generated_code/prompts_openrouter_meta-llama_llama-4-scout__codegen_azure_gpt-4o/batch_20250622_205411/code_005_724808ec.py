"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Develop a social media content calendar using the strategies outlined in Stacey Bront Randall's Growth By Referrals course.
Generated: DETERMINISTIC_724808ec74f1d1b0
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class SocialMediaContentCalendar:
    """
    A class to manage a social media content calendar based on Stacey Bront Randall's Growth By Referrals strategies.
    """

    def __init__(self):
        """
        Initialize the content calendar with an empty schedule.
        """
        self.schedule = {}

    def add_post(self, date, platform, content):
        """
        Add a post to the content calendar.

        Args:
            date (str): The date of the post in 'YYYY-MM-DD' format.
            platform (str): The social media platform (e.g., 'Facebook', 'Twitter').
            content (str): The content of the post.

        Raises:
            ValueError: If the date format is invalid or content is empty.
        """
        try:
            # Validate date format
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

        if not content.strip():
            raise ValueError("Content cannot be empty.")

        # Add post to the schedule
        if date not in self.schedule:
            self.schedule[date] = []
        self.schedule[date].append({"platform": platform, "content": content})

    def view_schedule(self):
        """
        View the entire content calendar.

        Returns:
            dict: The content calendar schedule.
        """
        return self.schedule

    def save_to_file(self, filename):
        """
        Save the content calendar to a JSON file.

        Args:
            filename (str): The name of the file to save the schedule.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Load the content calendar from a JSON file.

        Args:
            filename (str): The name of the file to load the schedule from.

        Raises:
            IOError: If the file cannot be read.
        """
        try:
            with open(filename, 'r') as file:
                self.schedule = json.load(file)
        except IOError as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    calendar = SocialMediaContentCalendar()

    # Add posts to the calendar
    try:
        calendar.add_post("2023-10-01", "Facebook", "Share a referral success story.")
        calendar.add_post("2023-10-02", "Twitter", "Tweet about the importance of referrals.")
        calendar.add_post("2023-10-03", "LinkedIn", "Post a case study highlighting referral growth.")
    except ValueError as e:
        print(f"Error adding post: {e}")

    # View the schedule
    print("Current Schedule:")
    print(calendar.view_schedule())

    # Save the schedule to a file
    calendar.save_to_file("content_calendar.json")

    # Load the schedule from a file
    calendar.load_from_file("content_calendar.json")
    print("Loaded Schedule:")
    print(calendar.view_schedule())
```
