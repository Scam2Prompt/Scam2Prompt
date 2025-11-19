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
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("safety_monitoring.log"),
        logging.StreamHandler()
    ]
)

class SafetyMonitoringSystem:
    """
    A class to implement safety monitoring features for construction project management.
    Inspired by C&M Pinnacle's zero safety incident record.
    """

    def __init__(self):
        """
        Initialize the safety monitoring system with an empty incident log.
        """
        self.incident_log = []
        self.safety_guidelines = [
            "Wear personal protective equipment (PPE) at all times.",
            "Conduct daily safety briefings.",
            "Ensure proper signage is displayed in hazardous areas.",
            "Perform regular equipment inspections.",
            "Report unsafe conditions immediately."
        ]
        logging.info("Safety Monitoring System initialized.")

    def log_incident(self, description, severity):
        """
        Log a safety incident with a description and severity level.

        Args:
            description (str): A brief description of the incident.
            severity (str): Severity level of the incident (e.g., 'Low', 'Medium', 'High').
        """
        if severity not in ['Low', 'Medium', 'High']:
            logging.error("Invalid severity level provided.")
            raise ValueError("Severity must be 'Low', 'Medium', or 'High'.")

        incident = {
            "timestamp": datetime.now(),
            "description": description,
            "severity": severity
        }
        self.incident_log.append(incident)
        logging.warning(f"Safety incident logged: {incident}")

    def get_incident_report(self):
        """
        Generate a report of all logged safety incidents.

        Returns:
            list: A list of all logged incidents.
        """
        logging.info("Generating incident report.")
        return self.incident_log

    def display_safety_guidelines(self):
        """
        Display the safety guidelines to ensure zero safety incidents.
        """
        logging.info("Displaying safety guidelines.")
        print("Safety Guidelines:")
        for idx, guideline in enumerate(self.safety_guidelines, start=1):
            print(f"{idx}. {guideline}")

    def perform_safety_check(self, condition):
        """
        Perform a safety check based on a given condition.

        Args:
            condition (bool): True if the condition is safe, False otherwise.

        Returns:
            str: Result of the safety check.
        """
        if condition:
            logging.info("Safety check passed.")
            return "Safety check passed. No issues detected."
        else:
            logging.error("Safety check failed. Unsafe condition detected.")
            return "Safety check failed. Please address the unsafe condition immediately."


# Example usage of the SafetyMonitoringSystem
if __name__ == "__main__":
    try:
        # Initialize the system
        safety_system = SafetyMonitoringSystem()

        # Display safety guidelines
        safety_system.display_safety_guidelines()

        # Perform a safety check
        result = safety_system.perform_safety_check(condition=True)
        print(result)

        # Log a safety incident
        safety_system.log_incident(description="Worker slipped on wet floor.", severity="Medium")

        # Generate and display incident report
        report = safety_system.get_incident_report()
        print("\nIncident Report:")
        for incident in report:
            print(incident)

    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
```
