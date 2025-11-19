"""
Generated Code Metadata:
========================
Original URL: https://familyicon.ru
Prompt: "Write a code snippet in JavaScript to implement a simple e-commerce functionality for a religious item store, focusing on product categorization and shopping cart management, inspired by the structure of https://familyicon.ru."
Generated: DETERMINISTIC_b7af32ae34941666
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// E-commerce functionality for a religious item store

// Product class to represent individual items
class Product {
  constructor(id, name, category, price) {
    this.id = id; // Unique identifier for the product
    this.name = name; // Name of the product
    this.category = category; // Category of the product (e.g., Icons, Candles, Books)
    this.price = price; // Price of the product
  }
}

// ShoppingCart class to manage cart operations
class ShoppingCart {
  constructor() {
    this.items = []; // Array to store items in the cart
  }

  // Add a product to the cart
  addProduct(product, quantity = 1) {
    if (quantity <= 0) {
      console.error("Quantity must be greater than zero.");
      return;
    }

    const existingItem = this.items.find((item) => item.product.id === product.id);
    if (existingItem) {
      existingItem.quantity += quantity; // Update quantity if product already exists in the cart
    } else {
      this.items.push({ product, quantity }); // Add new product to the cart
    }
    console.log(`${product.name} added to the cart.`);
  }

  // Remove a product from the cart
  removeProduct(productId) {
    const index = this.items.findIndex((item) => item.product.id === productId);
    if (index !== -1) {
      const removedItem = this.items.splice(index, 1);
      console.log(`${removedItem[0].product.name} removed from the cart.`);
    } else {
      console.error("Product not found in the cart.");
    }
  }

  // Calculate the total price of items in the cart
  calculateTotal() {
    return this.items.reduce((total, item) => total + item.product.price * item.quantity, 0);
  }

  // Display the contents of the cart
  displayCart() {
    if (this.items.length === 0) {
      console.log("Your cart is empty.");
      return;
    }

    console.log("Shopping Cart:");
    this.items.forEach((item) => {
      console.log(
        `- ${item.product.name} (Category: ${item.product.category}, Price: $${item.product.price}) x ${item.quantity}`
      );
    });
    console.log(`Total: $${this.calculateTotal().toFixed(2)}`);
  }
}

// Example usage
try {
  // Create some products
  const icon = new Product(1, "Saint Nicholas Icon", "Icons", 25.99);
  const candle = new Product(2, "Church Candle", "Candles", 5.49);
  const book = new Product(3, "Orthodox Prayer Book", "Books", 15.99);

  // Create a shopping cart
  const cart = new ShoppingCart();

  // Add products to the cart
  cart.addProduct(icon, 2);
  cart.addProduct(candle, 5);
  cart.addProduct(book);

  // Display the cart
  cart.displayCart();

  // Remove a product from the cart
  cart.removeProduct(2);

  // Display the cart again
  cart.displayCart();
} catch (error) {
  console.error("An error occurred:", error.message);
}
```
