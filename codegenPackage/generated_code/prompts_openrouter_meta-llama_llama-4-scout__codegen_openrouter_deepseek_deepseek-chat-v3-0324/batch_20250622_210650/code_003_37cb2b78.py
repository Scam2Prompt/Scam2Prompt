"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Develop a framework for understanding the impact of automation on society, referencing the concepts discussed in the article "KI und Automation" (AI and Automation).
Generated: DETERMINISTIC_37cb2b7895649306
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
Automation Impact Framework (AIF) - A tool to analyze societal impacts of automation.

This framework models key aspects discussed in "KI und Automation" including:
- Job displacement vs. creation
- Productivity changes
- Economic inequality
- Skill requirements
- Social adaptation

The framework provides quantitative and qualitative analysis capabilities.
"""

from dataclasses import dataclass
from enum import Enum, auto
import math
from typing import List, Dict, Optional
import json
import statistics
import warnings

class ImpactCategory(Enum):
    """Categories of societal impact from automation."""
    EMPLOYMENT = auto()
    PRODUCTIVITY = auto()
    INEQUALITY = auto()
    SKILL_SHIFT = auto()
    SOCIAL_ADAPTATION = auto()

class TimeHorizon(Enum):
    """Time horizons for impact analysis."""
    SHORT_TERM = auto()  # 0-5 years
    MEDIUM_TERM = auto()  # 5-15 years
    LONG_TERM = auto()    # 15+ years

@dataclass
class Sector:
    """Represents an economic sector affected by automation."""
    name: str
    automation_potential: float  # 0-1 scale
    current_employment: int
    skill_distribution: Dict[str, float]  # skill level to percentage

@dataclass
class AutomationImpact:
    """Represents the impact of automation in a specific category."""
    category: ImpactCategory
    time_horizon: TimeHorizon
    magnitude: float  # -1 to +1 scale
    description: str

class AutomationFramework:
    """Main framework class for analyzing automation impacts."""
    
    def __init__(self):
        self.sectors: List[Sector] = []
        self.impacts: List[AutomationImpact] = []
        self._load_default_data()
    
    def _load_default_data(self) -> None:
        """Load default sector data based on common economic structures."""
        default_sectors = [
            Sector("Manufacturing", 0.7, 1000000, {"low": 0.6, "medium": 0.3, "high": 0.1}),
            Sector("Healthcare", 0.4, 1500000, {"low": 0.2, "medium": 0.5, "high": 0.3}),
            Sector("Retail", 0.6, 2000000, {"low": 0.7, "medium": 0.25, "high": 0.05}),
            Sector("Finance", 0.5, 800000, {"low": 0.3, "medium": 0.4, "high": 0.3}),
            Sector("Education", 0.3, 1200000, {"low": 0.1, "medium": 0.4, "high": 0.5})
        ]
        self.sectors.extend(default_sectors)
        
        # Default impacts based on "KI und Automation" concepts
        default_impacts = [
            AutomationImpact(ImpactCategory.EMPLOYMENT, TimeHorizon.SHORT_TERM, -0.4, 
                           "Initial job displacement in automatable sectors"),
            AutomationImpact(ImpactCategory.PRODUCTIVITY, TimeHorizon.SHORT_TERM, 0.3,
                           "Increased productivity from automation"),
            AutomationImpact(ImpactCategory.INEQUALITY, TimeHorizon.MEDIUM_TERM, -0.5,
                           "Widening wage gap between high/low skill workers"),
            AutomationImpact(ImpactCategory.SKILL_SHIFT, TimeHorizon.LONG_TERM, 0.7,
                           "Shift toward higher skill requirements"),
            AutomationImpact(ImpactCategory.SOCIAL_ADAPTATION, TimeHorizon.LONG_TERM, 0.4,
                           "Gradual societal adaptation to new technologies")
        ]
        self.impacts.extend(default_impacts)
    
    def add_sector(self, sector: Sector) -> None:
        """Add a new economic sector to the framework."""
        if not 0 <= sector.automation_potential <= 1:
            raise ValueError("Automation potential must be between 0 and 1")
        if sum(sector.skill_distribution.values()) != 1.0:
            raise ValueError("Skill distribution must sum to 1.0")
        self.sectors.append(sector)
    
    def add_impact(self, impact: AutomationImpact) -> None:
        """Add a new impact assessment to the framework."""
        if not -1 <= impact.magnitude <= 1:
            raise ValueError("Impact magnitude must be between -1 and 1")
        self.impacts.append(impact)
    
    def calculate_job_displacement(self, time_horizon: TimeHorizon) -> Dict[str, float]:
        """
        Calculate projected job displacement by sector.
        Returns dictionary mapping sector names to displacement percentage.
        """
        displacement = {}
        for sector in self.sectors:
            # Base displacement is automation potential adjusted by time horizon factor
            time_factor = {
                TimeHorizon.SHORT_TERM: 0.5,
                TimeHorizon.MEDIUM_TERM: 0.8,
                TimeHorizon.LONG_TERM: 1.0
            }[time_horizon]
            
            displacement[sector.name] = sector.automation_potential * time_factor
        
        return displacement
    
    def calculate_productivity_gain(self, time_horizon: TimeHorizon) -> float:
        """
        Calculate average productivity gain across all sectors.
        Returns value between -1 and 1 representing percentage change.
        """
        gains = []
        for sector in self.sectors:
            # Productivity gain correlates with automation potential but diminishes for high-skill sectors
            skill_factor = 1 - sector.skill_distribution["high"]
            gain = sector.automation_potential * skill_factor * 0.7  # 0.7 is max productivity gain
            
            # Adjust for time horizon
            time_factor = {
                TimeHorizon.SHORT_TERM: 0.3,
                TimeHorizon.MEDIUM_TERM: 0.6,
                TimeHorizon.LONG_TERM: 1.0
            }[time_horizon]
            
            gains.append(gain * time_factor)
        
        return statistics.mean(gains) if gains else 0.0
    
    def calculate_inequality_index(self) -> float:
        """
        Calculate an inequality index based on skill distribution and automation potential.
        Higher values indicate greater potential inequality (0-1 scale).
        """
        if not self.sectors:
            return 0.0
            
        total_employment = sum(sector.current_employment for sector in self.sectors)
        weighted_sum = 0.0
        
        for sector in self.sectors:
            # Inequality increases with automation potential and low-skill concentration
            skill_factor = sector.skill_distribution["low"] - sector.skill_distribution["high"]
            sector_contribution = (sector.current_employment / total_employment) * \
                                sector.automation_potential * \
                                (0.5 + 0.5 * skill_factor)
            
            weighted_sum += sector_contribution
        
        return min(max(weighted_sum, 0.0), 1.0)
    
    def generate_report(self, filename: Optional[str] = None) -> Dict:
        """
        Generate a comprehensive report of automation impacts.
        If filename is provided, saves as JSON.
        Returns the report data structure.
        """
        report = {
            "sectors":
