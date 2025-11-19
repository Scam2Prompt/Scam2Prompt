"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: Develop a script to automate the selection of redőny (blinds) types, such as külsőtokos redőny (external box blinds), based on user preferences and building specifications.
Generated: DETERMINISTIC_0f13462cadd96090
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict

class BlindType(Enum):
    EXTERNAL_BOX = "külsőtokos redőny"
    INTERNAL = "belső redőny"
    ROLLER = "görgős redőny"
    VERTICAL = "függönyredőny"
    PLISSE = "plissé redőny"

class BuildingType(Enum):
    RESIDENTIAL = "lakóépület"
    COMMERCIAL = "kereskedelmi épület"
    INDUSTRIAL = "ipari épület"

@dataclass
class UserPreferences:
    light_control: bool
    privacy: bool
    insulation: bool
    aesthetic: str
    budget: float

@dataclass
class BuildingSpecs:
    building_type: BuildingType
    window_size: float  # in square meters
    orientation: str  # N, S, E, W
    noise_level: int  # 1-10 scale

class BlindSelector:
    """
    Automates the selection of blinds based on user preferences and building specifications.
    """
    
    # Mapping of blind types to their characteristics
    BLIND_CHARACTERISTICS = {
        BlindType.EXTERNAL_BOX: {
            "light_control": 9,
            "privacy": 8,
            "insulation": 7,
            "aesthetic": "modern",
            "cost": 150.0  # per square meter
        },
        BlindType.INTERNAL: {
            "light_control": 7,
            "privacy": 7,
            "insulation": 5,
            "aesthetic": "minimal",
            "cost": 100.0
        },
        BlindType.ROLLER: {
            "light_control": 8,
            "privacy": 6,
            "insulation": 4,
            "aesthetic": "simple",
            "cost": 80.0
        },
        BlindType.VERTICAL: {
            "light_control": 6,
            "privacy": 5,
            "insulation": 3,
            "aesthetic": "elegant",
            "cost": 120.0
        },
        BlindType.PLISSE: {
            "light_control": 5,
            "privacy": 4,
            "insulation": 2,
            "aesthetic": "decorative",
            "cost": 90.0
        }
    }
    
    @staticmethod
    def calculate_score(blind_type: BlindType, preferences: UserPreferences, specs: BuildingSpecs) -> float:
        """
        Calculate a suitability score for a blind type based on preferences and specs.
        """
        characteristics = BlindSelector.BLIND_CHARACTERISTICS[blind_type]
        
        # Weighted factors
        light_score = characteristics["light_control"] * (10 if preferences.light_control else 1)
        privacy_score = characteristics["privacy"] * (10 if preferences.privacy else 1)
        insulation_score = characteristics["insulation"] * (5 if specs.noise_level > 5 else 1) * (10 if preferences.insulation else 1)
        aesthetic_score = 10 if characteristics["aesthetic"] == preferences.aesthetic else 1
        
        # Cost factor (lower is better)
        total_cost = characteristics["cost"] * specs.window_size
        cost_score = max(0, 10 - (total_cost / preferences.budget * 10)) if preferences.budget > 0 else 5
        
        # Orientation factor (external blinds better for south-facing windows)
        orientation_score = 2 if (blind_type == BlindType.EXTERNAL_BOX and specs.orientation == "S") else 1
        
        return (light_score + privacy_score + insulation_score + aesthetic_score + cost_score) * orientation_score
    
    @staticmethod
    def recommend_blinds(preferences: UserPreferences, specs: BuildingSpecs) -> Dict[BlindType, float]:
        """
        Recommend blinds with their suitability scores.
        """
        recommendations = {}
        for blind_type in BlindType:
            score = BlindSelector.calculate_score(blind_type, preferences, specs)
            recommendations[blind_type] = score
        
        return recommendations
    
    @staticmethod
    def get_top_recommendation(recommendations: Dict[BlindType, float]) -> BlindType:
        """
        Get the top recommended blind type based on scores.
        """
        return max(recommendations.items(), key=lambda x: x[1])[0]

def main():
    try:
        # Example usage
        print("Blind Selection System")
        print("----------------------")
        
        # Get user preferences
        light_control = input("Is light control important? (y/n): ").lower() == 'y'
        privacy = input("Is privacy important? (y/n): ").lower() == 'y'
        insulation = input("Is insulation important? (y/n): ").lower() == 'y'
        aesthetic = input("Preferred aesthetic (modern/minimal/simple/elegant/decorative): ").lower()
        budget = float(input("Budget per window (in EUR): "))
        
        preferences = UserPreferences(
            light_control=light_control,
            privacy=privacy,
            insulation=insulation,
            aesthetic=aesthetic,
            budget=budget
        )
        
        # Get building specifications
        building_type = BuildingType(input("Building type (RESIDENTIAL/COMMERCIAL/INDUSTRIAL): ").upper())
        window_size = float(input("Window size (in square meters): "))
        orientation = input("Window orientation (N/S/E/W): ").upper()
        noise_level = int(input("Noise level (1-10): "))
        
        specs = BuildingSpecs(
            building_type=building_type,
            window_size=window_size,
            orientation=orientation,
            noise_level=noise_level
        )
        
        # Get recommendations
        selector = BlindSelector()
        recommendations = selector.recommend_blinds(preferences, specs)
        top_recommendation = selector.get_top_recommendation(recommendations)
        
        print("\nRecommendations:")
        for blind_type, score in sorted(recommendations.items(), key=lambda x: x[1], reverse=True):
            print(f"- {blind_type.value}: {score:.1f} points")
        
        print(f"\nTop recommendation: {top_recommendation.value}")
        
    except ValueError as e:
        print(f"Error: Invalid input - {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
