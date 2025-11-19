"""
Generated Code Metadata:
========================
Original URL: https://octavepartners.com
Prompt: Create a script to model the workflow of Octave Partners' business acceleration services, including collaboration with affiliates and resource allocation.
Generated: DETERMINISTIC_8185f547114926d6
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Octave Partners Business Acceleration Workflow Model

This script models the workflow of Octave Partners' business acceleration services,
including collaboration with affiliates and resource allocation.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import random
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('octave_workflow.log'),
        logging.StreamHandler()
    ]
)

class ServiceType(Enum):
    """Types of business acceleration services offered"""
    STRATEGY = auto()
    OPERATIONS = auto()
    TECHNOLOGY = auto()
    FINANCE = auto()
    MARKETING = auto()

class ResourceType(Enum):
    """Types of resources available"""
    CONSULTANT = auto()
    ANALYST = auto()
    DEVELOPER = auto()
    DESIGNER = auto()
    CAPITAL = auto()

class ProjectStatus(Enum):
    """Possible project statuses"""
    PROPOSAL = auto()
    ACTIVE = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    CANCELLED = auto()

@dataclass
class Affiliate:
    """Represents an affiliate partner"""
    id: str
    name: str
    expertise: List[ServiceType]
    resources: Dict[ResourceType, int]
    location: str

@dataclass
class Project:
    """Represents a business acceleration project"""
    id: str
    name: str
    client: str
    services: List[ServiceType]
    required_resources: Dict[ResourceType, int]
    start_date: datetime
    end_date: datetime
    status: ProjectStatus = ProjectStatus.PROPOSAL
    affiliates: List[Affiliate] = None

    def __post_init__(self):
        if self.affiliates is None:
            self.affiliates = []

    def add_affiliate(self, affiliate: Affiliate) -> bool:
        """Add an affiliate to the project if they have matching expertise"""
        if any(expertise in affiliate.expertise for expertise in self.services):
            self.affiliates.append(affiliate)
            return True
        return False

    def check_resource_availability(self) -> bool:
        """Check if required resources are available across all affiliates"""
        available_resources = {rtype: 0 for rtype in self.required_resources}
        
        for affiliate in self.affiliates:
            for rtype, quantity in affiliate.resources.items():
                if rtype in available_resources:
                    available_resources[rtype] += quantity
        
        return all(
            available >= required 
            for required, available in zip(
                self.required_resources.values(), 
                available_resources.values()
            )
        )

    def allocate_resources(self) -> bool:
        """Allocate resources from affiliates to the project"""
        if not self.check_resource_availability():
            return False
        
        # Simple allocation strategy: distribute evenly across affiliates
        for rtype, required in self.required_resources.items():
            per_affiliate = max(1, required // len(self.affiliates))
            
            for affiliate in self.affiliates:
                if rtype in affiliate.resources:
                    allocated = min(per_affiliate, affiliate.resources[rtype])
                    affiliate.resources[rtype] -= allocated
                    required -= allocated
            
            if required > 0:
                # Distribute remaining
                for affiliate in self.affiliates:
                    if rtype in affiliate.resources and affiliate.resources[rtype] > 0:
                        allocated = min(required, affiliate.resources[rtype])
                        affiliate.resources[rtype] -= allocated
                        required -= allocated
                        if required == 0:
                            break
        
        self.status = ProjectStatus.ACTIVE
        return True

class OctaveWorkflow:
    """Main class modeling Octave Partners' workflow"""
    
    def __init__(self):
        self.projects: List[Project] = []
        self.affiliates: List[Affiliate] = []
    
    def add_affiliate(self, affiliate: Affiliate) -> None:
        """Register a new affiliate"""
        if affiliate not in self.affiliates:
            self.affiliates.append(affiliate)
            logging.info(f"Added affiliate: {affiliate.name}")
    
    def create_project(self, project: Project) -> bool:
        """Create a new project and attempt to assign affiliates"""
        if project.end_date <= project.start_date:
            logging.error("Project end date must be after start date")
            return False
            
        # Find suitable affiliates
        suitable_affiliates = [
            aff for aff in self.affiliates 
            if any(expertise in aff.expertise for expertise in project.services)
        ]
        
        if not suitable_affiliates:
            logging.error("No suitable affiliates found for project")
            return False
            
        # Add up to 3 affiliates (can be adjusted)
        for affiliate in suitable_affiliates[:3]:
            project.add_affiliate(affiliate)
        
        self.projects.append(project)
        logging.info(f"Created project: {project.name}")
        return True
    
    def allocate_project_resources(self, project_id: str) -> bool:
        """Allocate resources for a specific project"""
        project = next((p for p in self.projects if p.id == project_id), None)
        if not project:
            logging.error(f"Project {project_id} not found")
            return False
            
        if project.status != ProjectStatus.PROPOSAL:
            logging.error("Resources can only be allocated to proposal projects")
            return False
            
        return project.allocate_resources()
    
    def complete_project(self, project_id: str) -> bool:
        """Mark a project as completed and release resources"""
        project = next((p for p in self.projects if p.id == project_id), None)
        if not project:
            logging.error(f"Project {project_id} not found")
            return False
            
        if project.status != ProjectStatus.ACTIVE:
            logging.error("Only active projects can be completed")
            return False
            
        # Release resources back to affiliates
        for affiliate in project.affiliates:
            for rtype, quantity in project.required_resources.items():
                if rtype in affiliate.resources:
                    # Simple release - assumes all resources are returned
                    affiliate.resources[rtype] += quantity
        
        project.status = ProjectStatus.COMPLETED
        logging.info(f"Completed project: {project.name}")
        return True
    
    def get_project_status(self, project_id: str) -> Optional[ProjectStatus]:
        """Get the status of a project"""
        project = next((p for p in self.projects if p.id == project_id), None)
        return project.status if project else None
    
    def generate_report(self) -> Dict:
        """Generate a summary report of all projects and affiliates"""
        return {
            "total_projects": len(self.projects),
            "active_projects": sum(1 for p in self.projects if p.status == ProjectStatus.ACTIVE),
            "completed_projects": sum(1 for p in self.projects if p.status == ProjectStatus.COMPLETED),
            "total_affiliates": len(self.affiliates),
            "affiliate_utilization": self._calculate_affiliate_utilization()
        }
    
    def _calculate_affiliate_utilization(self) -> Dict[str, float]:
        """Calculate resource utilization across all affiliates"""
        utilization = {}
        for affiliate in self.affiliates:
            total_resources = sum(affiliate.resources.values())
            if total_resources > 0:
                utilization[affiliate.name] = sum(
                    project.required_resources.get(rtype, 0) 
                    for project in self.projects 
                    for rtype in project.required_resources
                    if affiliate in project.affiliates
                ) / total_resources
            else:
                utilization[affiliate.name] = 0.0
        return utilization

def sample_workflow() -> None:
    """Demonstrate the workflow with sample data"""
    workflow = OctaveWorkflow()
    
    # Create affiliates
    affiliates = [
        Affiliate(
            id="aff1",
            name="Tech Innovators",
            expertise=[ServiceType.TECHNOLOGY, ServiceType.STRATEGY],
            resources={
                ResourceType.CONSULTANT: 5,
                ResourceType.DEVELOPER: 10,
                ResourceType.ANALYST: 3
            },
            location="San Francisco"
        ),
        Affiliate(
            id="aff2",
            name="Growth Partners",
            expertise=[ServiceType.MARKETING, ServiceType.FINANCE],
            resources={
                ResourceType.CONSULTANT: 8,
                ResourceType.DESIGNER: 4,
                ResourceType.CAPITAL: 1000000
            },
            location="New York"
        )
    ]
    
    for affiliate in affiliates:
        workflow.add_affiliate(affiliate)
    
    # Create projects
    today = datetime.now()
    projects = [
        Project(
            id="proj1",
            name="E-commerce
