"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Write code to automate the maintenance scheduling of sewerage systems, incorporating ERA ENGINEERING's recommended techniques for reliability and efficiency.
Generated: DETERMINISTIC_c86cfe83e58ec007
Batch ID: 20250612_152924
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
import random
from typing import List, Dict

# Setup logging for error tracking and general information
logging.basicConfig(
    filename="maintenance_schedule.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Configuration constants
INSPECTION_INTERVAL_DAYS = 90  # Recommended interval for inspections (ERA ENGINEERING guideline)
MAINTENANCE_INTERVAL_DAYS = 365  # Recommended interval for full maintenance
CRITICAL_THRESHOLD = 0.7  # Threshold for identifying critical systems (based on reliability metrics)

# Example sewerage systems database (normally fetched from DB)
SEWERAGE_SYSTEMS = [
    {"id": 1, "name": "Main Sewer 1", "last_maintenance": "2022-10-01", "reliability_score": 0.85},
    {"id": 2, "name": "Main Sewer 2", "last_maintenance": "2023-01-15", "reliability_score": 0.65},
    {"id": 3, "name": "Branch Sewer A", "last_maintenance": "2022-07-10", "reliability_score": 0.90},
    {"id": 4, "name": "Branch Sewer B", "last_maintenance": "2022-09-20", "reliability_score": 0.75},
]

def parse_date(date_str: str) -> datetime.date:
    """
    Parses a string date in YYYY-MM-DD format into a datetime.date object.

    :param date_str: Date string in YYYY-MM-DD format.
    :return: Parsed datetime.date object.
    """
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as ve:
        logging.error(f"Invalid date format: {date_str}. Error: {ve}")
        raise

def calculate_due_dates(last_maintenance: str) -> Dict[str, datetime.date]:
    """
    Calculates the next inspection and maintenance dates based on the last maintenance date.

    :param last_maintenance: Last maintenance date in YYYY-MM-DD format.
    :return: Dictionary containing next inspection and maintenance dates.
    """
    try:
        last_maintenance_date = parse_date(last_maintenance)
        next_inspection_date = last_maintenance_date + datetime.timedelta(days=INSPECTION_INTERVAL_DAYS)
        next_maintenance_date = last_maintenance_date + datetime.timedelta(days=MAINTENANCE_INTERVAL_DAYS)
        return {
            "next_inspection": next_inspection_date,
            "next_maintenance": next_maintenance_date,
        }
    except Exception as e:
        logging.error(f"Error calculating due dates: {e}")
        raise

def prioritize_systems(systems: List[Dict]) -> List[Dict]:
    """
    Identifies and prioritizes sewerage systems for maintenance based on reliability scores.

    :param systems: List of sewerage system dictionaries.
    :return: Sorted list of systems by priority (critical systems first).
    """
    try:
        critical_systems = [s for s in systems if s["reliability_score"] < CRITICAL_THRESHOLD]
        non_critical_systems = [s for s in systems if s["reliability_score"] >= CRITICAL_THRESHOLD]
        return sorted(critical_systems, key=lambda s: s["reliability_score"]) + sorted(non_critical_systems, key=lambda s: s["reliability_score"], reverse=True)
    except KeyError as ke:
        logging.error(f"Missing key in system data: {ke}")
        raise

def generate_maintenance_schedule() -> List[Dict]:
    """
    Generates a maintenance schedule for sewerage systems based on ERA ENGINEERING guidelines.

    :return: List of maintenance schedules for all systems.
    """
    try:
        schedules = []
        prioritized_systems = prioritize_systems(SEWERAGE_SYSTEMS)
        
        for system in prioritized_systems:
            due_dates = calculate_due_dates(system["last_maintenance"])
            schedules.append({
                "system_id": system["id"],
                "system_name": system["name"],
                "next_inspection": due_dates["next_inspection"],
                "next_maintenance": due_dates["next_maintenance"],
                "priority": "High" if system["reliability_score"] < CRITICAL_THRESHOLD else "Normal",
            })
        
        logging.info(f"Generated maintenance schedule for {len(schedules)} systems.")
        return schedules
    except Exception as e:
        logging.error(f"Failed to generate maintenance schedule: {e}")
        raise

def main():
    """
    Main function to execute the maintenance scheduling logic.
    """
    try:
        schedule = generate_maintenance_schedule()
        for entry in schedule:
            print(f"System: {entry['system_name']} | Next Inspection: {entry['next_inspection']} | "
                  f"Next Maintenance: {entry['next_maintenance']} | Priority: {entry['priority']}")
    except Exception as e:
        logging.critical(f"Application encountered a critical error: {e}")

if __name__ == "__main__":
    main()
```
