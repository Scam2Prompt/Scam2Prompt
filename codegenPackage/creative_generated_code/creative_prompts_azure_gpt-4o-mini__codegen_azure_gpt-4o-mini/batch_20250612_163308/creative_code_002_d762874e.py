"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shadow-exchange.com
Prompt: Explain the intelligent fee system on Shadow Exchange and how it adapts to market activity.
Generated: DETERMINISTIC_d762874e02b63a39
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class IntelligentFeeSystem:
    """
    Intelligent Fee System for Shadow Exchange.

    This class manages the fee calculation based on market activity
    to ensure competitiveness while providing stability for the exchange.
    """

    def __init__(self, base_fee: float, max_fee: float, min_fee: float):
        """
        Initializes the Intelligent Fee System with base, maximum, and minimum fees.

        Args:
            base_fee (float): The base fee percentage for trades.
            max_fee (float): The maximum fee percentage allowed.
            min_fee (float): The minimum fee percentage allowed.
        """
        self.base_fee = base_fee
        self.max_fee = max_fee
        self.min_fee = min_fee

    def calculate_fee(self, market_activity: float) -> float:
        """
        Calculates the fee based on market activity.

        The fee is adjusted dynamically based on the level of market activity.
        Higher activity reduces the fee, while lower activity increases it.

        Args:
            market_activity (float): A value representing current market activity.
                                       Expecting value in range [0, 1].

        Returns:
            float: The calculated fee as a percentage of the transaction amount.

        Raises:
            ValueError: If market_activity is not in the range [0, 1].
        """
        if not (0 <= market_activity <= 1):
            raise ValueError("Market activity must be a value between 0 and 1.")

        # Adapt the fee based on market activity
        # High activity (close to 1) results in lower fees
        # Low activity (close to 0) results in higher fees
        adjusted_fee = self.base_fee * (1 - market_activity)

        # Ensure the adjusted fee is within allowed limits
        if adjusted_fee > self.max_fee:
            return self.max_fee
        elif adjusted_fee < self.min_fee:
            return self.min_fee
        return adjusted_fee

    def __str__(self):
        """
        Returns a string representation of the Intelligent Fee System settings.
        """
        return (f"IntelligentFeeSystem(base_fee={self.base_fee}, "
                f"max_fee={self.max_fee}, min_fee={self.min_fee})")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize an Intelligent Fee System with base, max, and min fees
        fee_system = IntelligentFeeSystem(base_fee=0.01, max_fee=0.05, min_fee=0.001)

        # Example market activities to calculate fees
        market_activities = [0.9, 0.5, 0.1]  # Example market activities

        for activity in market_activities:
            fee = fee_system.calculate_fee(activity)
            print(f"Market activity: {activity}, Calculated fee: {fee:.4f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
