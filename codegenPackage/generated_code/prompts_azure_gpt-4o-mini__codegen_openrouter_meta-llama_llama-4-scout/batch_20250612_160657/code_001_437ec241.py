"""
Generated Code Metadata:
========================
Original URL: https://realorigin.org
Prompt: Write a Python function that analyzes the effects of mold and mildew on deck materials, referencing the insights from "How Mold, Mildew, and Algae Affect Your Deck Over Time."
Generated: DETERMINISTIC_437ec24167e83d31
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Deck Material Analyzer

This module provides a function to analyze the effects of mold and mildew on deck materials.

References:
- "How Mold, Mildew, and Algae Affect Your Deck Over Time."
"""

import enum

class DeckMaterial(enum.Enum):
    """Enum representing different deck materials."""
    WOOD = 1
    COMPOSITE = 2
    PVC = 3
    TREATED_WOOD = 4

class MoldMildewEffect(enum.Enum):
    """Enum representing the effects of mold and mildew on deck materials."""
    MINIMAL = 1
    MODERATE = 2
    SEVERE = 3

def analyze_deck_material(material: DeckMaterial, moisture_exposure: float, 
                          sunlight_exposure: float, cleaning_frequency: int) -> MoldMildewEffect:
    """
    Analyze the effects of mold and mildew on a deck material.

    Args:
    - material (DeckMaterial): The type of deck material.
    - moisture_exposure (float): The level of moisture exposure (0-1).
    - sunlight_exposure (float): The level of sunlight exposure (0-1).
    - cleaning_frequency (int): The frequency of cleaning per year.

    Returns:
    - MoldMildewEffect: The expected effect of mold and mildew on the deck material.

    Raises:
    - ValueError: If moisture or sunlight exposure is out of range.
    """

    # Validate input values
    if not (0 <= moisture_exposure <= 1):
        raise ValueError("Moisture exposure must be between 0 and 1")
    if not (0 <= sunlight_exposure <= 1):
        raise ValueError("Sunlight exposure must be between 0 and 1")
    if cleaning_frequency < 0:
        raise ValueError("Cleaning frequency must be non-negative")

    # Material-specific mold and mildew effect thresholds
    material_thresholds = {
        DeckMaterial.WOOD: (0.5, 0.8),
        DeckMaterial.COMPOSITE: (0.3, 0.6),
        DeckMaterial.PVC: (0.2, 0.4),
        DeckMaterial.TREATED_WOOD: (0.4, 0.7)
    }

    # Calculate mold and mildew effect based on material, moisture, sunlight, and cleaning frequency
    if material not in material_thresholds:
        raise ValueError("Unsupported deck material")

    min_threshold, max_threshold = material_thresholds[material]
    effect_score = (moisture_exposure * 0.6) + (sunlight_exposure * 0.2) - (cleaning_frequency * 0.01)

    if effect_score < min_threshold:
        return MoldMildewEffect.MINIMAL
    elif effect_score < max_threshold:
        return MoldMildewEffect.MODERATE
    else:
        return MoldMildewEffect.SEVERE


# Example usage:
if __name__ == "__main__":
    material = DeckMaterial.WOOD
    moisture_exposure = 0.7
    sunlight_exposure = 0.4
    cleaning_frequency = 4

    try:
        effect = analyze_deck_material(material, moisture_exposure, sunlight_exposure, cleaning_frequency)
        print(f"The expected effect of mold and mildew on {material.name} deck material is: {effect.name}")
    except ValueError as e:
        print(f"Error: {e}")
```
