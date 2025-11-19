"""
Generated Code Metadata:
========================
Original URL: https://testtt-ba0.pages.dev
Prompt: Write code to simulate economic dominance in Wolf Game by calculating WOOL production rates based on Sheep breeding and Farmer boosts.
Generated: DETERMINISTIC_bb5a5e5fd8fe66ea
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

class Sheep:
    """Represents a Sheep in Wolf Game with breeding and WOOL production capabilities."""
    
    def __init__(self, id: int, wool_rate: float = 1.0, breed_count: int = 0, max_breed_count: int = 7):
        """
        Initialize a Sheep.
        
        Args:
            id: Unique identifier for the Sheep.
            wool_rate: Base WOOL production rate per day (default: 1.0).
            breed_count: Number of times the Sheep has bred (default: 0).
            max_breed_count: Maximum allowed breed count (default: 7).
        """
        self.id = id
        self.wool_rate = wool_rate
        self.breed_count = breed_count
        self.max_breed_count = max_breed_count
    
    def can_breed(self) -> bool:
        """Check if the Sheep can breed."""
        return self.breed_count < self.max_breed_count
    
    def breed(self) -> bool:
        """
        Attempt to breed the Sheep.
        
        Returns:
            bool: True if breeding was successful, False otherwise.
        """
        if not self.can_breed():
            return False
        self.breed_count += 1
        return True
    
    def calculate_wool_production(self, days: int = 1) -> float:
        """
        Calculate WOOL production over a given number of days.
        
        Args:
            days: Number of days to calculate production for (default: 1).
            
        Returns:
            float: Total WOOL produced over the period.
        """
        return self.wool_rate * days


class Farmer:
    """Represents a Farmer in Wolf Game that can boost Sheep WOOL production."""
    
    def __init__(self, id: int, boost_rate: float = 1.1):
        """
        Initialize a Farmer.
        
        Args:
            id: Unique identifier for the Farmer.
            boost_rate: Multiplier applied to Sheep WOOL production (default: 1.1).
        """
        self.id = id
        self.boost_rate = boost_rate
    
    def apply_boost(self, sheep: Sheep) -> Sheep:
        """
        Apply boost to a Sheep's WOOL production rate.
        
        Args:
            sheep: Sheep to boost.
            
        Returns:
            Sheep: The boosted Sheep.
        """
        sheep.wool_rate *= self.boost_rate
        return sheep


class WolfGameEconomy:
    """Simulates economic dominance in Wolf Game through WOOL production."""
    
    def __init__(self):
        """Initialize the Wolf Game economy with empty collections."""
        self.sheep: Dict[int, Sheep] = {}
        self.farmers: Dict[int, Farmer] = {}
    
    def add_sheep(self, sheep: Sheep) -> None:
        """Add a Sheep to the economy."""
        if sheep.id in self.sheep:
            raise ValueError(f"Sheep with ID {sheep.id} already exists.")
        self.sheep[sheep.id] = sheep
    
    def add_farmer(self, farmer: Farmer) -> None:
        """Add a Farmer to the economy."""
        if farmer.id in self.farmers:
            raise ValueError(f"Farmer with ID {farmer.id} already exists.")
        self.farmers[farmer.id] = farmer
    
    def breed_sheep(self, sheep_id: int) -> bool:
        """
        Attempt to breed a Sheep.
        
        Args:
            sheep_id: ID of the Sheep to breed.
            
        Returns:
            bool: True if breeding was successful, False otherwise.
            
        Raises:
            ValueError: If Sheep does not exist.
        """
        if sheep_id not in self.sheep:
            raise ValueError(f"Sheep with ID {sheep_id} does not exist.")
        return self.sheep[sheep_id].breed()
    
    def calculate_total_wool_production(self, days: int = 1, boosted: bool = False) -> float:
        """
        Calculate total WOOL production across all Sheep.
        
        Args:
            days: Number of days to calculate production for (default: 1).
            boosted: Whether to apply Farmer boosts (default: False).
            
        Returns:
            float: Total WOOL produced by all Sheep.
        """
        total_wool = 0.0
        for sheep in self.sheep.values():
            current_sheep = sheep
            if boosted and self.farmers:
                # Apply average boost if multiple farmers exist
                avg_boost = sum(f.boost_rate for f in self.farmers.values()) / len(self.farmers)
                current_sheep = sheep
                current_sheep.wool_rate = sheep.wool_rate * avg_boost
            total_wool += current_sheep.calculate_wool_production(days)
        return total_wool
    
    def get_economic_dominance(self, days: int = 30, boosted: bool = True) -> float:
        """
        Calculate economic dominance score based on WOOL production.
        
        Args:
            days: Time period to consider (default: 30).
            boosted: Whether to include Farmer boosts (default: True).
            
        Returns:
            float: Economic dominance score (total WOOL produced).
        """
        return self.calculate_total_wool_production(days, boosted)


# Example usage
if __name__ == "__main__":
    economy = WolfGameEconomy()
    
    # Add some Sheep
    for i in range(1, 6):
        economy.add_sheep(Sheep(id=i, wool_rate=1.0))
    
    # Add some Farmers
    for i in range(1, 3):
        economy.add_farmer(Farmer(id=i, boost_rate=1.1))
    
    # Breed some Sheep
    for sheep_id in [1, 2, 3]:
        economy.breed_sheep(sheep_id)
    
    # Calculate economic dominance
    dominance_score = economy.get_economic_dominance()
    print(f"Economic Dominance Score: {dominance_score:.2f} WOOL over 30 days")
```
