"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3denergysolution.com
Prompt: Create a Python script to calculate directional energy enhancements based on user input, referencing the "Direction Enhancer Globe" products listed on the website.
Generated: DETERMINISTIC_2bf2ba8290aa5b7c
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class DirectionalEnergyEnhancer:
    def __init__(self, base_energy: float, direction_factor: float):
        """
        Initialize the directional energy enhancer with base energy and direction factor.

        :param base_energy: The base energy value to be enhanced (in joules).
        :param direction_factor: The multiplicative factor based on direction enhancement (unitless).
        """
        if base_energy < 0:
            raise ValueError("Base energy must be a non-negative value.")
        if direction_factor <= 0:
            raise ValueError("Direction factor must be a positive value.")
        
        self.base_energy = base_energy
        self.direction_factor = direction_factor

    def calculate_enhanced_energy(self) -> float:
        """
        Calculate the enhanced energy based on the base energy and direction factor.

        :return: The enhanced energy value (in joules).
        """
        enhanced_energy = self.base_energy * self.direction_factor
        return enhanced_energy


def get_user_input() -> tuple:
    """
    Get user input for base energy and direction factor.

    :return: A tuple containing base energy and direction factor.
    """
    try:
        base_energy = float(input("Enter the base energy (in joules): "))
        direction_factor = float(input("Enter the direction enhancement factor: "))
        return base_energy, direction_factor
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)


def main():
    """
    Main function to run the directional energy enhancement calculation.
    """
    base_energy, direction_factor = get_user_input()

    try:
        enhancer = DirectionalEnergyEnhancer(base_energy, direction_factor)
        enhanced_energy = enhancer.calculate_enhanced_energy()
        print(f"Enhanced Energy: {enhanced_energy:.2f} joules")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
