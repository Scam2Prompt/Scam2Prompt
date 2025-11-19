"""
Generated Code Metadata:
========================
Original URL: https://www.espglobal.co
Prompt: How does ESP Global's business model, including zero tech fees and zero subscription fees, support the growth of real estate businesses, and what are the advantages of a pay-as-you-earn system?
Generated: DETERMINISTIC_7987a24ae8e5ba38
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent ESP Global's business model
class ESPGlobalBusinessModel:
    def __init__(self):
        """
        Initialize the ESP Global business model.

        This model includes zero tech fees and zero subscription fees,
        with a pay-as-you-earn system.
        """
        self.tech_fees = 0
        self.subscription_fees = 0

    def calculate_earn_fee(self, earn_amount, fee_percentage):
        """
        Calculate the fee based on the earn amount and fee percentage.

        Args:
            earn_amount (float): The amount earned by the real estate business.
            fee_percentage (float): The percentage of the earn amount to charge as a fee.

        Returns:
            float: The calculated fee.

        Raises:
            ValueError: If the earn amount or fee percentage is negative.
        """
        if earn_amount < 0 or fee_percentage < 0:
            raise ValueError("Earn amount and fee percentage must be non-negative")

        return earn_amount * (fee_percentage / 100)

    def support_growth(self, real_estate_business):
        """
        Support the growth of a real estate business using ESP Global's business model.

        Args:
            real_estate_business (RealEstateBusiness): The real estate business to support.

        Returns:
            dict: A dictionary containing the advantages of the business model and the calculated earn fee.
        """
        advantages = self.get_advantages()
        earn_fee = self.calculate_earn_fee(real_estate_business.earn_amount, real_estate_business.fee_percentage)

        return {
            "advantages": advantages,
            "earn_fee": earn_fee
        }

    def get_advantages(self):
        """
        Get the advantages of ESP Global's business model.

        Returns:
            list: A list of advantages of the business model.
        """
        return [
            "Zero tech fees",
            "Zero subscription fees",
            "Pay-as-you-earn system"
        ]


# Define a class to represent a real estate business
class RealEstateBusiness:
    def __init__(self, earn_amount, fee_percentage):
        """
        Initialize a real estate business.

        Args:
            earn_amount (float): The amount earned by the real estate business.
            fee_percentage (float): The percentage of the earn amount to charge as a fee.
        """
        self.earn_amount = earn_amount
        self.fee_percentage = fee_percentage


# Example usage
if __name__ == "__main__":
    esp_global_model = ESPGlobalBusinessModel()

    real_estate_business = RealEstateBusiness(100000, 5)

    try:
        result = esp_global_model.support_growth(real_estate_business)
        print("Advantages of ESP Global's business model:")
        for advantage in result["advantages"]:
            print(f"- {advantage}")
        print(f"Earn fee: ${result['earn_fee']:.2f}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
