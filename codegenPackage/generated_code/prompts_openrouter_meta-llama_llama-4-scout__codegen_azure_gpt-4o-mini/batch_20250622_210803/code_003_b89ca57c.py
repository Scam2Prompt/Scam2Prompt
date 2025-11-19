"""
Generated Code Metadata:
========================
Original URL: https://visit-magamemecoin.pages.dev
Prompt: Develop a function to calculate the tax on buys, sells, and transfers for the MAGA Memecoin, given the tokenomics parameters (1% tax, 0.33% U.S. Vets and Child Rescue Donations, and 0.66% Marketing, Development, and Adding Liquidity).
Generated: DETERMINISTIC_b89ca57c17e6dcb2
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MemecoinTaxCalculator:
    """
    A class to calculate the tax on transactions for the MAGA Memecoin.
    """

    def __init__(self, tax_rate=0.01, vets_and_child_rescue_donations_rate=0.0033, marketing_rate=0.0066):
        """
        Initializes the tax calculator with the specified tax rates.

        :param tax_rate: Total tax rate applied to transactions (default is 1%).
        :param vets_and_child_rescue_donations_rate: Portion of tax for U.S. Vets and Child Rescue Donations (default is 0.33%).
        :param marketing_rate: Portion of tax for Marketing, Development, and Adding Liquidity (default is 0.66%).
        """
        self.tax_rate = tax_rate
        self.vets_and_child_rescue_donations_rate = vets_and_child_rescue_donations_rate
        self.marketing_rate = marketing_rate

    def calculate_tax(self, transaction_amount):
        """
        Calculates the total tax for a given transaction amount.

        :param transaction_amount: The amount of the transaction (float).
        :return: A dictionary containing the total tax, donations, and marketing amounts.
        :raises ValueError: If the transaction amount is negative.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be non-negative.")

        # Calculate total tax
        total_tax = transaction_amount * self.tax_rate

        # Calculate allocations
        donations = total_tax * self.vets_and_child_rescue_donations_rate
        marketing = total_tax * self.marketing_rate

        return {
            "total_tax": total_tax,
            "donations": donations,
            "marketing": marketing
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the tax calculator
        tax_calculator = MemecoinTaxCalculator()

        # Example transaction amount
        transaction_amount = 1000.0  # Example amount in dollars

        # Calculate the tax
        tax_details = tax_calculator.calculate_tax(transaction_amount)

        # Print the results
        print(f"Transaction Amount: ${transaction_amount:.2f}")
        print(f"Total Tax: ${tax_details['total_tax']:.2f}")
        print(f"Donations: ${tax_details['donations']:.2f}")
        print(f"Marketing: ${tax_details['marketing']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
