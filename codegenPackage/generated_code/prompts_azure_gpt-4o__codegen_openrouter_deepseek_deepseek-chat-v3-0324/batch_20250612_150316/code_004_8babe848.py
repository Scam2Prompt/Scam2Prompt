"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Write code to analyze and compare sled designs for tractor pulling, incorporating the guidelines for sled measurements provided on jobbo.com.au.
Generated: DETERMINISTIC_8babe848bce4120e
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple


class SledType(Enum):
    """Enumeration of sled types based on jobbo.com.au guidelines."""
    STANDARD = "Standard"
    MODIFIED = "Modified"
    SUPER_MODIFIED = "Super Modified"


@dataclass
class SledMeasurement:
    """Data class for sled measurements."""
    length: float  # in meters
    width: float  # in meters
    weight: float  # in kilograms
    pan_height: float  # in meters
    hitch_height: float  # in meters
    type: SledType


@dataclass
class SledComparisonResult:
    """Data class for sled comparison results."""
    sled1: SledMeasurement
    sled2: SledMeasurement
    length_diff: float
    width_diff: float
    weight_diff: float
    pan_height_diff: float
    hitch_height_diff: float
    type_compatibility: bool


class SledAnalyzer:
    """Class to analyze and compare sled designs for tractor pulling."""

    def __init__(self):
        self._valid_types = [t.value for t in SledType]

    def validate_measurement(self, measurement: SledMeasurement) -> Tuple[bool, Optional[str]]:
        """Validate sled measurements according to jobbo.com.au guidelines."""
        if measurement.length <= 0:
            return False, "Length must be positive"
        if measurement.width <= 0:
            return False, "Width must be positive"
        if measurement.weight <= 0:
            return False, "Weight must be positive"
        if measurement.pan_height <= 0:
            return False, "Pan height must be positive"
        if measurement.hitch_height <= 0:
            return False, "Hitch height must be positive"
        if measurement.type.value not in self._valid_types:
            return False, f"Invalid sled type. Must be one of: {self._valid_types}"
        return True, None

    def compare_sleds(self, sled1: SledMeasurement, sled2: SledMeasurement) -> SledComparisonResult:
        """
        Compare two sled designs and return a comparison result.
        
        Args:
            sled1: First sled measurement
            sled2: Second sled measurement
            
        Returns:
            SledComparisonResult with comparison metrics
        """
        # Validate inputs
        for sled in [sled1, sled2]:
            valid, msg = self.validate_measurement(sled)
            if not valid:
                raise ValueError(f"Invalid sled measurement: {msg}")

        return SledComparisonResult(
            sled1=sled1,
            sled2=sled2,
            length_diff=abs(sled1.length - sled2.length),
            width_diff=abs(sled1.width - sled2.width),
            weight_diff=abs(sled1.weight - sled2.weight),
            pan_height_diff=abs(sled1.pan_height - sled2.pan_height),
            hitch_height_diff=abs(sled1.hitch_height - sled2.hitch_height),
            type_compatibility=sled1.type == sled2.type
        )

    def calculate_pull_ratio(self, sled: SledMeasurement, tractor_weight: float) -> float:
        """
        Calculate the pull ratio (sled weight to tractor weight ratio).
        
        Args:
            sled: Sled measurement
            tractor_weight: Weight of the tractor in kg
            
        Returns:
            Pull ratio as float
        """
        if tractor_weight <= 0:
            raise ValueError("Tractor weight must be positive")
        valid, msg = self.validate_measurement(sled)
        if not valid:
            raise ValueError(f"Invalid sled measurement: {msg}")
        
        return sled.weight / tractor_weight

    def get_recommendations(self, comparison: SledComparisonResult) -> List[str]:
        """Generate recommendations based on sled comparison."""
        recommendations = []
        
        if not comparison.type_compatibility:
            recommendations.append("Sled types are not compatible for direct comparison")
        
        if comparison.weight_diff > 500:  # kg
            recommendations.append("Significant weight difference may affect performance")
            
        if comparison.hitch_height_diff > 0.1:  # meters
            recommendations.append("Hitch height difference may require tractor adjustments")
            
        if comparison.pan_height_diff > 0.15:  # meters
            recommendations.append("Pan height difference may affect weight transfer")
            
        return recommendations


# Example usage
if __name__ == "__main__":
    analyzer = SledAnalyzer()
    
    sled1 = SledMeasurement(
        length=6.5,
        width=2.5,
        weight=4500,
        pan_height=0.5,
        hitch_height=0.6,
        type=SledType.STANDARD
    )
    
    sled2 = SledMeasurement(
        length=7.0,
        width=2.4,
        weight=5000,
        pan_height=0.55,
        hitch_height=0.65,
        type=SledType.MODIFIED
    )
    
    try:
        comparison = analyzer.compare_sleds(sled1, sled2)
        print(f"Comparison Results:\n{comparison}")
        
        pull_ratio = analyzer.calculate_pull_ratio(sled1, 8000)
        print(f"Pull Ratio for Sled 1: {pull_ratio:.2f}")
        
        recommendations = analyzer.get_recommendations(comparison)
        print("\nRecommendations:")
        for rec in recommendations:
            print(f"- {rec}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
