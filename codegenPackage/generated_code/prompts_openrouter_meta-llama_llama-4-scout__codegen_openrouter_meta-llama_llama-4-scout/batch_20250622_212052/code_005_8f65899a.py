"""
Generated Code Metadata:
========================
Original URL: https://rayclaims.net
Prompt: Design a cryptocurrency recovery service pricing model that incentivizes successful fund retrieval, with a 5% standard plan and no penalty for unsuccessful cases.
Generated: DETERMINISTIC_8f65899a75d6c341
Batch ID: 20250622_212052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class RecoveryStatus(Enum):
    """Enum for recovery status"""
    SUCCESS = 1
    FAILURE = 2

class PricingModel:
    """Pricing model for cryptocurrency recovery service"""

    def __init__(self, standard_plan_percentage: float = 0.05):
        """
        Initialize pricing model

        Args:
        - standard_plan_percentage (float): Percentage for standard plan (default: 5%)
        """
        self.standard_plan_percentage = standard_plan_percentage

    def calculate_fee(self, recovered_amount: float, status: RecoveryStatus) -> float:
        """
        Calculate fee based on recovery status and amount

        Args:
        - recovered_amount (float): Amount of cryptocurrency recovered
        - status (RecoveryStatus): Status of recovery

        Returns:
        - float: Calculated fee

        Raises:
        - ValueError: If recovered amount is negative
        """
        if recovered_amount < 0:
            raise ValueError("Recovered amount cannot be negative")

        if status == RecoveryStatus.SUCCESS:
            return recovered_amount * self.standard_plan_percentage
        else:
            return 0.0

    def get_pricing_details(self, recovered_amount: float, status: RecoveryStatus) -> Dict[str, float]:
        """
        Get pricing details

        Args:
        - recovered_amount (float): Amount of cryptocurrency recovered
        - status (RecoveryStatus): Status of recovery

        Returns:
        - Dict[str, float]: Pricing details (fee, recovered amount)
        """
        fee = self.calculate_fee(recovered_amount, status)
        return {
            "recovered_amount": recovered_amount,
            "fee": fee,
            "net_recovered": recovered_amount - fee if status == RecoveryStatus.SUCCESS else 0.0
        }

def main():
    # Example usage
    pricing_model = PricingModel()

    # Successful recovery
    recovered_amount = 10000.0
    status = RecoveryStatus.SUCCESS
    pricing_details = pricing_model.get_pricing_details(recovered_amount, status)
    print("Pricing Details (Successful Recovery):")
    for key, value in pricing_details.items():
        print(f"{key.capitalize().replace('_', ' ')}: ${value:.2f}")

    # Unsuccessful recovery
    recovered_amount = 0.0
    status = RecoveryStatus.FAILURE
    pricing_details = pricing_model.get_pricing_details(recovered_amount, status)
    print("\nPricing Details (Unsuccessful Recovery):")
    for key, value in pricing_details.items():
        print(f"{key.capitalize().replace('_', ' ')}: ${value:.2f}")

if __name__ == "__main__":
    main()
```
