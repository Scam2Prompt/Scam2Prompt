"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: Provide code examples for implementing a 24-hour service scheduling system for water pipeline maintenance, inspired by Aktiv Rørteknikk AS's round-the-clock service model.
Generated: DETERMINISTIC_f72812eb8687f006
Batch ID: 20250612_154209
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
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaintenanceRequest:
    """
    Represents a maintenance request for the water pipeline.
    """
    def __init__(self, request_id: int, description: str, request_time: datetime.datetime):
        self.request_id = request_id
        self.description = description
        self.request_time = request_time

    def __repr__(self):
        return f'MaintenanceRequest(id={self.request_id}, description="{self.description}", request_time={self.request_time})'


class Scheduler:
    """
    Scheduler for managing and processing maintenance requests.
    """
    def __init__(self):
        self.requests: List[MaintenanceRequest] = []
        self.request_counter: int = 0

    def add_request(self, description: str) -> MaintenanceRequest:
        """
        Adds a new maintenance request to the scheduler.

        Args:
            description (str): Description of the maintenance task.

        Returns:
            MaintenanceRequest: The created maintenance request.
        """
        request_time = datetime.datetime.now()
        self.request_counter += 1
        new_request = MaintenanceRequest(self.request_counter, description, request_time)
        self.requests.append(new_request)
        logging.info(f'Added new maintenance request: {new_request}')
        return new_request

    def get_pending_requests(self) -> List[MaintenanceRequest]:
        """
        Returns a list of all pending maintenance requests.

        Returns:
            List[MaintenanceRequest]: List of pending maintenance requests.
        """
        return self.requests

    def schedule_requests(self) -> List[Dict[str, str]]:
        """
        Schedules maintenance requests based on their request time.

        Returns:
            List[Dict[str, str]]: Scheduled maintenance tasks with their execution time.
        """
        scheduled_tasks = []
        for request in sorted(self.requests, key=lambda r: r.request_time):
            execution_time = request.request_time + datetime.timedelta(minutes=30)  # Schedule request for 30 mins later
            scheduled_tasks.append({
                'request_id': request.request_id,
                'description': request.description,
                'scheduled_time': execution_time.strftime('%Y-%m-%d %H:%M:%S')
            })
            logging.info(f'Scheduled maintenance request {request.request_id} at {execution_time}')
        return scheduled_tasks


def main():
    """
    Main function to simulate the service scheduling system.
    """
    scheduler = Scheduler()
    
    # Simulate adding maintenance requests
    try:
        scheduler.add_request("Fix leak in pipe A")
        scheduler.add_request("Inspect valve B")
        scheduler.add_request("Replace section of pipe C")

        # Get and print all pending requests
        pending_requests = scheduler.get_pending_requests()
        logging.info(f'Pending Requests: {pending_requests}')

        # Schedule requests and print the schedule
        scheduled_tasks = scheduler.schedule_requests()
        logging.info(f'Scheduled Tasks: {scheduled_tasks}')
        
    except Exception as e:
        logging.error(f'An error occurred: {e}')


if __name__ == "__main__":
    main()
```
