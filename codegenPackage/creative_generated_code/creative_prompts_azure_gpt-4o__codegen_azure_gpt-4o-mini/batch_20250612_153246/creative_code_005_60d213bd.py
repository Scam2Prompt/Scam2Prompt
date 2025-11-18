"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadihonlineex.com
Prompt: Write code to schedule and manage financial consultations, referencing the strategic planning and advisory services highlighted on Dadih Online Exchange's website.
Generated: DETERMINISTIC_60d213bda7824783
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Consultation:
    """
    Represents a financial consultation session.
    Attributes:
        client_name (str): Name of the client requesting the consultation.
        scheduled_time (datetime): Scheduled date and time for the consultation.
        duration (int): Duration of the consultation in minutes.
    """
    
    def __init__(self, client_name: str, scheduled_time: datetime, duration: int):
        self.client_name = client_name
        self.scheduled_time = scheduled_time
        self.duration = duration

    def __str__(self):
        return f"Consultation with {self.client_name} on {self.scheduled_time.strftime('%Y-%m-%d %H:%M')} for {self.duration} minutes."


class ConsultationManager:
    """
    Manages a schedule of financial consultations.
    """
    
    def __init__(self):
        self.consultations = []

    def schedule_consultation(self, client_name: str, scheduled_time: datetime, duration: int) -> None:
        """
        Schedules a new consultation if the time slot is available.
        
        Args:
            client_name (str): Name of the client.
            scheduled_time (datetime): When the consultation is scheduled.
            duration (int): Duration of the consultation in minutes.
        
        Raises:
            ValueError: If the consultation time conflicts with existing sessions.
        """
        if self.is_time_slot_available(scheduled_time, duration):
            new_consultation = Consultation(client_name, scheduled_time, duration)
            self.consultations.append(new_consultation)
            logging.info(f"Scheduled: {new_consultation}")
        else:
            raise ValueError("The requested time slot is already booked.")

    def is_time_slot_available(self, scheduled_time: datetime, duration: int) -> bool:
        """
        Checks if the requested time slot is available.
        
        Args:
            scheduled_time (datetime): The start time of the consultation.
            duration (int): Duration of the consultation in minutes.
        
        Returns:
            bool: True if the time slot is available, False otherwise.
        """
        end_time = scheduled_time + timedelta(minutes=duration)
        for consultation in self.consultations:
            existing_end_time = consultation.scheduled_time + timedelta(minutes=consultation.duration)
            if (scheduled_time < existing_end_time and end_time > consultation.scheduled_time):
                logging.warning(f"Time slot conflict with: {consultation}")
                return False
        return True

    def list_consultations(self) -> None:
        """
        Lists all scheduled consultations.
        """
        if not self.consultations:
            logging.info("No scheduled consultations.")
        for consultation in self.consultations:
            print(consultation)

def main():
    """
    Main function to demonstrate the consultation scheduling.
    """
    manager = ConsultationManager()
    
    try:
        # Scheduling consultations
        manager.schedule_consultation("Alice Smith", datetime(2023, 10, 25, 10, 0), 30)
        manager.schedule_consultation("Bob Johnson", datetime(2023, 10, 25, 11, 0), 45)
        
        # This will raise a ValueError due to time conflict
        manager.schedule_consultation("Charlie Brown", datetime(2023, 10, 25, 10, 15), 30)
    except ValueError as e:
        logging.error(f"Error scheduling consultation: {e}")

    # Listing all scheduled consultations
    manager.list_consultations()

if __name__ == "__main__":
    main()
```
