"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Generate code to create an e-commerce product listing page for lighting products, including fields for product name, price, discount percentage, installment options, and free shipping eligibility, as seen in the "Plafon Chess 4xe27 Biv Newline 171bt" example.
Generated: DETERMINISTIC_2cc94dbd9f5d8760
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_listing.py

class Product:
    def __init__(self, name, price, discount_percentage=0, 
                 installment_options=None, free_shipping_eligible=False):
        """
        Initialize a Product object.

        Args:
            name (str): Product name.
            price (float): Product price.
            discount_percentage (int, optional): Discount percentage. Defaults to 0.
            installment_options (list, optional): Installment options. Defaults to None.
            free_shipping_eligible (bool, optional): Free shipping eligibility. Defaults to False.
        """
        self.name = name
        self.price = price
        self.discount_percentage = discount_percentage
        self.installment_options = installment_options if installment_options else []
        self.free_shipping_eligible = free_shipping_eligible

    def calculate_discounted_price(self):
        """
        Calculate the discounted price.

        Returns:
            float: Discounted price.
        """
        return self.price * (1 - self.discount_percentage / 100)

    def __str__(self):
        """
        Return a string representation of the Product object.

        Returns:
            str: String representation.
        """
        return f"{self.name}: ${self.price:.2f}"

class InstallmentOption:
    def __init__(self, months, interest_rate):
        """
        Initialize an InstallmentOption object.

        Args:
            months (int): Number of months.
            interest_rate (float): Interest rate.
        """
        self.months = months
        self.interest_rate = interest_rate

    def calculate_monthly_payment(self, price):
        """
        Calculate the monthly payment.

        Args:
            price (float): Price.

        Returns:
            float: Monthly payment.
        """
        return price * (1 + self.interest_rate / 100) / self.months

    def __str__(self):
        """
        Return a string representation of the InstallmentOption object.

        Returns:
            str: String representation.
        """
        return f"{self.months} months, {self.interest_rate}% interest"

def create_product_listing(product):
    """
    Create a product listing.

    Args:
        product (Product): Product object.

    Returns:
        str: Product listing.
    """
    listing = f"**{product.name}**\n"
    listing += f"Price: ${product.price:.2f}\n"
    if product.discount_percentage > 0:
        listing += f"Discount: {product.discount_percentage}%\n"
        listing += f"Discounted Price: ${product.calculate_discounted_price():.2f}\n"
    if product.installment_options:
        listing += "Installment Options:\n"
        for i, option in enumerate(product.installment_options):
            monthly_payment = option.calculate_monthly_payment(product.price)
            listing += f"{i+1}. {option} - ${monthly_payment:.2f}/month\n"
    if product.free_shipping_eligible:
        listing += "Free Shipping Eligible\n"
    return listing

# Example usage:
if __name__ == "__main__":
    try:
        product = Product(
            "Plafon Chess 4xe27 Biv Newline 171bt",
            100.0,
            discount_percentage=10,
            installment_options=[
                InstallmentOption(3, 0),
                InstallmentOption(6, 5),
                InstallmentOption(12, 10)
            ],
            free_shipping_eligible=True
        )
        print(create_product_listing(product))
    except Exception as e:
        print(f"An error occurred: {e}")
```
