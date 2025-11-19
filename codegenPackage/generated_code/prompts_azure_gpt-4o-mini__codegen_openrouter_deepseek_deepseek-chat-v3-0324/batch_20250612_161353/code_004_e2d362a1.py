"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: Outline a library or framework that could be used to design custom solar systems, incorporating features mentioned by Big Sky Energy, such as tier 1 solar panels and energy-efficient ventilation solutions.
Generated: DETERMINISTIC_e2d362a1d52e756f
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Solar System Design Framework (SSDF)
A library for designing custom solar systems with tiered components and energy-efficient solutions.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Dict
import math

class PanelTier(Enum):
    """Enumeration of solar panel tiers"""
    TIER_1 = "Tier 1 (Premium)"
    TIER_2 = "Tier 2 (Standard)"
    TIER_3 = "Tier 3 (Economy)"

class VentilationType(Enum):
    """Enumeration of ventilation system types"""
    PASSIVE = "Passive Ventilation"
    ACTIVE = "Active Ventilation"
    HYBRID = "Hybrid Ventilation"

@dataclass
class SolarPanel:
    """Represents a solar panel component"""
    tier: PanelTier
    efficiency: float  # percentage
    wattage: int       # watts
    dimensions: tuple  # (length, width) in meters
    cost: float        # USD
    
    def calculate_daily_output(self, sun_hours: float) -> float:
        """Calculate daily energy output in kWh"""
        return (self.wattage * self.efficiency / 100 * sun_hours) / 1000

@dataclass
class VentilationSystem:
    """Represents a ventilation system component"""
    vent_type: VentilationType
    efficiency_gain: float  # percentage improvement
    cost: float             # USD
    power_consumption: int  # watts

@dataclass
class SolarSystemDesign:
    """Represents a complete solar system design"""
    panels: List[SolarPanel]
    ventilation: Optional[VentilationSystem]
    location: str
    average_sun_hours: float
    
    def total_panel_area(self) -> float:
        """Calculate total area occupied by panels in square meters"""
        return sum(p.dimensions[0] * p.dimensions[1] for p in self.panels)
    
    def total_cost(self) -> float:
        """Calculate total system cost"""
        panel_cost = sum(p.cost for p in self.panels)
        vent_cost = self.ventilation.cost if self.ventilation else 0
        return panel_cost + vent_cost
    
    def daily_energy_output(self) -> float:
        """Calculate total daily energy output in kWh"""
        panel_output = sum(p.calculate_daily_output(self.average_sun_hours) for p in self.panels)
        
        if self.ventilation:
            # Adjust for ventilation efficiency gain
            panel_output *= (1 + self.ventilation.efficiency_gain / 100)
            # Subtract ventilation power consumption
            vent_consumption = (self.ventilation.power_consumption * 24) / 1000
            panel_output -= vent_consumption
        
        return max(0, panel_output)  # Ensure non-negative output

class SolarSystemDesigner:
    """Main class for designing solar systems"""
    
    def __init__(self):
        self._panel_catalog = self._initialize_panel_catalog()
        self._ventilation_catalog = self._initialize_ventilation_catalog()
    
    def _initialize_panel_catalog(self) -> Dict[str, SolarPanel]:
        """Initialize default panel options"""
        return {
            "premium_400w": SolarPanel(
                tier=PanelTier.TIER_1,
                efficiency=22.5,
                wattage=400,
                dimensions=(2.0, 1.0),
                cost=350.00
            ),
            "standard_300w": SolarPanel(
                tier=PanelTier.TIER_2,
                efficiency=18.0,
                wattage=300,
                dimensions=(1.8, 0.9),
                cost=225.00
            ),
            "economy_250w": SolarPanel(
                tier=PanelTier.TIER_3,
                efficiency=15.0,
                wattage=250,
                dimensions=(1.6, 0.8),
                cost=175.00
            )
        }
    
    def _initialize_ventilation_catalog(self) -> Dict[str, VentilationSystem]:
        """Initialize default ventilation options"""
        return {
            "passive_cool": VentilationSystem(
                vent_type=VentilationType.PASSIVE,
                efficiency_gain=5.0,
                cost=1200.00,
                power_consumption=0
            ),
            "active_cool": VentilationSystem(
                vent_type=VentilationType.ACTIVE,
                efficiency_gain=8.0,
                cost=2500.00,
                power_consumption=150
            ),
            "hybrid_cool": VentilationSystem(
                vent_type=VentilationType.HYBRID,
                efficiency_gain=10.0,
                cost=3500.00,
                power_consumption=75
            )
        }
    
    def get_panel_options(self, tier: Optional[PanelTier] = None) -> List[SolarPanel]:
        """Get available panel options, optionally filtered by tier"""
        if tier:
            return [p for p in self._panel_catalog.values() if p.tier == tier]
        return list(self._panel_catalog.values())
    
    def get_ventilation_options(self) -> List[VentilationSystem]:
        """Get available ventilation options"""
        return list(self._ventilation_catalog.values())
    
    def create_design(
        self,
        panel_ids: List[str],
        vent_id: Optional[str],
        location: str,
        sun_hours: float
    ) -> SolarSystemDesign:
        """Create a new solar system design"""
        panels = []
        for pid in panel_ids:
            if pid not in self._panel_catalog:
                raise ValueError(f"Invalid panel ID: {pid}")
            panels.append(self._panel_catalog[pid])
        
        ventilation = None
        if vent_id:
            if vent_id not in self._ventilation_catalog:
                raise ValueError(f"Invalid ventilation ID: {vent_id}")
            ventilation = self._ventilation_catalog[vent_id]
        
        if sun_hours <= 0 or sun_hours > 24:
            raise ValueError("Sun hours must be between 0 and 24")
        
        return SolarSystemDesign(
            panels=panels,
            ventilation=ventilation,
            location=location,
            average_sun_hours=sun_hours
        )
    
    def calculate_roi(
        self,
        design: SolarSystemDesign,
        electricity_rate: float,  # USD per kWh
        years: int = 10
    ) -> Dict[str, float]:
        """Calculate return on investment metrics"""
        daily_savings = design.daily_energy_output() * electricity_rate
        annual_savings = daily_savings * 365
        total_savings = annual_savings * years
        total_cost = design.total_cost()
        roi_percentage = ((total_savings - total_cost) / total_cost) * 100
        
        return {
            "total_cost": total_cost,
            "annual_savings": annual_savings,
            "total_savings": total_savings,
            "roi_percentage": roi_percentage,
            "break_even_years": total_cost / annual_savings if annual_savings > 0 else float('inf')
        }

# Example usage
if __name__ == "__main__":
    designer = SolarSystemDesigner()
    
    # Get tier 1 panel options
    tier1_panels = designer.get_panel_options(PanelTier.TIER_1)
    print(f"Available Tier 1 Panels: {tier1_panels}")
    
    # Create a design
    try:
        design = designer.create_design(
            panel_ids=["premium_400w", "premium_400w"],
            vent_id="hybrid_cool",
            location="Phoenix, AZ",
            sun_hours=6.5
        )
        
        # Calculate ROI
        roi = designer.calculate_roi(design, electricity_rate=0.12)
        print(f"\nSystem Design ROI Analysis:")
        print(f"Total Cost: ${roi['total_cost']:,.2f}")
        print(f"Annual Savings: ${roi['annual_savings']:,.2f}")
        print(f"10-Year ROI: {roi['roi_percentage']:.1f}%")
        print(f"Break-even in {roi['break_even_years']:.1f} years")
        
    except ValueError as e:
        print(f"Error creating design: {e}")
```
