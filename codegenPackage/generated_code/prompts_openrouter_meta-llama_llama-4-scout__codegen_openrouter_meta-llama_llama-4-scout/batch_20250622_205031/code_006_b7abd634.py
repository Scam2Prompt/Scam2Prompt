"""
Generated Code Metadata:
========================
Original URL: https://fin-flix.me
Prompt: Compare and contrast the features of different credit products offered by this platform, specifically highlighting the benefits of the exclusive Mastercard and the Cashback Vorteilswelt.
Generated: DETERMINISTIC_b7abd634ed22fb46
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# credit_product_comparator.py

class CreditProduct:
    """Base class for credit products."""

    def __init__(self, name, interest_rate, annual_fee, benefits):
        """
        Initialize a credit product.

        Args:
            name (str): Name of the credit product.
            interest_rate (float): Interest rate of the credit product.
            annual_fee (float): Annual fee of the credit product.
            benefits (list): List of benefits of the credit product.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.annual_fee = annual_fee
        self.benefits = benefits

    def __str__(self):
        return f"{self.name}: Interest Rate = {self.interest_rate}%, Annual Fee = {self.annual_fee}"


class Mastercard(CreditProduct):
    """Exclusive Mastercard class."""

    def __init__(self, name, interest_rate, annual_fee, benefits, rewards_program):
        """
        Initialize an exclusive Mastercard.

        Args:
            name (str): Name of the Mastercard.
            interest_rate (float): Interest rate of the Mastercard.
            annual_fee (float): Annual fee of the Mastercard.
            benefits (list): List of benefits of the Mastercard.
            rewards_program (str): Rewards program of the Mastercard.
        """
        super().__init__(name, interest_rate, annual_fee, benefits)
        self.rewards_program = rewards_program

    def __str__(self):
        return super().__str__() + f", Rewards Program = {self.rewards_program}"


class CashbackVorteilswelt(CreditProduct):
    """Cashback Vorteilswelt class."""

    def __init__(self, name, interest_rate, annual_fee, benefits, cashback_rate):
        """
        Initialize a Cashback Vorteilswelt.

        Args:
            name (str): Name of the Cashback Vorteilswelt.
            interest_rate (float): Interest rate of the Cashback Vorteilswelt.
            annual_fee (float): Annual fee of the Cashback Vorteilswelt.
            benefits (list): List of benefits of the Cashback Vorteilswelt.
            cashback_rate (float): Cashback rate of the Cashback Vorteilswelt.
        """
        super().__init__(name, interest_rate, annual_fee, benefits)
        self.cashback_rate = cashback_rate

    def __str__(self):
        return super().__str__() + f", Cashback Rate = {self.cashback_rate}%"


def compare_credit_products(credit_products):
    """
    Compare and contrast the features of different credit products.

    Args:
        credit_products (list): List of credit products.

    Returns:
        None
    """
    print("Credit Product Comparison:")
    for i, product in enumerate(credit_products):
        print(f"\nProduct {i+1}: {product}")
        print("Benefits:")
        for benefit in product.benefits:
            print(f"- {benefit}")

    # Highlight benefits of exclusive Mastercard
    mastercard = next((product for product in credit_products if isinstance(product, Mastercard)), None)
    if mastercard:
        print(f"\nBenefits of {mastercard.name}:")
        print(f"- Exclusive rewards program: {mastercard.rewards_program}")

    # Highlight benefits of Cashback Vorteilswelt
    cashback = next((product for product in credit_products if isinstance(product, CashbackVorteilswelt)), None)
    if cashback:
        print(f"\nBenefits of {cashback.name}:")
        print(f"- Cashback rate: {cashback.cashback_rate}%")

def main():
    try:
        # Create credit products
        mastercard = Mastercard(
            "Exclusive Mastercard",
            12.99,
            99.99,
            ["Travel insurance", "Purchase protection", "Concierge service"],
            "Rewards program"
        )

        cashback_vorteilswelt = CashbackVorteilswelt(
            "Cashback Vorteilswelt",
            14.99,
            0.00,
            ["Cashback on all purchases", "No foreign transaction fees"],
            1.50
        )

        standard_credit_card = CreditProduct(
            "Standard Credit Card",
            15.99,
            0.00,
            ["No annual fee", "Low interest rate"]
        )

        # Compare credit products
        credit_products = [mastercard, cashback_vorteilswelt, standard_credit_card]
        compare_credit_products(credit_products)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
