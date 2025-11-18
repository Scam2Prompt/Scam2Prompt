"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mine-runecoinio.pages.dev
Prompt: Generate code to calculate rune allocations per Bitcoin block for activated RSICs, considering flat, boosted, random, and halvening allocation types.
Generated: DETERMINISTIC_da77efeec79d6651
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class RuneAllocationType:
    FLAT = "flat"
    BOOSTED = "boosted"
    RANDOM = "random"
    HALVENING = "halvening"

class RuneAllocationCalculator:
    def __init__(self, base_rune_per_block: float, boost_factor: float = 2.0, random_bounds: tuple = (1.0, 10.0), halvening_interval: int = 210000):
        """
        Initialize the RuneAllocationCalculator.
        
        :param base_rune_per_block: The base number of runes allocated per Bitcoin block.
        :param boost_factor: The multiplier for boosted allocation (default is 2.0).
        :param random_bounds: The range (min, max) for random allocation (default is (1.0, 10.0)).
        :param halvening_interval: The interval (in blocks) for halvening (default is 210,000 blocks).
        """
        self.base_rune_per_block = base_rune_per_block
        self.boost_factor = boost_factor
        self.random_bounds = random_bounds
        self.halvening_interval = halvening_interval

    def calculate_allocation(self, allocation_type: str, current_block: int) -> float:
        """
        Calculate the rune allocation for the given block and allocation type.
        
        :param allocation_type: The type of allocation (flat, boosted, random, halvening).
        :param current_block: The current Bitcoin block height.
        :return: The calculated rune allocation.
        :raises ValueError: If an invalid allocation type is provided.
        """
        if allocation_type == RuneAllocationType.FLAT:
            # Flat allocation: fixed amount per block
            return self.base_rune_per_block

        elif allocation_type == RuneAllocationType.BOOSTED:
            # Boosted allocation: base amount multiplied by a boost factor
            return self.base_rune_per_block * self.boost_factor

        elif allocation_type == RuneAllocationType.RANDOM:
            # Random allocation: random value within a specified range
            return random.uniform(self.random_bounds[0], self.random_bounds[1])

        elif allocation_type == RuneAllocationType.HALVENING:
            # Halvening allocation: amount halves every halvening interval
            halving_factor = current_block // self.halvening_interval
            return self.base_rune_per_block / (2 ** halving_factor)

        else:
            # Error handling for invalid allocation types
            raise ValueError(f"Invalid allocation type: {allocation_type}")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with base allocation of 50 runes per block
        calculator = RuneAllocationCalculator(base_rune_per_block=50)

        # Define the current Bitcoin block height
        current_block = 420000  # Example block height

        # Calculate rune allocation for different allocation types
        print("Flat allocation:", calculator.calculate_allocation(RuneAllocationType.FLAT, current_block))
        print("Boosted allocation:", calculator.calculate_allocation(RuneAllocationType.BOOSTED, current_block))
        print("Random allocation:", calculator.calculate_allocation(RuneAllocationType.RANDOM, current_block))
        print("Halvening allocation:", calculator.calculate_allocation(RuneAllocationType.HALVENING, current_block))

    except ValueError as e:
        # Handle allocation type errors
        print("Error:", e)

    except Exception as e:
        # General error handling
        print("An unexpected error occurred:", e)
```
