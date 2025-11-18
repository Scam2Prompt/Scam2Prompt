"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Suggest tools and frameworks for creating a content calendar for social media campaigns, as taught in PDMA's Social Media Management course.
Generated: DETERMINISTIC_75d8468e05576492
Batch ID: 20250612_145730
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
from typing import List, Dict

class SocialMediaContentCalendar:
    """
    A class to manage a social media content calendar.
    """

    def __init__(self):
        """Initialize the content calendar with an empty list."""
        self.calendar: List[Dict] = []

    def add_post(self, date: str, platform: str, content: str) -> None:
        """
        Add a new post to the calendar.

        :param date: The date for the post in 'YYYY-MM-DD' format.
        :param platform: The social media platform (e.g., 'Facebook', 'Twitter').
        :param content: The content of the post.
        """
        try:
            # Validate date format
            post_date = datetime.datetime.strptime(date, '%Y-%m-%d')
            self.calendar.append({
                'date': post_date.date().isoformat(),
                'platform': platform,
                'content': content
            })
        except ValueError as e:
            print(f"Error: {e}. Please provide the date in 'YYYY-MM-DD' format.")

    def export_to_json(self, filename: str) -> None:
        """
        Export the content calendar to a JSON file.

        :param filename: The filename to save the calendar as.
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.calendar, json_file, indent=4)
            print(f"Content calendar exported successfully to {filename}.")
        except IOError as e:
            print(f"Error writing to file: {e}")

    def display_calendar(self) -> None:
        """
        Display the content calendar in a readable format.
        """
        if not self.calendar:
            print("The content calendar is empty.")
            return

        for post in self.calendar:
            print(f"{post['date']} - {post['platform']}: {post['content']}")

# Example usage
if __name__ == "__main__":
    content_calendar = SocialMediaContentCalendar()
    
    # Adding sample posts
    content_calendar.add_post("2023-11-01", "Facebook", "Post about new product launch.")
    content_calendar.add_post("2023-11-02", "Twitter", "Excited for our upcoming event!")
    
    # Display the calendar
    content_calendar.display_calendar()
    
    # Export the calendar to JSON
    content_calendar.export_to_json("social_media_calendar.json")
```
