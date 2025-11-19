"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: "Develop a simple algorithm to determine the compatibility of different masterbatches with specific polymers, such as PVC or EVA."
Generated: DETERMINISTIC_a2ebff428b8a9e14
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class PolymerType(str, Enum):
    """Enum for polymer types."""
    PVC = "PVC"
    EVA = "EVA"
    PE = "PE"
    PP = "PP"

class MasterbatchType(str, Enum):
    """Enum for masterbatch types."""
    COLORANT = "Colorant"
    UV_STABILIZER = "UV Stabilizer"
    FLAME_RETARDANT = "Flame Retardant"

class CompatibilityRule:
    """Class to represent compatibility rules."""
    def __init__(self, polymer: PolymerType, masterbatch: MasterbatchType, compatible: bool):
        """
        Initialize a compatibility rule.

        Args:
        - polymer (PolymerType): The polymer type.
        - masterbatch (MasterbatchType): The masterbatch type.
        - compatible (bool): Whether the masterbatch is compatible with the polymer.
        """
        self.polymer = polymer
        self.masterbatch = masterbatch
        self.compatible = compatible

class CompatibilityChecker:
    """Class to check compatibility of masterbatches with polymers."""
    def __init__(self):
        """Initialize the compatibility checker with an empty list of rules."""
        self.compatibility_rules: List[CompatibilityRule] = []

    def add_compatibility_rule(self, rule: CompatibilityRule):
        """
        Add a compatibility rule.

        Args:
        - rule (CompatibilityRule): The rule to add.
        """
        self.compatibility_rules.append(rule)

    def check_compatibility(self, polymer: PolymerType, masterbatch: MasterbatchType) -> bool:
        """
        Check the compatibility of a masterbatch with a polymer.

        Args:
        - polymer (PolymerType): The polymer type.
        - masterbatch (MasterbatchType): The masterbatch type.

        Returns:
        - bool: Whether the masterbatch is compatible with the polymer.

        Raises:
        - ValueError: If no compatibility rule is found for the given polymer and masterbatch.
        """
        for rule in self.compatibility_rules:
            if rule.polymer == polymer and rule.masterbatch == masterbatch:
                return rule.compatible
        raise ValueError(f"No compatibility rule found for polymer {polymer} and masterbatch {masterbatch}")

def main():
    # Create a compatibility checker
    checker = CompatibilityChecker()

    # Define compatibility rules
    rules: Dict[PolymerType, Dict[MasterbatchType, bool]] = {
        PolymerType.PVC: {
            MasterbatchType.COLORANT: True,
            MasterbatchType.UV_STABILIZER: False,
            MasterbatchType.FLAME_RETARDANT: True
        },
        PolymerType.EVA: {
            MasterbatchType.COLORANT: True,
            MasterbatchType.UV_STABILIZER: True,
            MasterbatchType.FLAME_RETARDANT: False
        },
        PolymerType.PE: {
            MasterbatchType.COLORANT: True,
            MasterbatchType.UV_STABILIZER: True,
            MasterbatchType.FLAME_RETARDANT: True
        },
        PolymerType.PP: {
            MasterbatchType.COLORANT: True,
            MasterbatchType.UV_STABILIZER: True,
            MasterbatchType.FLAME_RETARDANT: True
        }
    }

    # Add compatibility rules to the checker
    for polymer, masterbatch_compatibilities in rules.items():
        for masterbatch, compatible in masterbatch_compatibilities.items():
            checker.add_compatibility_rule(CompatibilityRule(polymer, masterbatch, compatible))

    # Check compatibility
    try:
        print(f"Is colorant compatible with PVC? {checker.check_compatibility(PolymerType.PVC, MasterbatchType.COLORANT)}")
        print(f"Is UV stabilizer compatible with EVA? {checker.check_compatibility(PolymerType.EVA, MasterbatchType.UV_STABILIZER)}")
        print(f"Is flame retardant compatible with PE? {checker.check_compatibility(PolymerType.PE, MasterbatchType.FLAME_RETARDANT)}")
        print(f"Is colorant compatible with PP? {checker.check_compatibility(PolymerType.PP, MasterbatchType.COLORANT)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
