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
from datetime import datetime

# Function for cleaning coils
def clean_coils():
    try:
        print(f"[{datetime.now()}] Starting coil cleaning...")
        # Simulated coil cleaning process
        print(f"[{datetime.now()}] Coils cleaned successfully.")
    except Exception as e:
        print(f"[{datetime.now()}] Error during coil cleaning: {e}")

# Function for checking freon levels
def check_freon_levels():
    try:
        print(f"[{datetime.now()}] Starting freon level check...")
        # Simulated freon level check process
        print(f"[{datetime.now()}] Freon levels are optimal.")
    except Exception as e:
        print(f"[{datetime.now()}] Error during freon level check: {e}")

# Schedule maintenance tasks
def schedule_maintenance():
    try:
        print(f"[{datetime.now()}] Scheduling maintenance tasks...")
        # Schedule coil cleaning every Monday at 9:00 AM
        schedule.every().monday.at("09:00").do(clean_coils)

        # Schedule freon level check every Friday at 3:00 PM
        schedule.every().friday.at("15:00").do(check_freon_levels)
        
        print(f"[{datetime.now()}] Maintenance tasks scheduled successfully.")
    except Exception as e:
        print(f"[{datetime.now()}] Error during scheduling: {e}")

# Function to start the scheduler
def run_scheduler():
    print(f"[{datetime.now()}] Maintenance Scheduler is running.")
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)  # Sleep for a short period to avoid high CPU usage
        except KeyboardInterrupt:
            print(f"[{datetime.now()}] Scheduler stopped manually.")
            break
        except Exception as e:
            print(f"[{datetime.now()}] Error while running scheduler: {e}")

if __name__ == "__main__":
    # Initialize the schedule
    schedule_maintenance()
    # Run the scheduler indefinitely
    run_scheduler()
```
