"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a Python script to simulate the checkout process, including applying discount coupons and calculating installment payments, inspired by the "Insira seu cupom de desconto na página de finalização" feature on the "Dal Cortivo Pneus" site.
Generated: DETERMINISTIC_5af9311a9fd56a00
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class Checkout:
    """Class to simulate the checkout process."""

    def __init__(self):
        self.total_amount = decimal.Decimal('0.00')
        self.discount = decimal.Decimal('0.00')
        self.installment_options = {
            1: 0,
            3: 0.05,  # 5% interest for 3 installments
            6: 0.10,  # 10% interest for 6 installments
            12: 0.15  # 15% interest for 12 installments
        }

    def add_item(self, item_name, price):
        """Add an item price to the total amount."""
        if price < 0:
            raise ValueError("Item price cannot be negative.")
        self.total_amount += decimal.Decimal(price)

    def apply_coupon(self, coupon_code):
        """Apply a discount coupon to the total amount."""
        coupons = {
            'SAVE10': decimal.Decimal('0.10'),  # 10% off
            'SAVE20': decimal.Decimal('0.20'),  # 20% off
            'SAVE50': decimal.Decimal('0.50'),  # $50 off
        }

        if coupon_code in coupons:
            discount_amount = self.total_amount * coupons[coupon_code] if coupon_code in {'SAVE10', 'SAVE20'} else decimal.Decimal('50.00')
            self.discount += discount_amount
            self.total_amount -= min(discount_amount, self.total_amount)  # Ensure total does not go negative
        else:
            raise ValueError("Invalid coupon code.")

    def calculate_installments(self, months):
        """Calculate the installment payment based on selected months."""
        if months not in self.installment_options:
            raise ValueError("Invalid number of months for installment. Choose from: {}".format(list(self.installment_options.keys())))

        interest_rate = self.installment_options[months]
        total_due = self.total_amount * (1 + interest_rate)
        installment_amount = total_due / months
        return total_due, installment_amount

    def display_summary(self):
        """Display the summary of the checkout process."""
        print(f"Total Amount: ${self.total_amount:.2f}")
        print(f"Discount Applied: ${self.discount:.2f}")
        print(f"Final Amount: ${self.total_amount:.2f}")

def main():
    """Main function to run the checkout simulation."""
    checkout = Checkout()

    # Adding items to cart
    try:
        checkout.add_item("Tire A", 100.00)
        checkout.add_item("Tire B", 150.00)
        
        # Apply a discount coupon
        coupon = input("Enter your discount coupon: ")
        checkout.apply_coupon(coupon.strip().upper())
        
        # Display summary before installment calculation
        checkout.display_summary()

        # Calculate installments
        months = int(input("Enter number of months for installment (1, 3, 6, 12): "))
        total_due, installment_amount = checkout.calculate_installments(months)
        
        print(f"Total Due: ${total_due:.2f} over {months} months.")
        print(f"Monthly Installment: ${installment_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
