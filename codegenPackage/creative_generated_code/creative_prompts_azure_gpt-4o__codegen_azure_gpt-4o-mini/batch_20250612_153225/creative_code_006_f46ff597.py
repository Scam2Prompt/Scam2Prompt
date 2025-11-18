"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Write code to implement a shopping cart system in Django that supports multiple product variants and calculates discounts for pre-orders, similar to MorevaCare's functionality.
Generated: DETERMINISTIC_f46ff597ee890314
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary Django modules
from django.db import models
from django.core.exceptions import ValidationError

# Define a model for Product Variants
class ProductVariant(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    is_preorder = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def clean(self):
        # Ensure that discount_percentage is between 0 and 100
        if self.discount_percentage < 0 or self.discount_percentage > 100:
            raise ValidationError('Discount percentage must be between 0 and 100.')

    def get_discounted_price(self):
        """
        Calculate the price after applying the discount.
        :return: Discounted price
        """
        return self.price * (1 - (self.discount_percentage / 100))

    def __str__(self):
        return f"{self.name} - ${self.price} (Preorder: {self.is_preorder})"


# Define a model for the Shopping Cart
class ShoppingCart(models.Model):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def clean(self):
        # Ensure that quantity is positive and not greater than available stock
        if self.quantity <= 0:
            raise ValidationError('Quantity must be a positive integer.')
        if self.quantity > self.product_variant.stock_quantity:
            raise ValidationError('Quantity exceeds available stock.')

    def total_price(self):
        """
        Calculate the total price of the items in the cart.
        :return: Total price
        """
        return self.product_variant.get_discounted_price() * self.quantity

    def __str__(self):
        return f"Cart Item: {self.product_variant.name} x {self.quantity}"


# Define a model for the Order
class Order(models.Model):
    cart_items = models.ManyToManyField(ShoppingCart)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def calculate_order_total(self):
        """
        Calculate the total price for the order based on cart items.
        :return: Total order price
        """
        total = sum(item.total_price() for item in self.cart_items.all())
        self.order_total = total
        self.save()

    def __str__(self):
        return f"Order Total: ${self.order_total}"


# Example usage of models (to be done in views or management commands)
def example_usage():
    try:
        # Create a product variant
        variant = ProductVariant.objects.create(name="Sample Product", price=100.00, stock_quantity=10, 
                                                is_preorder=True, discount_percentage=10.0)

        # Create a shopping cart item
        cart_item = ShoppingCart.objects.create(product_variant=variant, quantity=2)

        # Create an order and calculate the total
        order = Order.objects.create()
        order.cart_items.add(cart_item)
        order.calculate_order_total()

        print(order)

    except ValidationError as e:
        print(f"Validation Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ensure to run example_usage in appropriate context, e.g., through a Django view or shell.
```
