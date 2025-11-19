"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Develop a code to calculate the best fishing reel and line combination for a specific type of fishing, such as fly fishing for Trout or Salmon, using data from Emanuelson Reels."
Generated: DETERMINISTIC_f1c219b551c2d5df
Batch ID: 20250622_210655
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
class FishingReel:
    """Class representing a fishing reel."""
    name: str
    type: str
    weight_range: tuple  # (min_weight, max_weight) in ounces
    line_capacity: tuple  # (min_line_weight, max_line_weight) in lbs
    price: float
    brand: str = "Emanuelson"

@dataclass
class FishingLine:
    """Class representing a fishing line."""
    name: str
    type: str
    weight: float  # in lbs
    material: str
    price_per_foot: float

@dataclass
class FishingScenario:
    """Class representing a fishing scenario."""
    fish_type: str
    fishing_type: str
    average_fish_weight: float  # in lbs
    water_type: str  # e.g., freshwater, saltwater

class FishingGearCalculator:
    """Calculates the best reel and line combination for a fishing scenario."""
    
    def __init__(self, reels: List[FishingReel], lines: List[FishingLine]):
        self.reels = reels
        self.lines = lines
    
    def _filter_reels_by_type(self, fishing_type: str) -> List[FishingReel]:
        """Filter reels by fishing type."""
        return [reel for reel in self.reels if reel.type.lower() == fishing_type.lower()]
    
    def _filter_lines_by_type(self, fishing_type: str) -> List[FishingLine]:
        """Filter lines by fishing type."""
        return [line for line in self.lines if line.type.lower() == fishing_type.lower()]
    
    def _get_compatible_lines(self, reel: FishingReel, lines: List[FishingLine]) -> List[FishingLine]:
        """Get lines compatible with the reel's weight range."""
        min_line, max_line = reel.line_capacity
        return [line for line in lines if min_line <= line.weight <= max_line]
    
    def calculate_best_combination(self, scenario: FishingScenario) -> Dict[str, Optional[object]]:
        """
        Calculate the best reel and line combination for the given scenario.
        
        Returns:
            Dict with 'reel', 'line', and 'score' (higher is better).
        """
        try:
            filtered_reels = self._filter_reels_by_type(scenario.fishing_type)
            filtered_lines = self._filter_lines_by_type(scenario.fishing_type)
            
            if not filtered_reels or not filtered_lines:
                return {'reel': None, 'line': None, 'score': -1}
            
            best_combination = {'reel': None, 'line': None, 'score': -1}
            
            for reel in filtered_reels:
                compatible_lines = self._get_compatible_lines(reel, filtered_lines)
                
                for line in compatible_lines:
                    # Simple scoring: prioritize lines that match fish weight
                    score = 1 / (abs(line.weight - scenario.average_fish_weight) + 0.1)
                    
                    if score > best_combination['score']:
                        best_combination['reel'] = reel
                        best_combination['line'] = line
                        best_combination['score'] = score
            
            return best_combination
        
        except Exception as e:
            print(f"Error calculating fishing gear: {e}")
            return {'reel': None, 'line': None, 'score': -1}

def load_reels_from_json(file_path: str) -> List[FishingReel]:
    """Load reels from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [FishingReel(**reel) for reel in data]
    except Exception as e:
        print(f"Error loading reels: {e}")
        return []

def load_lines_from_json(file_path: str) -> List[FishingLine]:
    """Load lines from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [FishingLine(**line) for line in data]
    except Exception as e:
        print(f"Error loading lines: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Load data (in a real scenario, these would be from files/database)
    reels = [
        FishingReel("TroutMaster", "fly", (0.1, 0.3), (2, 6), 89.99),
        FishingReel("SalmonPro", "fly", (0.2, 0.5), (4, 10), 129.99),
        FishingReel("RiverKing", "fly", (0.1, 0.4), (3, 8), 109.99)
    ]
    
    lines = [
        FishingLine("FluoroFlex", "fly", 4, "fluorocarbon", 0.15),
        FishingLine("MonoMaster", "fly", 6, "monofilament", 0.10),
        FishingLine("SuperBraid", "fly", 8, "braided", 0.20)
    ]
    
    calculator = FishingGearCalculator(reels, lines)
    
    scenario = FishingScenario(
        fish_type="Trout",
        fishing_type="fly",
        average_fish_weight=5.0,
        water_type="freshwater"
    )
    
    result = calculator.calculate_best_combination(scenario)
    print(f"Best reel: {result['reel'].name if result['reel'] else 'None'}")
    print(f"Best line: {result['line'].name if result['line'] else 'None'}")
```
