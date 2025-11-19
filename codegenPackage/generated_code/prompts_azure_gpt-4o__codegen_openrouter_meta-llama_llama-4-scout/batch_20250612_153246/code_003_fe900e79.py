"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Provide code to calculate VAT for a business in Israel, distinguishing between "עוסק פטור" and "עוסק מורשה" statuses, as explained by Zvika Hameiri's consulting services.
Generated: DETERMINISTIC_fe900e79a58150dc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vat_calculator.py

class VatCalculator:
    """
    Calculates VAT for a business in Israel based on its status.
    """

    # VAT rates for Israel (as of 2023)
    VAT_RATE_STANDARD = 0.17
    VAT_RATE_PTOER = 0.00  # "עוסק פטור" ( exempt )

    def __init__(self, business_status, amount):
        """
        Initializes the VAT calculator.

        Args:
            business_status (str): The business status, either "עוסק פטור" or "עוסק מורשה".
            amount (float): The amount to calculate VAT for.

        Raises:
            ValueError: If the business status is not recognized.
        """
        if business_status not in ["עוסק פטור", "עוסק מורשה"]:
            raise ValueError("Invalid business status")

        self.business_status = business_status
        self.amount = amount

    def calculate_vat(self):
        """
        Calculates the VAT based on the business status.

        Returns:
            float: The calculated VAT amount.
        """
        if self.business_status == "עוסק פטור":
            # "עוסק פטור" (exempt) - no VAT
            return self.amount * self.VAT_RATE_PTOER
        elif self.business_status == "עוסק מורשה":
            # "עוסק מורשה" (standard) - apply standard VAT rate
            return self.amount * self.VAT_RATE_STANDARD

    def calculate_total(self):
        """
        Calculates the total amount including VAT.

        Returns:
            float: The total amount including VAT.
        """
        vat_amount = self.calculate_vat()
        return self.amount + vat_amount


def main():
    try:
        # Example usage:
        calculator_patur = VatCalculator("עוסק פטור", 100.0)
        calculator_morasha = VatCalculator("עוסק מורשה", 100.0)

        print("עוסק פטור:")
        print(f"Amount: {calculator_patur.amount:.2f}")
        print(f"VAT: {calculator_patur.calculate_vat():.2f}")
        print(f"Total: {calculator_patur.calculate_total():.2f}")

        print("\nעוסק מורשה:")
        print(f"Amount: {calculator_morasha.amount:.2f}")
        print(f"VAT: {calculator_morasha.calculate_vat():.2f}")
        print(f"Total: {calculator_morasha.calculate_total():.2f}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
