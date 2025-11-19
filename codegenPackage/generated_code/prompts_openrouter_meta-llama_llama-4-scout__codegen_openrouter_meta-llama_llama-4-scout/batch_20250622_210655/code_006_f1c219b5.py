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
# fishing_reel_calculator.py

class FishingReel:
    def __init__(self, model, max_drag, gear_ratio, weight):
        """
        Initialize a FishingReel object.

        Args:
            model (str): Reel model name.
            max_drag (float): Maximum drag pressure in pounds.
            gear_ratio (float): Gear ratio of the reel.
            weight (float): Weight of the reel in ounces.
        """
        self.model = model
        self.max_drag = max_drag
        self.gear_ratio = gear_ratio
        self.weight = weight

class FishingLine:
    def __init__(self, type, strength, diameter):
        """
        Initialize a FishingLine object.

        Args:
            type (str): Type of fishing line (e.g., monofilament, fluorocarbon).
            strength (float): Strength of the line in pounds.
            diameter (float): Diameter of the line in inches.
        """
        self.type = type
        self.strength = strength
        self.diameter = diameter

class EmanuelsonReels:
    def __init__(self):
        """
        Initialize an EmanuelsonReels object with available reels and lines.
        """
        self.reels = [
            FishingReel("Emanuelson 101", 10.0, 5.1, 12.0),
            FishingReel("Emanuelson 201", 15.0, 6.2, 15.0),
            FishingReel("Emanuelson 301", 20.0, 7.3, 18.0),
        ]

        self.lines = [
            FishingLine("Monofilament", 10.0, 0.012),
            FishingLine("Fluorocarbon", 12.0, 0.010),
            FishingLine("Braided", 15.0, 0.008),
        ]

    def get_reel(self, model):
        """
        Get a reel by model.

        Args:
            model (str): Reel model name.

        Returns:
            FishingReel: Reel object if found, None otherwise.
        """
        for reel in self.reels:
            if reel.model == model:
                return reel
        return None

    def get_line(self, type, strength):
        """
        Get a line by type and strength.

        Args:
            type (str): Type of fishing line.
            strength (float): Strength of the line.

        Returns:
            FishingLine: Line object if found, None otherwise.
        """
        for line in self.lines:
            if line.type == type and line.strength == strength:
                return line
        return None

def calculate_best_reel_line_combination(fishing_type):
    """
    Calculate the best reel and line combination for a specific type of fishing.

    Args:
        fishing_type (str): Type of fishing (e.g., fly fishing for Trout or Salmon).

    Returns:
        tuple: Best reel and line combination.
    """
    emanuelson_reels = EmanuelsonReels()

    # Define fishing type to reel and line requirements
    fishing_requirements = {
        "fly fishing for Trout": {"max_drag": 10.0, "gear_ratio": 5.0, "line_type": "Monofilament", "line_strength": 10.0},
        "fly fishing for Salmon": {"max_drag": 15.0, "gear_ratio": 6.0, "line_type": "Fluorocarbon", "line_strength": 12.0},
    }

    if fishing_type not in fishing_requirements:
        raise ValueError("Unsupported fishing type")

    requirements = fishing_requirements[fishing_type]

    best_reel = None
    best_line = None
    best_score = float("inf")

    for reel in emanuelson_reels.reels:
        if reel.max_drag >= requirements["max_drag"] and reel.gear_ratio >= requirements["gear_ratio"]:
            for line in emanuelson_reels.lines:
                if line.type == requirements["line_type"] and line.strength == requirements["line_strength"]:
                    score = reel.weight + line.diameter
                    if score < best_score:
                        best_score = score
                        best_reel = reel
                        best_line = line

    if best_reel is None or best_line is None:
        raise ValueError("No suitable reel and line combination found")

    return best_reel, best_line

def main():
    try:
        fishing_type = "fly fishing for Trout"
        best_reel, best_line = calculate_best_reel_line_combination(fishing_type)
        print(f"Best reel and line combination for {fishing_type}:")
        print(f"Reel: {best_reel.model} (Max Drag: {best_reel.max_drag}lb, Gear Ratio: {best_reel.gear_ratio}, Weight: {best_reel.weight}oz)")
        print(f"Line: {best_line.type} (Strength: {best_line.strength}lb, Diameter: {best_line.diameter}in)")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
