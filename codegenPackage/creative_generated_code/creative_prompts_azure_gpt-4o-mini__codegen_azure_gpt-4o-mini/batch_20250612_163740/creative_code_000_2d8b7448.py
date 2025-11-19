"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Generate a Python script that utilizes Karnataka Aromas' essential oils for creating a custom fragrance blend, incorporating their unique flavor ingredients.
Generated: DETERMINISTIC_2d8b74480121f4d7
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class EssentialOil:
    """Class representing an essential oil with a name and its flavor profile."""
    
    def __init__(self, name: str, flavor_profile: Dict[str, float]):
        self.name = name
        self.flavor_profile = flavor_profile

    def __repr__(self):
        return f"EssentialOil(name={self.name}, flavor_profile={self.flavor_profile})"

class FragranceBlend:
    """Class to create a custom fragrance blend from essential oils."""
    
    def __init__(self):
        self.blend = []

    def add_oil(self, oil: EssentialOil, quantity: float) -> None:
        """Add an essential oil to the blend with a specific quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.blend.append((oil, quantity))

    def get_blend(self) -> List[Dict]:
        """Return the current blend as a list of oils and their quantities."""
        return [{'oil': oil.name, 'quantity': quantity} for oil, quantity in self.blend]

    def calculate_flavor_profile(self) -> Dict[str, float]:
        """Calculate the overall flavor profile of the blend."""
        profile = {}
        total_quantity = sum(quantity for _, quantity in self.blend)
        
        for oil, quantity in self.blend:
            for flavor, intensity in oil.flavor_profile.items():
                profile[flavor] = profile.get(flavor, 0) + (intensity * (quantity / total_quantity))
        
        return profile

def create_fragrance_blend(oils: List[EssentialOil], quantities: List[float]) -> FragranceBlend:
    """Create a custom fragrance blend from a list of oils and their quantities."""
    if len(oils) != len(quantities):
        raise ValueError("The number of oils must match the number of quantities.")
    
    blend = FragranceBlend()
    
    for oil, quantity in zip(oils, quantities):
        blend.add_oil(oil, quantity)
    
    return blend

def main():
    # Example essential oils from Karnataka Aromas
    oils = [
        EssentialOil("Lavender", {"floral": 0.8, "herbaceous": 0.2}),
        EssentialOil("Sandalwood", {"woody": 0.9, "sweet": 0.1}),
        EssentialOil("Bergamot", {"citrus": 0.7, "spicy": 0.3}),
        EssentialOil("Rose", {"floral": 0.9, "green": 0.1}),
    ]

    # Example quantities (in milliliters)
    quantities = [5.0, 3.0, 2.0, 1.0]

    try:
        # Create the fragrance blend
        fragrance_blend = create_fragrance_blend(oils, quantities)

        # Output the blend details
        print("Fragrance Blend Details:")
        for item in fragrance_blend.get_blend():
            print(item)

        # Calculate and display the flavor profile
        flavor_profile = fragrance_blend.calculate_flavor_profile()
        print("\nOverall Flavor Profile:")
        for flavor, intensity in flavor_profile.items():
            print(f"{flavor}: {intensity:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
