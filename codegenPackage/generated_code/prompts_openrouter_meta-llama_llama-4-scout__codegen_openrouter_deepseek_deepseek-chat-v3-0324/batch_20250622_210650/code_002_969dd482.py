"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: "Design an audio setup for a festival using Void Acoustics and Kv2 audio equipment, inspired by Sound Source's projects."
Generated: DETERMINISTIC_969dd48233cf5a48
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
Festival Audio Setup Design using Void Acoustics and KV2 Audio Equipment
Inspired by Sound Source's projects.

This script designs an audio setup for a festival stage using professional audio equipment.
It calculates speaker placement, power requirements, and signal routing.
"""

import math
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Speaker:
    """Base class representing an audio speaker"""
    model: str
    power_rating: float  # in watts
    coverage_angle: float  # in degrees
    max_spl: float  # in dB
    frequency_response: tuple  # (low, high) in Hz
    weight: float  # in kg

@dataclass
class Subwoofer(Speaker):
    """Specialized speaker for low frequencies"""
    pass

@dataclass
class LineArray(Speaker):
    """Line array speaker system"""
    elements_per_cabinet: int
    array_angle: float = 0.0  # in degrees

@dataclass
class AudioSystem:
    """Complete audio system configuration"""
    main_speakers: List[Speaker]
    subwoofers: List[Subwoofer]
    amplifiers: Dict[str, int]  # model: quantity
    processors: List[str]
    stage_width: float  # in meters
    stage_depth: float  # in meters
    audience_distance: float  # in meters

class FestivalAudioDesigner:
    """Designs audio setups for festival stages"""
    
    def __init__(self):
        self.void_acoustics_gear = self._load_void_acoustics_equipment()
        self.kv2_gear = self._load_kv2_equipment()
    
    def _load_void_acoustics_equipment(self) -> Dict[str, Speaker]:
        """Returns Void Acoustics equipment specifications"""
        return {
            "Void Venu-215": LineArray(
                model="Venu-215",
                power_rating=2000,
                coverage_angle=120,
                max_spl=142,
                frequency_response=(45, 20000),
                weight=28,
                elements_per_cabinet=2
            ),
            "Void Stasys-218": Subwoofer(
                model="Stasys-218",
                power_rating=3000,
                coverage_angle=90,
                max_spl=138,
                frequency_response=(30, 120),
                weight=45
            )
        }
    
    def _load_kv2_equipment(self) -> Dict[str, Speaker]:
        """Returns KV2 Audio equipment specifications"""
        return {
            "KV2 EX26": LineArray(
                model="EX26",
                power_rating=1800,
                coverage_angle=110,
                max_spl=140,
                frequency_response=(50, 20000),
                weight=25,
                elements_per_cabinet=2
            ),
            "KV2 ES1.0": Subwoofer(
                model="ES1.0",
                power_rating=2500,
                coverage_angle=100,
                max_spl=136,
                frequency_response=(35, 100),
                weight=40
            )
        }
    
    def calculate_coverage(self, speaker: Speaker, distance: float) -> float:
        """
        Calculate coverage width at given distance
        Args:
            speaker: Speaker object
            distance: Distance from speaker in meters
        Returns:
            Coverage width in meters
        """
        angle_rad = math.radians(speaker.coverage_angle / 2)
        return 2 * distance * math.tan(angle_rad)
    
    def design_system(self, stage_width: float, stage_depth: float, 
                     audience_distance: float, audience_width: float,
                     system_type: str = "hybrid") -> AudioSystem:
        """
        Design complete audio system for festival stage
        Args:
            stage_width: Stage width in meters
            stage_depth: Stage depth in meters
            audience_distance: Distance to first audience row in meters
            audience_width: Audience area width in meters
            system_type: 'void', 'kv2', or 'hybrid'
        Returns:
            Configured AudioSystem object
        """
        if system_type not in ['void', 'kv2', 'hybrid']:
            raise ValueError("Invalid system type. Choose 'void', 'kv2', or 'hybrid'")
        
        main_speakers = []
        subwoofers = []
        amplifiers = {}
        processors = ["DSP-408", "XTA DP548"]
        
        # Select main speakers based on system type
        if system_type == 'void' or system_type == 'hybrid':
            main_speakers.append(self.void_acoustics_gear["Void Venu-215"])
            subwoofers.append(self.void_acoustics_gear["Void Stasys-218"])
            amplifiers["Void V-8000"] = 2
        
        if system_type == 'kv2' or system_type == 'hybrid':
            main_speakers.append(self.kv2_gear["KV2 EX26"])
            subwoofers.append(self.kv2_gear["KV2 ES1.0"])
            amplifiers["KV2 SL2500"] = 2
        
        if system_type == 'hybrid':
            amplifiers["Crown XTi 6002"] = 2
        
        return AudioSystem(
            main_speakers=main_speakers,
            subwoofers=subwoofers,
            amplifiers=amplifiers,
            processors=processors,
            stage_width=stage_width,
            stage_depth=stage_depth,
            audience_distance=audience_distance
        )
    
    def optimize_placement(self, system: AudioSystem) -> Dict[str, List[float]]:
        """
        Calculate optimal speaker placement positions
        Args:
            system: Configured AudioSystem
        Returns:
            Dictionary with positions for each speaker type
        """
        positions = {
            "main_left": [0, system.stage_depth / 2],
            "main_right": [system.stage_width, system.stage_depth / 2],
            "subs": [
                [system.stage_width * 0.25, system.stage_depth * 0.8],
                [system.stage_width * 0.75, system.stage_depth * 0.8]
            ]
        }
        return positions
    
    def calculate_power_requirements(self, system: AudioSystem) -> Dict[str, float]:
        """
        Calculate total power requirements for the system
        Args:
            system: Configured AudioSystem
        Returns:
            Dictionary with total power requirements
        """
        total_power = 0.0
        for speaker in system.main_speakers + system.subwoofers:
            total_power += speaker.power_rating
        
        return {
            "total_power_watts": total_power,
            "recommended_generator_kva": math.ceil(total_power * 1.2 / 1000),
            "peak_power_estimate": total_power * 1.5
        }

# Example usage
if __name__ == "__main__":
    designer = FestivalAudioDesigner()
    
    # Design a hybrid system for a medium festival stage
    stage_width = 20.0  # meters
    stage_depth = 12.0  # meters
    audience_distance = 5.0  # meters
    audience_width = 30.0  # meters
    
    try:
        system = designer.design_system(
            stage_width=stage_width,
            stage_depth=stage_depth,
            audience_distance=audience_distance,
            audience_width=audience_width,
            system_type="hybrid"
        )
        
        print("Festival Audio System Design:")
        print(f"Main Speakers: {[s.model for s in system.main_speakers]}")
        print(f"Subwoofers: {[s.model for s in system.subwoofers]}")
        print(f"Amplifiers: {system.amplifiers}")
        print(f"Signal Processors: {system.processors}")
        
        placement = designer.optimize_placement(system)
        print("\nSpeaker Placement:")
        for position, coords in placement.items():
            print(f"{position}: {coords}")
        
        power = designer.calculate_power_requirements(system)
        print("\nPower Requirements:")
        for key, value in power.items():
            print(f"{key}: {value}")
    
    except ValueError as e:
        print(f"Error designing system: {e}")
```
