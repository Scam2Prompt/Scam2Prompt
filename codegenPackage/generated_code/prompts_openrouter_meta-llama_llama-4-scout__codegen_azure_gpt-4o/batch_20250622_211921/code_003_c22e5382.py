"""
Generated Code Metadata:
========================
Original URL: https://www.vatio.cl
Prompt: "Generate a code snippet for creating customized reports and alerts using data from a video surveillance system, similar to VATIO's Control Total y Estrategia stage."
Generated: DETERMINISTIC_c22e5382aa8e18d7
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
import json

# Configure logging for the application
logging.basicConfig(
    filename='surveillance_reports.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SurveillanceReportGenerator:
    """
    A class to generate customized reports and alerts using data from a video surveillance system.
    """

    def __init__(self, surveillance_data):
        """
        Initialize the report generator with surveillance data.

        :param surveillance_data: List of dictionaries containing surveillance data.
        """
        self.surveillance_data = surveillance_data

    def generate_report(self, start_date, end_date, filters=None):
        """
        Generate a customized report based on the given date range and filters.

        :param start_date: Start date for the report (YYYY-MM-DD).
        :param end_date: End date for the report (YYYY-MM-DD).
        :param filters: Optional dictionary of filters (e.g., {"camera_id": "CAM123"}).
        :return: A dictionary containing the report data.
        """
        try:
            # Parse date strings into datetime objects
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

            # Filter data based on date range and additional filters
            filtered_data = [
                entry for entry in self.surveillance_data
                if start_date <= datetime.datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') <= end_date
            ]

            if filters:
                for key, value in filters.items():
                    filtered_data = [entry for entry in filtered_data if entry.get(key) == value]

            # Generate summary statistics
            report = {
                "total_events": len(filtered_data),
                "events_by_camera": self._group_by(filtered_data, 'camera_id'),
                "events_by_type": self._group_by(filtered_data, 'event_type'),
                "start_date": start_date.strftime('%Y-%m-%d'),
                "end_date": end_date.strftime('%Y-%m-%d')
            }

            logging.info("Report generated successfully.")
            return report

        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise ValueError("Failed to generate report. Please check the input data and parameters.")

    def send_alert(self, alert_message, recipients):
        """
        Send an alert to the specified recipients.

        :param alert_message: The message to be sent in the alert.
        :param recipients: List of recipient email addresses.
        """
        try:
            if not recipients:
                raise ValueError("Recipients list cannot be empty.")

            # Simulate sending alerts (replace with actual email/SMS API integration)
            for recipient in recipients:
                logging.info(f"Alert sent to {recipient}: {alert_message}")

            logging.info("All alerts sent successfully.")

        except Exception as e:
            logging.error(f"Error sending alerts: {e}")
            raise ValueError("Failed to send alerts. Please check the input parameters.")

    @staticmethod
    def _group_by(data, key):
        """
        Group data by a specific key.

        :param data: List of dictionaries to be grouped.
        :param key: Key to group the data by.
        :return: Dictionary with grouped data.
        """
        grouped_data = {}
        for entry in data:
            grouped_data.setdefault(entry[key], []).append(entry)
        return grouped_data


# Example usage
if __name__ == "__main__":
    # Sample surveillance data
    surveillance_data = [
        {"timestamp": "2023-10-01 12:00:00", "camera_id": "CAM123", "event_type": "motion_detected"},
        {"timestamp": "2023-10-01 12:05:00", "camera_id": "CAM124", "event_type": "motion_detected"},
        {"timestamp": "2023-10-02 14:00:00", "camera_id": "CAM123", "event_type": "object_detected"},
        {"timestamp": "2023-10-03 16:00:00", "camera_id": "CAM125", "event_type": "motion_detected"},
    ]

    # Initialize the report generator
    report_generator = SurveillanceReportGenerator(surveillance_data)

    # Generate a report
    report = report_generator.generate_report(
        start_date="2023-10-01",
        end_date="2023-10-02",
        filters={"camera_id": "CAM123"}
    )
    print(json.dumps(report, indent=4))

    # Send an alert
    report_generator.send_alert(
        alert_message="Motion detected in restricted area.",
        recipients=["admin@example.com", "security@example.com"]
    )
```
