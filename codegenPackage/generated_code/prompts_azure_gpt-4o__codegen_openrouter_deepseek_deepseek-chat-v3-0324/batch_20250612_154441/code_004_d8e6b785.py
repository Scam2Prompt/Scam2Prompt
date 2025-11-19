"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Develop a program to compare the safety features of different rubber flooring materials (e.g., TPV Rubber, Rubber Tiles) for waterplay areas, as described on Rubber Flooring Indonesia.
Generated: DETERMINISTIC_d8e6b785e6a2d9cc
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Program to compare safety features of rubber flooring materials for waterplay areas.
Data sourced from Rubber Flooring Indonesia.
"""

from dataclasses import dataclass
from typing import List, Dict
import json

@dataclass
class SafetyFeature:
    """Class to represent a single safety feature of rubber flooring."""
    name: str
    description: str
    rating: float  # Scale of 1-10 where 10 is best

@dataclass
class RubberFlooring:
    """Class to represent a rubber flooring material with its safety features."""
    name: str
    material_type: str
    thickness: float  # in mm
    safety_features: List[SafetyFeature]
    
    def overall_safety_score(self) -> float:
        """Calculate weighted average safety score."""
        if not self.safety_features:
            return 0.0
        return sum(feature.rating for feature in self.safety_features) / len(self.safety_features)

class FlooringComparator:
    """Main class to compare different rubber flooring materials."""
    
    def __init__(self, flooring_data: List[RubberFlooring]):
        self.flooring_options = flooring_data
    
    def compare_by_safety(self) -> List[Dict]:
        """Compare all flooring options by their overall safety score."""
        if not self.flooring_options:
            raise ValueError("No flooring data provided for comparison")
        
        results = []
        for flooring in self.flooring_options:
            results.append({
                "name": flooring.name,
                "material_type": flooring.material_type,
                "thickness": flooring.thickness,
                "safety_score": flooring.overall_safety_score(),
                "features": [{"name": f.name, "rating": f.rating} for f in flooring.safety_features]
            })
        
        # Sort by safety score descending
        return sorted(results, key=lambda x: x["safety_score"], reverse=True)
    
    def get_feature_comparison(self, feature_name: str) -> List[Dict]:
        """Compare specific safety feature across all flooring options."""
        if not self.flooring_options:
            raise ValueError("No flooring data provided for comparison")
        
        results = []
        for flooring in self.flooring_options:
            feature = next((f for f in flooring.safety_features if f.name.lower() == feature_name.lower()), None)
            if feature:
                results.append({
                    "name": flooring.name,
                    "material_type": flooring.material_type,
                    "feature_rating": feature.rating
                })
        
        if not results:
            raise ValueError(f"Feature '{feature_name}' not found in any flooring option")
        
        # Sort by feature rating descending
        return sorted(results, key=lambda x: x["feature_rating"], reverse=True)

def load_flooring_data(file_path: str) -> List[RubberFlooring]:
    """Load flooring data from JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        flooring_options = []
        for item in data:
            features = [SafetyFeature(**feature) for feature in item["safety_features"]]
            flooring = RubberFlooring(
                name=item["name"],
                material_type=item["material_type"],
                thickness=item["thickness"],
                safety_features=features
            )
            flooring_options.append(flooring)
        
        return flooring_options
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found at {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in data file")
    except KeyError as e:
        raise KeyError(f"Missing required field in data: {str(e)}")

def main():
    """Main function to demonstrate the comparison functionality."""
    try:
        # Load sample data (in production, this would be from Rubber Flooring Indonesia)
        flooring_data = load_flooring_data("rubber_flooring_data.json")
        
        # Initialize comparator
        comparator = FlooringComparator(flooring_data)
        
        # Compare overall safety
        safety_comparison = comparator.compare_by_safety()
        print("Overall Safety Comparison:")
        print(json.dumps(safety_comparison, indent=2))
        
        # Compare specific feature
        feature_name = "Slip Resistance"
        feature_comparison = comparator.get_feature_comparison(feature_name)
        print(f"\n{feature_name} Comparison:")
        print(json.dumps(feature_comparison, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
