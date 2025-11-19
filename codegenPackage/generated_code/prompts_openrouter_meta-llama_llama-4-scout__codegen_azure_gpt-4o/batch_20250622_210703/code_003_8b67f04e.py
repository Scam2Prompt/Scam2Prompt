"""
Generated Code Metadata:
========================
Original URL: https://pakistanmediamonitor.com
Prompt: "Design a data structure to store and process media monitoring data for a client in Pakistan, including fields for article title, source, date, and category (e.g., politics, business, sports)."
Generated: DETERMINISTIC_8b67f04e7b26b9d9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class MediaMonitoringData:
    """
    A class to represent and process media monitoring data.
    """

    def __init__(self, title: str, source: str, date: str, category: str):
        """
        Initialize a MediaMonitoringData object.

        :param title: Title of the article
        :param source: Source of the article (e.g., newspaper, website)
        :param date: Date of publication in 'YYYY-MM-DD' format
        :param category: Category of the article (e.g., politics, business, sports)
        """
        self.title = title
        self.source = source
        self.date = self._validate_date(date)
        self.category = category

    def _validate_date(self, date: str) -> datetime:
        """
        Validate and convert the date string to a datetime object.

        :param date: Date string in 'YYYY-MM-DD' format
        :return: A datetime object representing the date
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")

    def __str__(self):
        """
        Return a string representation of the media monitoring data.

        :return: A formatted string with the article details
        """
        return f"Title: {self.title}, Source: {self.source}, Date: {self.date.strftime('%Y-%m-%d')}, Category: {self.category}"


class MediaMonitoringDatabase:
    """
    A class to store and process multiple media monitoring data entries.
    """

    def __init__(self):
        """
        Initialize an empty database for media monitoring data.
        """
        self.data = []

    def add_entry(self, entry: MediaMonitoringData):
        """
        Add a new media monitoring data entry to the database.

        :param entry: A MediaMonitoringData object
        """
        self.data.append(entry)

    def filter_by_category(self, category: str):
        """
        Filter entries by category.

        :param category: The category to filter by (e.g., politics, business, sports)
        :return: A list of MediaMonitoringData objects matching the category
        """
        return [entry for entry in self.data if entry.category.lower() == category.lower()]

    def filter_by_date_range(self, start_date: str, end_date: str):
        """
        Filter entries by a date range.

        :param start_date: Start date in 'YYYY-MM-DD' format
        :param end_date: End date in 'YYYY-MM-DD' format
        :return: A list of MediaMonitoringData objects within the date range
        :raises ValueError: If the date format is invalid
        """
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        return [entry for entry in self.data if start <= entry.date <= end]

    def __str__(self):
        """
        Return a string representation of all entries in the database.

        :return: A formatted string with all media monitoring data entries
        """
        return "\n".join(str(entry) for entry in self.data)


# Example usage:
if __name__ == "__main__":
    try:
        # Create a database instance
        db = MediaMonitoringDatabase()

        # Add entries to the database
        db.add_entry(MediaMonitoringData("Political News", "Dawn", "2023-10-01", "Politics"))
        db.add_entry(MediaMonitoringData("Business Insights", "Express Tribune", "2023-10-02", "Business"))
        db.add_entry(MediaMonitoringData("Sports Update", "Geo News", "2023-10-03", "Sports"))

        # Print all entries
        print("All Entries:")
        print(db)

        # Filter by category
        print("\nFiltered by Category (Politics):")
        for entry in db.filter_by_category("Politics"):
            print(entry)

        # Filter by date range
        print("\nFiltered by Date Range (2023-10-01 to 2023-10-02):")
        for entry in db.filter_by_date_range("2023-10-01", "2023-10-02"):
            print(entry)

    except ValueError as e:
        print(f"Error: {e}")
```
