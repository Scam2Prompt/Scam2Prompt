"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: Generate a strategic roadmap for enhancing organizational capabilities, incorporating the techniques for بناء القدرات discussed by شركة الإتمام الاستشارية.
Generated: DETERMINISTIC_48755d936310af6b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Strategic Roadmap Generator for Organizational Capability Enhancement
Inspired by شركة الإتمام الاستشارية's capacity building (بناء القدرات) techniques.

This script generates a strategic roadmap with phases, objectives, and KPIs.
"""

from dataclasses import dataclass
from typing import List, Dict
import datetime
import json
from enum import Enum, auto

class CapabilityDomain(Enum):
    """Domains of organizational capability"""
    LEADERSHIP = auto()
    PROCESSES = auto()
    TECHNOLOGY = auto()
    HUMAN_RESOURCES = auto()
    FINANCIAL = auto()
    INNOVATION = auto()

@dataclass
class StrategicObjective:
    """Represents a strategic objective with associated metrics"""
    id: str
    title: str
    description: str
    domain: CapabilityDomain
    kpis: List[str]
    priority: int  # 1-5 where 1 is highest
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "domain": self.domain.name,
            "kpis": self.kpis,
            "priority": self.priority
        }

@dataclass
class RoadmapPhase:
    """Represents a phase in the strategic roadmap"""
    name: str
    start_date: datetime.date
    end_date: datetime.date
    objectives: List[StrategicObjective]
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization"""
        return {
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "objectives": [obj.to_dict() for obj in self.objectives]
        }

class RoadmapGenerator:
    """Generates a strategic roadmap for capability enhancement"""
    
    def __init__(self, organization_name: str):
        self.organization_name = organization_name
        self.phases: List[RoadmapPhase] = []
        self.current_id = 1
    
    def _generate_id(self) -> str:
        """Generate unique ID for objectives"""
        id_str = f"OBJ-{self.current_id:03d}"
        self.current_id += 1
        return id_str
    
    def add_phase(self, name: str, start_date: datetime.date, 
                 duration_months: int) -> None:
        """Add a new phase to the roadmap"""
        end_date = self._calculate_end_date(start_date, duration_months)
        self.phases.append(
            RoadmapPhase(name, start_date, end_date, [])
        )
    
    def _calculate_end_date(self, start_date: datetime.date, 
                          months: int) -> datetime.date:
        """Calculate end date based on start date and duration"""
        year = start_date.year + (start_date.month + months - 1) // 12
        month = (start_date.month + months - 1) % 12 + 1
        day = min(start_date.day, self._days_in_month(year, month))
        return datetime.date(year, month, day)
    
    def _days_in_month(self, year: int, month: int) -> int:
        """Get number of days in a month"""
        if month == 12:
            return 31
        return (datetime.date(year, month + 1, 1) - 
                datetime.date(year, month, 1)).days
    
    def add_objective(self, phase_name: str, title: str, description: str,
                     domain: CapabilityDomain, kpis: List[str], 
                     priority: int) -> None:
        """
        Add a strategic objective to a specific phase
        Raises ValueError if phase not found or invalid priority
        """
        if priority < 1 or priority > 5:
            raise ValueError("Priority must be between 1 and 5")
            
        phase = next((p for p in self.phases if p.name == phase_name), None)
        if not phase:
            raise ValueError(f"Phase '{phase_name}' not found")
            
        objective = StrategicObjective(
            id=self._generate_id(),
            title=title,
            description=description,
            domain=domain,
            kpis=kpis,
            priority=priority
        )
        phase.objectives.append(objective)
    
    def generate_report(self, output_format: str = "json") -> str:
        """
        Generate roadmap report in specified format
        Supported formats: json, text
        """
        roadmap_data = {
            "organization": self.organization_name,
            "generated_date": datetime.date.today().isoformat(),
            "phases": [phase.to_dict() for phase in self.phases]
        }
        
        if output_format == "json":
            return json.dumps(roadmap_data, indent=2, ensure_ascii=False)
        elif output_format == "text":
            return self._generate_text_report(roadmap_data)
        else:
            raise ValueError(f"Unsupported format: {output_format}")
    
    def _generate_text_report(self, data: Dict) -> str:
        """Generate human-readable text report"""
        report = []
        report.append(f"Strategic Roadmap for {data['organization']}")
        report.append(f"Generated on {data['generated_date']}\n")
        
        for phase in data["phases"]:
            report.append(f"=== Phase: {phase['name']} ===")
            report.append(f"Timeline: {phase['start_date']} to {phase['end_date']}\n")
            
            # Sort objectives by priority
            objectives = sorted(phase["objectives"], key=lambda x: x["priority"])
            
            for obj in objectives:
                report.append(f"Objective {obj['id']} (Priority {obj['priority']}):")
                report.append(f"  Title: {obj['title']}")
                report.append(f"  Domain: {obj['domain']}")
                report.append(f"  Description: {obj['description']}")
                report.append("  KPIs:")
                for kpi in obj["kpis"]:
                    report.append(f"    - {kpi}")
                report.append("")
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize roadmap generator
        roadmap = RoadmapGenerator("Example Organization")
        
        # Add phases
        today = datetime.date.today()
        roadmap.add_phase("Assessment", today, 3)
        roadmap.add_phase("Foundation", today + datetime.timedelta(days=90), 6)
        roadmap.add_phase("Growth", today + datetime.timedelta(days=270), 12)
        
        # Add objectives to Assessment phase
        roadmap.add_objective(
            "Assessment",
            "Current State Analysis",
            "Conduct comprehensive assessment of current capabilities",
            CapabilityDomain.PROCESSES,
            ["Assessment report completed", "Gap analysis documented"],
            1
        )
        
        roadmap.add_objective(
            "Assessment",
            "Stakeholder Alignment",
            "Engage leadership in capability building vision",
            CapabilityDomain.LEADERSHIP,
            ["Stakeholder workshops conducted", "Alignment score ≥80%"],
            2
        )
        
        # Add objectives to Foundation phase
        roadmap.add_objective(
            "Foundation",
            "Process Optimization",
            "Implement lean methodologies in core processes",
            CapabilityDomain.PROCESSES,
            ["Process cycle time reduced by 30%", "Error rate reduced by 25%"],
            1
        )
        
        # Generate and print roadmap
        print(roadmap.generate_report("text"))
        
        # Optionally save to JSON
        with open("strategic_roadmap.json", "w", encoding="utf-8") as f:
            f.write(roadmap.generate_report("json"))
            
    except Exception as e:
        print(f"Error generating roadmap: {str(e)}")
```
