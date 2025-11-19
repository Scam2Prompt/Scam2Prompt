"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Write code to model the deterioration of wall ties due to salt exposure near coastal areas and simulate the installation of remedial ties using the Thor Helical system.
Generated: DETERMINISTIC_bcd08b2fbc7ac3a6
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import random
from datetime import datetime, timedelta

class TieMaterial(Enum):
    """Enum representing different wall tie materials"""
    MILD_STEEL = 1
    STAINLESS_STEEL = 2
    GALVANIZED_STEEL = 3

class TieCondition(Enum):
    """Enum representing wall tie condition states"""
    INTACT = 1
    CORRODED = 2
    FAILED = 3

@dataclass
class WallTie:
    """Class representing a single wall tie"""
    id: int
    material: TieMaterial
    installation_date: datetime
    condition: TieCondition = TieCondition.INTACT
    corrosion_level: float = 0.0
    distance_from_coast: float  # in meters
    last_inspection_date: Optional[datetime] = None

    def __post_init__(self):
        if self.distance_from_coast <= 0:
            raise ValueError("Distance from coast must be positive")

@dataclass
class RemedialTie:
    """Class representing a remedial tie installation"""
    id: int
    original_tie_id: int
    installation_date: datetime
    system_type: str = "Thor Helical"
    is_installed: bool = False

class WallTieSystem:
    """Class to model wall tie deterioration and remedial installations"""
    
    def __init__(self, distance_from_coast: float, salt_level: float = 1.0):
        """
        Initialize wall tie system
        :param distance_from_coast: Distance from coast in meters
        :param salt_level: Salt exposure level (1.0 = normal coastal, higher = more severe)
        """
        self.distance_from_coast = distance_from_coast
        self.salt_level = salt_level
        self.wall_ties: List[WallTie] = []
        self.remedial_ties: List[RemedialTie] = []
        self.inspection_records: List[Dict] = []
        
    def add_wall_tie(self, material: TieMaterial, installation_date: datetime) -> WallTie:
        """Add a new wall tie to the system"""
        tie_id = len(self.wall_ties) + 1
        tie = WallTie(
            id=tie_id,
            material=material,
            installation_date=installation_date,
            distance_from_coast=self.distance_from_coast
        )
        self.wall_ties.append(tie)
        return tie
    
    def calculate_corrosion_rate(self, tie: WallTie) -> float:
        """Calculate corrosion rate based on material and environment"""
        base_rate = 0.01  # mm/year base corrosion rate
        
        # Material factors
        if tie.material == TieMaterial.MILD_STEEL:
            material_factor = 1.0
        elif tie.material == TieMaterial.GALVANIZED_STEEL:
            material_factor = 0.5
        elif tie.material == TieMaterial.STAINLESS_STEEL:
            material_factor = 0.1
        
        # Distance factor (exponential decay with distance)
        distance_factor = np.exp(-tie.distance_from_coast / 1000)
        
        # Salt level factor
        salt_factor = self.salt_level
        
        return base_rate * material_factor * distance_factor * salt_factor
    
    def update_tie_condition(self, tie: WallTie, current_date: datetime) -> None:
        """Update tie condition based on corrosion over time"""
        years_installed = (current_date - tie.installation_date).days / 365.25
        corrosion_rate = self.calculate_corrosion_rate(tie)
        tie.corrosion_level = corrosion_rate * years_installed
        
        # Update condition based on corrosion level
        if tie.corrosion_level > 0.8:
            tie.condition = TieCondition.FAILED
        elif tie.corrosion_level > 0.3:
            tie.condition = TieCondition.CORRODED
        else:
            tie.condition = TieCondition.INTACT
    
    def simulate_deterioration(self, current_date: datetime) -> None:
        """Simulate deterioration of all wall ties up to current date"""
        for tie in self.wall_ties:
            self.update_tie_condition(tie, current_date)
    
    def inspect_system(self, inspection_date: datetime) -> Dict:
        """Perform system inspection and return report"""
        self.simulate_deterioration(inspection_date)
        
        report = {
            "inspection_date": inspection_date,
            "total_ties": len(self.wall_ties),
            "intact": sum(1 for t in self.wall_ties if t.condition == TieCondition.INTACT),
            "corroded": sum(1 for t in self.wall_ties if t.condition == TieCondition.CORRODED),
            "failed": sum(1 for t in self.wall_ties if t.condition == TieCondition.FAILED),
            "recommended_replacements": sum(1 for t in self.wall_ties 
                                          if t.condition in (TieCondition.CORRODED, TieCondition.FAILED))
        }
        
        self.inspection_records.append(report)
        
        # Update last inspection date for all ties
        for tie in self.wall_ties:
            tie.last_inspection_date = inspection_date
            
        return report
    
    def install_remedial_tie(self, original_tie: WallTie, installation_date: datetime) -> RemedialTie:
        """Install a remedial tie using Thor Helical system"""
        if original_tie not in self.wall_ties:
            raise ValueError("Original tie not found in system")
            
        remedial_id = len(self.remedial_ties) + 1
        remedial_tie = RemedialTie(
            id=remedial_id,
            original_tie_id=original_tie.id,
            installation_date=installation_date
        )
        remedial_tie.is_installed = True
        self.remedial_ties.append(remedial_tie)
        
        return remedial_tie
    
    def plot_deterioration_over_time(self) -> None:
        """Plot deterioration of wall ties over time"""
        if not self.inspection_records:
            raise ValueError("No inspection records available")
            
        dates = [r["inspection_date"] for r in self.inspection_records]
        intact = [r["intact"] for r in self.inspection_records]
        corroded = [r["corroded"] for r in self.inspection_records]
        failed = [r["failed"] for r in self.inspection_records]
        
        plt.figure(figsize=(10, 6))
        plt.plot(dates, intact, label="Intact", marker='o')
        plt.plot(dates, corroded, label="Corroded", marker='o')
        plt.plot(dates, failed, label="Failed", marker='o')
        
        # Mark remedial installations
        for tie in self.remedial_ties:
            plt.axvline(x=tie.installation_date, color='r', linestyle='--', alpha=0.3)
        
        plt.title("Wall Tie Deterioration Over Time")
        plt.xlabel("Date")
        plt.ylabel("Number of Ties")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize system 500m from coast with high salt exposure
    system = WallTieSystem(distance_from_coast=500, salt_level=1.2)
    
    # Install initial wall ties (mix of materials)
    start_date = datetime(2010, 1, 1)
    for i in range(100):
        material = random.choice(list(TieMaterial))
        system.add_wall_tie(material, start_date)
    
    # Simulate inspections every 2 years
    current_date = start_date
    end_date = datetime(2023, 1, 1)
    
    while current_date <= end_date:
        report = system.inspect_system(current_date)
        
        # Install remedial ties for failed ties
        failed_ties = [t for t in system.wall_ties if t.condition == TieCondition.FAILED 
                      and not any(r.original_tie_id == t.id for r in system.remedial_ties)]
        
        for tie in failed_ties[:5]:  # Limit to 5 replacements per inspection
            system.install_remedial_tie(tie, current_date)
        
        current_date += timedelta(days=365.25 * 2)  # ~2 years
    
    # Plot results
    system.plot_deterioration_over_time()
```
