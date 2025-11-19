"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: Write code to simulate the production of EVA masterbatches with special effects, referencing Ray Colors' product descriptions.
Generated: DETERMINISTIC_9ac59d98b0584d6f
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List, Dict, Optional

class EffectType(Enum):
    """Enum representing different special effects for EVA masterbatches."""
    GLOW_IN_DARK = "Glow in the Dark"
    PEARLESCENT = "Pearlescent"
    METALLIC = "Metallic"
    FLUORESCENT = "Fluorescent"
    SPARKLE = "Sparkle"
    THERMOCHROMIC = "Thermochromic"
    PHOTOCHROMIC = "Photochromic"

class EvaMasterbatch:
    """Class representing an EVA masterbatch with special effects."""
    
    def __init__(
        self,
        name: str,
        base_color: str,
        effect_type: EffectType,
        concentration: float,
        batch_size: float
    ):
        """
        Initialize an EVA masterbatch.
        
        Args:
            name: Name of the masterbatch
            base_color: Base color of the masterbatch
            effect_type: Type of special effect
            concentration: Concentration of the effect (0-1)
            batch_size: Size of the batch in kg
        """
        self.name = name
        self.base_color = base_color
        self.effect_type = effect_type
        self.concentration = concentration
        self.batch_size = batch_size
        
    def __str__(self) -> str:
        """String representation of the masterbatch."""
        return (
            f"EVA Masterbatch: {self.name}\n"
            f"Base Color: {self.base_color}\n"
            f"Effect: {self.effect_type.value}\n"
            f"Concentration: {self.concentration * 100:.1f}%\n"
            f"Batch Size: {self.batch_size} kg"
        )
    
    def quality_check(self) -> bool:
        """Perform quality check on the masterbatch."""
        if not (0 < self.concentration <= 1):
            return False
        if self.batch_size <= 0:
            return False
        return True

class EvaMasterbatchFactory:
    """Factory class for producing EVA masterbatches with special effects."""
    
    def __init__(self):
        """Initialize the factory with default parameters."""
        self.available_colors = [
            "Red", "Blue", "Green", "Yellow", "Black", "White", 
            "Orange", "Purple", "Pink", "Brown"
        ]
        self.available_effects = list(EffectType)
        
    def produce_batch(
        self,
        name: str,
        base_color: Optional[str] = None,
        effect_type: Optional[EffectType] = None,
        concentration: Optional[float] = None,
        batch_size: float = 1000.0
    ) -> EvaMasterbatch:
        """
        Produce an EVA masterbatch with specified parameters.
        
        Args:
            name: Name of the masterbatch
            base_color: Base color (random if None)
            effect_type: Effect type (random if None)
            concentration: Effect concentration (random 0.1-0.5 if None)
            batch_size: Batch size in kg (default 1000)
            
        Returns:
            EvaMasterbatch: Produced masterbatch
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        # Validate inputs
        if batch_size <= 0:
            raise ValueError("Batch size must be positive")
        
        # Set default values if not provided
        if base_color is None:
            base_color = random.choice(self.available_colors)
        elif base_color not in self.available_colors:
            raise ValueError(f"Invalid color: {base_color}")
            
        if effect_type is None:
            effect_type = random.choice(self.available_effects)
        elif not isinstance(effect_type, EffectType):
            raise ValueError("Invalid effect type")
            
        if concentration is None:
            concentration = round(random.uniform(0.1, 0.5), 2)
        elif not (0 < concentration <= 1):
            raise ValueError("Concentration must be between 0 and 1")
            
        # Create and return the masterbatch
        batch = EvaMasterbatch(
            name=name,
            base_color=base_color,
            effect_type=effect_type,
            concentration=concentration,
            batch_size=batch_size
        )
        
        if not batch.quality_check():
            raise ValueError("Produced batch failed quality check")
            
        return batch
    
    def produce_random_batches(self, count: int = 5) -> List[EvaMasterbatch]:
        """
        Produce multiple random masterbatches.
        
        Args:
            count: Number of batches to produce
            
        Returns:
            List[EvaMasterbatch]: List of produced batches
        """
        batches = []
        for i in range(count):
            name = f"Batch-{i+1}"
            try:
                batch = self.produce_batch(name)
                batches.append(batch)
            except ValueError as e:
                print(f"Failed to produce {name}: {str(e)}")
        return batches

def display_batches(batches: List[EvaMasterbatch]) -> None:
    """Display information about produced batches."""
    print("\n=== Produced EVA Masterbatches ===")
    for batch in batches:
        print("\n" + str(batch))
        print("-" * 40)

def main():
    """Main function to demonstrate EVA masterbatch production."""
    factory = EvaMasterbatchFactory()
    
    # Produce some random batches
    random_batches = factory.produce_random_batches(3)
    display_batches(random_batches)
    
    # Produce a custom batch
    try:
        custom_batch = factory.produce_batch(
            name="Custom-Glow",
            base_color="Blue",
            effect_type=EffectType.GLOW_IN_DARK,
            concentration=0.3,
            batch_size=500.0
        )
        display_batches([custom_batch])
    except ValueError as e:
        print(f"Failed to produce custom batch: {str(e)}")

if __name__ == "__main__":
    main()
```
