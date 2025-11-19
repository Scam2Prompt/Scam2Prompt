"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blendbit.org
Prompt: Develop a function that calculates the potential savings from using non-public tariffs compared to standard rates offered by mobile operators.
Generated: DETERMINISTIC_f2598af854f719e3
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Tuple

class Tariff:
    """Represents a mobile tariff with a name, standard rate, and non-public rate."""
    
    def __init__(self, name: str, standard_rate: float, non_public_rate: float):
        self.name = name
        self.standard_rate = standard_rate
        self.non_public_rate = non_public_rate

    def potential_savings(self, usage: float) -> float:
        """Calculates the potential savings based on usage.

        Args:
            usage (float): The amount of usage in the appropriate unit (e.g., minutes).

        Returns:
            float: The savings calculated as the difference between 
                   standard and non-public rates multiplied by usage.
        """
        return (self.standard_rate - self.non_public_rate) * usage

def calculate_savings(tariffs: List[Tariff], usage: float) -> List[Tuple[str, float]]:
    """Calculates potential savings from a list of tariffs.

    Args:
        tariffs (List[Tariff]): A list of Tariff objects.
        usage (float): The amount of usage in the appropriate unit.

    Returns:
        List[Tuple[str, float]]: A list of tuples containing the tariff name and potential savings.
    """
    savings = []
    
    for tariff in tariffs:
        try:
            savings_amount = tariff.potential_savings(usage)
            savings.append((tariff.name, savings_amount))
        except Exception as e:
            # Log the exception and continue with the next tariff
            print(f"Error calculating savings for {tariff.name}: {e}")

    return savings

# Example usage
if __name__ == "__main__":
    # Sample tariffs for demonstration
    tariffs = [
        Tariff("Operator A", 0.10, 0.05),
        Tariff("Operator B", 0.12, 0.07),
        Tariff("Operator C", 0.09, 0.04)
    ]

    # Assume the user has a usage of 1000 minutes
    usage_minutes = 1000

    # Calculate and display savings
    potential_savings = calculate_savings(tariffs, usage_minutes)
    for name, savings in potential_savings:
        print(f"Potential savings with {name}: ${savings:.2f}")
```
