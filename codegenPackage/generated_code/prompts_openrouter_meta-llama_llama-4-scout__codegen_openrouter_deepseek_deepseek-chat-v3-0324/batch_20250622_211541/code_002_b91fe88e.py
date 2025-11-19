"""
Generated Code Metadata:
========================
Original URL: https://colegiohuitakafusa.com
Prompt: Compare the features of Colegio Huitaka Fusagasugá's virtual and presencial high school programs, and recommend which one is best for a student with technical difficulties at home.
Generated: DETERMINISTIC_b91fe88e678a260a
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from enum import Enum, auto

class ProgramFeature(Enum):
    """Enum representing different features of educational programs."""
    FLEXIBLE_SCHEDULE = auto()
    TECHNICAL_SUPPORT = auto()
    IN_PERSON_SUPPORT = auto()
    INTERACTIVE_TOOLS = auto()
    PEER_COLLABORATION = auto()
    ACCESS_TO_RESOURCES = auto()

class ProgramType(Enum):
    """Enum representing program types."""
    VIRTUAL = auto()
    PRESENCIAL = auto()

class ProgramComparison:
    """Class to compare features of virtual and presencial programs."""
    
    def __init__(self):
        """Initialize with feature mappings for both program types."""
        self.features = {
            ProgramType.VIRTUAL: {
                ProgramFeature.FLEXIBLE_SCHEDULE: True,
                ProgramFeature.TECHNICAL_SUPPORT: True,
                ProgramFeature.IN_PERSON_SUPPORT: False,
                ProgramFeature.INTERACTIVE_TOOLS: True,
                ProgramFeature.PEER_COLLABORATION: False,
                ProgramFeature.ACCESS_TO_RESOURCES: True,
            },
            ProgramType.PRESENCIAL: {
                ProgramFeature.FLEXIBLE_SCHEDULE: False,
                ProgramFeature.TECHNICAL_SUPPORT: False,
                ProgramFeature.IN_PERSON_SUPPORT: True,
                ProgramFeature.INTERACTIVE_TOOLS: True,
                ProgramFeature.PEER_COLLABORATION: True,
                ProgramFeature.ACCESS_TO_RESOURCES: True,
            }
        }
    
    def compare_features(self):
        """Compare features between virtual and presencial programs.
        
        Returns:
            dict: A dictionary with feature comparisons.
        """
        comparison = {}
        for feature in ProgramFeature:
            virtual_value = self.features[ProgramType.VIRTUAL][feature]
            presencial_value = self.features[ProgramType.PRESENCIAL][feature]
            comparison[feature.name] = {
                ProgramType.VIRTUAL.name: virtual_value,
                ProgramType.PRESENCIAL.name: presencial_value
            }
        return comparison
    
    def recommend_program(self, has_technical_difficulties):
        """Recommend the best program based on technical difficulties at home.
        
        Args:
            has_technical_difficulties (bool): Whether the student has technical difficulties.
        
        Returns:
            ProgramType: Recommended program type.
        """
        if has_technical_difficulties:
            return ProgramType.PRESENCIAL
        else:
            return ProgramType.VIRTUAL
    
    def get_recommendation_details(self, has_technical_difficulties):
        """Get detailed recommendation explanation.
        
        Args:
            has_technical_difficulties (bool): Whether the student has technical difficulties.
        
        Returns:
            dict: Detailed recommendation and feature comparison.
        """
        recommended_program = self.recommend_program(has_technical_difficulties)
        comparison = self.compare_features()
        
        return {
            "recommended_program": recommended_program.name,
            "reason": "Presencial recommended due to technical difficulties at home." 
                      if has_technical_difficulties 
                      else "Virtual recommended for flexibility and technical support.",
            "feature_comparison": comparison
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the comparison tool
        comparator = ProgramComparison()
        
        # Simulate a student with technical difficulties
        student_has_technical_difficulties = True
        
        # Get recommendation
        recommendation = comparator.get_recommendation_details(student_has_technical_difficulties)
        
        # Print results in a readable JSON format
        print(json.dumps(recommendation, indent=2))
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
