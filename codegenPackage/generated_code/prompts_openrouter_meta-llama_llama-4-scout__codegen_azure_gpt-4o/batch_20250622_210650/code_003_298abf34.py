"""
Generated Code Metadata:
========================
Original URL: https://dalilamedeiros.com
Prompt: Create a social media content calendar for a sales mentor targeting entrepreneurs on TikTok, Kwai, Pinterest, and YouTube.
Generated: DETERMINISTIC_298abf3425c59226
Batch ID: 20250622_210650
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

# Define the platforms and content types
PLATFORMS = ["TikTok", "Kwai", "Pinterest", "YouTube"]
CONTENT_TYPES = ["Motivational Video", "Sales Tips", "Entrepreneurial Advice", "Success Stories"]

# Function to generate a content calendar
def generate_content_calendar(start_date, num_days):
    """
    Generates a social media content calendar for the specified number of days.

    Args:
        start_date (str): The start date in the format 'YYYY-MM-DD'.
        num_days (int): The number of days to generate content for.

    Returns:
        dict: A dictionary representing the content calendar.
    """
    try:
        # Parse the start date
        current_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

    content_calendar = {}

    for day in range(num_days):
        daily_schedule = {}
        for platform in PLATFORMS:
            # Randomly assign a content type to each platform
            content_type = CONTENT_TYPES[day % len(CONTENT_TYPES)]
            daily_schedule[platform] = {
                "date": current_date.strftime("%Y-%m-%d"),
                "content_type": content_type,
                "description": f"Post a {content_type.lower()} on {platform}."
            }
        content_calendar[current_date.strftime("%Y-%m-%d")] = daily_schedule
        current_date += datetime.timedelta(days=1)

    return content_calendar

# Function to save the content calendar to a JSON file
def save_calendar_to_file(calendar, filename):
    """
    Saves the content calendar to a JSON file.

    Args:
        calendar (dict): The content calendar to save.
        filename (str): The name of the file to save the calendar to.
    """
    try:
        with open(filename, "w") as file:
            json.dump(calendar, file, indent=4)
    except IOError as e:
        raise IOError("Failed to save the calendar to file.") from e

# Main function
def main():
    """
    Main function to generate and save the social media content calendar.
    """
    try:
        # User inputs
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        num_days = int(input("Enter the number of days to generate content for: "))
        filename = input("Enter the filename to save the calendar (e.g., 'content_calendar.json'): ")

        # Generate the content calendar
        calendar = generate_content_calendar(start_date, num_days)

        # Save the calendar to a file
        save_calendar_to_file(calendar, filename)

        print(f"Content calendar successfully saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
```
