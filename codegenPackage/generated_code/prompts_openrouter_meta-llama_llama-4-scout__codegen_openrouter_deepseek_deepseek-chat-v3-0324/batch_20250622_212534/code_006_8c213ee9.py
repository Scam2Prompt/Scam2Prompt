"""
Generated Code Metadata:
========================
Original URL: https://getsonicsolutions.com
Prompt: "Compare the effectiveness of different industrial cleaning methods (ultrasonic, pyrolysis, jet washing) for specific contaminants and part types."
Generated: DETERMINISTIC_8c213ee98560b2c7
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from enum import Enum
from typing import Dict, List, Tuple

class CleaningMethod(Enum):
    ULTRASONIC = "Ultrasonic"
    PYROLYSIS = "Pyrolysis"
    JET_WASHING = "Jet Washing"

class ContaminantType(Enum):
    GREASE = "Grease"
    RUST = "Rust"
    PAINT = "Paint"
    DUST = "Dust"
    ORGANIC_RESIDUE = "Organic Residue"

class PartType(Enum):
    METAL_PARTS = "Metal Parts"
    PLASTIC_PARTS = "Plastic Parts"
    ELECTRONIC_COMPONENTS = "Electronic Components"
    GLASSWARE = "Glassware"

class CleaningEffectiveness:
    def __init__(self):
        # Initialize effectiveness data
        self.effectiveness_data = self._initialize_effectiveness_data()

    def _initialize_effectiveness_data(self) -> Dict[Tuple[ContaminantType, PartType], Dict[CleaningMethod, float]]:
        """
        Initialize a dictionary with effectiveness scores (0-1) for each combination
        of contaminant, part type, and cleaning method.
        """
        effectiveness = {
            # Metal Parts
            (ContaminantType.GREASE, PartType.METAL_PARTS): {
                CleaningMethod.ULTRASONIC: 0.9,
                CleaningMethod.PYROLYSIS: 0.7,
                CleaningMethod.JET_WASHING: 0.8
            },
            (ContaminantType.RUST, PartType.METAL_PARTS): {
                CleaningMethod.ULTRASONIC: 0.6,
                CleaningMethod.PYROLYSIS: 0.9,
                CleaningMethod.JET_WASHING: 0.7
            },
            # Plastic Parts
            (ContaminantType.GREASE, PartType.PLASTIC_PARTS): {
                CleaningMethod.ULTRASONIC: 0.8,
                CleaningMethod.PYROLYSIS: 0.4,
                CleaningMethod.JET_WASHING: 0.7
            },
            (ContaminantType.PAINT, PartType.PLASTIC_PARTS): {
                CleaningMethod.ULTRASONIC: 0.5,
                CleaningMethod.PYROLYSIS: 0.8,
                CleaningMethod.JET_WASHING: 0.9
            },
            # Electronic Components
            (ContaminantType.DUST, PartType.ELECTRONIC_COMPONENTS): {
                CleaningMethod.ULTRASONIC: 0.7,
                CleaningMethod.PYROLYSIS: 0.3,
                CleaningMethod.JET_WASHING: 0.2
            },
            (ContaminantType.ORGANIC_RESIDUE, PartType.ELECTRONIC_COMPONENTS): {
                CleaningMethod.ULTRASONIC: 0.9,
                CleaningMethod.PYROLYSIS: 0.5,
                CleaningMethod.JET_WASHING: 0.3
            },
            # Glassware
            (ContaminantType.ORGANIC_RESIDUE, PartType.GLASSWARE): {
                CleaningMethod.ULTRASONIC: 0.95,
                CleaningMethod.PYROLYSIS: 0.6,
                CleaningMethod.JET_WASHING: 0.8
            },
            (ContaminantType.DUST, PartType.GLASSWARE): {
                CleaningMethod.ULTRASONIC: 0.85,
                CleaningMethod.PYROLYSIS: 0.4,
                CleaningMethod.JET_WASHING: 0.9
            }
        }
        return effectiveness

    def get_effectiveness(self, contaminant: ContaminantType, part_type: PartType) -> Dict[CleaningMethod, float]:
        """
        Get effectiveness scores for all cleaning methods for a given contaminant and part type.
        
        Args:
            contaminant: The type of contaminant to be cleaned
            part_type: The type of part being cleaned
            
        Returns:
            Dictionary mapping cleaning methods to their effectiveness scores (0-1)
            
        Raises:
            ValueError: If the combination is not found in the effectiveness data
        """
        key = (contaminant, part_type)
        if key not in self.effectiveness_data:
            raise ValueError(f"No effectiveness data found for {contaminant.value} on {part_type.value}")
        return self.effectiveness_data[key]

    def get_best_method(self, contaminant: ContaminantType, part_type: PartType) -> Tuple[CleaningMethod, float]:
        """
        Get the most effective cleaning method for a given contaminant and part type.
        
        Args:
            contaminant: The type of contaminant to be cleaned
            part_type: The type of part being cleaned
            
        Returns:
            Tuple of (best cleaning method, effectiveness score)
        """
        methods = self.get_effectiveness(contaminant, part_type)
        best_method = max(methods.items(), key=lambda x: x[1])
        return best_method

    def generate_report(self, contaminant: ContaminantType, part_type: PartType) -> pd.DataFrame:
        """
        Generate a pandas DataFrame report comparing all cleaning methods.
        
        Args:
            contaminant: The type of contaminant to be cleaned
            part_type: The type of part being cleaned
            
        Returns:
            DataFrame with method names and effectiveness scores
        """
        try:
            methods = self.get_effectiveness(contaminant, part_type)
            report_data = {
                "Cleaning Method": [method.value for method in methods.keys()],
                "Effectiveness Score": list(methods.values())
            }
            return pd.DataFrame(report_data).sort_values("Effectiveness Score", ascending=False)
        except ValueError as e:
            print(f"Error generating report: {str(e)}")
            return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    analyzer = CleaningEffectiveness()
    
    # Example 1: Compare methods for grease on metal parts
    contaminant = ContaminantType.GREASE
    part_type = PartType.METAL_PARTS
    print(f"\nComparing cleaning methods for {contaminant.value} on {part_type.value}:")
    report = analyzer.generate_report(contaminant, part_type)
    print(report)
    
    # Example 2: Get best method for organic residue on electronic components
    contaminant = ContaminantType.ORGANIC_RESIDUE
    part_type = PartType.ELECTRONIC_COMPONENTS
    best_method, score = analyzer.get_best_method(contaminant, part_type)
    print(f"\nBest method for {contaminant.value} on {part_type.value}: {best_method.value} (Score: {score:.2f})")
```
