"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Create a Python script to automate the generation of safety recommendations for accessing rooftops securely, inspired by AFCO's guidelines on preventing falls from heights.
Generated: DETERMINISTIC_ef3ba8022ad42fe3
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum, auto

class SafetyLevel(Enum):
    """Enum representing different safety levels for rooftop access."""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    EXTREME = auto()

class RooftopSafetyGenerator:
    """
    A class to generate safety recommendations for rooftop access based on AFCO guidelines.
    """
    
    def __init__(self):
        self.recommendations = {
            SafetyLevel.LOW: [
                "Conduct a pre-access risk assessment",
                "Ensure proper footwear with slip-resistant soles",
                "Check weather conditions before access"
            ],
            SafetyLevel.MEDIUM: [
                "Install temporary guardrails or barriers",
                "Use a safety harness with proper anchor points",
                "Have a spotter present during access"
            ],
            SafetyLevel.HIGH: [
                "Implement a permit-to-work system",
                "Use a fall arrest system with full body harness",
                "Conduct safety training for all personnel"
            ],
            SafetyLevel.EXTREME: [
                "Restrict access to trained professionals only",
                "Use a safety net system below work area",
                "Implement continuous monitoring during access"
            ]
        }
        
        self.additional_checks = [
            "Inspect rooftop surface for stability",
            "Verify structural integrity of anchor points",
            "Check for overhead hazards",
            "Ensure emergency rescue plan is in place"
        ]
    
    def determine_safety_level(self, height: float, slope: float, access_frequency: str) -> SafetyLevel:
        """
        Determine the safety level based on rooftop parameters.
        
        Args:
            height: Height of the rooftop in meters
            slope: Slope of the rooftop in degrees
            access_frequency: Frequency of access ('rare', 'occasional', 'frequent', 'constant')
            
        Returns:
            SafetyLevel: The determined safety level
        """
        if height > 10 or slope > 30 or access_frequency == 'constant':
            return SafetyLevel.EXTREME
        elif height > 6 or slope > 15 or access_frequency == 'frequent':
            return SafetyLevel.HIGH
        elif height > 3 or slope > 5 or access_frequency == 'occasional':
            return SafetyLevel.MEDIUM
        else:
            return SafetyLevel.LOW
    
    def generate_recommendations(self, height: float, slope: float, access_frequency: str) -> dict:
        """
        Generate safety recommendations based on rooftop parameters.
        
        Args:
            height: Height of the rooftop in meters
            slope: Slope of the rooftop in degrees
            access_frequency: Frequency of access ('rare', 'occasional', 'frequent', 'constant')
            
        Returns:
            dict: A dictionary containing all safety recommendations
        """
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Height must be a positive number")
        if not isinstance(slope, (int, float)) or slope < 0 or slope > 90:
            raise ValueError("Slope must be a number between 0 and 90 degrees")
        if access_frequency not in ['rare', 'occasional', 'frequent', 'constant']:
            raise ValueError("Invalid access frequency")
        
        safety_level = self.determine_safety_level(height, slope, access_frequency)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "parameters": {
                "height_meters": height,
                "slope_degrees": slope,
                "access_frequency": access_frequency
            },
            "safety_level": safety_level.name,
            "specific_recommendations": self.recommendations[safety_level],
            "additional_checks": self.additional_checks,
            "compliance_notes": "Always follow local regulations and AFCO guidelines"
        }
    
    def save_to_file(self, recommendations: dict, filename: str = "rooftop_safety_report.json") -> None:
        """
        Save recommendations to a JSON file.
        
        Args:
            recommendations: Dictionary containing safety recommendations
            filename: Name of the output file
        """
        try:
            with open(filename, 'w') as f:
                json.dump(recommendations, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save recommendations: {str(e)}")

def main():
    """Main function to demonstrate the rooftop safety generator."""
    try:
        generator = RooftopSafetyGenerator()
        
        # Example parameters
        height = 7.5  # meters
        slope = 20    # degrees
        access_frequency = "frequent"
        
        # Generate recommendations
        recommendations = generator.generate_recommendations(height, slope, access_frequency)
        
        # Print to console
        print("Rooftop Safety Recommendations:")
        print(json.dumps(recommendations, indent=4))
        
        # Save to file
        generator.save_to_file(recommendations)
        print(f"\nRecommendations saved to 'rooftop_safety_report.json'")
        
    except Exception as e:
        print(f"Error generating recommendations: {str(e)}")

if __name__ == "__main__":
    main()
```
