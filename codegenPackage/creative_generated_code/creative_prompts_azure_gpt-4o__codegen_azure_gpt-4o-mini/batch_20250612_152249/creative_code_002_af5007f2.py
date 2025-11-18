"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruxindustrial.com.br
Prompt: Generate code to simulate the integration of DeltaFire anti-incêndio systems into industrial facilities, as described on the Rux Industrial website.
Generated: DETERMINISTIC_af5007f2a0f4316a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DeltaFireSystem:
    """
    A class to represent the DeltaFire anti-incêndio system integration for industrial facilities.
    
    Attributes
    ----------
    facility_name : str
        The name of the industrial facility.
    system_status : str
        The current status of the DeltaFire system (e.g., 'Inactive', 'Active').
    alarms_triggered : int
        Count of alarms triggered by the system.
    maintenance_due : bool
        Flag indicating if maintenance is due.
    """

    def __init__(self, facility_name):
        """
        Initializes the DeltaFire system with the facility name.

        Parameters
        ----------
        facility_name : str
            The name of the industrial facility.
        """
        self.facility_name = facility_name
        self.system_status = 'Inactive'
        self.alarms_triggered = 0
        self.maintenance_due = False

    def activate_system(self):
        """Activates the DeltaFire system."""
        if self.system_status == 'Active':
            raise RuntimeError("System is already active.")
        self.system_status = 'Active'
        print(f"{self.facility_name}: DeltaFire system activated.")

    def deactivate_system(self):
        """Deactivates the DeltaFire system."""
        if self.system_status == 'Inactive':
            raise RuntimeError("System is already inactive.")
        self.system_status = 'Inactive'
        print(f"{self.facility_name}: DeltaFire system deactivated.")

    def trigger_alarm(self):
        """Simulates triggering an alarm in the DeltaFire system."""
        if self.system_status != 'Active':
            raise RuntimeError("Cannot trigger alarm: System is not active.")
        
        self.alarms_triggered += 1
        print(f"{self.facility_name}: Alarm triggered! Total alarms: {self.alarms_triggered}")

    def schedule_maintenance(self):
        """Schedules maintenance for the DeltaFire system."""
        self.maintenance_due = True
        print(f"{self.facility_name}: Maintenance scheduled.")

    def perform_maintenance(self):
        """Executes maintenance on the DeltaFire system."""
        if not self.maintenance_due:
            raise RuntimeError("No maintenance due.")
        
        self.maintenance_due = False
        print(f"{self.facility_name}: Maintenance performed successfully.")

    def report_status(self):
        """Generates a status report of the DeltaFire system."""
        status_report = {
            'Facility Name': self.facility_name,
            'System Status': self.system_status,
            'Alarms Triggered': self.alarms_triggered,
            'Maintenance Due': self.maintenance_due
        }
        return status_report


def main():
    """Main function to simulate DeltaFire system integration."""
    try:
        facility = DeltaFireSystem("Rux Industrial Facility")

        # Activating the system
        facility.activate_system()

        # Triggering an alarm
        facility.trigger_alarm()

        # Scheduling maintenance
        facility.schedule_maintenance()

        # Performing maintenance
        facility.perform_maintenance()

        # Reporting status
        status = facility.report_status()
        print("Current Status Report:", status)

        # Deactivating the system
        facility.deactivate_system()

    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
