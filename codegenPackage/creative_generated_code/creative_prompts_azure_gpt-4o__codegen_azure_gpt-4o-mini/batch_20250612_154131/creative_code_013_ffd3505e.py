"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.extra-fl.io
Prompt: Generate code to calculate the collateralization ratio and liquidation risks for a leveraged yield farming position on Extra Finance.
Generated: DETERMINISTIC_ffd3505ee7f3e73a
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LeveragedYieldFarming:
    """
    A class to calculate collateralization ratio and liquidation risk for leveraged yield farming positions.
    """

    def __init__(self, collateral_amount: float, borrowed_amount: float, liquidation_threshold: float):
        """
        Initialize the leveraged yield farming instance.

        :param collateral_amount: Amount of collateral provided by the user.
        :param borrowed_amount: Amount of assets borrowed for leverage.
        :param liquidation_threshold: The collateralization ratio at which liquidation occurs.
        """
        if collateral_amount <= 0 or borrowed_amount < 0:
            raise ValueError("Collateral amount must be positive and borrowed amount must be non-negative.")

        self.collateral_amount = collateral_amount
        self.borrowed_amount = borrowed_amount
        self.liquidation_threshold = liquidation_threshold

    def collateralization_ratio(self) -> float:
        """
        Calculate the collateralization ratio.

        :return: The collateralization ratio as a percentage.
        """
        if self.borrowed_amount == 0:
            return 100.0  # No borrowed amount means full collateralization

        ratio = (self.collateral_amount / self.borrowed_amount) * 100
        return ratio

    def liquidation_risk(self) -> str:
        """
        Assess the liquidation risk based on the collateralization ratio.

        :return: A string indicating the liquidation risk status.
        """
        ratio = self.collateralization_ratio()

        if ratio >= self.liquidation_threshold:
            return "Safe: The position is well-collateralized."
        else:
            return "Risky: The position is under-collateralized and may be liquidated."

# Example usage of the LeveragedYieldFarming class
if __name__ == "__main__":
    try:
        # Define parameters for the leveraged position
        collateral = 1000.0  # Amount of collateral
        borrowed = 500.0     # Amount borrowed
        threshold = 150.0    # Liquidation threshold (in percentage)

        # Create an instance of the LeveragedYieldFarming class
        position = LeveragedYieldFarming(collateral, borrowed, threshold)

        # Calculate and print the collateralization ratio
        print(f"Collateralization Ratio: {position.collateralization_ratio():.2f}%")

        # Assess and print the liquidation risk
        print(position.liquidation_risk())

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
