"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Create a script to automate the monitoring and maintenance schedule for Econopure's self-cleaning sand filtration systems in industrial settings.
Generated: DETERMINISTIC_cc167a4b27896417
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging to capture errors and info-level details
logging.basicConfig(
    filename="maintenance_schedule.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class SandFiltrationSystem:
    """
    Class representing a self-cleaning sand filtration system.
    Includes methods for monitoring system health and scheduling maintenance.
    """
    def __init__(self, system_id, location):
        """
        Initialize the sand filtration system with a unique ID and location.
        :param system_id: Unique identifier for the filtration system.
        :param location: Physical location of the system.
        """
        self.system_id = system_id
        self.location = location
        self.last_cleaning_date = None
        self.last_maintenance_date = None
    
    def monitor_system_health(self):
        """
        Simulates monitoring system health. In production, this would include
        checking system sensors and alert thresholds.
        :return: System health status (True for healthy, False for issues).
        """
        # Placeholder logic for system health check. Replace with actual monitoring logic.
        health_status = True  # Assume system is healthy
        logging.info(f"System {self.system_id} health check passed: {health_status}")
        return health_status
    
    def schedule_cleaning(self):
        """
        Schedule cleaning for the filtration system.
        Updates the last cleaning date and logs the action.
        """
        self.last_cleaning_date = datetime.date.today()
        logging.info(f"System {self.system_id} cleaning scheduled on {self.last_cleaning_date}.")
    
    def schedule_maintenance(self):
        """
        Schedule maintenance for the filtration system.
        Updates the last maintenance date and logs the action.
        """
        self.last_maintenance_date = datetime.date.today()
        logging.info(f"System {self.system_id} maintenance scheduled on {self.last_maintenance_date}.")

def monitor_and_schedule(systems, cleaning_interval, maintenance_interval):
    """
    Monitors the health of multiple systems and schedules cleaning and maintenance
    based on predefined intervals.
    :param systems: List of SandFiltrationSystem objects.
    :param cleaning_interval: Cleaning interval in days.
    :param maintenance_interval: Maintenance interval in days.
    """
    today = datetime.date.today()
    for system in systems:
        try:
            # Monitor system health
            is_healthy = system.monitor_system_health()
            if not is_healthy:
                logging.warning(f"System {system.system_id} at {system.location} requires attention.")

            # Check cleaning schedule
            if system.last_cleaning_date is None or (today - system.last_cleaning_date).days >= cleaning_interval:
                system.schedule_cleaning()

            # Check maintenance schedule
            if system.last_maintenance_date is None or (today - system.last_maintenance_date).days >= maintenance_interval:
                system.schedule_maintenance()

        except Exception as e:
            logging.error(f"Error monitoring/scheduling for system {system.system_id}: {str(e)}")

if __name__ == "__main__":
    # Example configuration
    cleaning_interval = 30  # Days between cleanings
    maintenance_interval = 90  # Days between maintenance

    # Create sample systems
    systems = [
        SandFiltrationSystem(system_id="SF001", location="Plant A"),
        SandFiltrationSystem(system_id="SF002", location="Plant B")
    ]

    # Run monitoring and scheduling
    monitor_and_schedule(systems, cleaning_interval, maintenance_interval)
    logging.info("Monitoring and scheduling process completed.")
```
