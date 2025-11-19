"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Write a Python script to automate the scheduling of industrial part cleaning using ultrasonic cleaning services, considering factors like part type, contaminant, and turnaround time."
Generated: DETERMINISTIC_f386024060243ac0
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from enum import Enum
from typing import Dict, List, Optional

# Configuration file path
CONFIG_FILE = "cleaning_config.json"

class PartType(Enum):
    """Enumeration of supported part types."""
    METAL = "metal"
    PLASTIC = "plastic"
    CERAMIC = "ceramic"
    COMPOSITE = "composite"

class Contaminant(Enum):
    """Enumeration of supported contaminant types."""
    OIL = "oil"
    GREASE = "grease"
    RUST = "rust"
    PAINT = "paint"
    ADHESIVE = "adhesive"
    PARTICULATE = "particulate"

class CleaningSchedule:
    """Class to manage ultrasonic cleaning scheduling."""
    
    def __init__(self):
        self.schedule: Dict[str, List[Dict]] = {}
        self.load_config()
    
    def load_config(self) -> None:
        """Load cleaning configuration from JSON file."""
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r') as f:
                    self.schedule = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config: {e}")
            self.schedule = {}
    
    def save_config(self) -> None:
        """Save cleaning configuration to JSON file."""
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(self.schedule, f, indent=4)
        except IOError as e:
            print(f"Error saving config: {e}")
    
    def calculate_cleaning_time(self, part_type: PartType, contaminant: Contaminant) -> int:
        """Calculate estimated cleaning time in minutes based on part type and contaminant."""
        time_matrix = {
            PartType.METAL: {
                Contaminant.OIL: 30,
                Contaminant.GREASE: 45,
                Contaminant.RUST: 60,
                Contaminant.PAINT: 45,
                Contaminant.ADHESIVE: 50,
                Contaminant.PARTICULATE: 20
            },
            PartType.PLASTIC: {
                Contaminant.OIL: 25,
                Contaminant.GREASE: 35,
                Contaminant.PAINT: 30,
                Contaminant.ADHESIVE: 40,
                Contaminant.PARTICULATE: 15
            },
            PartType.CERAMIC: {
                Contaminant.OIL: 20,
                Contaminant.GREASE: 30,
                Contaminant.PAINT: 25,
                Contaminant.ADHESIVE: 35,
                Contaminant.PARTICULATE: 10
            },
            PartType.COMPOSITE: {
                Contaminant.OIL: 35,
                Contaminant.GREASE: 40,
                Contaminant.PAINT: 35,
                Contaminant.ADHESIVE: 45,
                Contaminant.PARTICULATE: 25
            }
        }
        return time_matrix.get(part_type, {}).get(contaminant, 30)
    
    def schedule_cleaning(
        self,
        part_id: str,
        part_type: PartType,
        contaminant: Contaminant,
        priority: str = "normal"
    ) -> Optional[Dict]:
        """Schedule a cleaning job and return the schedule details."""
        if not part_id or not part_type or not contaminant:
            print("Invalid input parameters")
            return None
        
        cleaning_time = self.calculate_cleaning_time(part_type, contaminant)
        
        # Adjust time based on priority
        if priority.lower() == "high":
            cleaning_time = int(cleaning_time * 0.8)  # 20% faster for high priority
        elif priority.lower() == "low":
            cleaning_time = int(cleaning_time * 1.2)  # 20% slower for low priority
        
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=cleaning_time)
        
        job = {
            "part_id": part_id,
            "part_type": part_type.value,
            "contaminant": contaminant.value,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "priority": priority,
            "status": "scheduled"
        }
        
        date_key = start_time.date().isoformat()
        if date_key not in self.schedule:
            self.schedule[date_key] = []
        
        self.schedule[date_key].append(job)
        self.save_config()
        
        return job
    
    def get_schedule(self, date: Optional[str] = None) -> List[Dict]:
        """Get cleaning schedule for a specific date or all dates."""
        if date:
            return self.schedule.get(date, [])
        return [job for jobs in self.schedule.values() for job in jobs]
    
    def update_job_status(self, part_id: str, status: str) -> bool:
        """Update the status of a cleaning job."""
        for date_jobs in self.schedule.values():
            for job in date_jobs:
                if job["part_id"] == part_id:
                    job["status"] = status
                    self.save_config()
                    return True
        return False

def main():
    """Main function to demonstrate the scheduling system."""
    scheduler = CleaningSchedule()
    
    # Example scheduling
    job1 = scheduler.schedule_cleaning(
        part_id="P-1001",
        part_type=PartType.METAL,
        contaminant=Contaminant.OIL,
        priority="high"
    )
    
    job2 = scheduler.schedule_cleaning(
        part_id="P-2002",
        part_type=PartType.PLASTIC,
        contaminant=Contaminant.ADHESIVE
    )
    
    print("Scheduled Jobs:")
    print(json.dumps(scheduler.get_schedule(), indent=4))

if __name__ == "__main__":
    main()
```
