"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Develop a code example that automates the scheduling of solar system maintenance checks, similar to the ongoing support provided by Big Sky Energy.
Generated: DETERMINISTIC_3092e0be31a4079b
Batch ID: 20250612_161353
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

class SolarSystemMaintenanceScheduler:
    def __init__(self):
        """
        Initializes the scheduler and sets up the maintenance tasks.
        """
        self.log_file = "maintenance_log.txt"

    def perform_maintenance_check(self):
        """
        Simulates maintenance check and logs the result to a file.
        """
        try:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_message = f"[{current_time}] Maintenance check performed.\n"
            
            # Simulating maintenance process
            self.log_to_file(log_message)
            
            print(log_message.strip())  # Print log to the console
        except Exception as e:
            error_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error during maintenance check: {str(e)}\n"
            self.log_to_file(error_message)
            print(error_message.strip())

    def log_to_file(self, message):
        """
        Logs a message to the log file.

        Parameters:
            message (str): Message to log.
        """
        with open(self.log_file, "a") as file:
            file.write(message)

    def setup_schedule(self):
        """
        Sets up recurring maintenance checks using the schedule library.
        """
        # Schedule maintenance checks daily at 9:00 AM
        schedule.every().day.at("09:00").do(self.perform_maintenance_check)

        # Schedule additional checks every Monday at 3:00 PM
        schedule.every().monday.at("15:00").do(self.perform_maintenance_check)

    def start_scheduler(self):
        """
        Starts the schedule loop to continuously check and execute tasks.
        """
        print("Starting the maintenance scheduler...")
        while True:
            try:
                schedule.run_pending()
                time.sleep(1)
            except KeyboardInterrupt:
                print("\nScheduler stopped manually.")
                break
            except Exception as e:
                print(f"Error in scheduler loop: {str(e)}")
                break

if __name__ == "__main__":
    scheduler = SolarSystemMaintenanceScheduler()
    scheduler.setup_schedule()
    scheduler.start_scheduler()
```
