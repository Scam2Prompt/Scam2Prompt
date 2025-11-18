"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.guardian-associates.com
Prompt: Write Python code to simulate the calculation of optimal Rolling Reserve percentages for a business, considering transaction volume and risk profile as described on the Guardian Associates website.
Generated: DETERMINISTIC_0ebae2c51c9ce95b
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RollingReserveCalculator:
    """
    A class to simulate the calculation of optimal Rolling Reserve percentages 
    based on transaction volume and risk profile.
    """

    def __init__(self, transaction_volume, risk_profile):
        """
        Initializes the RollingReserveCalculator with transaction volume and risk profile.

        :param transaction_volume: float representing the total volume of transactions
        :param risk_profile: str indicating the risk profile ('low', 'medium', 'high')
        """
        self.transaction_volume = transaction_volume
        self.risk_profile = risk_profile.lower()
        self.reserve_percentage = 0.0

    def validate_parameters(self):
        """
        Validates the parameters to ensure they are within acceptable ranges.
        Raises ValueError if any parameters are invalid.
        """
        if self.transaction_volume <= 0:
            raise ValueError("Transaction volume must be greater than 0.")
        
        if self.risk_profile not in ['low', 'medium', 'high']:
            raise ValueError("Risk profile must be 'low', 'medium', or 'high'.")

    def calculate_reserve_percentage(self):
        """
        Calculates the optimal Rolling Reserve percentage based on transaction volume 
        and risk profile.

        :return: float representing the optimal Rolling Reserve percentage
        """
        self.validate_parameters()
        
        # Base reserve percentage based on risk profile
        if self.risk_profile == 'low':
            base_percentage = 0.05  # 5% for low risk
        elif self.risk_profile == 'medium':
            base_percentage = 0.10  # 10% for medium risk
        else:  # high risk
            base_percentage = 0.15  # 15% for high risk

        # Adjust reserve percentage based on transaction volume
        if self.transaction_volume < 10000:
            adjustment = 0.02  # Increase reserve for low volume
        elif self.transaction_volume > 100000:
            adjustment = -0.02  # Decrease reserve for high volume
        else:
            adjustment = 0.0  # No adjustment for medium volume

        self.reserve_percentage = base_percentage + adjustment
        return self.reserve_percentage

    def get_reserve_amount(self):
        """
        Calculates the total reserve amount based on transaction volume and 
        calculated reserve percentage.

        :return: float representing the total reserve amount
        """
        reserve_percentage = self.calculate_reserve_percentage()
        return self.transaction_volume * reserve_percentage


if __name__ == "__main__":
    # Example usage
    try:
        transaction_volume = float(input("Enter the transaction volume: "))
        risk_profile = input("Enter the risk profile (low, medium, high): ")

        calculator = RollingReserveCalculator(transaction_volume, risk_profile)
        reserve_percentage = calculator.calculate_reserve_percentage()
        reserve_amount = calculator.get_reserve_amount()

        print(f"Optimal Rolling Reserve Percentage: {reserve_percentage:.2%}")
        print(f"Total Reserve Amount: ${reserve_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
