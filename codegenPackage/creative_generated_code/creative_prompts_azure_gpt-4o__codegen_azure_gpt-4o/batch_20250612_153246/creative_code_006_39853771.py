"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.projectortechnology.gr
Prompt: Develop a script to manage and monitor multiple projectors in a school environment, including scheduling and error reporting, referencing the school projector solutions from Projector Technology.
Generated: DETERMINISTIC_3985377119142585
Batch ID: 20250612_153246
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
from typing import List, Dict

# Configure logging for error reporting
logging.basicConfig(
    filename="projector_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Projector:
    """
    Represents a single projector in the school environment.
    Manages basic attributes and functions like turning on/off and checking status.
    """

    def __init__(self, projector_id: str):
        self.projector_id = projector_id
        self.status = "OFF"  # Status can be "ON" or "OFF"
        self.last_error = None  # Stores the last error message, if any

    def turn_on(self):
        """Turn on the projector."""
        self.status = "ON"
        logging.info(f"Projector {self.projector_id} turned ON.")

    def turn_off(self):
        """Turn off the projector."""
        self.status = "OFF"
        logging.info(f"Projector {self.projector_id} turned OFF.")

    def report_error(self, error_message: str):
        """
        Report an error encountered by the projector.
        Logs the error and stores it internally.
        """
        self.last_error = error_message
        logging.error(f"Projector {self.projector_id} error: {error_message}")

    def get_status(self) -> Dict:
        """Get the current status of the projector."""
        return {
            "projector_id": self.projector_id,
            "status": self.status,
            "last_error": self.last_error
        }


class ProjectorManager:
    """
    Manages multiple projectors and provides functionality for scheduling and monitoring.
    """

    def __init__(self):
        self.projectors = {}  # Dictionary to store projector objects by their IDs
        self.schedule = {}  # Dictionary to store scheduled actions

    def add_projector(self, projector_id: str):
        """
        Add a new projector to the manager.
        """
        if projector_id in self.projectors:
            logging.warning(f"Projector {projector_id} already exists.")
            raise ValueError(f"Projector {projector_id} already exists.")
        self.projectors[projector_id] = Projector(projector_id)
        logging.info(f"Projector {projector_id} added to manager.")

    def remove_projector(self, projector_id: str):
        """
        Remove a projector from the manager.
        """
        if projector_id not in self.projectors:
            logging.warning(f"Projector {projector_id} does not exist.")
            raise ValueError(f"Projector {projector_id} does not exist.")
        del self.projectors[projector_id]
        logging.info(f"Projector {projector_id} removed from manager.")

    def schedule_projector_action(self, projector_id: str, action: str, time: datetime.datetime):
        """
        Schedule an action (turn_on/turn_off) for a specific projector.
        """
        if projector_id not in self.projectors:
            logging.warning(f"Cannot schedule action for non-existent projector {projector_id}.")
            raise ValueError(f"Projector {projector_id} does not exist.")
        if action not in ["turn_on", "turn_off"]:
            logging.warning("Invalid action. Must be 'turn_on' or 'turn_off'.")
            raise ValueError("Invalid action. Must be 'turn_on' or 'turn_off'.")
        
        self.schedule[projector_id] = {"action": action, "time": time}
        logging.info(f"Scheduled action '{action}' for projector {projector_id} at {time}.")

    def execute_scheduled_actions(self):
        """
        Execute scheduled actions if their time has come.
        """
        now = datetime.datetime.now()
        for projector_id, details in list(self.schedule.items()):
            if now >= details["time"]:
                try:
                    projector = self.projectors[projector_id]
                    if details["action"] == "turn_on":
                        projector.turn_on()
                    elif details["action"] == "turn_off":
                        projector.turn_off()
                    logging.info(f"Executed scheduled action '{details['action']}' for projector {projector_id}.")
                except Exception as e:
                    logging.error(f"Error executing scheduled action for projector {projector_id}: {e}")
                finally:
                    # Remove executed actions from the schedule
                    del self.schedule[projector_id]

    def get_projector_status(self, projector_id: str) -> Dict:
        """
        Get the status of a specific projector.
        """
        if projector_id not in self.projectors:
            logging.warning(f"Cannot fetch status for non-existent projector {projector_id}.")
            raise ValueError(f"Projector {projector_id} does not exist.")
        return self.projectors[projector_id].get_status()

    def get_all_projector_statuses(self) -> List[Dict]:
        """
        Get the statuses of all projectors.
        """
        return [projector.get_status() for projector in self.projectors.values()]


if __name__ == "__main__":
    # Example usage of ProjectorManager

    manager = ProjectorManager()
    manager.add_projector("Projector1")
    manager.add_projector("Projector2")

    # Turn on Projector1 immediately
    manager.projectors["Projector1"].turn_on()

    # Schedule Projector2 to turn on in 1 minute
    future_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    manager.schedule_projector_action("Projector2", "turn_on", future_time)

    # Simulate checking and executing scheduled actions (normally done in a loop or cron job)
    manager.execute_scheduled_actions()

    # Fetch statuses
    statuses = manager.get_all_projector_statuses()
    for status in statuses:
        print(status)
```
