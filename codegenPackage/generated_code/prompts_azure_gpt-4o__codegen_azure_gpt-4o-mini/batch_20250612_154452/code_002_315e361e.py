"""
Generated Code Metadata:
========================
Original URL: https://omegaenergy.co
Prompt: Generate code to model the specialized lifting systems used in the Bloque Cóndor for maximizing production efficiency, as outlined in Omega Energy's operations.
Generated: DETERMINISTIC_315e361ecddb5ede
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LiftingSystem:
    """
    A class to model a specialized lifting system used in the Bloque Cóndor for maximizing production efficiency.
    """

    def __init__(self, capacity: float, efficiency: float):
        """
        Initializes the lifting system with a specified capacity and efficiency.

        :param capacity: The maximum weight the lifting system can handle (in tons).
        :param efficiency: The efficiency of the lifting system (0 to 1).
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive number.")
        if not (0 <= efficiency <= 1):
            raise ValueError("Efficiency must be between 0 and 1.")

        self.capacity = capacity
        self.efficiency = efficiency

    def lift(self, weight: float) -> float:
        """
        Lifts a specified weight and returns the effective weight lifted based on system efficiency.

        :param weight: The weight to be lifted (in tons).
        :return: The effective weight lifted (in tons).
        :raises ValueError: If the weight exceeds the system's capacity.
        """
        if weight > self.capacity:
            raise ValueError("Weight exceeds the lifting system's capacity.")

        effective_weight = weight * self.efficiency
        return effective_weight

    def __str__(self):
        """
        Returns a string representation of the lifting system.
        """
        return f"LiftingSystem(capacity={self.capacity}, efficiency={self.efficiency})"


class BloqueCondor:
    """
    A class to model the Bloque Cóndor operations utilizing specialized lifting systems.
    """

    def __init__(self):
        """
        Initializes the Bloque Cóndor with an empty list of lifting systems.
        """
        self.lifting_systems = []

    def add_lifting_system(self, lifting_system: LiftingSystem):
        """
        Adds a lifting system to the Bloque Cóndor operations.

        :param lifting_system: An instance of LiftingSystem to be added.
        """
        if not isinstance(lifting_system, LiftingSystem):
            raise TypeError("Expected an instance of LiftingSystem.")
        self.lifting_systems.append(lifting_system)

    def lift_with_system(self, index: int, weight: float) -> float:
        """
        Uses a specified lifting system to lift a weight.

        :param index: The index of the lifting system in the list.
        :param weight: The weight to be lifted (in tons).
        :return: The effective weight lifted (in tons).
        :raises IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.lifting_systems):
            raise IndexError("Lifting system index out of range.")

        lifting_system = self.lifting_systems[index]
        return lifting_system.lift(weight)

    def __str__(self):
        """
        Returns a string representation of the Bloque Cóndor operations.
        """
        return f"BloqueCondor(lifting_systems={self.lifting_systems})"


# Example usage
if __name__ == "__main__":
    try:
        # Create lifting systems
        system1 = LiftingSystem(capacity=10, efficiency=0.9)
        system2 = LiftingSystem(capacity=15, efficiency=0.85)

        # Initialize Bloque Cóndor
        bloque_condor = BloqueCondor()
        bloque_condor.add_lifting_system(system1)
        bloque_condor.add_lifting_system(system2)

        # Lift weights using the systems
        effective_weight1 = bloque_condor.lift_with_system(0, 8)
        print(f"Effective weight lifted by system 1: {effective_weight1} tons")

        effective_weight2 = bloque_condor.lift_with_system(1, 12)
        print(f"Effective weight lifted by system 2: {effective_weight2} tons")

    except (ValueError, TypeError, IndexError) as e:
        print(f"Error: {e}")
```
