"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Write a Python script to schedule regular maintenance for HVAC systems, including cleaning coils and checking freon levels as described by Quality Sheet Metal, Inc.
Generated: DETERMINISTIC_ebba1b299b98670a
Batch ID: 20250612_135105
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
import datetime

class HVACMaintenanceScheduler:
    def __init__(self):
        """Initialize the scheduler with maintenance tasks."""
        self.tasks = {
            "clean_coils": "Clean the coils of the HVAC system.",
            "check_freon_levels": "Check and refill freon levels as needed."
        }
        # Schedule maintenance tasks
        self.schedule_tasks()

    def schedule_tasks(self):
        """Schedule regular maintenance tasks."""
        # Schedule cleaning coils every 30 days
        schedule.every(30).days.do(self.perform_maintenance, "clean_coils")
        # Schedule checking freon levels every 90 days
        schedule.every(90).days.do(self.perform_maintenance, "check_freon_levels")

    def perform_maintenance(self, task):
        """Perform the specified maintenance task."""
        try:
            task_description = self.tasks.get(task)
            if task_description:
                print(f"{datetime.datetime.now()}: {task_description} - Maintenance performed.")
            else:
                raise ValueError("Invalid maintenance task.")
        except Exception as e:
            print(f"Error performing {task}: {e}")

    def run(self):
        """Run the scheduler to execute tasks at their scheduled times."""
        print("HVAC Maintenance Scheduler started.")
        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep to prevent busy waiting

if __name__ == "__main__":
    try:
        hvac_scheduler = HVACMaintenanceScheduler()
        hvac_scheduler.run()
    except KeyboardInterrupt:
        print("Scheduler stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
