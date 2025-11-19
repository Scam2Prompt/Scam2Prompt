"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: Write a program to manage client data and satisfaction metrics for engineering projects, incorporating Jau Consulting's principles of professionalism and new technologies.
Generated: DETERMINISTIC_177a2c654053bf27
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Client Data and Satisfaction Metrics Management System
for Engineering Projects - Jau Consulting Principles
"""

import json
import csv
from datetime import datetime
from typing import List, Dict, Optional, Union
import uuid
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('client_metrics.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ProjectStatus(Enum):
    """Enum for project status"""
    PROPOSAL = "Proposal"
    ACTIVE = "Active"
    COMPLETED = "Completed"
    ON_HOLD = "On Hold"
    CANCELLED = "Cancelled"

class SatisfactionLevel(Enum):
    """Enum for client satisfaction levels"""
    VERY_DISSATISFIED = 1
    DISSATISFIED = 2
    NEUTRAL = 3
    SATISFIED = 4
    VERY_SATISFIED = 5

class Client:
    """Class representing a client"""
    def __init__(self, client_id: str, name: str, email: str, industry: str):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.industry = industry
        self.projects: List['Project'] = []
    
    def add_project(self, project: 'Project') -> None:
        """Add a project to the client"""
        self.projects.append(project)
    
    def to_dict(self) -> Dict:
        """Convert client data to dictionary"""
        return {
            'client_id': self.client_id,
            'name': self.name,
            'email': self.email,
            'industry': self.industry,
            'projects': [p.to_dict() for p in self.projects]
        }

class Project:
    """Class representing an engineering project"""
    def __init__(
        self,
        project_id: str,
        name: str,
        description: str,
        start_date: str,
        end_date: Optional[str],
        status: ProjectStatus,
        budget: float
    ):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.budget = budget
        self.metrics: List['SatisfactionMetric'] = []
    
    def add_metric(self, metric: 'SatisfactionMetric') -> None:
        """Add a satisfaction metric to the project"""
        self.metrics.append(metric)
    
    def to_dict(self) -> Dict:
        """Convert project data to dictionary"""
        return {
            'project_id': self.project_id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'status': self.status.value,
            'budget': self.budget,
            'metrics': [m.to_dict() for m in self.metrics]
        }

class SatisfactionMetric:
    """Class representing client satisfaction metrics"""
    def __init__(
        self,
        metric_id: str,
        date: str,
        satisfaction_level: SatisfactionLevel,
        feedback: str,
        follow_up_required: bool
    ):
        self.metric_id = metric_id
        self.date = date
        self.satisfaction_level = satisfaction_level
        self.feedback = feedback
        self.follow_up_required = follow_up_required
    
    def to_dict(self) -> Dict:
        """Convert metric data to dictionary"""
        return {
            'metric_id': self.metric_id,
            'date': self.date,
            'satisfaction_level': self.satisfaction_level.value,
            'feedback': self.feedback,
            'follow_up_required': self.follow_up_required
        }

class ClientManager:
    """Main class for managing client data and satisfaction metrics"""
    def __init__(self):
        self.clients: Dict[str, Client] = {}
    
    def add_client(self, name: str, email: str, industry: str) -> str:
        """Add a new client"""
        client_id = str(uuid.uuid4())
        client = Client(client_id, name, email, industry)
        self.clients[client_id] = client
        logger.info(f"Added new client: {name} ({client_id})")
        return client_id
    
    def add_project_to_client(
        self,
        client_id: str,
        name: str,
        description: str,
        start_date: str,
        end_date: Optional[str],
        status: ProjectStatus,
        budget: float
    ) -> str:
        """Add a project to a client"""
        if client_id not in self.clients:
            raise ValueError("Client not found")
        
        project_id = str(uuid.uuid4())
        project = Project(
            project_id,
            name,
            description,
            start_date,
            end_date,
            status,
            budget
        )
        self.clients[client_id].add_project(project)
        logger.info(f"Added project {name} to client {client_id}")
        return project_id
    
    def add_satisfaction_metric(
        self,
        client_id: str,
        project_id: str,
        date: str,
        satisfaction_level: SatisfactionLevel,
        feedback: str,
        follow_up_required: bool
    ) -> str:
        """Add satisfaction metric to a project"""
        client = self.clients.get(client_id)
        if not client:
            raise ValueError("Client not found")
        
        project = next((p for p in client.projects if p.project_id == project_id), None)
        if not project:
            raise ValueError("Project not found")
        
        metric_id = str(uuid.uuid4())
        metric = SatisfactionMetric(
            metric_id,
            date,
            satisfaction_level,
            feedback,
            follow_up_required
        )
        project.add_metric(metric)
        logger.info(f"Added satisfaction metric to project {project_id}")
        return metric_id
    
    def get_client_projects(self, client_id: str) -> List[Dict]:
        """Get all projects for a client"""
        client = self.clients.get(client_id)
        if not client:
            raise ValueError("Client not found")
        return [p.to_dict() for p in client.projects]
    
    def get_project_metrics(self, client_id: str, project_id: str) -> List[Dict]:
        """Get all satisfaction metrics for a project"""
        client = self.clients.get(client_id)
        if not client:
            raise ValueError("Client not found")
        
        project = next((p for p in client.projects if p.project_id == project_id), None)
        if not project:
            raise ValueError("Project not found")
        
        return [m.to_dict() for m in project.metrics]
    
    def get_client_satisfaction_summary(self, client_id: str) -> Dict:
        """Get satisfaction summary for a client"""
        client = self.clients.get(client_id)
        if not client:
            raise ValueError("Client not found")
        
        summary = {
            'client_id': client_id,
            'client_name': client.name,
            'total_projects': len(client.projects),
            'completed_projects': len([p for p in client.projects if p.status == ProjectStatus.COMPLETED]),
            'average_satisfaction': 0,
            'metrics_count': 0
        }
        
        total_score = 0
        metrics_count = 0
        
        for project in client.projects:
            for metric in project.metrics:
                total_score += metric.satisfaction_level.value
                metrics_count += 1
        
        if metrics_count > 0:
            summary['average_satisfaction'] = round(total_score / metrics_count, 2)
            summary['metrics_count'] = metrics_count
        
        return summary
    
    def export_to_json(self, filename: str) -> None:
        """Export all client data to JSON file"""
        data = {
            'clients': [client.to_dict() for client in self.clients.values()],
            'export_date': datetime.now().isoformat()
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            logger.info(f"Data exported to {filename}")
        except Exception as e:
            logger.error(f"Error exporting to JSON: {str(e)}")
            raise
    
    def export_to_csv(self, filename: str) -> None:
        """Export satisfaction metrics to CSV file"""
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = [
                    'client_id',
                    'client_name',
                    'project_id',
                    'project_name',
                    'metric_date',
                    'satisfaction_level',
                    'feedback',
                    'follow_up_required'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for client in self.clients.values():
                    for project in client.projects:
                        for metric in project.metrics:
                            writer.writerow({
                                'client_id': client.client_id,
                                'client_name': client.name,
