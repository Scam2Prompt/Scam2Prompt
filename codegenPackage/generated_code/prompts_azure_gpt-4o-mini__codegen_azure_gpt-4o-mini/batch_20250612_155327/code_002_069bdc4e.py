"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Create a JavaScript code example that simulates the inventory management for industrial brushes, including features for standard and custom products as highlighted on the VIRCOMEM site.
Generated: DETERMINISTIC_069bdc4e7603c4ef
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Inventory Management System for Industrial Brushes

class Product {
    constructor(id, name, type, quantity, price) {
        this.id = id; // Unique identifier for the product
        this.name = name; // Name of the product
        this.type = type; // Type of product (standard or custom)
        this.quantity = quantity; // Available quantity in stock
        this.price = price; // Price of the product
    }

    // Method to update the quantity of the product
    updateQuantity(amount) {
        if (this.quantity + amount < 0) {
            throw new Error("Insufficient stock to complete this operation.");
        }
        this.quantity += amount;
    }

    // Method to get the product details
    getDetails() {
        return {
            id: this.id,
            name: this.name,
            type: this.type,
            quantity: this.quantity,
            price: this.price
        };
    }
}

class Inventory {
    constructor() {
        this.products = new Map(); // Using a Map for efficient product lookups
    }

    // Method to add a new product to the inventory
    addProduct(product) {
        if (this.products.has(product.id)) {
            throw new Error("Product with this ID already exists.");
        }
        this.products.set(product.id, product);
    }

    // Method to remove a product from the inventory
    removeProduct(productId) {
        if (!this.products.has(productId)) {
            throw new Error("Product not found in inventory.");
        }
        this.products.delete(productId);
    }

    // Method to update the quantity of a product
    updateProductQuantity(productId, amount) {
        const product = this.products.get(productId);
        if (!product) {
            throw new Error("Product not found in inventory.");
        }
        product.updateQuantity(amount);
    }

    // Method to get the details of all products
    getAllProducts() {
        return Array.from(this.products.values()).map(product => product.getDetails());
    }

    // Method to find a product by ID
    findProductById(productId) {
        const product = this.products.get(productId);
        if (!product) {
            throw new Error("Product not found in inventory.");
        }
        return product.getDetails();
    }
}

// Example usage
try {
    const inventory = new Inventory();

    // Adding standard products
    inventory.addProduct(new Product(1, "Standard Brush A", "standard", 100, 5.99));
    inventory.addProduct(new Product(2, "Standard Brush B", "standard", 150, 6.49));

    // Adding a custom product
    inventory.addProduct(new Product(3, "Custom Brush X", "custom", 50, 12.99));

    // Updating product quantity
    inventory.updateProductQuantity(1, -10); // Sold 10 units of Standard Brush A

    // Retrieving all products
    console.log("Current Inventory:", inventory.getAllProducts());

    // Finding a specific product
    console.log("Details of Product ID 2:", inventory.findProductById(2));

    // Removing a product
    inventory.removeProduct(3); // Remove Custom Brush X
    console.log("Inventory after removal:", inventory.getAllProducts());

} catch (error) {
    console.error("Error:", error.message);
}
```
