"""
Generated Code Metadata:
========================
Original URL: https://sosmenuiserie.fr
Prompt: How would you implement a scheduling system for emergency services, like those provided by SOS Menuiserie, using a programming language of your choice?
Generated: DETERMINISTIC_05a25d55c02687fe
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import heapq
from enum import Enum
from typing import List, Dict, Optional, Tuple


class EmergencyLevel(Enum):
    """Priority levels for emergency services."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Technician:
    """Represents a technician available for emergency services."""
    def __init__(self, id: int, name: str, skills: List[str], location: Tuple[float, float]):
        self.id = id
        self.name = name
        self.skills = skills
        self.location = location  # (latitude, longitude)
        self.available = True
        self.current_job = None


class EmergencyJob:
    """Represents an emergency service request."""
    def __init__(self, id: int, description: str, location: Tuple[float, float], 
                 emergency_level: EmergencyLevel, required_skills: List[str], 
                 created_at: datetime.datetime = datetime.datetime.now()):
        self.id = id
        self.description = description
        self.location = location
        self.emergency_level = emergency_level
        self.required_skills = required_skills
        self.created_at = created_at
        self.assigned_technician = None
        self.completed = False


class Scheduler:
    """Manages scheduling of emergency jobs to technicians."""
    def __init__(self):
        self.technicians: Dict[int, Technician] = {}
        self.jobs: Dict[int, EmergencyJob] = {}
        self.job_queue = []
    
    def add_technician(self, technician: Technician) -> None:
        """Add a technician to the available pool."""
        if technician.id in self.technicians:
            raise ValueError(f"Technician with ID {technician.id} already exists")
        self.technicians[technician.id] = technician
    
    def create_job(self, job: EmergencyJob) -> None:
        """Create a new emergency job and add it to the queue."""
        if job.id in self.jobs:
            raise ValueError(f"Job with ID {job.id} already exists")
        self.jobs[job.id] = job
        # Priority queue based on emergency level and creation time
        heapq.heappush(self.job_queue, (
            -job.emergency_level.value,  # Negative for max-heap
            job.created_at.timestamp(),
            job.id
        ))
    
    def _calculate_distance(self, loc1: Tuple[float, float], loc2: Tuple[float, float]) -> float:
        """Calculate approximate distance between two points (simplified for demo)."""
        # In production, use proper geospatial calculation (e.g., Haversine formula)
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    
    def _find_best_technician(self, job: EmergencyJob) -> Optional[Technician]:
        """Find the best available technician for a job."""
        available_techs = [t for t in self.technicians.values() 
                          if t.available and 
                          all(skill in t.skills for skill in job.required_skills)]
        
        if not available_techs:
            return None
        
        # Find technician with minimum distance to job location
        best_tech = min(
            available_techs,
            key=lambda t: self._calculate_distance(t.location, job.location)
        )
        return best_tech
    
    def assign_jobs(self) -> Dict[int, Optional[int]]:
        """Assign jobs to technicians based on priority and availability.
        Returns a dictionary mapping job IDs to assigned technician IDs (or None)."""
        assignments = {}
        temp_queue = []
        
        while self.job_queue:
            _, _, job_id = heapq.heappop(self.job_queue)
            job = self.jobs[job_id]
            
            if job.completed or job.assigned_technician:
                continue
                
            technician = self._find_best_technician(job)
            if technician:
                job.assigned_technician = technician.id
                technician.available = False
                technician.current_job = job.id
                assignments[job.id] = technician.id
            else:
                assignments[job.id] = None
                temp_queue.append((-job.emergency_level.value, job.created_at.timestamp(), job.id))
        
        # Re-add unassigned jobs to the queue
        for item in temp_queue:
            heapq.heappush(self.job_queue, item)
        
        return assignments
    
    def complete_job(self, job_id: int) -> None:
        """Mark a job as completed and free up the technician."""
        if job_id not in self.jobs:
            raise ValueError(f"Job with ID {job_id} not found")
        
        job = self.jobs[job_id]
        if job.completed:
            return
            
        if job.assigned_technician:
            technician = self.technicians[job.assigned_technician]
            technician.available = True
            technician.current_job = None
        
        job.completed = True
    
    def get_job_status(self, job_id: int) -> Dict:
        """Get the status of a job."""
        if job_id not in self.jobs:
            raise ValueError(f"Job with ID {job_id} not found")
        
        job = self.jobs[job_id]
        return {
            "id": job.id,
            "description": job.description,
            "status": "completed" if job.completed else 
                     "assigned" if job.assigned_technician else "pending",
            "assigned_technician": job.assigned_technician,
            "emergency_level": job.emergency_level.name,
            "created_at": job.created_at.isoformat()
        }


# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()
    
    # Add some technicians
    scheduler.add_technician(Technician(
        id=1,
        name="Jean Dupont",
        skills=["window_repair", "door_repair"],
        location=(48.8566, 2.3522)  # Paris
    ))
    
    scheduler.add_technician(Technician(
        id=2,
        name="Marie Curie",
        skills=["lock_repair", "door_repair"],
        location=(48.8534, 2.3488)  # Near Paris
    ))
    
    # Create some emergency jobs
    scheduler.create_job(EmergencyJob(
        id=101,
        description="Broken window in living room",
        location=(48.8570, 2.3525),
        emergency_level=EmergencyLevel.HIGH,
        required_skills=["window_repair"]
    ))
    
    scheduler.create_job(EmergencyJob(
        id=102,
        description="Front door lock broken",
        location=(48.8550, 2.3500),
        emergency_level=EmergencyLevel.CRITICAL,
        required_skills=["lock_repair"],
        created_at=datetime.datetime.now() - datetime.timedelta(minutes=30)
    ))
    
    # Assign jobs
    assignments = scheduler.assign_jobs()
    print("Job assignments:", assignments)
    
    # Check status
    print("Job 101 status:", scheduler.get_job_status(101))
    print("Job 102 status:", scheduler.get_job_status(102))
    
    # Complete a job
    scheduler.complete_job(101)
    print("After completion - Job 101 status:", scheduler.get_job_status(101))
```
