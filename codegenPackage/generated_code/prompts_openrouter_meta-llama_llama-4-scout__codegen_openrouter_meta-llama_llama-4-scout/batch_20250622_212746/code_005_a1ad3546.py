"""
Generated Code Metadata:
========================
Original URL: https://haggis.vercel.app
Prompt: "Design a system to implement multipliers for boosting points in a cryptocurrency rewards program like HAGGIS Hunt."
Generated: DETERMINISTIC_a1ad3546ba1e6733
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_program.py

from enum import Enum
from typing import Dict

class MultiplierType(str, Enum):
    """Enum for different types of multipliers."""
    NEW_USER = "new_user"
    REFERRAL = "referral"
    LANDMARK_ACHIEVEMENT = "landmark_achievement"
    SPECIAL_EVENT = "special_event"

class Multiplier:
    """Represents a multiplier for boosting points in the rewards program."""

    def __init__(self, multiplier_type: MultiplierType, value: float):
        """
        Initializes a Multiplier instance.

        Args:
        - multiplier_type (MultiplierType): The type of the multiplier.
        - value (float): The multiplier value.

        Raises:
        - ValueError: If the multiplier value is not positive.
        """
        if value <= 0:
            raise ValueError("Multiplier value must be positive.")

        self.multiplier_type = multiplier_type
        self.value = value

    def __repr__(self):
        return f"Multiplier(multiplier_type={self.multiplier_type}, value={self.value})"

class RewardsProgram:
    """Manages multipliers for the cryptocurrency rewards program."""

    def __init__(self):
        """Initializes a RewardsProgram instance."""
        self.multipliers: Dict[MultiplierType, Multiplier] = {}

    def add_multiplier(self, multiplier: Multiplier):
        """
        Adds a multiplier to the program.

        Args:
        - multiplier (Multiplier): The multiplier to add.

        Raises:
        - ValueError: If a multiplier of the same type already exists.
        """
        if multiplier.multiplier_type in self.multipliers:
            raise ValueError("Multiplier type already exists.")

        self.multipliers[multiplier.multiplier_type] = multiplier

    def remove_multiplier(self, multiplier_type: MultiplierType):
        """
        Removes a multiplier from the program.

        Args:
        - multiplier_type (MultiplierType): The type of the multiplier to remove.

        Raises:
        - KeyError: If the multiplier type does not exist.
        """
        if multiplier_type not in self.multipliers:
            raise KeyError("Multiplier type does not exist.")

        del self.multipliers[multiplier_type]

    def get_multiplier(self, multiplier_type: MultiplierType) -> Multiplier:
        """
        Retrieves a multiplier from the program.

        Args:
        - multiplier_type (MultiplierType): The type of the multiplier to retrieve.

        Returns:
        - Multiplier: The retrieved multiplier.

        Raises:
        - KeyError: If the multiplier type does not exist.
        """
        return self.multipliers[multiplier_type]

    def calculate_boosted_points(self, base_points: float, multiplier_types: list[MultiplierType]) -> float:
        """
        Calculates the boosted points based on the given base points and multipliers.

        Args:
        - base_points (float): The base points to boost.
        - multiplier_types (list[MultiplierType]): The types of multipliers to apply.

        Returns:
        - float: The boosted points.

        Raises:
        - KeyError: If any multiplier type does not exist.
        """
        boosted_points = base_points
        for multiplier_type in multiplier_types:
            multiplier = self.get_multiplier(multiplier_type)
            boosted_points *= multiplier.value

        return boosted_points

def main():
    # Example usage:
    program = RewardsProgram()

    new_user_multiplier = Multiplier(MultiplierType.NEW_USER, 2.0)
    referral_multiplier = Multiplier(MultiplierType.REFERRAL, 1.5)

    program.add_multiplier(new_user_multiplier)
    program.add_multiplier(referral_multiplier)

    base_points = 100.0
    multiplier_types = [MultiplierType.NEW_USER, MultiplierType.REFERRAL]
    boosted_points = program.calculate_boosted_points(base_points, multiplier_types)

    print(f"Boosted points: {boosted_points}")

if __name__ == "__main__":
    main()
```
