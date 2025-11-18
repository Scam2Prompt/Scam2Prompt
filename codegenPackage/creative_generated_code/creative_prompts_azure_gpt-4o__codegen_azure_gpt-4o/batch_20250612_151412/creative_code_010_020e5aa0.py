"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Create a Python script to calculate the benefits of Klar Plus membership, including cashback, promotions, and exclusive features.
Generated: DETERMINISTIC_020e5aa06b9b3a1a
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the benefits of Klar Plus membership

class KlarPlusMembership:
    """
    A class to represent the benefits of Klar Plus membership.
    It allows calculating cashback, promotional discounts, 
    and other exclusive benefits based on user spending.
    """

    def __init__(self, monthly_fee, cashback_rate, promo_discount_rate):
        """
        Initialize Klar Plus membership attributes.
        
        :param monthly_fee: Cost of the Klar Plus monthly membership
        :param cashback_rate: Percentage of cashback on eligible spending (e.g., 0.03 for 3%)
        :param promo_discount_rate: Percentage discount on promotional offers (e.g., 0.10 for 10%)
        """
        self.monthly_fee = monthly_fee
        self.cashback_rate = cashback_rate
        self.promo_discount_rate = promo_discount_rate

    def calculate_cashback(self, eligible_spending):
        """
        Calculate the cashback benefit based on eligible spending.
        
        :param eligible_spending: Total eligible spending for cashback
        :return: Cashback amount
        """
        try:
            if eligible_spending < 0:
                raise ValueError("Eligible spending cannot be negative.")
            return eligible_spending * self.cashback_rate
        except TypeError:
            raise TypeError("Eligible spending must be a numeric value.")

    def calculate_promo_savings(self, promo_spending):
        """
        Calculate the savings from promotional discounts.
        
        :param promo_spending: Total spending on promotion-eligible items
        :return: Savings amount
        """
        try:
            if promo_spending < 0:
                raise ValueError("Promotional spending cannot be negative.")
            return promo_spending * self.promo_discount_rate
        except TypeError:
            raise TypeError("Promotional spending must be a numeric value.")

    def calculate_total_benefits(self, eligible_spending, promo_spending):
        """
        Calculate the total benefits provided by Klar Plus membership.
        
        :param eligible_spending: Spending eligible for cashback
        :param promo_spending: Spending eligible for promotional discounts
        :return: Total benefits (cashback + promo savings - membership fee)
        """
        try:
            cashback = self.calculate_cashback(eligible_spending)
            promo_savings = self.calculate_promo_savings(promo_spending)
            total_benefits = cashback + promo_savings - self.monthly_fee
            return total_benefits
        except Exception as e:
            raise RuntimeError(f"Error calculating total benefits: {str(e)}")


def main():
    """
    Main function to interact with the user and calculate Klar Plus benefits.
    """
    print("Welcome to the Klar Plus Benefits Calculator!")

    try:
        # Input monthly fee, cashback rate, and promo discount rate
        monthly_fee = float(input("Enter the monthly fee for Klar Plus membership: "))
        cashback_rate = float(input("Enter the cashback rate (e.g., 0.03 for 3%): "))
        promo_discount_rate = float(input("Enter the promotional discount rate (e.g., 0.10 for 10%): "))

        # Create an instance of KlarPlusMembership
        klar_plus = KlarPlusMembership(monthly_fee, cashback_rate, promo_discount_rate)

        # Input user spending
        eligible_spending = float(input("Enter your total eligible spending for cashback: "))
        promo_spending = float(input("Enter your total promotional spending: "))

        # Calculate total benefits
        total_benefits = klar_plus.calculate_total_benefits(eligible_spending, promo_spending)
        
        # Output results
        print("\n=== Klar Plus Benefits Summary ===")
        print(f"Cashback Earned: ${klar_plus.calculate_cashback(eligible_spending):.2f}")
        print(f"Promotional Savings: ${klar_plus.calculate_promo_savings(promo_spending):.2f}")
        print(f"Monthly Membership Fee: ${monthly_fee:.2f}")
        print(f"Total Benefits (Net): ${total_benefits:.2f}")

        if total_benefits > 0:
            print("Klar Plus membership is beneficial for you!")
        else:
            print("Klar Plus membership may not be worth it based on your current spending.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
