"""
Generated Code Metadata:
========================
Original URL: https://sctoll.io
Prompt: "Write a Python script to determine the optimal wheel fitment for a luxury vehicle, such as a Rolls-Royce Wraith, using Brixton Forged's wheel collection and vehicle specifications."
Generated: DETERMINISTIC_c68097bba769a38c
Batch ID: 20250622_211454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class WheelSpecs:
    """Dataclass to store wheel specifications."""
    model: str
    diameter: float  # in inches
    width: float     # in inches
    offset: float    # in mm
    bolt_pattern: str
    center_bore: float  # in mm
    material: str
    finish: str

@dataclass
class VehicleSpecs:
    """Dataclass to store vehicle specifications."""
    make: str
    model: str
    year: int
    stock_wheel_diameter: float  # in inches
    stock_wheel_width: float     # in inches
    stock_offset: float          # in mm
    bolt_pattern: str
    center_bore: float           # in mm
    min_tire_width: float        # in mm
    max_tire_width: float        # in mm
    min_tire_aspect_ratio: float # in percentage
    max_tire_aspect_ratio: float # in percentage

class WheelFitmentCalculator:
    """Class to calculate optimal wheel fitment for a vehicle."""
    
    def __init__(self, vehicle_specs: VehicleSpecs, wheels_db: List[WheelSpecs]):
        """
        Initialize with vehicle specs and available wheels database.
        
        Args:
            vehicle_specs: VehicleSpecs object containing vehicle details
            wheels_db: List of WheelSpecs objects representing available wheels
        """
        self.vehicle_specs = vehicle_specs
        self.wheels_db = wheels_db
    
    def _validate_wheel(self, wheel: WheelSpecs) -> bool:
        """Validate if a wheel meets basic compatibility requirements."""
        try:
            # Check bolt pattern and center bore
            if (wheel.bolt_pattern != self.vehicle_specs.bolt_pattern or 
                wheel.center_bore < self.vehicle_specs.center_bore):
                return False
            
            # Check diameter is within reasonable range (stock ± 3 inches)
            if not (self.vehicle_specs.stock_wheel_diameter - 3 <= wheel.diameter <= 
                    self.vehicle_specs.stock_wheel_diameter + 3):
                return False
            
            return True
        except Exception as e:
            print(f"Error validating wheel: {e}")
            return False
    
    def calculate_fitment_score(self, wheel: WheelSpecs) -> float:
        """
        Calculate a fitment score for a wheel (0-100).
        Higher score means better fitment.
        """
        try:
            if not self._validate_wheel(wheel):
                return 0
            
            score = 100
            
            # Deduct points based on diameter difference from stock
            diameter_diff = abs(wheel.diameter - self.vehicle_specs.stock_wheel_diameter)
            score -= diameter_diff * 5
            
            # Deduct points based on width difference from stock
            width_diff = abs(wheel.width - self.vehicle_specs.stock_wheel_width)
            score -= width_diff * 3
            
            # Deduct points based on offset difference from stock
            offset_diff = abs(wheel.offset - self.vehicle_specs.stock_offset)
            score -= offset_diff * 0.5
            
            # Ensure score is within bounds
            return max(0, min(100, score))
        except Exception as e:
            print(f"Error calculating fitment score: {e}")
            return 0
    
    def get_optimal_wheels(self, top_n: int = 5) -> List[Dict]:
        """
        Get top N optimal wheels based on fitment score.
        
        Args:
            top_n: Number of top wheels to return
            
        Returns:
            List of dictionaries containing wheel info and score, sorted by score
        """
        try:
            scored_wheels = []
            for wheel in self.wheels_db:
                score = self.calculate_fitment_score(wheel)
                if score > 0:
                    scored_wheels.append({
                        'model': wheel.model,
                        'diameter': wheel.diameter,
                        'width': wheel.width,
                        'offset': wheel.offset,
                        'material': wheel.material,
                        'finish': wheel.finish,
                        'score': round(score, 2)
                    })
            
            # Sort by score descending
            scored_wheels.sort(key=lambda x: x['score'], reverse=True)
            return scored_wheels[:top_n]
        except Exception as e:
            print(f"Error getting optimal wheels: {e}")
            return []

def load_wheels_from_json(file_path: str) -> List[WheelSpecs]:
    """Load wheel specifications from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [WheelSpecs(**wheel) for wheel in data]
    except Exception as e:
        print(f"Error loading wheels from JSON: {e}")
        return []

def main():
    """Main function to demonstrate wheel fitment calculation."""
    # Example vehicle specs for Rolls-Royce Wraith
    wraith_specs = VehicleSpecs(
        make="Rolls-Royce",
        model="Wraith",
        year=2023,
        stock_wheel_diameter=21.0,
        stock_wheel_width=9.5,
        stock_offset=40,
        bolt_pattern="5x120",
        center_bore=72.6,
        min_tire_width=245,
        max_tire_width=285,
        min_tire_aspect_ratio=35,
        max_tire_aspect_ratio=45
    )
    
    # Load wheels database (in a real scenario, this would be from a DB or API)
    try:
        wheels_db = load_wheels_from_json("brixton_forged_wheels.json")
    except:
        # Fallback example data if file not found
        wheels_db = [
            WheelSpecs(
                model="Brixton Forged M14",
                diameter=21.0,
                width=9.5,
                offset=40,
                bolt_pattern="5x120",
                center_bore=72.6,
                material="Forged Aluminum",
                finish="Gloss Black"
            ),
            WheelSpecs(
                model="Brixton Forged RF1",
                diameter=22.0,
                width=10.0,
                offset=35,
                bolt_pattern="5x120",
                center_bore=72.6,
                material="Forged Aluminum",
                finish="Brushed Titanium"
            ),
            WheelSpecs(
                model="Brixton Forged CM1",
                diameter=20.0,
                width=9.0,
                offset=45,
                bolt_pattern="5x120",
                center_bore=72.6,
                material="Forged Aluminum",
                finish="Polished"
            )
        ]
    
    # Calculate optimal wheels
    calculator = WheelFitmentCalculator(wraith_specs, wheels_db)
    optimal_wheels = calculator.get_optimal_wheels()
    
    # Print results
    print(f"Optimal wheel fitment for {wraith_specs.make} {wraith_specs.model}:")
    for i, wheel in enumerate(optimal_wheels, 1):
        print(f"{i}. {wheel['model']} - Score: {wheel['score']}")
        print(f"   Size: {wheel['diameter']}x{wheel['width']}, Offset: {wheel['offset']}mm")
        print(f"   Material: {wheel['material']}, Finish: {wheel['finish']}\n")

if __name__ == "__main__":
    main()
```
