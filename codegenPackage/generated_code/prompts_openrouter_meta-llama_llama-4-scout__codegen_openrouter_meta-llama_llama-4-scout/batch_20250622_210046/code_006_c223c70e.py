"""
Generated Code Metadata:
========================
Original URL: https://compound.morpho.dev
Prompt: What are the terms of use for interacting with Morpho's markets, and how do they impact borrowing and supplying on the platform?
Generated: DETERMINISTIC_c223c70e1bb838c9
Batch ID: 20250622_210046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Terms of Use for Interacting with Morpho's Markets

class MorphoTermsOfUse:
    """
    This class outlines the terms of use for interacting with Morpho's markets.
    It provides information on how these terms impact borrowing and supplying on the platform.
    """

    def __init__(self):
        self.terms = {
            "borrowing": {
                "interest_rate": 0.05,  # 5% interest rate
                "liquidation_threshold": 0.8,  # 80% liquidation threshold
                "max_borrow_amount": 100000  # Maximum borrow amount
            },
            "supplying": {
                "interest_rate": 0.03,  # 3% interest rate
                "max_supply_amount": 500000  # Maximum supply amount
            }
        }

    def get_borrowing_terms(self):
        """
        Returns the terms of use for borrowing on Morpho's markets.

        Returns:
            dict: A dictionary containing the borrowing terms.
        """
        return self.terms["borrowing"]

    def get_supplying_terms(self):
        """
        Returns the terms of use for supplying on Morpho's markets.

        Returns:
            dict: A dictionary containing the supplying terms.
        """
        return self.terms["supplying"]

    def calculate_borrow_interest(self, borrow_amount, borrow_time):
        """
        Calculates the interest for borrowing on Morpho's markets.

        Args:
            borrow_amount (float): The amount borrowed.
            borrow_time (int): The time borrowed for in seconds.

        Returns:
            float: The interest for borrowing.

        Raises:
            ValueError: If borrow_amount or borrow_time is negative.
        """
        if borrow_amount < 0 or borrow_time < 0:
            raise ValueError("Borrow amount and borrow time must be non-negative.")

        borrowing_terms = self.get_borrowing_terms()
        interest_rate = borrowing_terms["interest_rate"]
        interest = borrow_amount * interest_rate * (borrow_time / 31536000)  # 31536000 seconds in a year
        return interest

    def calculate_supply_interest(self, supply_amount, supply_time):
        """
        Calculates the interest for supplying on Morpho's markets.

        Args:
            supply_amount (float): The amount supplied.
            supply_time (int): The time supplied for in seconds.

        Returns:
            float: The interest for supplying.

        Raises:
            ValueError: If supply_amount or supply_time is negative.
        """
        if supply_amount < 0 or supply_time < 0:
            raise ValueError("Supply amount and supply time must be non-negative.")

        supplying_terms = self.get_supplying_terms()
        interest_rate = supplying_terms["interest_rate"]
        interest = supply_amount * interest_rate * (supply_time / 31536000)  # 31536000 seconds in a year
        return interest


def main():
    try:
        morpho_terms = MorphoTermsOfUse()
        borrowing_terms = morpho_terms.get_borrowing_terms()
        supplying_terms = morpho_terms.get_supplying_terms()

        print("Borrowing Terms:")
        for term, value in borrowing_terms.items():
            print(f"{term.capitalize().replace('_', ' ')}: {value}")

        print("\nSupplying Terms:")
        for term, value in supplying_terms.items():
            print(f"{term.capitalize().replace('_', ' ')}: {value}")

        borrow_amount = 10000
        borrow_time = 31536000  # 1 year
        borrow_interest = morpho_terms.calculate_borrow_interest(borrow_amount, borrow_time)
        print(f"\nBorrow Interest for {borrow_amount} for {borrow_time} seconds: {borrow_interest}")

        supply_amount = 50000
        supply_time = 31536000  # 1 year
        supply_interest = morpho_terms.calculate_supply_interest(supply_amount, supply_time)
        print(f"Supply Interest for {supply_amount} for {supply_time} seconds: {supply_interest}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
