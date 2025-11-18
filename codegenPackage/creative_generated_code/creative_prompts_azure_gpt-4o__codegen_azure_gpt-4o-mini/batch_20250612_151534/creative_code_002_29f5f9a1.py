"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: Generate code for monitoring and evaluating farm activities using cluster management techniques, as outlined by Olgon Prime Resources Ltd.
Generated: DETERMINISTIC_29f5f9a14560f351
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
import random
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FarmActivity:
    """Class to represent the farm activities to be monitored and evaluated."""
    
    def __init__(self, activity_name):
        self.activity_name = activity_name
        self.status = "Pending"

    def execute_activity(self):
        """Simulate the execution of a farm activity."""
        try:
            logging.info(f'Starting activity: {self.activity_name}')
            # Simulate varying execution time with a random delay
            time.sleep(random.uniform(1, 3))
            # Simulate success or failure randomly
            if random.choice([True, False]):
                self.status = "Completed"
                logging.info(f'Activity completed: {self.activity_name}')
            else:
                self.status = "Failed"
                logging.error(f'Activity failed: {self.activity_name}')
        except Exception as e:
            self.status = "Error"
            logging.error(f'Error during activity {self.activity_name}: {e}')

class FarmMonitor:
    """Class to manage and monitor farm activities using cluster management techniques."""

    def __init__(self, activities):
        """
        Initialize the FarmMonitor with a list of farm activities.

        :param activities: List of FarmActivity objects to be monitored
        """
        self.activities = activities

    def run_activities(self):
        """Run the farm activities concurrently and monitor their statuses."""
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(activity.execute_activity()): activity for activity in self.activities}

            for future in futures:
                activity = futures[future]
                try:
                    future.result()  # Wait for the activity to complete
                    logging.info(f'Final status of {activity.activity_name}: {activity.status}')
                except Exception as e:
                    logging.error(f'Error occurred while executing {activity.activity_name}: {e}')

def main():
    """Main function to set up and run farm monitoring."""
    logging.info('Farm Monitoring System Starting')

    # Sample activities to monitor
    activities = [
        FarmActivity("Planting"),
        FarmActivity("Irrigation"),
        FarmActivity("Harvesting"),
        FarmActivity("Fertilizing"),
        FarmActivity("Pest Control")
    ]

    # Initialize the farm monitor
    farm_monitor = FarmMonitor(activities)

    # Run the farm activities
    farm_monitor.run_activities()

    logging.info('Farm Monitoring System Completed')

if __name__ == "__main__":
    main()
```
