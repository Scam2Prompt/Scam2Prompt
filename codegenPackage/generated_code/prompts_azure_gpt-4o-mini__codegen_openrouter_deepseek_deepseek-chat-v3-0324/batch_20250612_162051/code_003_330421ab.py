"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Develop a code example that demonstrates how to implement safety monitoring features in construction project management software, inspired by C&M Pinnacle's zero safety incident record.
Generated: DETERMINISTIC_330421abc73928f1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SafetyIncidentType(Enum):
    """Enumeration of possible safety incident types"""
    NEAR_MISS = auto()
    MINOR_INJURY = auto()
    MAJOR_INJURY = auto()
    FATALITY = auto()

@dataclass
class SafetyCheck:
    """Data class representing a safety check"""
    id: str
    name: str
    description: str
    required: bool
    completed: bool = False
    completed_by: Optional[str] = None
    completed_at: Optional[datetime.datetime] = None

@dataclass
class SafetyIncident:
    """Data class representing a safety incident"""
    id: str
    type: SafetyIncidentType
    description: str
    location: str
    reported_by: str
    reported_at: datetime.datetime
    resolved: bool = False
    resolution_notes: Optional[str] = None

class SafetyMonitor:
    """Class for managing safety monitoring in construction projects"""
    
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.safety_checks: List[SafetyCheck] = []
        self.incidents: List[SafetyIncident] = []
        self.zero_incident_days: int = 0
        self.last_incident_date: Optional[datetime.datetime] = None
    
    def add_safety_check(self, check: SafetyCheck) -> bool:
        """Add a new safety check to the project"""
        try:
            if any(c.id == check.id for c in self.safety_checks):
                logger.warning(f"Safety check with ID {check.id} already exists")
                return False
            self.safety_checks.append(check)
            logger.info(f"Added safety check: {check.name}")
            return True
        except Exception as e:
            logger.error(f"Error adding safety check: {e}")
            return False
    
    def complete_safety_check(self, check_id: str, completed_by: str) -> bool:
        """Mark a safety check as completed"""
        try:
            for check in self.safety_checks:
                if check.id == check_id:
                    check.completed = True
                    check.completed_by = completed_by
                    check.completed_at = datetime.datetime.now()
                    logger.info(f"Completed safety check: {check.name}")
                    return True
            logger.warning(f"Safety check with ID {check_id} not found")
            return False
        except Exception as e:
            logger.error(f"Error completing safety check: {e}")
            return False
    
    def report_incident(self, incident: SafetyIncident) -> bool:
        """Report a new safety incident"""
        try:
            if any(i.id == incident.id for i in self.incidents):
                logger.warning(f"Incident with ID {incident.id} already exists")
                return False
            
            self.incidents.append(incident)
            self.last_incident_date = datetime.datetime.now()
            logger.warning(f"New safety incident reported: {incident.type.name}")
            
            # Reset zero incident days counter
            self.zero_incident_days = 0
            return True
        except Exception as e:
            logger.error(f"Error reporting incident: {e}")
            return False
    
    def resolve_incident(self, incident_id: str, resolution_notes: str) -> bool:
        """Mark an incident as resolved"""
        try:
            for incident in self.incidents:
                if incident.id == incident_id:
                    incident.resolved = True
                    incident.resolution_notes = resolution_notes
                    logger.info(f"Resolved incident: {incident_id}")
                    return True
            logger.warning(f"Incident with ID {incident_id} not found")
            return False
        except Exception as e:
            logger.error(f"Error resolving incident: {e}")
            return False
    
    def update_zero_incident_days(self) -> None:
        """Update the zero incident days counter"""
        try:
            if not self.last_incident_date:
                self.zero_incident_days += 1
            else:
                days_since_last = (datetime.datetime.now() - self.last_incident_date).days
                self.zero_incident_days = days_since_last
            logger.info(f"Updated zero incident days: {self.zero_incident_days}")
        except Exception as e:
            logger.error(f"Error updating zero incident days: {e}")
    
    def get_safety_compliance(self) -> float:
        """Calculate safety compliance percentage based on completed checks"""
        try:
            if not self.safety_checks:
                return 100.0  # No checks means perfect compliance
            
            required_checks = [c for c in self.safety_checks if c.required]
            if not required_checks:
                return 100.0
            
            completed = sum(1 for c in required_checks if c.completed)
            return (completed / len(required_checks)) * 100
        except Exception as e:
            logger.error(f"Error calculating safety compliance: {e}")
            return 0.0
    
    def generate_safety_report(self) -> Dict:
        """Generate a comprehensive safety report"""
        try:
            self.update_zero_incident_days()
            
            report = {
                "project_id": self.project_id,
                "report_date": datetime.datetime.now().isoformat(),
                "safety_compliance": self.get_safety_compliance(),
                "zero_incident_days": self.zero_incident_days,
                "total_incidents": len(self.incidents),
                "open_incidents": sum(1 for i in self.incidents if not i.resolved),
                "incident_types": {
                    type.name: sum(1 for i in self.incidents if i.type == type)
                    for type in SafetyIncidentType
                },
                "pending_safety_checks": [
                    c.name for c in self.safety_checks 
                    if c.required and not c.completed
                ]
            }
            logger.info("Generated safety report")
            return report
        except Exception as e:
            logger.error(f"Error generating safety report: {e}")
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Initialize safety monitor for a project
    safety_monitor = SafetyMonitor("PROJ-2023-001")
    
    # Add some safety checks
    safety_monitor.add_safety_check(SafetyCheck(
        id="SC-001",
        name="Hard Hat Check",
        description="Verify all workers are wearing hard hats",
        required=True
    ))
    
    safety_monitor.add_safety_check(SafetyCheck(
        id="SC-002",
        name="Fall Protection Check",
        description="Verify fall protection systems are in place",
        required=True
    ))
    
    # Complete some checks
    safety_monitor.complete_safety_check("SC-001", "John Doe")
    
    # Generate initial report
    report = safety_monitor.generate_safety_report()
    print("Initial Safety Report:", report)
    
    # Report an incident
    safety_monitor.report_incident(SafetyIncident(
        id="INC-001",
        type=SafetyIncidentType.NEAR_MISS,
        description="Worker nearly fell from scaffolding",
        location="North building, 3rd floor",
        reported_by="Jane Smith",
        reported_at=datetime.datetime.now()
    ))
    
    # Generate updated report
    report = safety_monitor.generate_safety_report()
    print("Updated Safety Report:", report)
```
