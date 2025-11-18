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
import logging

# Configure logging to display errors and warnings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LeveragedYieldFarming:
    """
    A class to calculate collateralization ratio and liquidation risks for
    a leveraged yield farming position on Extra Finance.
    """

    def __init__(self, collateral_amount, borrowed_amount, liquidation_threshold):
        """
        Initializes the leveraged yield farming position.

        :param collateral_amount: Amount of collateral provided (float).
        :param borrowed_amount: Amount borrowed for farming (float).
        :param liquidation_threshold: The minimum collateralization ratio
                                       before liquidation occurs (float).
        """
        self.collateral_amount = collateral_amount
        self.borrowed_amount = borrowed_amount
        self.liquidation_threshold = liquidation_threshold

    def calculate_collateralization_ratio(self):
        """
        Calculates the collateralization ratio.

        :return: Collateralization ratio as a float.
        """
        try:
            # Ensure borrowed_amount is not zero to avoid division by zero
            if self.borrowed_amount <= 0:
                raise ValueError("Borrowed amount must be greater than zero.")

            collateralization_ratio = self.collateral_amount / self.borrowed_amount
            return collateralization_ratio

        except Exception as e:
            logging.error(f"Error calculating collateralization ratio: {e}")
            return None

    def check_liquidation_risk(self):
        """
        Checks if the position is at risk of liquidation.

        :return: Boolean indicating liquidation risk (True if at risk, False otherwise).
        """
        try:
            collateralization_ratio = self.calculate_collateralization_ratio()
            if collateralization_ratio is None:
                raise ValueError("Collateralization ratio could not be calculated.")

            return collateralization_ratio < self.liquidation_threshold

        except Exception as e:
            logging.error(f"Error checking liquidation risk: {e}")
            return None


# Example usage
if __name__ == "__main__":
    try:
        # Example position parameters
        collateral_amount = 1000.0
        borrowed_amount = 500.0
        liquidation_threshold = 2.0  # Collateralization ratio must stay above 2.0

        # Create the leveraged farming position
        position = LeveragedYieldFarming(collateral_amount, borrowed_amount, liquidation_threshold)

        # Calculate collateralization ratio
        collateralization_ratio = position.calculate_collateralization_ratio()
        if collateralization_ratio is not None:
            print(f"Collateralization Ratio: {collateralization_ratio:.2f}")

        # Check liquidation risk
        is_at_risk = position.check_liquidation_risk()
        if is_at_risk is not None:
            if is_at_risk:
                print("Warning: Position is at risk of liquidation!")
            else:
                print("Position is safe from liquidation.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
