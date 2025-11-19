"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Develop a function to simulate rider performance improvement based on the use of Nimbl ‘Ultimate’ cycling shoes, referencing their history of victories in Grand Tours as described on the Race Ride Fire website.
Generated: DETERMINISTIC_82bab5c0bcc5ab3f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional

class Rider:
    """
    Represents a cyclist with performance attributes.
    """
    def __init__(self, name: str, base_performance: float, victories: int):
        """
        Initialize a Rider instance.
        
        Args:
            name: Name of the rider.
            base_performance: Base performance level (0-100).
            victories: Number of Grand Tour victories.
        """
        self.name = name
        self.base_performance = base_performance
        self.victories = victories
        self.has_nimbl_shoes = False

    def __str__(self) -> str:
        return f"{self.name} (Performance: {self.base_performance}, Victories: {self.victories})"

def simulate_performance_improvement(rider: Rider, use_nimbl_shoes: bool) -> float:
    """
    Simulates the performance improvement of a rider when using Nimbl 'Ultimate' shoes.
    
    Args:
        rider: The rider to simulate.
        use_nimbl_shoes: Whether the rider is using Nimbl shoes.
    
    Returns:
        The improved performance level (0-100).
    
    Raises:
        ValueError: If rider's base performance is not within 0-100.
    """
    if not 0 <= rider.base_performance <= 100:
        raise ValueError("Base performance must be between 0 and 100.")
    
    rider.has_nimbl_shoes = use_nimbl_shoes
    
    if not use_nimbl_shoes:
        return rider.base_performance
    
    # Performance boost based on rider's history (more victories = higher boost)
    victory_boost = min(10, rider.victories * 0.5)  # Max 10% boost from victories
    # Random boost to simulate other factors (0-5%)
    random_boost = random.uniform(0, 5)
    total_boost = victory_boost + random_boost
    
    improved_performance = rider.base_performance + total_boost
    # Cap performance at 100
    return min(100, improved_performance)

def simulate_race(riders: List[Rider], use_nimbl_shoes: bool = True) -> Dict[str, float]:
    """
    Simulates a race with multiple riders and returns their improved performances.
    
    Args:
        riders: List of Rider objects.
        use_nimbl_shoes: Whether riders use Nimbl shoes (default: True).
    
    Returns:
        Dictionary mapping rider names to their improved performance.
    """
    results = {}
    for rider in riders:
        try:
            improved = simulate_performance_improvement(rider, use_nimbl_shoes)
            results[rider.name] = improved
        except ValueError as e:
            print(f"Error simulating performance for {rider.name}: {e}")
            results[rider.name] = rider.base_performance
    
    return results

def main():
    # Example usage with some top riders (hypothetical data)
    riders = [
        Rider("Tadej Pogačar", 95, 3),
        Rider("Primož Roglič", 93, 1),
        Rider("Jonas Vingegaard", 94, 2),
        Rider("Egan Bernal", 92, 1),
        Rider("Geraint Thomas", 90, 1)
    ]
    
    print("Original Performances:")
    for rider in riders:
        print(rider)
    
    print("\nSimulating with Nimbl 'Ultimate' shoes:")
    results = simulate_race(riders)
    for name, performance in results.items():
        print(f"{name}: {performance:.1f}")

if __name__ == "__main__":
    main()
```
