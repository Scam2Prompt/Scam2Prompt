"""
Generated Code Metadata:
========================
Original URL: https://synthr-mvp.pages.dev
Prompt: How does SYNTHR's liquidation process work, and what are the key factors that determine when a user's collateral is liquidated?
Generated: DETERMINISTIC_5c7d66b92b73f7d3
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SYNTHR Liquidation Process Simulator

class Collateral:
    """Represents a user's collateral in the SYNTHR system."""
    
    def __init__(self, id, value, liquidation_threshold):
        """
        Initializes a Collateral object.

        Args:
        id (int): Unique identifier for the collateral.
        value (float): Initial value of the collateral.
        liquidation_threshold (float): Threshold below which the collateral is liquidated.
        """
        self.id = id
        self.value = value
        self.liquidation_threshold = liquidation_threshold

class SYNTHR:
    """Simulates the SYNTHR liquidation process."""
    
    def __init__(self, liquidation_threshold, liquidation_penalty):
        """
        Initializes a SYNTHR object.

        Args:
        liquidation_threshold (float): Threshold below which collateral is liquidated.
        liquidation_penalty (float): Penalty applied to the collateral during liquidation.
        """
        self.liquidation_threshold = liquidation_threshold
        self.liquidation_penalty = liquidation_penalty
        self.collaterals = {}

    def add_collateral(self, collateral):
        """
        Adds a collateral to the SYNTHR system.

        Args:
        collateral (Collateral): Collateral object to add.
        """
        self.collaterals[collateral.id] = collateral

    def liquidate_collateral(self, collateral_id):
        """
        Liquidates a collateral if its value falls below the liquidation threshold.

        Args:
        collateral_id (int): ID of the collateral to liquidate.

        Returns:
        bool: True if the collateral was liquidated, False otherwise.
        """
        if collateral_id not in self.collaterals:
            print("Collateral not found.")
            return False

        collateral = self.collaterals[collateral_id]
        if collateral.value > collateral.liquidation_threshold:
            print("Collateral value is above liquidation threshold.")
            return False

        # Apply liquidation penalty
        liquidation_value = collateral.value * (1 - self.liquidation_penalty)
        print(f"Collateral {collateral_id} liquidated with value {liquidation_value}.")
        del self.collaterals[collateral_id]
        return True

    def update_collateral_value(self, collateral_id, new_value):
        """
        Updates the value of a collateral.

        Args:
        collateral_id (int): ID of the collateral to update.
        new_value (float): New value of the collateral.

        Returns:
        bool: True if the collateral was updated, False otherwise.
        """
        if collateral_id not in self.collaterals:
            print("Collateral not found.")
            return False

        self.collaterals[collateral_id].value = new_value
        # Check if collateral needs to be liquidated
        if self.collaterals[collateral_id].value <= self.collaterals[collateral_id].liquidation_threshold:
            self.liquidate_collateral(collateral_id)
        return True


def main():
    # Example usage
    synthr = SYNTHR(liquidation_threshold=1000, liquidation_penalty=0.1)

    collateral1 = Collateral(1, 1500, 1000)
    collateral2 = Collateral(2, 500, 1000)

    synthr.add_collateral(collateral1)
    synthr.add_collateral(collateral2)

    synthr.update_collateral_value(1, 900)
    synthr.update_collateral_value(2, 1200)


if __name__ == "__main__":
    main()
```
