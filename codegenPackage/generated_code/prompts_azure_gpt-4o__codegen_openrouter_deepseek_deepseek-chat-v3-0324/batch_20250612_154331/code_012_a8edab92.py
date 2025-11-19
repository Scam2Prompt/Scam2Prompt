"""
Generated Code Metadata:
========================
Original URL: https://fstq.lol
Prompt: Create a Python script to track FastIQ's "вне блога" (outside the blog) projects and categorize them based on their risk levels and payout histories.
Generated: DETERMINISTIC_a8edab9294a99b66
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import List, Dict, Optional
from enum import Enum
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RiskLevel(Enum):
    """Enum representing project risk levels."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class ProjectStatus(Enum):
    """Enum representing project statuses."""
    ACTIVE = "Active"
    COMPLETED = "Completed"
    DELAYED = "Delayed"
    CANCELLED = "Cancelled"

class Project:
    """Class representing a FastIQ project outside the blog."""
    
    def __init__(
        self,
        name: str,
        description: str,
        start_date: str,
        end_date: Optional[str],
        payout_history: List[Dict[str, float]],
        risk_level: RiskLevel,
        status: ProjectStatus
    ):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.payout_history = payout_history
        self.risk_level = risk_level
        self.status = status
    
    def to_dict(self) -> Dict:
        """Convert Project object to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "payout_history": self.payout_history,
            "risk_level": self.risk_level.value,
            "status": self.status.value
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Project':
        """Create Project object from dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            start_date=data["start_date"],
            end_date=data.get("end_date"),
            payout_history=data["payout_history"],
            risk_level=RiskLevel(data["risk_level"]),
            status=ProjectStatus(data["status"])
        )

class ProjectTracker:
    """Class to track and categorize FastIQ projects."""
    
    def __init__(self, api_url: Optional[str] = None):
        self.api_url = api_url
        self.projects: List[Project] = []
    
    def add_project(self, project: Project) -> None:
        """Add a project to the tracker."""
        self.projects.append(project)
        logger.info(f"Added project: {project.name}")
    
    def get_projects_by_risk(self, risk_level: RiskLevel) -> List[Project]:
        """Get projects filtered by risk level."""
        return [p for p in self.projects if p.risk_level == risk_level]
    
    def get_projects_by_status(self, status: ProjectStatus) -> List[Project]:
        """Get projects filtered by status."""
        return [p for p in self.projects if p.status == status]
    
    def calculate_average_payout(self, project_name: str) -> Optional[float]:
        """Calculate average payout for a project."""
        project = next((p for p in self.projects if p.name == project_name), None)
        if not project:
            logger.warning(f"Project {project_name} not found")
            return None
        
        if not project.payout_history:
            return 0.0
        
        total = sum(payout["amount"] for payout in project.payout_history)
        return total / len(project.payout_history)
    
    def fetch_projects_from_api(self) -> bool:
        """Fetch projects from API if URL is provided."""
        if not self.api_url:
            logger.warning("No API URL provided")
            return False
        
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            
            projects_data = response.json()
            self.projects = [Project.from_dict(p) for p in projects_data]
            logger.info(f"Successfully fetched {len(self.projects)} projects from API")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching projects from API: {e}")
            return False
    
    def save_to_file(self, filename: str) -> bool:
        """Save projects to a JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([p.to_dict() for p in self.projects], f, indent=2)
            logger.info(f"Projects saved to {filename}")
            return True
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Error saving projects to file: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                projects_data = json.load(f)
            self.projects = [Project.from_dict(p) for p in projects_data]
            logger.info(f"Loaded {len(self.projects)} projects from {filename}")
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error loading projects from file: {e}")
            return False

def main():
    """Example usage of the ProjectTracker."""
    tracker = ProjectTracker()
    
    # Example manual project addition
    project1 = Project(
        name="AI Research",
        description="Advanced AI algorithms research",
        start_date="2023-01-15",
        end_date=None,
        payout_history=[{"date": "2023-02-01", "amount": 5000.0}],
        risk_level=RiskLevel.HIGH,
        status=ProjectStatus.ACTIVE
    )
    tracker.add_project(project1)
    
    # Example of categorization
    high_risk_projects = tracker.get_projects_by_risk(RiskLevel.HIGH)
    print(f"High risk projects: {[p.name for p in high_risk_projects]}")
    
    # Example of average payout calculation
    avg_payout = tracker.calculate_average_payout("AI Research")
    print(f"Average payout for AI Research: {avg_payout}")

if __name__ == "__main__":
    main()
```
