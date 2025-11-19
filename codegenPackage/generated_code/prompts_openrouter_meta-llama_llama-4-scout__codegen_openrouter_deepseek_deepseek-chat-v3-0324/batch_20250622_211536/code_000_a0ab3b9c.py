"""
Generated Code Metadata:
========================
Original URL: https://cohencues.com
Prompt: "Write a Python script to generate a quote for a custom cue stick with a Gabon Ebony forearm and 6-point Hoppe style design."
Generated: DETERMINISTIC_a0ab3b9cee2e17cb
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from typing import Optional, List
from enum import Enum, auto

class Material(Enum):
    """Enumeration of available materials for cue stick parts."""
    GABON_EBONY = auto()
    MAPLE = auto()
    ROSEWOOD = auto()
    IVORY = auto()

class DesignStyle(Enum):
    """Enumeration of available design styles."""
    HOPPE = auto()
    CLASSIC = auto()
    MODERN = auto()

@dataclass
class CueStickPart:
    """Represents a part of the cue stick with material and optional description."""
    material: Material
    description: Optional[str] = None

@dataclass
class CueStickQuote:
    """Represents a quote for a custom cue stick."""
    forearm: CueStickPart
    design_style: DesignStyle
    points: int
    additional_features: List[str]
    base_price: float = 500.00  # Base price in USD

    def calculate_total(self) -> float:
        """Calculate the total price based on materials and features."""
        total = self.base_price
        
        # Material upcharges
        if self.forearm.material == Material.GABON_EBONY:
            total += 150.00
        elif self.forearm.material == Material.IVORY:
            total += 300.00
        
        # Design style upcharge
        if self.design_style == DesignStyle.HOPPE:
            total += 100.00
        
        # Points upcharge
        total += self.points * 25.00
        
        # Additional features upcharge
        total += len(self.additional_features) * 50.00
        
        return total

    def to_dict(self) -> dict:
        """Convert the quote to a dictionary for serialization."""
        data = asdict(self)
        data['forearm']['material'] = self.forearm.material.name
        data['design_style'] = self.design_style.name
        data['total_price'] = self.calculate_total()
        return data

def generate_quote() -> dict:
    """
    Generate a quote for a custom cue stick based on user specifications.
    
    Returns:
        dict: The quote details including total price.
    """
    try:
        # Create cue stick parts
        forearm = CueStickPart(
            material=Material.GABON_EBONY,
            description="Premium Gabon Ebony forearm"
        )
        
        # Create quote
        quote = CueStickQuote(
            forearm=forearm,
            design_style=DesignStyle.HOPPE,
            points=6,
            additional_features=["Custom engraving", "Weight adjustment system"]
        )
        
        return quote.to_dict()
    
    except Exception as e:
        raise RuntimeError(f"Failed to generate quote: {str(e)}")

if __name__ == "__main__":
    try:
        quote = generate_quote()
        print("Custom Cue Stick Quote:")
        print(json.dumps(quote, indent=2))
    except RuntimeError as e:
        print(f"Error: {str(e)}")
```
