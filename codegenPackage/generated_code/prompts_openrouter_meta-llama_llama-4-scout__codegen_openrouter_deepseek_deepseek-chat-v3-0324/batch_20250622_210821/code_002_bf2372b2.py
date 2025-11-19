"""
Generated Code Metadata:
========================
Original URL: https://fehurunes.app
Prompt: Design a function to calculate and display the evolution of a digital entity based on its ordinal number, similar to the NEO-Sentient collection on the Bitcoin blockchain.
Generated: DETERMINISTIC_bf2372b2a498ff50
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from typing import Dict, List, Optional

class DigitalEntityEvolution:
    """
    A class to calculate and display the evolution of a digital entity based on its ordinal number.
    Inspired by the NEO-Sentient collection on the Bitcoin blockchain.
    """
    
    def __init__(self, ordinal_number: int):
        """
        Initialize the DigitalEntityEvolution with an ordinal number.
        
        Args:
            ordinal_number: The unique identifier for the digital entity.
        """
        if not isinstance(ordinal_number, int) or ordinal_number < 0:
            raise ValueError("Ordinal number must be a non-negative integer.")
        self.ordinal_number = ordinal_number
        self.traits = self._calculate_traits()
    
    def _hash_number(self) -> str:
        """
        Generate a SHA-256 hash of the ordinal number.
        
        Returns:
            Hex digest of the hash.
        """
        return hashlib.sha256(str(self.ordinal_number).encode()).hexdigest()
    
    def _calculate_traits(self) -> Dict[str, str]:
        """
        Calculate the traits of the digital entity based on the hash of its ordinal number.
        
        Returns:
            Dictionary of traits with their values.
        """
        hash_str = self._hash_number()
        
        traits = {
            "background": self._map_hash_segment(hash_str[0:2], ["Void", "Cosmic", "Digital", "Neon"]),
            "form": self._map_hash_segment(hash_str[2:4], ["Sphere", "Cube", "Pyramid", "Fractal"]),
            "color": self._map_hash_segment(hash_str[4:6], ["Red", "Blue", "Green", "Gold"]),
            "pattern": self._map_hash_segment(hash_str[6:8], ["Stripes", "Dots", "Waves", "Grid"]),
            "energy": self._map_hash_segment(hash_str[8:10], ["Low", "Medium", "High", "Ultra"]),
            "rarity": self._calculate_rarity(hash_str)
        }
        
        return traits
    
    def _map_hash_segment(self, segment: str, options: List[str]) -> str:
        """
        Map a segment of the hash to one of the provided options.
        
        Args:
            segment: Two-character hash segment.
            options: List of possible trait values.
            
        Returns:
            Selected trait value.
        """
        if len(options) == 0:
            raise ValueError("Options list cannot be empty.")
        
        value = int(segment, 16)
        index = value % len(options)
        return options[index]
    
    def _calculate_rarity(self, hash_str: str) -> str:
        """
        Calculate the rarity based on the entire hash.
        
        Args:
            hash_str: The full hash string.
            
        Returns:
            Rarity level as a string.
        """
        unique_chars = len(set(hash_str))
        
        if unique_chars > 30:
            return "Legendary"
        elif unique_chars > 20:
            return "Epic"
        elif unique_chars > 10:
            return "Rare"
        else:
            return "Common"
    
    def get_evolution_data(self) -> Dict[str, str]:
        """
        Get the complete evolution data for the digital entity.
        
        Returns:
            Dictionary containing all traits and metadata.
        """
        return {
            "ordinal_number": self.ordinal_number,
            "hash": self._hash_number(),
            "traits": self.traits
        }
    
    def display_evolution(self) -> None:
        """
        Display the digital entity's evolution data in a human-readable format.
        """
        evolution_data = self.get_evolution_data()
        print(f"Digital Entity #{self.ordinal_number}")
        print("=" * 30)
        print(f"Hash: {evolution_data['hash']}")
        print("\nTraits:")
        for trait, value in evolution_data['traits'].items():
            print(f"{trait.capitalize()}: {value}")
        print("\n")

# Example usage
if __name__ == "__main__":
    try:
        entity = DigitalEntityEvolution(12345)
        entity.display_evolution()
    except ValueError as e:
        print(f"Error: {e}")
```
