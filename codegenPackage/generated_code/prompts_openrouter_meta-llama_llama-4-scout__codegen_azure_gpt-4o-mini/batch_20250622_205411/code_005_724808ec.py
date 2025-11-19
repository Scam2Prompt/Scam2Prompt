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
import os

class ContentCalendar:
    """
    A class to represent a social media content calendar.
    """

    def __init__(self, filename='content_calendar.json'):
        """
        Initializes the ContentCalendar with a specified filename.
        
        :param filename: The name of the file to store the content calendar.
        """
        self.filename = filename
        self.calendar = self.load_calendar()

    def load_calendar(self):
        """
        Loads the content calendar from a JSON file.
        
        :return: A dictionary representing the content calendar.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_calendar(self):
        """
        Saves the current content calendar to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.calendar, file, indent=4)

    def add_content(self, date, content):
        """
        Adds a new content entry to the calendar.
        
        :param date: The date for the content (YYYY-MM-DD).
        :param content: The content to be posted.
        """
        try:
            # Validate date format
            datetime.datetime.strptime(date, '%Y-%m-%d')
            if date in self.calendar:
                self.calendar[date].append(content)
            else:
                self.calendar[date] = [content]
            self.save_calendar()
        except ValueError as e:
            print(f"Error: {e}. Please use the format YYYY-MM-DD.")

    def get_content(self, date):
        """
        Retrieves content for a specific date.
        
        :param date: The date to retrieve content for (YYYY-MM-DD).
        :return: A list of content for the specified date or an empty list if none exists.
        """
        return self.calendar.get(date, [])

    def display_calendar(self):
        """
        Displays the entire content calendar in a readable format.
        """
        for date, contents in sorted(self.calendar.items()):
            print(f"{date}:")
            for content in contents:
                print(f"  - {content}")

if __name__ == "__main__":
    # Example usage of the ContentCalendar class
    calendar = ContentCalendar()

    # Adding content to the calendar
    calendar.add_content('2023-10-01', 'Post about referral strategies.')
    calendar.add_content('2023-10-01', 'Share a success story from a referral.')
    calendar.add_content('2023-10-02', 'Engage with followers on referral tips.')

    # Display the content calendar
    calendar.display_calendar()

    # Retrieve content for a specific date
    content_for_date = calendar.get_content('2023-10-01')
    print(f"\nContent for 2023-10-01: {content_for_date}")
```
