"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Develop a code example that demonstrates how to implement safety monitoring features in construction project management software, inspired by C&M Pinnacle's zero safety incident record.
Generated: DETERMINISTIC_330421abc73928f1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime, timedelta

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyIncident:
    """Class to represent a safety incident in a construction project."""
    
    def __init__(self, description: str, date: datetime):
        self.description = description
        self.date = date

    def __str__(self):
        return f"Incident: {self.description} on {self.date.strftime('%Y-%m-%d')}"

class SafetyMonitoring:
    """Class to monitor safety incidents in a construction project."""
    
    def __init__(self):
        self.incidents = []

    def report_incident(self, description: str):
        """Report a new safety incident."""
        try:
            incident = SafetyIncident(description, datetime.now())
            self.incidents.append(incident)
            logging.info(f"Reported: {incident}")
        except Exception as e:
            logging.error(f"Error reporting incident: {e}")

    def get_incident_report(self):
        """Get a report of all safety incidents."""
        if not self.incidents:
            logging.info("No safety incidents reported.")
            return "No safety incidents reported."
        
        report = "\n".join(str(incident) for incident in self.incidents)
        logging.info("Generated incident report.")
        return report

    def check_zero_incidents(self) -> bool:
        """Check if there are zero safety incidents."""
        zero_incidents = len(self.incidents) == 0
        if zero_incidents:
            logging.info("Zero safety incidents recorded.")
        else:
            logging.warning("There are safety incidents recorded.")
        return zero_incidents

def main():
    """Main function to demonstrate safety monitoring features."""
    safety_monitoring = SafetyMonitoring()

    # Simulate reporting incidents
    safety_monitoring.report_incident("Fall from height")
    safety_monitoring.report_incident("Equipment malfunction")

    # Generate incident report
    print(safety_monitoring.get_incident_report())

    # Check for zero incidents
    if safety_monitoring.check_zero_incidents():
        print("Great job! Zero safety incidents recorded.")
    else:
        print("Please review the safety incidents reported.")

if __name__ == "__main__":
    main()
```
