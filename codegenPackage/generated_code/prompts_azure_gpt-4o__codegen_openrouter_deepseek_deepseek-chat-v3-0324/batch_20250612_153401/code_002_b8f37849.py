"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Generate code to analyze the weight and aerodynamic properties of Hunt wheels (1380g) and their compatibility with modern width road tires, as highlighted on the Race Ride Fire website.
Generated: DETERMINISTIC_b8f37849e0a76150
Batch ID: 20250612_153401
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
from typing import Optional, List, Dict

@dataclass
class WheelAnalysis:
    """Dataclass to store wheel analysis results."""
    wheel_model: str
    weight_grams: int
    max_tire_width_mm: int
    is_aero_optimized: bool
    compatibility_rating: float
    notes: Optional[str] = None

class WheelAnalyzer:
    """Analyzes wheel properties and compatibility with modern road tires."""
    
    def __init__(self, wheel_data: Dict):
        """
        Initialize with wheel data.
        
        Args:
            wheel_data: Dictionary containing wheel specifications
        """
        self.wheel_data = wheel_data
        self.standard_tire_widths = [23, 25, 28, 30, 32]  # in mm
        
    def _calculate_aero_score(self, rim_depth: int, rim_width: int) -> float:
        """Calculate aerodynamic score based on rim dimensions."""
        if rim_depth < 25:
            aero_score = 0.5
        elif 25 <= rim_depth < 40:
            aero_score = 0.7
        else:
            aero_score = 0.9
            
        width_factor = min(1.0, rim_width / 25)
        return aero_score * width_factor
    
    def _check_tire_compatibility(self, max_tire_width: int) -> Dict[int, bool]:
        """Check compatibility with standard tire widths."""
        compatibility = {}
        for width in self.standard_tire_widths:
            compatibility[width] = width <= max_tire_width
        return compatibility
    
    def analyze_wheel(self) -> WheelAnalysis:
        """Perform comprehensive wheel analysis."""
        try:
            # Extract data
            model = self.wheel_data.get('model', 'Unknown')
            weight = self.wheel_data.get('weight_grams', 0)
            max_width = self.wheel_data.get('max_tire_width_mm', 25)
            rim_depth = self.wheel_data.get('rim_depth_mm', 0)
            rim_width = self.wheel_data.get('rim_width_mm', 0)
            
            # Perform calculations
            aero_score = self._calculate_aero_score(rim_depth, rim_width)
            tire_compatibility = self._check_tire_compatibility(max_width)
            
            # Calculate overall compatibility rating
            compatible_widths = sum(tire_compatibility.values())
            total_widths = len(self.standard_tire_widths)
            compatibility_rating = compatible_widths / total_widths
            
            # Determine if aero optimized
            is_aero_optimized = aero_score >= 0.7
            
            # Generate notes
            notes = []
            if weight < 1500:
                notes.append("Lightweight construction")
            if rim_depth >= 30:
                notes.append("Deep rim profile for aero benefits")
            if max_width >= 28:
                notes.append("Wide tire compatible")
                
            return WheelAnalysis(
                wheel_model=model,
                weight_grams=weight,
                max_tire_width_mm=max_width,
                is_aero_optimized=is_aero_optimized,
                compatibility_rating=compatibility_rating,
                notes=", ".join(notes) if notes else None
            )
            
        except Exception as e:
            raise ValueError(f"Error analyzing wheel: {str(e)}")

def load_wheel_data_from_json(file_path: str) -> Dict:
    """Load wheel data from JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Wheel data file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in wheel data file")

def generate_report(analysis: WheelAnalysis) -> str:
    """Generate a human-readable analysis report."""
    report = [
        f"Wheel Model: {analysis.wheel_model}",
        f"Weight: {analysis.weight_grams}g",
        f"Max Tire Width: {analysis.max_tire_width_mm}mm",
        f"Aero Optimized: {'Yes' if analysis.is_aero_optimized else 'No'}",
        f"Compatibility Rating: {analysis.compatibility_rating:.1%}",
        f"Notes: {analysis.notes if analysis.notes else 'None'}"
    ]
    return "\n".join(report)

# Example usage
if __name__ == "__main__":
    # Sample wheel data (could be loaded from JSON)
    hunt_wheel_data = {
        "model": "Hunt 34 Aero Wide",
        "weight_grams": 1380,
        "max_tire_width_mm": 30,
        "rim_depth_mm": 34,
        "rim_width_mm": 23
    }
    
    try:
        analyzer = WheelAnalyzer(hunt_wheel_data)
        analysis = analyzer.analyze_wheel()
        report = generate_report(analysis)
        print(report)
    except ValueError as e:
        print(f"Error: {e}")
```
