"""
Generated Code Metadata:
========================
Original URL: https://agoda.host
Prompt: "Design a self-care gift basket for anxiety relief using sterling silver fidget rings and aromatherapy oils."
Generated: DETERMINISTIC_d6d4a6acb8e186c1
Batch ID: 20250622_212043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Self-Care Gift Basket Generator for Anxiety Relief
This script generates a personalized self-care gift basket recommendation
with sterling silver fidget rings and aromatherapy oils.
"""

from typing import List, Dict
import random

class GiftBasketGenerator:
    """
    A class to generate personalized self-care gift baskets for anxiety relief.
    """
    
    def __init__(self):
        self.fidget_rings = [
            "Sterling Silver Spinner Ring",
            "Sterling Silver Twister Ring",
            "Sterling Silver Puzzle Ring",
            "Sterling Silver Beaded Ring",
            "Sterling Silver Gear Ring"
        ]
        
        self.aromatherapy_oils = {
            "Lavender": "Calming and stress-relieving",
            "Bergamot": "Uplifting and anxiety-reducing",
            "Chamomile": "Soothing and relaxing",
            "Frankincense": "Grounding and meditative",
            "Ylang Ylang": "Balancing and tension-relieving"
        }
        
        self.additional_items = [
            "Soft velvet pouch",
            "Handwritten self-care guide",
            "Organic cotton eye mask",
            "Herbal tea sampler",
            "Journal with pen"
        ]
    
    def generate_basket(self, name: str) -> Dict[str, List[str]]:
        """
        Generates a personalized gift basket recommendation.
        
        Args:
            name (str): Recipient's name
            
        Returns:
            Dict[str, List[str]]: Dictionary containing basket items
        """
        try:
            if not name or not isinstance(name, str):
                raise ValueError("Name must be a non-empty string")
                
            basket = {
                "recipient": name,
                "fidget_ring": random.choice(self.fidget_rings),
                "essential_oils": self._select_oils(),
                "additional_items": self._select_additional_items()
            }
            
            return basket
            
        except Exception as e:
            print(f"Error generating basket: {str(e)}")
            return {}
    
    def _select_oils(self) -> List[Dict[str, str]]:
        """Selects 3 random aromatherapy oils with descriptions"""
        oils = list(self.aromatherapy_oils.items())
        selected = random.sample(oils, min(3, len(oils)))
        return [{"name": oil[0], "benefit": oil[1]} for oil in selected]
    
    def _select_additional_items(self) -> List[str]:
        """Selects 2 random additional items"""
        return random.sample(self.additional_items, min(2, len(self.additional_items)))
    
    def print_basket(self, basket: Dict[str, List[str]]) -> None:
        """Prints the gift basket contents in a user-friendly format"""
        try:
            if not basket:
                print("No basket items to display")
                return
                
            print(f"\nSelf-Care Gift Basket for {basket['recipient']}")
            print("=" * 40)
            print(f"Fidget Ring: {basket['fidget_ring']}")
            print("\nAromatherapy Oils:")
            for oil in basket['essential_oils']:
                print(f"- {oil['name']}: {oil['benefit']}")
            print("\nAdditional Items:")
            for item in basket['additional_items']:
                print(f"- {item}")
            print("=" * 40)
            
        except KeyError as e:
            print(f"Invalid basket format: missing {str(e)}")
        except Exception as e:
            print(f"Error displaying basket: {str(e)}")


# Example usage
if __name__ == "__main__":
    generator = GiftBasketGenerator()
    basket = generator.generate_basket("Alex")
    generator.print_basket(basket)
```
