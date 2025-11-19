"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Generate a Python script to calculate the optimal tractor model for agricultural tasks based on user input, considering SCOUT's specifications and features.
Generated: DETERMINISTIC_bc19267b0aa81484
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class TractorSpec:
    """Data class to store tractor specifications."""
    model: str
    horsepower: float
    fuel_efficiency: float  # in liters per hour
    cost: float
    weight: float  # in kg
    features: List[str]
    suitability_score: float = 0.0

class TractorSelector:
    """Class to select the optimal tractor based on user requirements."""
    
    def __init__(self):
        self.tractors = [
            TractorSpec(
                model="SCOUT-100",
                horsepower=75,
                fuel_efficiency=5.2,
                cost=45000,
                weight=3200,
                features=["4WD", "Basic GPS", "Standard PTO"]
            ),
            TractorSpec(
                model="SCOUT-200",
                horsepower=95,
                fuel_efficiency=5.8,
                cost=55000,
                weight=3800,
                features=["4WD", "Advanced GPS", "Enhanced PTO", "Auto-Steer"]
            ),
            TractorSpec(
                model="SCOUT-300",
                horsepower=120,
                fuel_efficiency=6.5,
                cost=68000,
                weight=4200,
                features=["4WD", "Premium GPS", "Enhanced PTO", "Auto-Steer", "Telematics"]
            )
        ]
    
    def get_user_input(self) -> Dict[str, float]:
        """Collect user requirements for tractor selection."""
        print("Please enter your requirements for the tractor:")
        try:
            min_horsepower = float(input("Minimum horsepower required: "))
            max_fuel_consumption = float(input("Maximum fuel consumption (liters/hour): "))
            max_cost = float(input("Maximum budget (USD): "))
            required_features = input("Required features (comma-separated, e.g., '4WD,GPS'): ").split(',')
            required_features = [f.strip() for f in required_features if f.strip()]
            
            return {
                "min_horsepower": min_horsepower,
                "max_fuel_consumption": max_fuel_consumption,
                "max_cost": max_cost,
                "required_features": required_features
            }
        except ValueError as e:
            print(f"Invalid input: {e}")
            sys.exit(1)
    
    def calculate_suitability(self, tractor: TractorSpec, requirements: Dict[str, float]) -> float:
        """Calculate suitability score for a tractor based on requirements."""
        score = 0.0
        
        # Horsepower contribution (30% weight)
        hp_score = min(1.0, tractor.horsepower / requirements["min_horsepower"])
        score += hp_score * 0.3
        
        # Fuel efficiency contribution (25% weight)
        if tractor.fuel_efficiency <= requirements["max_fuel_consumption"]:
            fe_score = 1 - (tractor.fuel_efficiency / requirements["max_fuel_consumption"])
            score += fe_score * 0.25
        
        # Cost contribution (25% weight)
        if tractor.cost <= requirements["max_cost"]:
            cost_score = 1 - (tractor.cost / requirements["max_cost"])
            score += cost_score * 0.25
        
        # Features contribution (20% weight)
        required_features = set(requirements["required_features"])
        tractor_features = set(tractor.features)
        matched_features = required_features.intersection(tractor_features)
        feature_score = len(matched_features) / len(required_features) if required_features else 1.0
        score += feature_score * 0.2
        
        return score
    
    def filter_tractors(self, requirements: Dict[str, float]) -> List[TractorSpec]:
        """Filter tractors based on basic requirements."""
        filtered = []
        for tractor in self.tractors:
            if (tractor.horsepower >= requirements["min_horsepower"] and
                tractor.fuel_efficiency <= requirements["max_fuel_consumption"] and
                tractor.cost <= requirements["max_cost"]):
                
                # Check if all required features are present
                required_features = set(requirements["required_features"])
                tractor_features = set(tractor.features)
                if required_features.issubset(tractor_features):
                    filtered.append(tractor)
        
        return filtered
    
    def select_optimal_tractor(self) -> Optional[TractorSpec]:
        """Main method to select the optimal tractor."""
        requirements = self.get_user_input()
        candidates = self.filter_tractors(requirements)
        
        if not candidates:
            print("No tractors meet your requirements.")
            return None
        
        # Calculate suitability scores
        for tractor in candidates:
            tractor.suitability_score = self.calculate_suitability(tractor, requirements)
        
        # Select tractor with highest score
        optimal_tractor = max(candidates, key=lambda x: x.suitability_score)
        return optimal_tractor
    
    def display_result(self, tractor: Optional[TractorSpec]):
        """Display the selection result to the user."""
        if not tractor:
            return
        
        print("\nOptimal Tractor Selection:")
        print("-------------------------")
        print(f"Model: {tractor.model}")
        print(f"Horsepower: {tractor.horsepower} HP")
        print(f"Fuel Efficiency: {tractor.fuel_efficiency} L/h")
        print(f"Cost: ${tractor.cost:,.2f}")
        print(f"Weight: {tractor.weight} kg")
        print(f"Features: {', '.join(tractor.features)}")
        print(f"Suitability Score: {tractor.suitability_score:.2%}")
        print("-------------------------")

def main():
    """Main function to run the tractor selection program."""
    selector = TractorSelector()
    optimal_tractor = selector.select_optimal_tractor()
    selector.display_result(optimal_tractor)

if __name__ == "__main__":
    main()
```
