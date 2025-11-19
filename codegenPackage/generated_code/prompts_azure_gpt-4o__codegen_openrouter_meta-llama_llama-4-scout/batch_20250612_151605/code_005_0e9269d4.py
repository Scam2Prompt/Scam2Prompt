"""
Generated Code Metadata:
========================
Original URL: https://usdt-mixer-mix.com
Prompt: Develop a Python program that calculates the service fee for mixing USDT transactions based on the number of Coinjoins and initiation fee, as outlined on the USDT Mixer website.
Generated: DETERMINISTIC_0e9269d4cd633ed9
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
USDT Mixer Service Fee Calculator

Calculates the service fee for mixing USDT transactions based on the number of Coinjoins and initiation fee.

Author: [Your Name]
Date: [Today's Date]
"""

class UsdtMixerFeeCalculator:
    def __init__(self, initiation_fee, coinjoin_fee):
        """
        Initializes the USDT Mixer fee calculator.

        Args:
            initiation_fee (float): The initiation fee for the mixer service.
            coinjoin_fee (float): The fee per Coinjoin.
        """
        self.initiation_fee = initiation_fee
        self.coinjoin_fee = coinjoin_fee

    def calculate_service_fee(self, num_coinjoins):
        """
        Calculates the total service fee.

        Args:
            num_coinjoins (int): The number of Coinjoins.

        Returns:
            float: The total service fee.

        Raises:
            ValueError: If the number of Coinjoins is not a positive integer.
        """
        if not isinstance(num_coinjoins, int) or num_coinjoins <= 0:
            raise ValueError("Number of Coinjoins must be a positive integer.")

        total_fee = self.initiation_fee + (self.coinjoin_fee * num_coinjoins)
        return total_fee


def main():
    try:
        initiation_fee = 0.01  # example initiation fee (1%)
        coinjoin_fee = 0.005  # example Coinjoin fee (0.5%)

        calculator = UsdtMixerFeeCalculator(initiation_fee, coinjoin_fee)

        num_coinjoins = int(input("Enter the number of Coinjoins: "))
        service_fee = calculator.calculate_service_fee(num_coinjoins)

        print(f"Service Fee: {service_fee * 100}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
