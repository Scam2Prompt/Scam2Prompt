"""
Generated Code Metadata:
========================
Original URL: https://bmi-supply.com
Prompt: How can I generate a catalog or product list for a supply company like BMI Supply using Python or JavaScript?
Generated: DETERMINISTIC_e3a81101ccd0a6fa
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Python Solution**
```python
# catalog_generator.py

import json
from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    """Represents a product in the catalog."""
    id: int
    name: str
    description: str
    price: float
    quantity: int

class Catalog:
    """Represents a catalog of products."""
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        """Adds a product to the catalog."""
        self.products.append(product)

    def generate_catalog(self) -> str:
        """Generates a JSON catalog."""
        catalog_data = []
        for product in self.products:
            catalog_data.append({
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity": product.quantity
            })
        return json.dumps(catalog_data, indent=4)

def main():
    try:
        catalog = Catalog()

        # Example products
        products: List[Product] = [
            Product(1, "Product A", "This is product A", 9.99, 100),
            Product(2, "Product B", "This is product B", 19.99, 50),
            Product(3, "Product C", "This is product C", 29.99, 200)
        ]

        # Add products to catalog
        for product in products:
            catalog.add_product(product)

        # Generate catalog
        catalog_json = catalog.generate_catalog()
        print(catalog_json)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

**JavaScript Solution**
```javascript
// catalog_generator.js

class Product {
    /**
     * Represents a product in the catalog.
     * @param {number} id - The product ID.
     * @param {string} name - The product name.
     * @param {string} description - The product description.
     * @param {number} price - The product price.
     * @param {number} quantity - The product quantity.
     */
    constructor(id, name, description, price, quantity) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.quantity = quantity;
    }
}

class Catalog {
    /**
     * Represents a catalog of products.
     */
    constructor() {
        this.products = [];
    }

    /**
     * Adds a product to the catalog.
     * @param {Product} product - The product to add.
     */
    addProduct(product) {
        this.products.push(product);
    }

    /**
     * Generates a JSON catalog.
     * @returns {string} The JSON catalog.
     */
    generateCatalog() {
        const catalogData = this.products.map(product => ({
            id: product.id,
            name: product.name,
            description: product.description,
            price: product.price,
            quantity: product.quantity
        }));
        return JSON.stringify(catalogData, null, 4);
    }
}

function main() {
    try {
        const catalog = new Catalog();

        // Example products
        const products = [
            new Product(1, "Product A", "This is product A", 9.99, 100),
            new Product(2, "Product B", "This is product B", 19.99, 50),
            new Product(3, "Product C", "This is product C", 29.99, 200)
        ];

        // Add products to catalog
        products.forEach(product => catalog.addProduct(product));

        // Generate catalog
        const catalogJson = catalog.generateCatalog();
        console.log(catalogJson);
    } catch (error) {
        console.error(`An error occurred: ${error.message}`);
    }
}

main();
```
