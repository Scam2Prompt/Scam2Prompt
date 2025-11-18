"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migration-soniclabs.net
Prompt: Create a function that calculates the deposit fee (0.1 FTM) and the estimated time (21 seconds) for upgrading FTM to Sonic, as described in the Sonic Labs documentation.
Generated: DETERMINISTIC_d715b379d40adae4
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UpgradeFTMToSonic:
    def __init__(self):
        """
        Initialize the parameters for the upgrade process.
        """
        self.deposit_fee = 0.1  # Deposit fee in FTM
        self.estimated_time = 21  # Estimated time in seconds

    def calculate_upgrade_cost(self, amount_ftm: float) -> float:
        """
        Calculate the total cost for upgrading a given amount of FTM to Sonic.

        Args:
            amount_ftm (float): The amount of FTM to be upgraded.

        Returns:
            float: The total cost including the deposit fee.
        """
        if amount_ftm <= 0:
            raise ValueError("The amount of FTM must be greater than zero.")

        total_cost = amount_ftm + self.deposit_fee
        return total_cost

    def get_estimated_time(self) -> int:
        """
        Get the estimated time for the upgrade process.

        Returns:
            int: The estimated time in seconds.
        """
        return self.estimated_time

    def upgrade(self, amount_ftm: float) -> dict:
        """
        Perform the upgrade from FTM to Sonic and return the details.

        Args:
            amount_ftm (float): The amount of FTM to be upgraded.

        Returns:
            dict: A dictionary containing the total cost and estimated time.
        """
        try:
            total_cost = self.calculate_upgrade_cost(amount_ftm)
            estimated_time = self.get_estimated_time()
            return {
                'total_cost_ftm': total_cost,
                'estimated_time_seconds': estimated_time
            }
        except ValueError as e:
            return {'error': str(e)}

# Example usage
if __name__ == "__main__":
    upgrade_service = UpgradeFTMToSonic()
    result = upgrade_service.upgrade(1.0)  # Example amount of FTM to upgrade
    print(result)
```
