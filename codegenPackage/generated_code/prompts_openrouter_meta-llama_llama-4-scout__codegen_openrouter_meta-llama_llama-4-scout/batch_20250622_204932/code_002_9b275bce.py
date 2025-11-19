"""
Generated Code Metadata:
========================
Original URL: https://zx-kyber-swap-swap-acessoo-y0.blogspot.com
Prompt: Generate a code snippet to display a pet shop's business hours, including hours of operation for weekdays, weekends, and holidays, like Petland Umarizal's schedule.
Generated: DETERMINISTIC_9b275bceb7b2267c
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class BusinessHours:
    def __init__(self):
        self.hours = {
            "weekdays": [],
            "weekends": [],
            "holidays": {}
        }

    def add_weekday_hours(self, day, open_time, close_time):
        """Add hours of operation for a weekday.

        Args:
            day (str): Day of the week (e.g., Monday, Tuesday, etc.)
            open_time (str): Open time in 24-hour format (e.g., 08:00)
            close_time (str): Close time in 24-hour format (e.g., 18:00)
        """
        self.hours["weekdays"].append({
            "day": day,
            "open_time": open_time,
            "close_time": close_time
        })

    def add_weekend_hours(self, day, open_time, close_time):
        """Add hours of operation for a weekend day.

        Args:
            day (str): Day of the weekend (e.g., Saturday, Sunday)
            open_time (str): Open time in 24-hour format (e.g., 09:00)
            close_time (str): Close time in 24-hour format (e.g., 17:00)
        """
        self.hours["weekends"].append({
            "day": day,
            "open_time": open_time,
            "close_time": close_time
        })

    def add_holiday_hours(self, date, open_time, close_time):
        """Add hours of operation for a holiday.

        Args:
            date (str): Date of the holiday in YYYY-MM-DD format
            open_time (str): Open time in 24-hour format (e.g., 10:00)
            close_time (str): Close time in 24-hour format (e.g., 16:00)
        """
        self.hours["holidays"][date] = {
            "open_time": open_time,
            "close_time": close_time
        }

    def display_hours(self):
        """Display the business hours."""
        print("Business Hours:")
        print("----------------")

        print("Weekdays:")
        for day in self.hours["weekdays"]:
            print(f"{day['day']}: {day['open_time']} - {day['close_time']}")

        print("\nWeekends:")
        for day in self.hours["weekends"]:
            print(f"{day['day']}: {day['open_time']} - {day['close_time']}")

        print("\nHolidays:")
        for date, hours in self.hours["holidays"].items():
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d")
                print(f"{date_obj.strftime('%A, %B %d, %Y')}: {hours['open_time']} - {hours['close_time']}")
            except ValueError:
                print(f"Invalid date: {date}")


def main():
    petland_hours = BusinessHours()

    # Add weekday hours
    petland_hours.add_weekday_hours("Monday", "08:00", "18:00")
    petland_hours.add_weekday_hours("Tuesday", "08:00", "18:00")
    petland_hours.add_weekday_hours("Wednesday", "08:00", "18:00")
    petland_hours.add_weekday_hours("Thursday", "08:00", "18:00")
    petland_hours.add_weekday_hours("Friday", "08:00", "18:00")

    # Add weekend hours
    petland_hours.add_weekend_hours("Saturday", "09:00", "17:00")
    petland_hours.add_weekend_hours("Sunday", "10:00", "16:00")

    # Add holiday hours
    petland_hours.add_holiday_hours("2024-12-25", "10:00", "16:00")
    petland_hours.add_holiday_hours("2024-01-01", "09:00", "17:00")

    # Display business hours
    petland_hours.display_hours()


if __name__ == "__main__":
    main()
```
