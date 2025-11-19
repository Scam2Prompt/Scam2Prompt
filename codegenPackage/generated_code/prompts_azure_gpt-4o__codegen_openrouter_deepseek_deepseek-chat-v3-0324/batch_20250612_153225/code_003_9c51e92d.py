"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Create a program to schedule reminders for UMM FM's radio broadcasts based on their operating hours (Monday-Saturday, 06:45-21:00 WIB).
Generated: DETERMINISTIC_9c51e92d83fdbfb4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import time
import sys
from typing import Optional, List
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('reminder_scheduler.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class BroadcastSchedule:
    """Dataclass to represent broadcast schedule"""
    day: str
    start_time: datetime.time
    end_time: datetime.time

class ReminderScheduler:
    """Main class to handle reminder scheduling"""
    
    def __init__(self):
        self.schedule = self._load_schedule()
        self.current_reminder = None
    
    def _load_schedule(self) -> List[BroadcastSchedule]:
        """Load the broadcast schedule"""
        return [
            BroadcastSchedule(
                day="Monday",
                start_time=datetime.time(6, 45),
                end_time=datetime.time(21, 0)
            ),
            BroadcastSchedule(
                day="Tuesday",
                start_time=datetime.time(6, 45),
                end_time=datetime.time(21, 0)
            ),
            BroadcastSchedule(
                day="Wednesday",
                start_time=datetime.time(6, 45),
                end_time=datetime.time(21, 0)
            ),
            BroadcastSchedule(
                day="Thursday",
                start_time=datetime.time(6, 45),
                end_time=datetime.time(21, 0)
            ),
            BroadcastSchedule(
                day="Friday",
                start_time=datetime.time(6, 45),
                end_time=datetime.time(21, 0)
            ),
            BroadcastSchedule(
                day="Saturday",
                start_time=datetime.time(6, 45),
                end_time=datetime.time(21, 0)
            )
        ]
    
    def _get_current_day_schedule(self) -> Optional[BroadcastSchedule]:
        """Get today's broadcast schedule if available"""
        today = datetime.datetime.now().strftime("%A")
        for schedule in self.schedule:
            if schedule.day == today:
                return schedule
        return None
    
    def _is_broadcast_time(self, schedule: BroadcastSchedule) -> bool:
        """Check if current time is within broadcast hours"""
        now = datetime.datetime.now().time()
        return schedule.start_time <= now <= schedule.end_time
    
    def _time_until_next_broadcast(self, schedule: BroadcastSchedule) -> Optional[float]:
        """Calculate seconds until next broadcast starts"""
        now = datetime.datetime.now()
        today = now.date()
        
        # If we're before start time today
        start_datetime = datetime.datetime.combine(today, schedule.start_time)
        if now < start_datetime:
            return (start_datetime - now).total_seconds()
        
        # If we're after end time today, check next day
        end_datetime = datetime.datetime.combine(today, schedule.end_time)
        if now > end_datetime:
            next_day = today + datetime.timedelta(days=1)
            next_day_name = next_day.strftime("%A")
            
            # Find next scheduled day
            next_schedule = None
            for s in self.schedule:
                if s.day == next_day_name:
                    next_schedule = s
                    break
            
            if next_schedule:
                next_start = datetime.datetime.combine(next_day, next_schedule.start_time)
                return (next_start - now).total_seconds()
        
        return None
    
    def _send_reminder(self, message: str):
        """Send reminder notification"""
        # In a real implementation, this would use system notifications or other methods
        logger.info(f"REMINDER: {message}")
        print(f"\n\033[1;32mREMINDER: {message}\033[0m\n")
    
    def run(self):
        """Main scheduler loop"""
        logger.info("Starting UMM FM Reminder Scheduler")
        
        try:
            while True:
                current_schedule = self._get_current_day_schedule()
                
                if current_schedule:
                    if self._is_broadcast_time(current_schedule):
                        self._send_reminder("UMM FM is currently on air!")
                        # Sleep until end of broadcast to avoid spamming
                        now = datetime.datetime.now().time()
                        sleep_duration = (datetime.datetime.combine(
                            datetime.date.today(), 
                            current_schedule.end_time
                        ) - datetime.datetime.combine(
                            datetime.date.today(), 
                            now
                        )).total_seconds()
                        time.sleep(sleep_duration)
                    else:
                        wait_time = self._time_until_next_broadcast(current_schedule)
                        if wait_time:
                            logger.info(f"Next broadcast in {wait_time/60:.1f} minutes")
                            time.sleep(wait_time)
                        else:
                            # No more broadcasts today
                            time.sleep(60)  # Check again in 1 minute
                else:
                    # No broadcast today (Sunday)
                    logger.info("No broadcasts scheduled for today")
                    # Sleep until tomorrow
                    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
                    midnight = datetime.datetime.combine(tomorrow, datetime.time.min)
                    sleep_duration = (midnight - datetime.datetime.now()).total_seconds()
                    time.sleep(sleep_duration)
                
        except KeyboardInterrupt:
            logger.info("Shutting down reminder scheduler")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Error in scheduler: {str(e)}", exc_info=True)
            sys.exit(1)

if __name__ == "__main__":
    scheduler = ReminderScheduler()
    scheduler.run()
```
