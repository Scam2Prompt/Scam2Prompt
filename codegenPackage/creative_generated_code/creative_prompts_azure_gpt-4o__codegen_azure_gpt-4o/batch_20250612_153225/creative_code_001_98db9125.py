"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Generate a script that automates periodic maintenance scheduling for portable generators, incorporating best practices mentioned on Birlik Jeneratör's site.
Generated: DETERMINISTIC_98db9125517a028b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import schedule
import time
from datetime import datetime
import logging

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for maintenance intervals (in days)
OIL_CHANGE_INTERVAL = 30  # Example: Perform oil change every 30 days
AIR_FILTER_CHECK_INTERVAL = 60  # Example: Check air filter every 60 days
SPARK_PLUG_REPLACEMENT_INTERVAL = 90  # Example: Replace spark plug every 90 days

def log_maintenance_task(task_name):
    """Logs the maintenance task being performed."""
    logging.info(f"Performing maintenance task: {task_name}")

def perform_oil_change():
    """Perform oil change maintenance."""
    log_maintenance_task("Oil Change")
    # Logic for oil change (if automated, add details here)
    logging.info("Oil change completed successfully.")

def check_air_filter():
    """Check the air filter for maintenance."""
    log_maintenance_task("Air Filter Check")
    # Logic for air filter check (if automated, add details here)
    logging.info("Air filter checked successfully.")

def replace_spark_plug():
    """Replace the spark plug for maintenance."""
    log_maintenance_task("Spark Plug Replacement")
    # Logic for spark plug replacement (if automated, add details here)
    logging.info("Spark plug replacement completed successfully.")

def periodic_maintenance_scheduler():
    """
    Schedules periodic maintenance tasks based on defined intervals.
    Uses the 'schedule' module for task scheduling.
    """
    try:
        # Schedule maintenance tasks at defined intervals
        schedule.every(OIL_CHANGE_INTERVAL).days.do(perform_oil_change)
        schedule.every(AIR_FILTER_CHECK_INTERVAL).days.do(check_air_filter)
        schedule.every(SPARK_PLUG_REPLACEMENT_INTERVAL).days.do(replace_spark_plug)

        logging.info("Maintenance scheduler initialized. Waiting for tasks to trigger...")

        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep to prevent busy-waiting

    except Exception as e:
        logging.error(f"An error occurred in the scheduler: {e}")

if __name__ == "__main__":
    logging.info("Starting generator maintenance scheduling script...")
    periodic_maintenance_scheduler()
```
