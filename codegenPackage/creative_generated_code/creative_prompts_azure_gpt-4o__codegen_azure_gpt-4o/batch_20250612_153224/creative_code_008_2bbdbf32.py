"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gesec.com.co
Prompt: Write a Python script to calculate and track key safety indicators for reducing workplace incidents, following GESEC's methodology for improving organizational processes.
Generated: DETERMINISTIC_2bbdbf32fb3b0499
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SafetyIndicatorsTracker:
    """
    A class to calculate and track key safety indicators using GESEC's methodology.
    """

    def __init__(self):
        """
        Initializes the SafetyIndicatorsTracker with empty data structures to store incident data.
        """
        self.incidents = []  # List to store incident records
        self.total_working_hours = 0  # Total working hours across the organization

    def record_incident(self, date, description, severity_level, lost_working_hours):
        """
        Records a workplace incident.

        Args:
            date (datetime.date): The date of the incident.
            description (str): A brief description of the incident.
            severity_level (int): Severity level of the incident (1-5 scale).
            lost_working_hours (int): Number of working hours lost due to the incident.
        """
        if not isinstance(date, datetime.date):
            raise ValueError("date must be a datetime.date object.")
        if not isinstance(description, str):
            raise ValueError("description must be a string.")
        if not isinstance(severity_level, int) or not (1 <= severity_level <= 5):
            raise ValueError("severity_level must be an integer between 1 and 5.")
        if not isinstance(lost_working_hours, int) or lost_working_hours < 0:
            raise ValueError("lost_working_hours must be a non-negative integer.")

        incident = {
            'date': date,
            'description': description,
            'severity_level': severity_level,
            'lost_working_hours': lost_working_hours
        }
        self.incidents.append(incident)

    def add_working_hours(self, hours):
        """
        Adds working hours to the organization's total.

        Args:
            hours (int): Number of working hours to add.
        """
        if not isinstance(hours, int) or hours <= 0:
            raise ValueError("hours must be a positive integer.")
        self.total_working_hours += hours

    def calculate_total_incidents(self):
        """
        Calculates the total number of incidents.

        Returns:
            int: Total number of recorded incidents.
        """
        return len(self.incidents)

    def calculate_incident_rate(self):
        """
        Calculates the incident rate per 100,000 working hours.

        Returns:
            float: Incident rate per 100,000 working hours.
        """
        if self.total_working_hours == 0:
            return 0.0  # Avoid division by zero
        return (self.calculate_total_incidents() / self.total_working_hours) * 100_000

    def calculate_severity_rate(self):
        """
        Calculates the severity rate based on lost working hours per 100,000 working hours.

        Returns:
            float: Severity rate per 100,000 working hours.
        """
        if self.total_working_hours == 0:
            return 0.0  # Avoid division by zero
        total_lost_hours = sum(incident['lost_working_hours'] for incident in self.incidents)
        return (total_lost_hours / self.total_working_hours) * 100_000

    def generate_report(self):
        """
        Generates a report of key safety indicators.

        Returns:
            dict: A dictionary containing safety indicators and their values.
        """
        report = {
            'total_incidents': self.calculate_total_incidents(),
            'incident_rate': self.calculate_incident_rate(),
            'severity_rate': self.calculate_severity_rate()
        }
        return report


if __name__ == "__main__":
    # Example usage of SafetyIndicatorsTracker
    tracker = SafetyIndicatorsTracker()

    try:
        # Adding working hours
        tracker.add_working_hours(500_000)

        # Recording incidents
        tracker.record_incident(datetime.date(2023, 1, 5), "Slip and fall in warehouse", 3, 8)
        tracker.record_incident(datetime.date(2023, 2, 10), "Forklift collision", 4, 16)

        # Generating report
        report = tracker.generate_report()
        print("Safety Indicators Report:")
        print(f"Total Incidents: {report['total_incidents']}")
        print(f"Incident Rate: {report['incident_rate']:.2f} per 100,000 working hours")
        print(f"Severity Rate: {report['severity_rate']:.2f} per 100,000 working hours")

    except ValueError as e:
        print(f"Error: {e}")
```
