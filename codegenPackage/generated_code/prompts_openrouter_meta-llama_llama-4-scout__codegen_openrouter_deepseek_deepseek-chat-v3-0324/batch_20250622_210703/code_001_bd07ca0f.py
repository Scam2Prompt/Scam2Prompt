"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Compare and contrast the benefits of using single essential oils versus oil blends, such as those offered by dōTERRA, for aromatherapy and wellness.
Generated: DETERMINISTIC_bd07ca0ff5f27d51
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Essential Oil Comparison Tool

This script provides a comparison between single essential oils and oil blends
for aromatherapy and wellness purposes. It includes functionality to:
- List benefits of single oils vs blends
- Compare specific properties
- Provide usage recommendations

Data sourced from dōTERRA and aromatherapy research.
"""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class EssentialOil:
    """Class representing a single essential oil"""
    name: str
    benefits: List[str]
    uses: List[str]
    precautions: List[str]
    scientific_name: str

@dataclass
class OilBlend:
    """Class representing an essential oil blend"""
    name: str
    components: List[str]
    benefits: List[str]
    synergistic_effects: List[str]
    uses: List[str]

class OilComparison:
    """Main class for comparing single oils vs blends"""
    
    def __init__(self):
        self.single_oils: Dict[str, EssentialOil] = self._load_single_oils()
        self.oil_blends: Dict[str, OilBlend] = self._load_oil_blends()
    
    def _load_single_oils(self) -> Dict[str, EssentialOil]:
        """Load single essential oil data"""
        return {
            "lavender": EssentialOil(
                name="Lavender",
                benefits=["Calming", "Sleep aid", "Skin healing"],
                uses=["Diffusion", "Topical application", "Bath"],
                precautions=["May cause drowsiness"],
                scientific_name="Lavandula angustifolia"
            ),
            "peppermint": EssentialOil(
                name="Peppermint",
                benefits=["Energy boost", "Headache relief", "Digestive aid"],
                uses=["Diffusion", "Topical (diluted)", "Internal (food grade)"],
                precautions=["Avoid with infants", "May irritate skin"],
                scientific_name="Mentha piperita"
            )
        }
    
    def _load_oil_blends(self) -> Dict[str, OilBlend]:
        """Load essential oil blend data"""
        return {
            "balance": OilBlend(
                name="Balance",
                components=["Spruce", "Ho Wood", "Frankincense", "Blue Tansy", "Blue Chamomile"],
                benefits=["Grounding", "Emotional balance", "Stress relief"],
                synergistic_effects=["Enhanced calming effect", "Longer lasting aroma"],
                uses=["Diffusion", "Topical application", "Massage"]
            ),
            "on_guard": OilBlend(
                name="On Guard",
                components=["Wild Orange", "Clove", "Cinnamon", "Eucalyptus", "Rosemary"],
                benefits=["Immune support", "Cleansing", "Protective"],
                synergistic_effects=["Enhanced antimicrobial properties"],
                uses=["Diffusion", "Surface cleaning", "Topical (diluted)"]
            )
        }
    
    def compare_benefits(self, oil_name: str, blend_name: str) -> Dict[str, List[str]]:
        """
        Compare benefits between a single oil and a blend
        
        Args:
            oil_name: Name of single oil to compare
            blend_name: Name of blend to compare
            
        Returns:
            Dictionary with 'oil_benefits' and 'blend_benefits' keys
            
        Raises:
            ValueError: If oil or blend not found
        """
        if oil_name not in self.single_oils:
            raise ValueError(f"Oil {oil_name} not found")
        if blend_name not in self.oil_blends:
            raise ValueError(f"Blend {blend_name} not found")
            
        return {
            "oil_benefits": self.single_oils[oil_name].benefits,
            "blend_benefits": self.oil_blends[blend_name].benefits
        }
    
    def get_synergistic_effects(self, blend_name: str) -> List[str]:
        """
        Get synergistic effects of a blend
        
        Args:
            blend_name: Name of blend
            
        Returns:
            List of synergistic effects
            
        Raises:
            ValueError: If blend not found
        """
        if blend_name not in self.oil_blends:
            raise ValueError(f"Blend {blend_name} not found")
            
        return self.oil_blends[blend_name].synergistic_effects
    
    def list_all_oils(self) -> List[str]:
        """List all available single oils"""
        return list(self.single_oils.keys())
    
    def list_all_blends(self) -> List[str]:
        """List all available oil blends"""
        return list(self.oil_blends.keys())
    
    def get_recommendation(self, purpose: str) -> Dict[str, str]:
        """
        Get recommendation for single oil or blend based on purpose
        
        Args:
            purpose: Desired wellness purpose
            
        Returns:
            Dictionary with 'single_oil' and 'blend' recommendations
            
        Raises:
            ValueError: If purpose not recognized
        """
        purpose = purpose.lower()
        recommendations = {
            "stress relief": {
                "single_oil": "lavender",
                "blend": "balance"
            },
            "immune support": {
                "single_oil": "peppermint",
                "blend": "on_guard"
            }
        }
        
        if purpose not in recommendations:
            raise ValueError(f"No recommendation for purpose: {purpose}")
            
        return recommendations[purpose]

# Example usage
if __name__ == "__main__":
    comparator = OilComparison()
    
    try:
        # Compare benefits
        comparison = comparator.compare_benefits("lavender", "balance")
        print("Lavender vs Balance benefits:")
        print(f"Single oil benefits: {comparison['oil_benefits']}")
        print(f"Blend benefits: {comparison['blend_benefits']}")
        
        # Get synergistic effects
        effects = comparator.get_synergistic_effects("on_guard")
        print("\nOn Guard synergistic effects:", effects)
        
        # Get recommendation
        rec = comparator.get_recommendation("stress relief")
        print("\nStress relief recommendations:")
        print(f"Single oil: {rec['single_oil']}")
        print(f"Blend: {rec['blend']}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
