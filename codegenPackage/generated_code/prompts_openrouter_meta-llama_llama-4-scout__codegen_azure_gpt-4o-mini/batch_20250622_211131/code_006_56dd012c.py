"""
Generated Code Metadata:
========================
Original URL: https://to-ousd.pages.dev
Prompt: Write a code snippet in Python to calculate the redemption value of OUSD, considering the 0.25% fee charged when redeeming or burning OUSD on the OUSD dapp.
Generated: DETERMINISTIC_56dd012c809f245e
Batch ID: 20250622_211131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OUSDRedemption:
    """
    A class to calculate the redemption value of OUSD considering a fee.
    """

    def __init__(self, fee_percentage=0.0025):
        """
        Initializes the OUSDRedemption class with a specified fee percentage.

        :param fee_percentage: The fee charged during redemption (default is 0.25%).
        """
        self.fee_percentage = fee_percentage

    def calculate_redemption_value(self, ousd_amount, ousd_value_per_token):
        """
        Calculates the redemption value after applying the fee.

        :param ousd_amount: The amount of OUSD to redeem.
        :param ousd_value_per_token: The current value of one OUSD token.
        :return: The net redemption value after fee deduction.
        :raises ValueError: If the OUSD amount or value per token is negative.
        """
        if ousd_amount < 0 or ousd_value_per_token < 0:
            raise ValueError("OUSD amount and value per token must be non-negative.")

        # Calculate the gross redemption value
        gross_redemption_value = ousd_amount * ousd_value_per_token

        # Calculate the fee
        fee = gross_redemption_value * self.fee_percentage

        # Calculate the net redemption value
        net_redemption_value = gross_redemption_value - fee

        return net_redemption_value


# Example usage
if __name__ == "__main__":
    try:
        ousd_amount = 1000  # Amount of OUSD to redeem
        ousd_value_per_token = 1.05  # Current value of one OUSD token

        redemption_calculator = OUSDRedemption()
        redemption_value = redemption_calculator.calculate_redemption_value(ousd_amount, ousd_value_per_token)

        print(f"The net redemption value of {ousd_amount} OUSD is: ${redemption_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
