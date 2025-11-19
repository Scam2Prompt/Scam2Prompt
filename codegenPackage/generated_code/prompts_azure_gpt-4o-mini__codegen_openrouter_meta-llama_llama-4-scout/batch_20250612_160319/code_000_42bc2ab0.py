"""
Generated Code Metadata:
========================
Original URL: https://suplementosdeaz.blogspot.com
Prompt: Generate a code snippet to create an e-commerce product listing for "Creatina Hardcore" from Integralmédica, including price and payment options.
Generated: DETERMINISTIC_42bc2ab0a93ae7e0
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_product_listing.py

class Product:
    def __init__(self, name, price, description, brand):
        """
        Initialize a Product object.

        Args:
            name (str): Product name.
            price (float): Product price.
            description (str): Product description.
            brand (str): Product brand.
        """
        self.name = name
        self.price = price
        self.description = description
        self.brand = brand

class PaymentOption:
    def __init__(self, name, description):
        """
        Initialize a PaymentOption object.

        Args:
            name (str): Payment option name.
            description (str): Payment option description.
        """
        self.name = name
        self.description = description

class ECommerceProductListing:
    def __init__(self, product, payment_options):
        """
        Initialize an ECommerceProductListing object.

        Args:
            product (Product): Product object.
            payment_options (list[PaymentOption]): List of payment options.
        """
        self.product = product
        self.payment_options = payment_options

    def display_product_listing(self):
        """
        Display the product listing.
        """
        print(f"**{self.product.name}** by {self.product.brand}")
        print(f"Price: R${self.product.price:.2f}")
        print(self.product.description)
        print("**Payment Options:**")
        for i, option in enumerate(self.payment_options, start=1):
            print(f"{i}. {option.name} - {option.description}")

def main():
    try:
        # Create product
        product = Product(
            name="Creatina Hardcore",
            price=99.90,
            description="Suplemento de creatina para atletas de alto desempenho.",
            brand="Integralmédica"
        )

        # Create payment options
        payment_options = [
            PaymentOption("Boleto Bancário", "Pagamento com boleto bancário"),
            PaymentOption("Cartão de Crédito", "Pagamento com cartão de crédito"),
            PaymentOption("Transferência Bancária", "Pagamento com transferência bancária")
        ]

        # Create e-commerce product listing
        product_listing = ECommerceProductListing(product, payment_options)

        # Display product listing
        product_listing.display_product_listing()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
