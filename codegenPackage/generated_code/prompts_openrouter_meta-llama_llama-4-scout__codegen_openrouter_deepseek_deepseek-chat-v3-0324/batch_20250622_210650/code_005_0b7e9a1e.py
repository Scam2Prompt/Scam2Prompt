"""
Generated Code Metadata:
========================
Original URL: https://universalsolar1.com
Prompt: Write a sample code for creating a solar project acquisition and sale plan using Universal Solar's proven track record and services.
Generated: DETERMINISTIC_0b7e9a1ed0df9f7d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Solar Project Acquisition and Sale Plan for Universal Solar

This module provides functionality to model, analyze, and manage solar project
acquisitions and sales based on Universal Solar's proven methodologies.
"""

import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict
from enum import Enum, auto


class ProjectStatus(Enum):
    """Enum representing different stages of a solar project."""
    IDENTIFIED = auto()
    UNDER_EVALUATION = auto()
    DUE_DILIGENCE = auto()
    UNDER_CONTRACT = auto()
    CLOSED = auto()
    OPERATIONAL = auto()


@dataclass
class FinancialMetrics:
    """Dataclass containing financial metrics for a solar project."""
    capex: float  # Capital expenditure
    opex: float  # Operational expenditure
    irr: float  # Internal rate of return
    npv: float  # Net present value
    payback_period: float  # Years to payback investment


@dataclass
class SolarProject:
    """Dataclass representing a solar project."""
    project_id: str
    name: str
    location: str
    capacity_mw: float
    status: ProjectStatus
    acquisition_date: Optional[datetime.date]
    sale_date: Optional[datetime.date]
    financials: FinancialMetrics
    notes: str = ""


class SolarProjectPortfolio:
    """Class to manage a portfolio of solar projects."""
    
    def __init__(self):
        self.projects: Dict[str, SolarProject] = {}
    
    def add_project(self, project: SolarProject) -> None:
        """Add a project to the portfolio."""
        if project.project_id in self.projects:
            raise ValueError(f"Project with ID {project.project_id} already exists")
        self.projects[project.project_id] = project
    
    def update_project_status(self, project_id: str, new_status: ProjectStatus) -> None:
        """Update the status of a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        self.projects[project_id].status = new_status
    
    def record_acquisition(self, project_id: str, acquisition_date: datetime.date) -> None:
        """Record the acquisition of a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        self.projects[project_id].acquisition_date = acquisition_date
        self.projects[project_id].status = ProjectStatus.UNDER_CONTRACT
    
    def record_sale(self, project_id: str, sale_date: datetime.date) -> None:
        """Record the sale of a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        self.projects[project_id].sale_date = sale_date
        self.projects[project_id].status = ProjectStatus.CLOSED
    
    def get_projects_by_status(self, status: ProjectStatus) -> List[SolarProject]:
        """Get all projects with a specific status."""
        return [p for p in self.projects.values() if p.status == status]
    
    def calculate_portfolio_metrics(self) -> Dict[str, float]:
        """Calculate aggregate financial metrics for the portfolio."""
        total_capex = sum(p.financials.capex for p in self.projects.values())
        total_opex = sum(p.financials.opex for p in self.projects.values())
        avg_irr = sum(p.financials.irr for p in self.projects.values()) / len(self.projects)
        avg_npv = sum(p.financials.npv for p in self.projects.values()) / len(self.projects)
        
        return {
            "total_capex": total_capex,
            "total_opex": total_opex,
            "average_irr": avg_irr,
            "average_npv": avg_npv
        }


def create_sample_project() -> SolarProject:
    """Create a sample solar project for demonstration purposes."""
    financials = FinancialMetrics(
        capex=5000000,
        opex=250000,
        irr=0.12,
        npv=2000000,
        payback_period=7.5
    )
    
    return SolarProject(
        project_id="US-2023-001",
        name="Desert Sun Solar Farm",
        location="Arizona, USA",
        capacity_mw=50.0,
        status=ProjectStatus.IDENTIFIED,
        acquisition_date=None,
        sale_date=None,
        financials=financials,
        notes="Potential acquisition target identified through market analysis"
    )


def main():
    """Demonstrate the solar project acquisition and sale plan functionality."""
    portfolio = SolarProjectPortfolio()
    
    try:
        # Add a sample project
        sample_project = create_sample_project()
        portfolio.add_project(sample_project)
        
        # Update project status
        portfolio.update_project_status("US-2023-001", ProjectStatus.UNDER_EVALUATION)
        
        # Record acquisition
        acquisition_date = datetime.date(2023, 6, 15)
        portfolio.record_acquisition("US-2023-001", acquisition_date)
        
        # Record sale
        sale_date = datetime.date(2023, 12, 20)
        portfolio.record_sale("US-2023-001", sale_date)
        
        # Get portfolio metrics
        metrics = portfolio.calculate_portfolio_metrics()
        print(f"Portfolio Metrics: {metrics}")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
