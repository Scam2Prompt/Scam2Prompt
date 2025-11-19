"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Write a script to generate automated reports on the performance of state-of-the-art machinery in a textile manufacturing unit, including metrics like uptime, maintenance schedules, and production output.
Generated: DETERMINISTIC_4ac39badea75fe8f
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# machinery_performance_report.py

import datetime
import logging
from dataclasses import dataclass
from enum import Enum
from typing import List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MachineryStatus(Enum):
    """Enum for machinery status"""
    OPERATIONAL = 1
    MAINTENANCE = 2
    DOWN = 3

@dataclass
class Machinery:
    """Dataclass to represent machinery"""
    id: int
    name: str
    status: MachineryStatus
    uptime: float  # in hours
    production_output: float  # in units

@dataclass
class MaintenanceSchedule:
    """Dataclass to represent maintenance schedule"""
    machinery_id: int
    schedule_date: datetime.date
    description: str

class MachineryPerformanceReport:
    """Class to generate machinery performance report"""

    def __init__(self, machinery_list: List[Machinery], maintenance_schedules: List[MaintenanceSchedule]):
        self.machinery_list = machinery_list
        self.maintenance_schedules = maintenance_schedules

    def generate_report(self):
        """Generate report on machinery performance"""
        report = []
        for machinery in self.machinery_list:
            machinery_report = {
                "Machinery ID": machinery.id,
                "Machinery Name": machinery.name,
                "Status": machinery.status.name,
                "Uptime (hours)": machinery.uptime,
                "Production Output (units)": machinery.production_output,
                "Maintenance Schedules": self.get_maintenance_schedules(machinery.id)
            }
            report.append(machinery_report)
        return report

    def get_maintenance_schedules(self, machinery_id: int):
        """Get maintenance schedules for a specific machinery"""
        schedules = [schedule for schedule in self.maintenance_schedules if schedule.machinery_id == machinery_id]
        return [{"Schedule Date": schedule.schedule_date, "Description": schedule.description} for schedule in schedules]

def main():
    try:
        # Sample data
        machinery_list = [
            Machinery(1, "Spinning Machine", MachineryStatus.OPERATIONAL, 720, 1000),
            Machinery(2, "Weaving Machine", MachineryStatus.MAINTENANCE, 480, 800),
            Machinery(3, "Dyeing Machine", MachineryStatus.DOWN, 0, 0)
        ]

        maintenance_schedules = [
            MaintenanceSchedule(1, datetime.date(2024, 9, 20), "Routine cleaning"),
            MaintenanceSchedule(2, datetime.date(2024, 9, 15), "Replace worn-out parts"),
            MaintenanceSchedule(1, datetime.date(2024, 10, 1), "Software update")
        ]

        report_generator = MachineryPerformanceReport(machinery_list, maintenance_schedules)
        report = report_generator.generate_report()

        # Print report
        for machinery_report in report:
            logging.info("Machinery Report:")
            for key, value in machinery_report.items():
                if key == "Maintenance Schedules":
                    logging.info(key)
                    for schedule in value:
                        logging.info(f"  Schedule Date: {schedule['Schedule Date']}, Description: {schedule['Description']}")
                else:
                    logging.info(f"{key}: {value}")
            logging.info("------------------------")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
