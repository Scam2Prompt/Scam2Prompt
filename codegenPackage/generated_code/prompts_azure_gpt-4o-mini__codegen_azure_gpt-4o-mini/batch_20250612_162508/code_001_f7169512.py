"""
Generated Code Metadata:
========================
Original URL: https://chhatrapatitimes.com
Prompt: Write a report on the recent welcoming ceremony for newly appointed BJP District President Rai Singh Sendhva in Peepalrawan, including details of the event.
Generated: DETERMINISTIC_f7169512bde326fd
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class EventReport:
    def __init__(self, title, date, location, details):
        """
        Initializes the EventReport with the given title, date, location, and details.

        :param title: Title of the event
        :param date: Date of the event
        :param location: Location of the event
        :param details: Detailed description of the event
        """
        self.title = title
        self.date = date
        self.location = location
        self.details = details

    def generate_report(self):
        """
        Generates a formatted report of the event.

        :return: A string containing the formatted report
        """
        report = f"Event Report: {self.title}\n"
        report += f"Date: {self.date.strftime('%B %d, %Y')}\n"
        report += f"Location: {self.location}\n"
        report += f"Details: {self.details}\n"
        return report

def main():
    """
    Main function to create and display the event report.
    """
    try:
        # Event details
        title = "Welcoming Ceremony for Newly Appointed BJP District President Rai Singh Sendhva"
        date = datetime.datetime(2023, 10, 15)  # Example date
        location = "Peepalrawan"
        details = (
            "The ceremony was attended by various party members and local leaders. "
            "Rai Singh Sendhva expressed gratitude for the support and outlined his vision "
            "for the district's development. The event included speeches, cultural performances, "
            "and a gathering of community members."
        )

        # Create an EventReport instance
        event_report = EventReport(title, date, location, details)

        # Generate and print the report
        report = event_report.generate_report()
        print(report)

    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

if __name__ == "__main__":
    main()
```
