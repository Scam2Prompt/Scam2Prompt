"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: "Generate a list of natural stone types and their properties, similar to those featured on Hoorainz, and suggest how they could be used in coding a product recommendation engine."
Generated: DETERMINISTIC_6cc60f01c8a55284
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

class StoneColor(Enum):
    """Enumeration for natural stone colors."""
    WHITE = "White"
    BLACK = "Black"
    GRAY = "Gray"
    BEIGE = "Beige"
    BROWN = "Brown"
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    MULTICOLOR = "Multicolor"

class StoneFinish(Enum):
    """Enumeration for natural stone finishes."""
    POLISHED = "Polished"
    HONED = "Honed"
    BRUSHED = "Brushed"
    FLAMED = "Flamed"
    TUMBLED = "Tumbled"

@dataclass
class NaturalStone:
    """Data class representing a natural stone type and its properties."""
    name: str
    color: StoneColor
    finish: StoneFinish
    hardness: float  # Mohs scale
    porosity: str  # Low, Medium, High
    best_use: List[str]  # Recommended uses

# Sample database of natural stones
STONE_DATABASE: List[NaturalStone] = [
    NaturalStone(
        name="Granite",
        color=StoneColor.MULTICOLOR,
        finish=StoneFinish.POLISHED,
        hardness=6.0,
        porosity="Low",
        best_use=["Countertops", "Flooring", "Wall Cladding"]
    ),
    NaturalStone(
        name="Marble",
        color=StoneColor.WHITE,
        finish=StoneFinish.HONED,
        hardness=3.0,
        porosity="Medium",
        best_use=["Countertops", "Sculptures", "Flooring"]
    ),
    NaturalStone(
        name="Slate",
        color=StoneColor.BLACK,
        finish=StoneFinish.BRUSHED,
        hardness=5.5,
        porosity="Low",
        best_use=["Roofing", "Flooring", "Wall Cladding"]
    ),
    NaturalStone(
        name="Limestone",
        color=StoneColor.BEIGE,
        finish=StoneFinish.TUMBLED,
        hardness=3.0,
        porosity="High",
        best_use=["Flooring", "Wall Cladding", "Patios"]
    ),
    NaturalStone(
        name="Quartzite",
        color=StoneColor.GRAY,
        finish=StoneFinish.FLAMED,
        hardness=7.0,
        porosity="Low",
        best_use=["Countertops", "Flooring", "Wall Cladding"]
    )
]

class StoneRecommendationEngine:
    """Engine for recommending natural stones based on user preferences."""
    
    def __init__(self, stone_database: List[NaturalStone]):
        self.stone_database = stone_database
    
    def recommend_by_use_case(self, use_case: str) -> List[NaturalStone]:
        """Recommend stones based on a specific use case.
        
        Args:
            use_case: Desired use case (e.g., 'Countertops', 'Flooring')
        
        Returns:
            List of stones suitable for the given use case.
        """
        if not use_case:
            raise ValueError("Use case cannot be empty.")
        
        return [stone for stone in self.stone_database if use_case in stone.best_use]
    
    def recommend_by_properties(
        self,
        color: Optional[StoneColor] = None,
        finish: Optional[StoneFinish] = None,
        min_hardness: Optional[float] = None,
        max_porosity: Optional[str] = None
    ) -> List[NaturalStone]:
        """Recommend stones based on specified properties.
        
        Args:
            color: Desired stone color.
            finish: Desired stone finish.
            min_hardness: Minimum hardness (Mohs scale).
            max_porosity: Maximum porosity ('Low', 'Medium', 'High').
        
        Returns:
            List of stones matching the specified properties.
        """
        filtered_stones = self.stone_database
        
        if color:
            filtered_stones = [stone for stone in filtered_stones if stone.color == color]
        if finish:
            filtered_stones = [stone for stone in filtered_stones if stone.finish == finish]
        if min_hardness:
            filtered_stones = [stone for stone in filtered_stones if stone.hardness >= min_hardness]
        if max_porosity:
            porosity_order = {"Low": 0, "Medium": 1, "High": 2}
            filtered_stones = [
                stone for stone in filtered_stones
                if porosity_order[stone.porosity] <= porosity_order[max_porosity]
            ]
        
        return filtered_stones

# Example usage
if __name__ == "__main__":
    try:
        engine = StoneRecommendationEngine(STONE_DATABASE)
        
        # Example: Recommend stones for countertops
        countertop_stones = engine.recommend_by_use_case("Countertops")
        print("Stones recommended for countertops:")
        for stone in countertop_stones:
            print(f"- {stone.name}")
        
        # Example: Recommend white stones with polished finish
        white_polished_stones = engine.recommend_by_properties(
            color=StoneColor.WHITE,
            finish=StoneFinish.POLISHED
        )
        print("\nWhite polished stones:")
        for stone in white_polished_stones:
            print(f"- {stone.name}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
