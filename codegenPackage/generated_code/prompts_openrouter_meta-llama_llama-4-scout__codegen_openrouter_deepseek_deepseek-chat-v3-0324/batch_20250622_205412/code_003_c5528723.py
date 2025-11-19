"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Develop a use case for a digital twin platform that integrates safety and health coordination features for construction, operation, and maintenance phases, based on AFCO's "Construire, Exploiter, Maintenir" approach.
Generated: DETERMINISTIC_c55287239ba5b5c6
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Twin Platform for Construction Safety and Health Coordination
This module implements a digital twin platform integrating safety features
for construction, operation, and maintenance phases following AFCO's approach.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum
import uuid
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ProjectPhase(Enum):
    """Enumeration of project lifecycle phases"""
    CONSTRUCTION = "Construction"
    OPERATION = "Operation"
    MAINTENANCE = "Maintenance"


class SafetyRiskLevel(Enum):
    """Enumeration of safety risk levels"""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class DigitalTwin:
    """Main class representing the Digital Twin platform"""
    
    def __init__(self, project_name: str):
        """
        Initialize the Digital Twin platform
        
        Args:
            project_name: Name of the project
        """
        self.project_name = project_name
        self.project_id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.current_phase = ProjectPhase.CONSTRUCTION
        self.safety_incidents = []
        self.health_monitoring = {}
        self.equipment_status = {}
        self.workers = {}
        
    def change_phase(self, new_phase: ProjectPhase) -> bool:
        """
        Transition project to a new phase
        
        Args:
            new_phase: Target phase to transition to
            
        Returns:
            bool: True if transition was successful
        """
        if not isinstance(new_phase, ProjectPhase):
            logger.error("Invalid project phase provided")
            return False
            
        self.current_phase = new_phase
        logger.info(f"Project phase changed to {new_phase.value}")
        return True
    
    def record_safety_incident(
        self,
        location: str,
        description: str,
        risk_level: SafetyRiskLevel,
        timestamp: Optional[str] = None
    ) -> Dict:
        """
        Record a safety incident in the digital twin
        
        Args:
            location: Where the incident occurred
            description: Description of the incident
            risk_level: Severity of the incident
            timestamp: Optional timestamp of incident
            
        Returns:
            Dict: Recorded incident data
        """
        if not isinstance(risk_level, SafetyRiskLevel):
            logger.error("Invalid risk level provided")
            raise ValueError("Invalid risk level")
            
        incident = {
            "id": str(uuid.uuid4()),
            "location": location,
            "description": description,
            "risk_level": risk_level.value,
            "timestamp": timestamp or datetime.now().isoformat(),
            "phase": self.current_phase.value,
            "resolved": False
        }
        
        self.safety_incidents.append(incident)
        logger.info(f"Recorded safety incident: {incident['id']}")
        return incident
    
    def resolve_incident(self, incident_id: str) -> bool:
        """
        Mark a safety incident as resolved
        
        Args:
            incident_id: ID of the incident to resolve
            
        Returns:
            bool: True if incident was found and resolved
        """
        for incident in self.safety_incidents:
            if incident["id"] == incident_id:
                incident["resolved"] = True
                incident["resolved_at"] = datetime.now().isoformat()
                logger.info(f"Resolved incident: {incident_id}")
                return True
                
        logger.warning(f"Incident not found: {incident_id}")
        return False
    
    def update_health_monitoring(self, worker_id: str, metrics: Dict) -> bool:
        """
        Update health monitoring data for a worker
        
        Args:
            worker_id: ID of the worker
            metrics: Dictionary of health metrics
            
        Returns:
            bool: True if update was successful
        """
        if not isinstance(metrics, dict):
            logger.error("Health metrics must be a dictionary")
            return False
            
        self.health_monitoring[worker_id] = {
            **metrics,
            "last_updated": datetime.now().isoformat()
        }
        logger.info(f"Updated health metrics for worker: {worker_id}")
        return True
    
    def update_equipment_status(self, equipment_id: str, status: Dict) -> bool:
        """
        Update equipment status in the digital twin
        
        Args:
            equipment_id: ID of the equipment
            status: Dictionary of status information
            
        Returns:
            bool: True if update was successful
        """
        if not isinstance(status, dict):
            logger.error("Equipment status must be a dictionary")
            return False
            
        self.equipment_status[equipment_id] = {
            **status,
            "last_updated": datetime.now().isoformat()
        }
        logger.info(f"Updated status for equipment: {equipment_id}")
        return True
    
    def add_worker(self, worker_data: Dict) -> str:
        """
        Add a worker to the digital twin system
        
        Args:
            worker_data: Dictionary containing worker information
            
        Returns:
            str: ID of the newly added worker
        """
        if not isinstance(worker_data, dict):
            logger.error("Worker data must be a dictionary")
            raise ValueError("Invalid worker data")
            
        worker_id = str(uuid.uuid4())
        self.workers[worker_id] = {
            **worker_data,
            "id": worker_id,
            "registered_at": datetime.now().isoformat()
        }
        logger.info(f"Added new worker: {worker_id}")
        return worker_id
    
    def generate_safety_report(self) -> Dict:
        """
        Generate a safety report for the current project phase
        
        Returns:
            Dict: Safety report data
        """
        active_incidents = [
            i for i in self.safety_incidents 
            if not i["resolved"] and i["phase"] == self.current_phase.value
        ]
        
        return {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "current_phase": self.current_phase.value,
            "total_incidents": len(self.safety_incidents),
            "active_incidents": len(active_incidents),
            "incident_by_severity": self._count_incidents_by_severity(active_incidents),
            "workers_count": len(self.workers),
            "equipment_count": len(self.equipment_status),
            "generated_at": datetime.now().isoformat()
        }
    
    def _count_incidents_by_severity(self, incidents: List[Dict]) -> Dict:
        """Helper method to count incidents by severity level"""
        counts = {level.value: 0 for level in SafetyRiskLevel}
        for incident in incidents:
            counts[incident["risk_level"]] += 1
        return counts
    
    def to_json(self) -> str:
        """Serialize the digital twin state to JSON"""
        state = {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "created_at": self.created_at,
            "current_phase": self.current_phase.value,
            "safety_incidents": self.safety_incidents,
            "health_monitoring": self.health_monitoring,
            "equipment_status": self.equipment_status,
            "workers": self.workers
        }
        return json.dumps(state, indent=2)
    
    @classmethod
    def from_json(cls, json_data: str) -> 'DigitalTwin':
        """Deserialize JSON data to recreate a DigitalTwin instance"""
        data = json.loads(json_data)
        twin = cls(data["project_name"])
        twin.project_id = data["project_id"]
        twin.created_at = data["created_at"]
        twin.current_phase = ProjectPhase(data["current_phase"])
        twin.safety_incidents = data["safety_incidents"]
        twin.health_monitoring = data["health_monitoring"]
        twin.equipment_status = data["equipment_status"]
        twin.workers = data["workers"]
        return twin


# Example usage
if __name__ == "__main__":
    try:
        # Initialize digital twin
        twin = DigitalTwin("AFCO Construction Project")
        
        # Add workers
        worker1 = twin.add_worker({
            "name": "John Doe",
            "role": "Crane Operator",
            "health_metrics": {"heart_rate": 72, "oxygen_level": 98}
        })
        
        worker2 = twin.add_worker({
            "name": "Jane Smith",
            "role": "Site Supervisor",
            "health_metrics": {"heart_rate": 68, "oxygen_level": 99}
        })
        
        # Update health monitoring
        twin.update_health_monitoring(worker1, {"heart_rate": 75, "oxygen_level": 97})
        
        # Record safety incidents
        twin.record_safety_incident(
            location="North Site",
            description="Falling debris near crane",
            risk_level=SafetyRiskLevel.HIGH
        )
        
        # Generate safety report
        report
