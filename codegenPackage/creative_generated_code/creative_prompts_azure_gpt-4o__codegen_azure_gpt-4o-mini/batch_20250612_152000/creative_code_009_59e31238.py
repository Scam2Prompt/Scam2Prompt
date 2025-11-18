"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a function to calculate total costs for products like "OLEO DE MOTOR 2100 PROTECT+ 10W30" and "CAPACETE PARA BIKE WILD," including discounts or taxes, referencing "autopecasbrazz."
Generated: DETERMINISTIC_59e312385b98db4c
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """
    A class to represent a product with its details.
    """

    def __init__(self, name, price, quantity, discount=0, tax=0):
        """
        Initializes a new product instance.

        :param name: The name of the product.
        :param price: The price per unit of the product.
        :param quantity: The quantity of the product.
        :param discount: The discount percentage on the product.
        :param tax: The tax percentage on the product.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.tax = tax

    def calculate_total(self):
        """
        Calculates the total cost for the product including discounts and taxes.

        :return: The total cost after applying discount and adding tax.
        """
        try:
            # Calculate total before discount
            total_price = self.price * self.quantity
            
            # Apply discount
            discount_amount = total_price * (self.discount / 100)
            total_price_after_discount = total_price - discount_amount

            # Apply tax
            tax_amount = total_price_after_discount * (self.tax / 100)
            total_cost = total_price_after_discount + tax_amount
            
            return round(total_cost, 2)  # Round to 2 decimal places for currency
            
        except Exception as e:
            raise ValueError(f"Error calculating total cost for {self.name}: {str(e)}")


def calculate_total_costs(products):
    """
    Calculates the total costs for a list of products.

    :param products: A list of Product instances.
    :return: The total cost for all products.
    """
    total_cost = 0
    
    for product in products:
        try:
            total_cost += product.calculate_total()
        except ValueError as e:
            print(e)  # Log the error message
            
    return round(total_cost, 2)  # Round to 2 decimal places for currency


# Example usage:
if __name__ == "__main__":
    # Create a list of products
    products = [
        Product(name="OLEO DE MOTOR 2100 PROTECT+ 10W30", price=150.00, quantity=2, discount=10, tax=5),
        Product(name="CAPACETE PARA BIKE WILD", price=200.00, quantity=1, discount=0, tax=15)
    ]

    # Calculate total costs for the products
    try:
        total_cost = calculate_total_costs(products)
        print(f"Total cost for products: R$ {total_cost}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
