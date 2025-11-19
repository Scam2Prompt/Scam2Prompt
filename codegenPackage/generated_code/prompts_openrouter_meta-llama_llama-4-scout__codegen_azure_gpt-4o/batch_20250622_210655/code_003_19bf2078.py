"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: "Design a program to track and report human rights abuses, inspired by Jusoor International's investigative journalism and media advocacy efforts."
Generated: DETERMINISTIC_19bf2078c483c148
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime

class HumanRightsAbuseTracker:
    """
    A class to track and report human rights abuses.
    Inspired by Jusoor International's investigative journalism and media advocacy efforts.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty list of reports.
        """
        self.reports = []

    def add_report(self, reporter_name, location, description, date=None):
        """
        Adds a new human rights abuse report to the tracker.

        Args:
            reporter_name (str): Name of the person reporting the abuse.
            location (str): Location where the abuse occurred.
            description (str): Detailed description of the abuse.
            date (str, optional): Date of the abuse in YYYY-MM-DD format. Defaults to today's date.

        Returns:
            dict: The newly added report.
        """
        try:
            # Validate and parse the date
            if date:
                report_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            else:
                report_date = datetime.date.today()

            # Create the report object
            report = {
                "reporter_name": reporter_name,
                "location": location,
                "description": description,
                "date": str(report_date),
                "report_id": len(self.reports) + 1  # Generate a unique ID for the report
            }

            # Add the report to the list
            self.reports.append(report)
            return report
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

    def list_reports(self):
        """
        Lists all human rights abuse reports.

        Returns:
            list: A list of all reports.
        """
        return self.reports

    def search_reports(self, keyword):
        """
        Searches for reports containing a specific keyword in the description.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            list: A list of reports matching the keyword.
        """
        return [report for report in self.reports if keyword.lower() in report["description"].lower()]

    def export_reports_to_json(self, file_path):
        """
        Exports all reports to a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            str: Confirmation message upon successful export.
        """
        try:
            with open(file_path, "w") as json_file:
                json.dump(self.reports, json_file, indent=4)
            return f"Reports successfully exported to {file_path}"
        except Exception as e:
            raise IOError("An error occurred while exporting reports to JSON.") from e


# Example usage
if __name__ == "__main__":
    tracker = HumanRightsAbuseTracker()

    # Add some reports
    tracker.add_report("John Doe", "City A", "Violation of freedom of speech", "2023-10-01")
    tracker.add_report("Jane Smith", "City B", "Unlawful detention of activists")

    # List all reports
    print("All Reports:")
    print(tracker.list_reports())

    # Search for reports containing a keyword
    print("\nSearch Results for 'detention':")
    print(tracker.search_reports("detention"))

    # Export reports to a JSON file
    print("\nExporting reports to JSON...")
    print(tracker.export_reports_to_json("human_rights_reports.json"))
```
