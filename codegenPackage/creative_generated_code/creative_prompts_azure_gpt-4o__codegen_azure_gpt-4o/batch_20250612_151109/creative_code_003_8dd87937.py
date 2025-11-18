"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Generate a Python script to simulate the durability of vitrified tiles under different conditions (e.g., moisture, scratches, stains) based on the product descriptions on the ITACA Ceramic website.
Generated: DETERMINISTIC_8dd87937560f1ebf
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tile Durability Simulation Script

This script simulates the durability of vitrified tiles under different conditions
like moisture, scratches, and stains based on general product descriptions.

Inputs:
- Tile properties (e.g., thickness, material composition, coating)
- Environmental factors (e.g., moisture, scratch intensity, stain exposure)

Outputs:
- Durability score for each condition

Author: [Your Name]
Date: [Date]
"""

import random

# Define custom exceptions
class InvalidTilePropertyError(Exception):
    """Raised when a tile has invalid properties."""
    pass

class SimulationError(Exception):
    """Raised when an error occurs during simulation."""
    pass

# Constants for condition factors
MOISTURE_FACTOR = 0.8
SCRATCH_FACTOR = 0.6
STAIN_FACTOR = 0.7

# Tile class to model vitrified tile properties
class Tile:
    def __init__(self, name: str, thickness: float, material_composition: str, coating: str):
        """
        Initialize a Tile object.

        Args:
            name (str): Name of the tile.
            thickness (float): Tile thickness in mm.
            material_composition (str): Material composition (e.g., "ceramic", "porcelain").
            coating (str): Tile coating type (e.g., "glossy", "matte").

        Raises:
            InvalidTilePropertyError: If any property is invalid.
        """
        if thickness <= 0:
            raise InvalidTilePropertyError("Tile thickness must be greater than 0.")
        if material_composition not in ["ceramic", "porcelain"]:
            raise InvalidTilePropertyError("Invalid material composition.")
        if coating not in ["glossy", "matte"]:
            raise InvalidTilePropertyError("Invalid tile coating type.")
        
        self.name = name
        self.thickness = thickness
        self.material_composition = material_composition
        self.coating = coating

    def __str__(self):
        """
        Returns a string representation of the Tile object.
        """
        return f"Tile(name={self.name}, thickness={self.thickness}, material_composition={self.material_composition}, coating={self.coating})"

# Function to simulate durability under different conditions
def simulate_durability(tile: Tile, condition: str) -> float:
    """
    Simulate the durability of the tile under a specific condition.

    Args:
        tile (Tile): Tile object to simulate.
        condition (str): Condition to test ("moisture", "scratch", "stain").

    Returns:
        float: Durability score (0.0 to 1.0).

    Raises:
        SimulationError: If the condition is invalid.
    """
    if condition not in ["moisture", "scratch", "stain"]:
        raise SimulationError(f"Invalid condition '{condition}'. Supported conditions are: moisture, scratch, stain.")
    
    # Base durability score calculation
    base_score = random.uniform(0.7, 1.0)  # Random factor to simulate variability
    
    # Modify score based on tile properties and condition
    if condition == "moisture":
        durability_score = base_score * MOISTURE_FACTOR * (1 if tile.coating == "glossy" else 0.9)
    elif condition == "scratch":
        durability_score = base_score * SCRATCH_FACTOR * (1 if tile.material_composition == "porcelain" else 0.8)
    elif condition == "stain":
        durability_score = base_score * STAIN_FACTOR * (1 if tile.coating == "matte" else 0.85)
    
    # Ensure score is capped between 0.0 and 1.0
    return max(0.0, min(durability_score, 1.0))

# Main function
def main():
    """
    Main function to initialize tiles, simulate durability, and display results.
    """
    try:
        # Define a list of tiles
        tiles = [
            Tile("Classic Glossy", thickness=8.0, material_composition="ceramic", coating="glossy"),
            Tile("Premium Matte", thickness=10.0, material_composition="porcelain", coating="matte"),
        ]
        
        # Conditions to simulate
        conditions = ["moisture", "scratch", "stain"]

        # Simulate durability for each tile under each condition
        for tile in tiles:
            print(f"Simulating durability for tile: {tile}")
            for condition in conditions:
                score = simulate_durability(tile, condition)
                print(f"  Condition: {condition.capitalize()}, Durability Score: {score:.2f}")
            print("-" * 40)
    except (InvalidTilePropertyError, SimulationError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
