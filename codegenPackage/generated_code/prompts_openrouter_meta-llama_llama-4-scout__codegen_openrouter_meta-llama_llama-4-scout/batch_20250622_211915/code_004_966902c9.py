"""
Generated Code Metadata:
========================
Original URL: https://poocoinswapse.blogspot.com
Prompt: Develop a product catalog entry for a new style of tenis de corrida for men.
Generated: DETERMINISTIC_966902c931419f68
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

class Product:
    def __init__(self, product_id, name, description, price, size_options, color_options):
        """
        Initialize a Product object.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            size_options (list): List of available sizes.
            color_options (list): List of available colors.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.size_options = size_options
        self.color_options = color_options

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"

    def get_product_info(self):
        """
        Return a dictionary containing product information.

        Returns:
            dict: Product information.
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "size_options": self.size_options,
            "color_options": self.color_options
        }


class TennisShoes(Product):
    def __init__(self, product_id, name, description, price, size_options, color_options, material, technology):
        """
        Initialize a TennisShoes object.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            size_options (list): List of available sizes.
            color_options (list): List of available colors.
            material (str): Material used to make the shoes.
            technology (str): Technology used in the shoes.
        """
        super().__init__(product_id, name, description, price, size_options, color_options)
        self.material = material
        self.technology = technology

    def get_product_info(self):
        """
        Return a dictionary containing tennis shoes product information.

        Returns:
            dict: Tennis shoes product information.
        """
        product_info = super().get_product_info()
        product_info["material"] = self.material
        product_info["technology"] = self.technology
        return product_info


def create_tennis_de_corrida(product_id, name, description, price, size_options, color_options, material, technology):
    """
    Create a new tennis de corrida product.

    Args:
        product_id (int): Unique product identifier.
        name (str): Product name.
        description (str): Product description.
        price (float): Product price.
        size_options (list): List of available sizes.
        color_options (list): List of available colors.
        material (str): Material used to make the shoes.
        technology (str): Technology used in the shoes.

    Returns:
        TennisShoes: Tennis de corrida product.
    """
    try:
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if not size_options or not color_options:
            raise ValueError("Size options and color options must not be empty.")
        product = TennisShoes(product_id, name, description, price, size_options, color_options, material, technology)
        return product
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    product_id = 12345
    name = "Tenis de Corrida X500"
    description = "Tenis de corrida para homens, leve e confortável."
    price = 129.99
    size_options = ["39", "40", "41", "42", "43"]
    color_options = ["Preto", "Branco", "Vermelho"]
    material = "Borracha e tecido sintético"
    technology = "Amortecimento de impacto"

    product = create_tennis_de_corrida(product_id, name, description, price, size_options, color_options, material, technology)
    if product:
        print(product)
        print(product.get_product_info())


if __name__ == "__main__":
    main()
```
