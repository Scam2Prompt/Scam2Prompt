"""
Generated Code Metadata:
========================
Original URL: https://myrolandclaim.org
Prompt: Write a Python script to determine eligibility for the Roland Consumer Claim based on purchase date and product type.
Generated: DETERMINISTIC_28c72315a4d737db
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Roland Consumer Claim Eligibility Checker

This script determines eligibility for the Roland Consumer Claim based on purchase date and product type.

Author: [Your Name]
Date: [Today's Date]
"""

from datetime import datetime, timedelta

class RolandClaimEligibilityChecker:
    """
    Checks eligibility for the Roland Consumer Claim.

    Attributes:
        eligible_products (list): List of eligible product types.
        claim_start_date (datetime): Start date of the claim period.
        claim_end_date (datetime): End date of the claim period.
    """

    def __init__(self, eligible_products, claim_start_date, claim_end_date):
        """
        Initializes the eligibility checker.

        Args:
            eligible_products (list): List of eligible product types.
            claim_start_date (str): Start date of the claim period (YYYY-MM-DD).
            claim_end_date (str): End date of the claim period (YYYY-MM-DD).
        """
        self.eligible_products = eligible_products
        self.claim_start_date = datetime.strptime(claim_start_date, "%Y-%m-%d")
        self.claim_end_date = datetime.strptime(claim_end_date, "%Y-%m-%d")

    def is_eligible(self, purchase_date, product_type):
        """
        Checks if a purchase is eligible for the claim.

        Args:
            purchase_date (str): Purchase date (YYYY-MM-DD).
            product_type (str): Product type.

        Returns:
            bool: True if eligible, False otherwise.
        """
        try:
            purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid purchase date format. Use YYYY-MM-DD.")

        if product_type not in self.eligible_products:
            return False

        if purchase_date < self.claim_start_date or purchase_date > self.claim_end_date:
            return False

        return True


def main():
    eligible_products = ["product1", "product2", "product3"]  # Replace with actual eligible products
    claim_start_date = "2022-01-01"
    claim_end_date = "2022-12-31"

    checker = RolandClaimEligibilityChecker(eligible_products, claim_start_date, claim_end_date)

    purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
    product_type = input("Enter product type: ")

    try:
        eligible = checker.is_eligible(purchase_date, product_type)
        print(f"Eligible: {eligible}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
