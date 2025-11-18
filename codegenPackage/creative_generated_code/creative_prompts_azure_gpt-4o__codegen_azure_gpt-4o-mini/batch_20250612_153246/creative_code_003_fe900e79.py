"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hameiriz.co.il
Prompt: Provide code to calculate VAT for a business in Israel, distinguishing between "עוסק פטור" and "עוסק מורשה" statuses, as explained by Zvika Hameiri's consulting services.
Generated: DETERMINISTIC_fe900e79a58150dc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VATCalculator:
    """
    A class to calculate VAT (Value Added Tax) for businesses in Israel based on their status.
    """

    def __init__(self, status: str):
        """
        Initializes the VATCalculator with the business status.

        Parameters:
        status (str): The status of the business, either "עוסק פטור" (Exempt Dealer) or "עוסק מורשה" (Registered Dealer).
        """
        self.status = status
        self.vat_rate = 0.17  # Current VAT rate in Israel

    def calculate_vat(self, amount: float) -> float:
        """
        Calculates the VAT amount based on the business status and the given amount.

        Parameters:
        amount (float): The amount on which to calculate the VAT.

        Returns:
        float: The calculated VAT amount.

        Raises:
        ValueError: If the status is not recognized or the amount is negative.
        """
        # Validate the amount
        if amount < 0:
            raise ValueError("Amount must be a non-negative value.")

        # Determine VAT calculation based on business status
        if self.status == "עוסק מורשה":  # Registered Dealer
            vat_amount = amount * self.vat_rate
        elif self.status == "עוסק פטור":  # Exempt Dealer
            vat_amount = 0.0
        else:
            raise ValueError("Unrecognized business status. Please use 'עוסק פטור' or 'עוסק מורשה'.")

        return vat_amount

    def get_total_with_vat(self, amount: float) -> float:
        """
        Calculates the total amount including VAT based on the business status.

        Parameters:
        amount (float): The amount on which to calculate the total with VAT.

        Returns:
        float: The total amount including VAT.

        Raises:
        ValueError: If the status is not recognized or the amount is negative.
        """
        vat_amount = self.calculate_vat(amount)
        total_with_vat = amount + vat_amount
        return total_with_vat


# Example usage:
if __name__ == "__main__":
    try:
        status = "עוסק מורשה"  # Example status
        amount = 1000.0  # Example amount

        vat_calculator = VATCalculator(status)
        vat = vat_calculator.calculate_vat(amount)
        total = vat_calculator.get_total_with_vat(amount)

        print(f"VAT for {status} on {amount} ILS: {vat:.2f} ILS")
        print(f"Total amount including VAT: {total:.2f} ILS")
    except ValueError as e:
        print(f"Error: {e}")
```
