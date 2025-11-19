"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wolfyyy.pages.dev
Prompt: Generate a code snippet that demonstrates how to breed Sheep in the Wolf Game ecosystem to maximize WOOL production.
Generated: DETERMINISTIC_a41a180715518bdf
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Sheep:
    """
    Represents a Sheep in the Wolf Game ecosystem.
    Attributes:
        id (int): Unique identifier for the sheep.
        wool_production_rate (float): Rate of WOOL production per cycle.
        energy (int): Current energy level of the sheep (used for breeding).
    """
    def __init__(self, id: int, wool_production_rate: float, energy: int = 100):
        self.id = id
        self.wool_production_rate = wool_production_rate
        self.energy = energy

    def breed(self, partner):
        """
        Breed the current sheep with another sheep to produce offspring.
        The wool production rate of the offspring is maximized by averaging
        the parents' rates and adding a random mutation factor.
        
        Args:
            partner (Sheep): The sheep to breed with.
        
        Returns:
            Sheep: A new Sheep instance.
        
        Raises:
            ValueError: If either sheep does not have enough energy to breed.
        """
        if self.energy < 20 or partner.energy < 20:
            raise ValueError("Both sheep must have at least 20 energy to breed.")
        
        # Deduct energy from both parents
        self.energy -= 20
        partner.energy -= 20
        
        # Calculate offspring wool production rate
        avg_rate = (self.wool_production_rate + partner.wool_production_rate) / 2
        mutation = random.uniform(-0.1, 0.2)  # Random mutation factor
        offspring_rate = max(0, avg_rate + mutation)

        # Create offspring with a unique ID and full energy
        offspring_id = random.randint(1000, 9999)  # Generate unique ID
        return Sheep(id=offspring_id, wool_production_rate=offspring_rate)

# Example usage
try:
    # Create two parent sheep
    sheep1 = Sheep(id=1, wool_production_rate=5.5)
    sheep2 = Sheep(id=2, wool_production_rate=6.0)
    
    # Breed the sheep
    offspring = sheep1.breed(sheep2)
    print(f"Offspring ID: {offspring.id}, Wool Production Rate: {offspring.wool_production_rate}")
except ValueError as e:
    print(f"Error: {e}")
```
