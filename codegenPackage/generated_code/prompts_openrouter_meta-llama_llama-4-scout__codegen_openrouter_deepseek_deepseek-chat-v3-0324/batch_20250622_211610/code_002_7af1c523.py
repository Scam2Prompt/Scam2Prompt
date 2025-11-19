"""
Generated Code Metadata:
========================
Original URL: https://harda-ke.org
Prompt: How does HARDA approach disaster risk reduction and climate change adaptation in the Horn of Africa region?
Generated: DETERMINISTIC_7af1c5230e9aee3a
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
HARDA (Horn of Africa Risk and Disaster Adaptation) Framework Implementation

This module provides a programmatic representation of HARDA's approach to disaster risk reduction (DRR)
and climate change adaptation (CCA) in the Horn of Africa region.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import datetime

class InterventionType(Enum):
    """Types of interventions HARDA implements"""
    EARLY_WARNING = auto()
    COMMUNITY_TRAINING = auto()
    INFRASTRUCTURE = auto()
    POLICY_ADVOCACY = auto()
    RESEARCH = auto()
    LIVELIHOOD_SUPPORT = auto()

@dataclass
class Intervention:
    """Represents a specific intervention activity"""
    name: str
    intervention_type: InterventionType
    target_region: str
    start_date: datetime.date
    end_date: Optional[datetime.date] = None
    beneficiaries: Optional[int] = None
    budget: Optional[float] = None

    def is_active(self) -> bool:
        """Check if intervention is currently active"""
        today = datetime.date.today()
        return self.start_date <= today and (self.end_date is None or today <= self.end_date)

class HARDAFramework:
    """Main class representing HARDA's DRR and CCA approach"""
    
    def __init__(self):
        self.interventions: List[Intervention] = []
        self.regions = ["Djibouti", "Eritrea", "Ethiopia", "Kenya", "Somalia", "South Sudan", "Sudan"]
        self.strategic_pillars = {
            "DRR": "Disaster Risk Reduction",
            "CCA": "Climate Change Adaptation",
            "CB": "Capacity Building",
            "PA": "Policy Advocacy",
            "KM": "Knowledge Management"
        }
    
    def add_intervention(self, intervention: Intervention) -> bool:
        """Add a new intervention to HARDA's portfolio"""
        if intervention.target_region not in self.regions:
            raise ValueError(f"Invalid region. Must be one of: {', '.join(self.regions)}")
        
        self.interventions.append(intervention)
        return True
    
    def get_active_interventions(self) -> List[Intervention]:
        """Get all currently active interventions"""
        return [i for i in self.interventions if i.is_active()]
    
    def get_interventions_by_region(self, region: str) -> List[Intervention]:
        """Get interventions targeting a specific region"""
        if region not in self.regions:
            raise ValueError(f"Invalid region. Must be one of: {', '.join(self.regions)}")
        
        return [i for i in self.interventions if i.target_region == region]
    
    def get_interventions_by_type(self, intervention_type: InterventionType) -> List[Intervention]:
        """Get interventions of a specific type"""
        return [i for i in self.interventions if i.intervention_type == intervention_type]
    
    def get_strategic_coverage(self) -> Dict[str, int]:
        """Get count of interventions per strategic pillar"""
        coverage = {pillar: 0 for pillar in self.strategic_pillars}
        
        for intervention in self.interventions:
            if intervention.intervention_type in [InterventionType.EARLY_WARNING, InterventionType.INFRASTRUCTURE]:
                coverage["DRR"] += 1
            elif intervention.intervention_type in [InterventionType.LIVELIHOOD_SUPPORT, InterventionType.COMMUNITY_TRAINING]:
                coverage["CCA"] += 1
            elif intervention.intervention_type == InterventionType.COMMUNITY_TRAINING:
                coverage["CB"] += 1
            elif intervention.intervention_type == InterventionType.POLICY_ADVOCACY:
                coverage["PA"] += 1
            elif intervention.intervention_type == InterventionType.RESEARCH:
                coverage["KM"] += 1
                
        return coverage

# Example usage
if __name__ == "__main__":
    harda = HARDAFramework()
    
    # Add sample interventions
    try:
        harda.add_intervention(Intervention(
            name="Drought Early Warning System",
            intervention_type=InterventionType.EARLY_WARNING,
            target_region="Somalia",
            start_date=datetime.date(2022, 1, 1),
            beneficiaries=50000,
            budget=1500000.00
        ))
        
        harda.add_intervention(Intervention(
            name="Climate-Smart Agriculture Training",
            intervention_type=InterventionType.COMMUNITY_TRAINING,
            target_region="Kenya",
            start_date=datetime.date(2023, 3, 15),
            end_date=datetime.date(2023, 12, 31),
            beneficiaries=2000,
            budget=500000.00
        ))
        
        # Print some reports
        print("Active Interventions:")
        for intervention in harda.get_active_interventions():
            print(f"- {intervention.name} in {intervention.target_region}")
        
        print("\nStrategic Coverage:")
        for pillar, count in harda.get_strategic_coverage().items():
            print(f"{harda.strategic_pillars[pillar]}: {count} interventions")
            
    except ValueError as e:
        print(f"Error: {e}")
```
