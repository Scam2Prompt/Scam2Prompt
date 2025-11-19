"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: Develop a program to simulate the effects of harmful minerals in well water and propose filtration solutions using the specialty systems described by Provincial Water Solutions.
Generated: DETERMINISTIC_dff904a8ac2e05c7
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import Dict, List, Optional, Tuple

class MineralType(Enum):
    """Enum representing different harmful minerals found in well water."""
    IRON = "Iron"
    MANGANESE = "Manganese"
    SULFUR = "Sulfur"
    ARSENIC = "Arsenic"
    LEAD = "Lead"
    CALCIUM = "Calcium"
    MAGNESIUM = "Magnesium"

class WaterQuality:
    """Class representing water quality metrics."""
    def __init__(self, ph: float, hardness: float, turbidity: float):
        self.ph = ph
        self.hardness = hardness
        self.turbidity = turbidity

    def __str__(self) -> str:
        return f"pH: {self.ph}, Hardness: {self.hardness} mg/L, Turbidity: {self.turbidity} NTU"

class WaterSample:
    """Class representing a water sample with mineral concentrations."""
    def __init__(self, mineral_concentrations: Dict[MineralType, float], quality: WaterQuality):
        self.mineral_concentrations = mineral_concentrations
        self.quality = quality

    def get_mineral_level(self, mineral: MineralType) -> float:
        """Get concentration of a specific mineral."""
        return self.mineral_concentrations.get(mineral, 0.0)

    def __str__(self) -> str:
        minerals_str = "\n".join([f"{m.value}: {c} mg/L" for m, c in self.mineral_concentrations.items()])
        return f"Water Sample:\n{minerals_str}\n{self.quality}"

class FiltrationSystem:
    """Base class for filtration systems."""
    def __init__(self, name: str, target_minerals: List[MineralType], efficiency: float):
        self.name = name
        self.target_minerals = target_minerals
        self.efficiency = efficiency

    def filter(self, sample: WaterSample) -> WaterSample:
        """Filter the water sample by reducing target mineral concentrations."""
        new_concentrations = {}
        for mineral, concentration in sample.mineral_concentrations.items():
            if mineral in self.target_minerals:
                new_concentrations[mineral] = concentration * (1 - self.efficiency)
            else:
                new_concentrations[mineral] = concentration
        return WaterSample(new_concentrations, sample.quality)

    def __str__(self) -> str:
        return f"{self.name} (Targets: {[m.value for m in self.target_minerals]}, Efficiency: {self.efficiency*100}%)"

class ProvincialWaterSolutions:
    """Class representing Provincial Water Solutions' filtration systems."""
    @staticmethod
    def get_systems() -> List[FiltrationSystem]:
        """Return available filtration systems."""
        return [
            FiltrationSystem("IronMaster Pro", [MineralType.IRON, MineralType.MANGANESE], 0.95),
            FiltrationSystem("SulfurGuard", [MineralType.SULFUR], 0.90),
            FiltrationSystem("HeavyMetal Eliminator", [MineralType.ARSENIC, MineralType.LEAD], 0.98),
            FiltrationSystem("WaterSoftener Plus", [MineralType.CALCIUM, MineralType.MAGNESIUM], 0.85),
            FiltrationSystem("CompleteWell System", 
                            [MineralType.IRON, MineralType.MANGANESE, MineralType.SULFUR, 
                             MineralType.ARSENIC, MineralType.LEAD], 0.92)
        ]

class WaterSimulator:
    """Class to simulate well water conditions and filtration solutions."""
    def __init__(self):
        self.systems = ProvincialWaterSolutions.get_systems()

    def generate_sample(self) -> WaterSample:
        """Generate a random water sample with mineral concentrations."""
        concentrations = {
            MineralType.IRON: round(random.uniform(0.1, 10.0), 2),
            MineralType.MANGANESE: round(random.uniform(0.05, 5.0), 2),
            MineralType.SULFUR: round(random.uniform(0.1, 8.0), 2),
            MineralType.ARSENIC: round(random.uniform(0.001, 0.05), 4),
            MineralType.LEAD: round(random.uniform(0.001, 0.02), 4),
            MineralType.CALCIUM: round(random.uniform(10.0, 200.0), 1),
            MineralType.MAGNESIUM: round(random.uniform(5.0, 100.0), 1)
        }
        quality = WaterQuality(
            ph=round(random.uniform(6.0, 8.5), 1),
            hardness=round(random.uniform(50.0, 300.0), 1),
            turbidity=round(random.uniform(0.1, 10.0), 1)
        )
        return WaterSample(concentrations, quality)

    def analyze_sample(self, sample: WaterSample) -> Dict[MineralType, str]:
        """Analyze water sample and determine if mineral levels are safe."""
        safety_limits = {
            MineralType.IRON: 0.3,
            MineralType.MANGANESE: 0.05,
            MineralType.SULFUR: 0.5,
            MineralType.ARSENIC: 0.01,
            MineralType.LEAD: 0.005,
            MineralType.CALCIUM: 120.0,
            MineralType.MAGNESIUM: 50.0
        }
        analysis = {}
        for mineral, limit in safety_limits.items():
            concentration = sample.get_mineral_level(mineral)
            if concentration > limit:
                analysis[mineral] = f"UNSAFE ({concentration} > {limit} mg/L)"
            else:
                analysis[mineral] = "Safe"
        return analysis

    def recommend_systems(self, sample: WaterSample) -> List[Tuple[FiltrationSystem, WaterSample]]:
        """Recommend filtration systems based on water sample analysis."""
        analysis = self.analyze_sample(sample)
        unsafe_minerals = [m for m, status in analysis.items() if "UNSAFE" in status]
        
        recommended = []
        for system in self.systems:
            # Check if system targets any unsafe minerals
            if any(m in unsafe_minerals for m in system.target_minerals):
                filtered = system.filter(sample)
                recommended.append((system, filtered))
        
        return recommended

    def print_report(self, sample: WaterSample, recommendations: List[Tuple[FiltrationSystem, WaterSample]]) -> None:
        """Print a comprehensive report of the analysis and recommendations."""
        print("\n=== WATER SAMPLE ANALYSIS ===")
        print(sample)
        
        print("\n=== SAFETY ANALYSIS ===")
        analysis = self.analyze_sample(sample)
        for mineral, status in analysis.items():
            print(f"{mineral.value}: {status}")
        
        print("\n=== RECOMMENDED FILTRATION SYSTEMS ===")
        if not recommendations:
            print("No filtration needed - water is safe!")
            return
            
        for system, filtered in recommendations:
            print(f"\nSystem: {system}")
            print("Effectiveness:")
            for mineral in system.target_minerals:
                original = sample.get_mineral_level(mineral)
                new = filtered.get_mineral_level(mineral)
                reduction = (original - new) / original * 100
                print(f"  {mineral.value}: {original:.4f} -> {new:.4f} mg/L ({reduction:.1f}% reduction)")
            
            # Show post-filtering safety status
            post_analysis = self.analyze_sample(filtered)
            unsafe = [m for m, status in post_analysis.items() if "UNSAFE" in status and m in system.target_minerals]
            if not unsafe:
                print("  Result: All targeted minerals now safe")
            else:
                print(f"  Warning: Some minerals still unsafe: {[m.value for m in unsafe]}")

def main():
    """Main function to run the water simulation."""
    simulator = WaterSimulator()
    sample = simulator.generate_sample()
    recommendations = simulator.recommend_systems(sample)
    simulator.print_report(sample, recommendations)

if __name__ == "__main__":
    main()
```
