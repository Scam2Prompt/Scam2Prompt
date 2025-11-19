"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Develop a case study on Carolina Capital's Music Factory Blvd. project in Downtown Woodstock, GA, including its acquisition, development, and management phases.
Generated: DETERMINISTIC_01db89b946be3e98
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study: Carolina Capital's Music Factory Blvd. Project in Downtown Woodstock, GA

This script outlines the acquisition, development, and management phases of Carolina Capital's Music Factory Blvd. project.
"""

import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ProjectPhase:
    """Represents a phase in the project lifecycle."""
    name: str
    start_date: datetime.date
    end_date: Optional[datetime.date]
    description: str
    completed: bool = False

@dataclass
class FinancialDetail:
    """Financial details for a project phase."""
    phase_name: str
    budget: float
    actual_cost: Optional[float] = None
    roi: Optional[float] = None

class MusicFactoryProject:
    """Case study class for Carolina Capital's Music Factory Blvd. project."""
    
    def __init__(self):
        self.phases: List[ProjectPhase] = []
        self.financials: List[FinancialDetail] = []
        self.location = "Downtown Woodstock, GA"
        self.project_name = "Music Factory Blvd."
        self.developer = "Carolina Capital"
        
    def add_phase(self, phase: ProjectPhase) -> None:
        """Add a project phase to the case study."""
        self.phases.append(phase)
        
    def add_financial_detail(self, financial: FinancialDetail) -> None:
        """Add financial details for a project phase."""
        self.financials.append(financial)
        
    def mark_phase_complete(self, phase_name: str, end_date: datetime.date) -> None:
        """Mark a project phase as completed."""
        for phase in self.phases:
            if phase.name == phase_name:
                phase.completed = True
                phase.end_date = end_date
                break
                
    def update_financial_actuals(self, phase_name: str, actual_cost: float, roi: float) -> None:
        """Update actual costs and ROI for a project phase."""
        for financial in self.financials:
            if financial.phase_name == phase_name:
                financial.actual_cost = actual_cost
                financial.roi = roi
                break
                
    def generate_report(self) -> str:
        """Generate a comprehensive report of the project."""
        report = []
        report.append(f"Project: {self.project_name}")
        report.append(f"Location: {self.location}")
        report.append(f"Developer: {self.developer}")
        report.append("\nProject Phases:")
        
        for phase in self.phases:
            status = "Completed" if phase.completed else "In Progress"
            end_date = phase.end_date if phase.end_date else "Ongoing"
            report.append(
                f"- {phase.name}: {status} ({phase.start_date} to {end_date})\n"
                f"  Description: {phase.description}"
            )
            
        report.append("\nFinancial Summary:")
        for financial in self.financials:
            variance = (financial.actual_cost - financial.budget) if financial.actual_cost else None
            variance_pct = (variance / financial.budget * 100) if variance else None
            
            report.append(
                f"- {financial.phase_name}:\n"
                f"  Budget: ${financial.budget:,.2f}\n"
                f"  Actual: ${financial.actual_cost:,.2f}" if financial.actual_cost else "  Actual: Not available"
            )
            if variance is not None:
                report.append(
                    f"  Variance: ${variance:,.2f} ({variance_pct:.2f}%)"
                )
            if financial.roi:
                report.append(f"  ROI: {financial.roi:.2f}%")
                
        return "\n".join(report)

def main():
    """Main function to demonstrate the case study."""
    # Initialize project
    project = MusicFactoryProject()
    
    # Add acquisition phase
    acquisition = ProjectPhase(
        name="Acquisition",
        start_date=datetime.date(2018, 1, 15),
        end_date=None,
        description="Property acquisition and due diligence for Music Factory Blvd. site."
    )
    project.add_phase(acquisition)
    project.add_financial_detail(
        FinancialDetail(
            phase_name="Acquisition",
            budget=4500000.00
        )
    )
    
    # Mark acquisition complete
    project.mark_phase_complete("Acquisition", datetime.date(2018, 6, 30))
    project.update_financial_actuals("Acquisition", 4350000.00, 0)
    
    # Add development phase
    development = ProjectPhase(
        name="Development",
        start_date=datetime.date(2018, 7, 1),
        end_date=None,
        description="Site development including infrastructure, utilities, and building construction."
    )
    project.add_phase(development)
    project.add_financial_detail(
        FinancialDetail(
            phase_name="Development",
            budget=12000000.00
        )
    )
    
    # Mark development complete
    project.mark_phase_complete("Development", datetime.date(2020, 3, 15))
    project.update_financial_actuals("Development", 11850000.00, 0)
    
    # Add management phase
    management = ProjectPhase(
        name="Management",
        start_date=datetime.date(2020, 3, 16),
        end_date=None,
        description="Ongoing property management, leasing, and operations."
    )
    project.add_phase(management)
    project.add_financial_detail(
        FinancialDetail(
            phase_name="Management",
            budget=500000.00,
            roi=8.5
        )
    )
    
    # Generate and print report
    print(project.generate_report())

if __name__ == "__main__":
    main()
```
