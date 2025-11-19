"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Generate a list of baby clothing and accessory products with their prices in Brazilian Real (BRL), similar to the product listings on Somos Corujas, and calculate the total cost of a shopping cart with 5 items.
Generated: DETERMINISTIC_8c3de7842181ded7
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    Represents a baby clothing or accessory product with name, price, and category.
    """
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - R${self.price:.2f} ({self.category})"


class ShoppingCart:
    """
    Manages a collection of products and calculates the total cost.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product: Product, quantity: int = 1):
        """
        Adds a product to the cart with specified quantity.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items.append((product, quantity))

    def calculate_total(self) -> float:
        """
        Calculates the total cost of items in the cart.
        """
        return sum(product.price * quantity for product, quantity in self.items)

    def __str__(self):
        return "\n".join(f"{product.name} x{quantity} - R${product.price * quantity:.2f}" 
                         for product, quantity in self.items)


def generate_sample_products() -> list[Product]:
    """
    Generates a list of sample baby products similar to Somos Corujas.
    """
    return [
        Product("Body manga longa algodão", 49.90, "Roupas"),
        Product("Conjunto de meias", 19.90, "Acessórios"),
        Product("Macacão com estampa", 89.90, "Roupas"),
        Product("Touca de bebê", 29.90, "Acessórios"),
        Product("Manta de algodão", 119.90, "Enxoval"),
        Product("Sapatinho de lã", 39.90, "Calçados"),
        Product("Babador conjunto 3 peças", 59.90, "Acessórios"),
        Product("Calça jeans infantil", 69.90, "Roupas")
    ]


def main():
    try:
        # Generate sample products
        products = generate_sample_products()
        
        # Create shopping cart and add 5 items
        cart = ShoppingCart()
        cart.add_item(products[0], 1)  # Body manga longa
        cart.add_item(products[2], 1)  # Macacão
        cart.add_item(products[3], 2)  # 2 Toupas
        cart.add_item(products[4], 1)  # Manta
        cart.add_item(products[6], 1)  # Babador
        
        # Display cart contents and total
        print("=== Carrinho de Compras ===")
        print(cart)
        print(f"\nTotal: R${cart.calculate_total():.2f}")
        
    except Exception as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
```
