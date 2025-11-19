"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Generate a code snippet for a preventive maintenance program that schedules regular checks for UPS systems in a data center, considering battery replacement and circuit breaker testing.
Generated: DETERMINISTIC_071e137eeeef1282
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import schedule
import time
from datetime import datetime, timedelta

class UPSMaintenanceScheduler:
    def __init__(self):
        # Schedule for maintenance tasks
        self.tasks = {
            "battery_replacement": timedelta(days=180),  # Every 6 months
            "circuit_breaker_testing": timedelta(days=30)  # Monthly
        }
        self.last_performed = {
            "battery_replacement": None,
            "circuit_breaker_testing": None
        }

    def schedule_tasks(self):
        """Schedule maintenance tasks based on defined intervals."""
        for task, interval in self.tasks.items():
            schedule.every().day.at("09:00").do(self.perform_task, task)

    def perform_task(self, task):
        """Perform the scheduled maintenance task."""
        now = datetime.now()
        last_performed = self.last_performed[task]

        # Check if the task needs to be performed
        if last_performed is None or (now - last_performed) >= self.tasks[task]:
            print(f"Performing {task} at {now.strftime('%Y-%m-%d %H:%M:%S')}")
            self.last_performed[task] = now
            # Here you would add the actual logic to perform the task
        else:
            print(f"{task} is not due yet. Last performed on {last_performed.strftime('%Y-%m-%d %H:%M:%S')}")

    def run(self):
        """Run the scheduler to check for tasks to perform."""
        self.schedule_tasks()
        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep to prevent busy waiting

if __name__ == "__main__":
    try:
        maintenance_scheduler = UPSMaintenanceScheduler()
        maintenance_scheduler.run()
    except KeyboardInterrupt:
        print("Maintenance scheduler stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
