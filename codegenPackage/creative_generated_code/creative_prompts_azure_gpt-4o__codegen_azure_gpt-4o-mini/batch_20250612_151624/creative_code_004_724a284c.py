"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesks.info
Prompt: Develop a function to calculate the final payment amount for a shopping cart on FirstCry.com, considering discounts, shipping charges, and estimated GST.
Generated: DETERMINISTIC_724a284c54204cb4
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount = 0.0
        self.shipping_charge = 0.0
        self.gst_rate = 0.18  # GST is 18%

    def add_item(self, item_price, quantity):
        """
        Adds an item to the shopping cart.

        :param item_price: Price of the item
        :param quantity: Number of items to add
        """
        if item_price < 0 or quantity < 0:
            raise ValueError("Item price and quantity must be non-negative.")
        self.items.append((item_price, quantity))

    def set_discount(self, discount):
        """
        Sets the discount for the shopping cart.

        :param discount: Discount amount to be applied
        """
        if discount < 0:
            raise ValueError("Discount must be non-negative.")
        self.discount = discount

    def set_shipping_charge(self, shipping_charge):
        """
        Sets the shipping charge for the shopping cart.

        :param shipping_charge: Shipping charge to be applied
        """
        if shipping_charge < 0:
            raise ValueError("Shipping charge must be non-negative.")
        self.shipping_charge = shipping_charge

    def calculate_total(self):
        """
        Calculates the total amount of the shopping cart before applying discounts, GST, and shipping.

        :return: Total amount before additional charges
        """
        total_amount = sum(price * quantity for price, quantity in self.items)
        return total_amount

    def calculate_final_amount(self):
        """
        Calculates the final payment amount after applying discounts, shipping charges, and GST.

        :return: Final payment amount
        """
        try:
            total_amount = self.calculate_total()

            # Apply the discount
            discounted_amount = total_amount - self.discount
            if discounted_amount < 0:
                discounted_amount = 0  # Ensure the amount doesn't go negative

            # Calculate GST on the discounted amount
            gst_amount = discounted_amount * self.gst_rate

            # Calculate final amount
            final_amount = discounted_amount + gst_amount + self.shipping_charge
            
            return round(final_amount, 2)  # Round to 2 decimal places for currency formatting

        except Exception as e:
            raise RuntimeError("Error while calculating final payment amount: " + str(e))


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(100.0, 2)  # Adding 2 items each costing 100.0
    cart.add_item(50.0, 1)    # Adding 1 item costing 50.0
    cart.set_discount(20.0)   # Setting a discount of 20.0
    cart.set_shipping_charge(15.0)  # Setting shipping charge of 15.0

    try:
        final_payment = cart.calculate_final_amount()
        print(f"The final payment amount is: ₹{final_payment}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
