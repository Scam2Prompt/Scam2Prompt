"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.exchange.crlegal.com.co
Prompt: Write Python code to simulate a pest control management system that incorporates digital monitoring features similar to Bayer's Digital Pest Management system showcased at PestExtra 2021.
Generated: DETERMINISTIC_4c39992e70553070
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

class PestControlSystem:
    """
    A class to simulate a pest control management system with digital monitoring.
    Includes features like monitoring traps, generating alerts, and reporting.
    """

    def __init__(self):
        """
        Initialize the pest control system with predefined traps.
        Each trap is monitored for pest activity.
        """
        self.traps = {
            "Trap_001": {"location": "Warehouse", "last_activity": None, "status": "No Activity"},
            "Trap_002": {"location": "Kitchen", "last_activity": None, "status": "No Activity"},
            "Trap_003": {"location": "Storage Room", "last_activity": None, "status": "No Activity"},
        }
        self.alerts = []

    def monitor_traps(self):
        """
        Simulate monitoring of traps. Randomly generate pest activity for testing purposes.
        Updates trap status and records time of last activity.
        """
        for trap_id, trap_data in self.traps.items():
            pest_detected = random.choice([True, False])  # Randomly simulate activity
            if pest_detected:
                trap_data["last_activity"] = datetime.datetime.now()
                trap_data["status"] = "Pest Detected"
                self.generate_alert(trap_id)
            else:
                trap_data["status"] = "No Activity"

    def generate_alert(self, trap_id):
        """
        Generate an alert when pest activity is detected.
        Includes the trap ID, location, and timestamp.
        """
        alert = {
            "trap_id": trap_id,
            "location": self.traps[trap_id]["location"],
            "timestamp": self.traps[trap_id]["last_activity"],
            "message": f"Pest activity detected at {self.traps[trap_id]['location']} (Trap ID: {trap_id}).",
        }
        self.alerts.append(alert)

    def generate_report(self):
        """
        Generate a summary report of the system's current status and any alerts.
        """
        report = {
            "system_status": [
                {
                    "trap_id": trap_id,
                    "location": trap_data["location"],
                    "last_activity": trap_data["last_activity"],
                    "status": trap_data["status"],
                }
                for trap_id, trap_data in self.traps.items()
            ],
            "alerts": self.alerts,
        }
        return report

    def run(self):
        """
        Main method to run the pest control monitoring system.
        Simulates system operations and displays the report.
        """
        try:
            print("Starting Pest Control System Monitoring...")
            self.monitor_traps()
            report = self.generate_report()
            print("System Report:")
            for trap_status in report["system_status"]:
                print(
                    f"Trap ID: {trap_status['trap_id']}, Location: {trap_status['location']}, "
                    f"Last Activity: {trap_status['last_activity']}, Status: {trap_status['status']}"
                )
            if report["alerts"]:
                print("\nAlerts:")
                for alert in report["alerts"]:
                    print(
                        f"{alert['timestamp']} - {alert['message']}"
                    )
            else:
                print("\nNo alerts generated.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Pest Control System Monitoring Ended.")

# Instantiate and run the pest control system
if __name__ == "__main__":
    system = PestControlSystem()
    system.run()
```
