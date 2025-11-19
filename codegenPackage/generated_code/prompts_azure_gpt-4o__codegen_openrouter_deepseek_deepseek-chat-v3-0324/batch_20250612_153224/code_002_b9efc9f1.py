"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Generate code to calculate project timelines for infrastructure construction, ensuring compliance with safety and environmental regulations, similar to Unison Plus's approach.
Generated: DETERMINISTIC_b9efc9f1dfee7c85
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RegulationType(Enum):
    """Types of regulations that affect project timelines."""
    SAFETY = "Safety"
    ENVIRONMENTAL = "Environmental"
    ZONING = "Zoning"
    PERMITTING = "Permitting"


class ProjectPhase(Enum):
    """Phases of a construction project."""
    PLANNING = "Planning"
    DESIGN = "Design"
    PERMITTING = "Permitting"
    CONSTRUCTION = "Construction"
    INSPECTION = "Inspection"
    COMPLETION = "Completion"


class Regulation:
    """Represents a regulation that affects project timelines."""
    
    def __init__(
        self,
        name: str,
        regulation_type: RegulationType,
        required_days: int,
        description: str = ""
    ):
        self.name = name
        self.type = regulation_type
        self.required_days = required_days
        self.description = description


class ProjectTimeline:
    """Calculates and manages project timelines with regulatory compliance."""
    
    def __init__(self, project_name: str, start_date: datetime.date):
        self.project_name = project_name
        self.start_date = start_date
        self.phases: Dict[ProjectPhase, int] = {}
        self.regulations: List[Regulation] = []
        self.contingency_days = 0
    
    def add_phase(self, phase: ProjectPhase, duration_days: int) -> None:
        """Add a project phase with its duration."""
        if phase in self.phases:
            raise ValueError(f"Phase {phase} already exists in the project.")
        if duration_days <= 0:
            raise ValueError("Duration must be positive.")
        self.phases[phase] = duration_days
    
    def add_regulation(self, regulation: Regulation) -> None:
        """Add a regulation that affects the project timeline."""
        self.regulations.append(regulation)
    
    def set_contingency(self, days: int) -> None:
        """Set contingency days for unexpected delays."""
        if days < 0:
            raise ValueError("Contingency days cannot be negative.")
        self.contingency_days = days
    
    def calculate_timeline(self) -> Dict[ProjectPhase, Tuple[datetime.date, datetime.date]]:
        """
        Calculate the timeline considering phases and regulations.
        
        Returns:
            Dict mapping each phase to its start and end dates.
        """
        if not self.phases:
            raise ValueError("No phases have been added to the project.")
        
        timeline = {}
        current_date = self.start_date
        
        # Calculate base timeline without regulations
        for phase, duration in self.phases.items():
            end_date = current_date + datetime.timedelta(days=duration - 1)
            timeline[phase] = (current_date, end_date)
            current_date = end_date + datetime.timedelta(days=1)
        
        # Apply regulation delays
        regulation_delays = self._calculate_regulation_delays()
        if regulation_delays > 0:
            logger.info(f"Adding {regulation_delays} days for regulatory compliance")
            self._adjust_timeline_for_delays(timeline, regulation_delays)
        
        # Add contingency
        if self.contingency_days > 0:
            logger.info(f"Adding {self.contingency_days} contingency days")
            self._adjust_timeline_for_delays(timeline, self.contingency_days)
        
        return timeline
    
    def _calculate_regulation_delays(self) -> int:
        """Calculate total days needed for regulatory compliance."""
        total_delay = 0
        for regulation in self.regulations:
            total_delay += regulation.required_days
        return total_delay
    
    def _adjust_timeline_for_delays(
        self,
        timeline: Dict[ProjectPhase, Tuple[datetime.date, datetime.date]],
        delay_days: int
    ) -> None:
        """Adjust the timeline by adding delay days after the permitting phase."""
        if ProjectPhase.PERMITTING not in timeline:
            raise ValueError("Permitting phase required for regulation delays")
        
        permitting_end = timeline[ProjectPhase.PERMITTING][1]
        adjusted_date = permitting_end + datetime.timedelta(days=delay_days + 1)
        
        for phase in timeline:
            phase_start, phase_end = timeline[phase]
            if phase_start > permitting_end:
                new_start = phase_start + datetime.timedelta(days=delay_days)
                new_end = phase_end + datetime.timedelta(days=delay_days)
                timeline[phase] = (new_start, new_end)
    
    def get_project_end_date(self) -> datetime.date:
        """Get the calculated end date of the project."""
        timeline = self.calculate_timeline()
        last_phase = max(timeline.values(), key=lambda x: x[1])
        return last_phase[1]
    
    def generate_report(self) -> str:
        """Generate a human-readable project timeline report."""
        timeline = self.calculate_timeline()
        report = [f"Project: {self.project_name}"]
        report.append(f"Start Date: {self.start_date.strftime('%Y-%m-%d')}")
        
        for phase, (start, end) in timeline.items():
            report.append(
                f"{phase.value}: {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}"
            )
        
        report.append(f"Projected Completion: {self.get_project_end_date().strftime('%Y-%m-%d')}")
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    try:
        # Create a project starting today
        project = ProjectTimeline(
            "Highway Expansion Project",
            datetime.date.today()
        )
        
        # Add project phases
        project.add_phase(ProjectPhase.PLANNING, 30)
        project.add_phase(ProjectPhase.DESIGN, 60)
        project.add_phase(ProjectPhase.PERMITTING, 90)
        project.add_phase(ProjectPhase.CONSTRUCTION, 180)
        project.add_phase(ProjectPhase.INSPECTION, 30)
        project.add_phase(ProjectPhase.COMPLETION, 14)
        
        # Add regulations
        project.add_regulation(Regulation(
            "OSHA Safety Standards",
            RegulationType.SAFETY,
            15,
            "Additional time for safety compliance"
        ))
        project.add_regulation(Regulation(
            "EPA Environmental Review",
            RegulationType.ENVIRONMENTAL,
            30,
            "Environmental impact assessment"
        ))
        
        # Set contingency
        project.set_contingency(14)
        
        # Generate and print report
        print(project.generate_report())
        
    except Exception as e:
        logger.error(f"Error calculating project timeline: {e}")
        raise
```
