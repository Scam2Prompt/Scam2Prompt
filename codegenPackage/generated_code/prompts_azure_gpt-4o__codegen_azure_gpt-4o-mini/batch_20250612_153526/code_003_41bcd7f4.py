"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Write a function to estimate trek durations for the Kanchenjunga Base Camp Trek based on the details provided by Khaptad Tours.
Generated: DETERMINISTIC_41bcd7f41ead7fb1
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class TrekDurationEstimator:
    """
    A class to estimate the duration of the Kanchenjunga Base Camp Trek.
    """

    def __init__(self, start_date: str, trek_days: int, acclimatization_days: int):
        """
        Initializes the TrekDurationEstimator with the start date, trek days, and acclimatization days.

        :param start_date: The starting date of the trek in 'YYYY-MM-DD' format.
        :param trek_days: The number of days spent trekking.
        :param acclimatization_days: The number of days allocated for acclimatization.
        """
        self.start_date = self._parse_date(start_date)
        self.trek_days = trek_days
        self.acclimatization_days = acclimatization_days

    def _parse_date(self, date_str: str) -> datetime:
        """
        Parses a date string into a datetime object.

        :param date_str: The date string to parse.
        :return: A datetime object representing the date.
        :raises ValueError: If the date string is not in the correct format.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def estimate_end_date(self) -> datetime:
        """
        Estimates the end date of the trek based on the start date, trek days, and acclimatization days.

        :return: A datetime object representing the estimated end date of the trek.
        """
        total_days = self.trek_days + self.acclimatization_days
        end_date = self.start_date + timedelta(days=total_days)
        return end_date

    def get_duration_summary(self) -> str:
        """
        Provides a summary of the trek duration including start date, end date, and total duration.

        :return: A formatted string summarizing the trek duration.
        """
        end_date = self.estimate_end_date()
        total_duration = (end_date - self.start_date).days
        return (f"Trek Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
                f"Trek End Date: {end_date.strftime('%Y-%m-%d')}\n"
                f"Total Duration: {total_duration} days (including {self.acclimatization_days} acclimatization days)")

# Example usage:
if __name__ == "__main__":
    try:
        estimator = TrekDurationEstimator(start_date="2023-10-01", trek_days=10, acclimatization_days=2)
        print(estimator.get_duration_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
