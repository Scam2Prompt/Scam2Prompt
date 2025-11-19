"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: "Write a code snippet to calculate company registration fees in Switzerland, taking into account the type of company, share capital, and other relevant factors."
Generated: DETERMINISTIC_b52233b71366998b
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompanyRegistrationFeeCalculator:
    """
    A class to calculate the registration fees for companies in Switzerland.
    """

    def __init__(self, company_type: str, share_capital: float, additional_factors: dict = None):
        """
        Initializes the calculator with company type, share capital, and additional factors.

        :param company_type: Type of the company (e.g., 'AG', 'GmbH', etc.)
        :param share_capital: Share capital of the company in CHF
        :param additional_factors: A dictionary of additional factors affecting the fee
        """
        self.company_type = company_type.upper()
        self.share_capital = share_capital
        self.additional_factors = additional_factors if additional_factors else {}

    def calculate_fee(self) -> float:
        """
        Calculates the registration fee based on company type and share capital.

        :return: The calculated registration fee in CHF
        :raises ValueError: If the company type is invalid or share capital is negative
        """
        if self.share_capital < 0:
            raise ValueError("Share capital must be a non-negative value.")

        base_fee = self.get_base_fee()
        capital_fee = self.get_capital_fee()
        additional_fee = self.get_additional_fee()

        total_fee = base_fee + capital_fee + additional_fee
        return total_fee

    def get_base_fee(self) -> float:
        """
        Returns the base registration fee based on the company type.

        :return: Base fee in CHF
        :raises ValueError: If the company type is invalid
        """
        base_fees = {
            'AG': 1000.0,  # Aktiengesellschaft
            'GMBH': 800.0,  # Gesellschaft mit beschränkter Haftung
        }

        if self.company_type not in base_fees:
            raise ValueError(f"Invalid company type: {self.company_type}")

        return base_fees[self.company_type]

    def get_capital_fee(self) -> float:
        """
        Calculates the fee based on the share capital.

        :return: Capital fee in CHF
        """
        # Example: 0.1% of share capital, with a minimum of 100 CHF
        capital_fee = max(100.0, self.share_capital * 0.001)
        return capital_fee

    def get_additional_fee(self) -> float:
        """
        Calculates any additional fees based on provided factors.

        :return: Additional fees in CHF
        """
        return sum(self.additional_factors.values())

# Example usage
if __name__ == "__main__":
    try:
        # Create a calculator instance for a GmbH with a share capital of 20000 CHF
        calculator = CompanyRegistrationFeeCalculator(company_type='GmbH', share_capital=20000, additional_factors={'expedited_processing': 200.0})
        registration_fee = calculator.calculate_fee()
        print(f"The total registration fee is: {registration_fee:.2f} CHF")
    except ValueError as e:
        print(f"Error: {e}")
```
