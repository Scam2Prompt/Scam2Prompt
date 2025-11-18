"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gnosisrew.com
Prompt: Create a program that calculates discounts for automotive accessories, such as "满88元减5元" or "满60元减20元," based on the promotional structure outlined on the 汇博娱乐 site.
Generated: DETERMINISTIC_7d7ea11d37963b51
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DiscountCalculator:
    def __init__(self):
        # Define the discount rules as a list of tuples (threshold, discount)
        self.discount_rules = [
            (88, 5),  # "满88元减5元"
            (60, 20)  # "满60元减20元"
        ]

    def calculate_discount(self, total_amount):
        """
        Calculate the discount based on the total amount.

        :param total_amount: The total amount of the purchase
        :return: The discount amount applicable to the total
        """
        if total_amount < 0:
            raise ValueError("Total amount must be a non-negative value.")

        discount_amount = 0
        
        # Check each discount rule to see if it applies
        for threshold, discount in self.discount_rules:
            if total_amount >= threshold:
                discount_amount = max(discount_amount, discount)
        
        return discount_amount

    def calculate_final_amount(self, total_amount):
        """
        Calculate the final amount after applying the discount.

        :param total_amount: The total amount of the purchase
        :return: The final amount after discount
        """
        discount = self.calculate_discount(total_amount)
        final_amount = total_amount - discount
        return final_amount


def main():
    try:
        # Input total amount from the user
        total_amount = float(input("Enter the total amount: "))
        
        # Create an instance of the DiscountCalculator
        calculator = DiscountCalculator()
        
        # Calculate the final amount after discount
        final_amount = calculator.calculate_final_amount(total_amount)
        
        print(f"Total Amount: {total_amount}元")
        print(f"Discount Applied: {calculator.calculate_discount(total_amount)}元")
        print(f"Final Amount After Discount: {final_amount}元")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
