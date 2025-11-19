"""
Generated Code Metadata:
========================
Original URL: https://tiburonfishingreels.com
Prompt: Write JavaScript code to implement a dynamic shopping cart system for TiburonFishingReels.com, allowing users to add items like reel clamps and fasteners while updating the total cost in real-time.
Generated: DETERMINISTIC_55f48fb097d1f425
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// shoppingCart.js

class Product {
  /**
   * Represents a product in the shopping cart.
   * @param {number} id - Unique product ID.
   * @param {string} name - Product name.
   * @param {number} price - Product price.
   * @param {number} quantity - Product quantity.
   */
  constructor(id, name, price, quantity = 1) {
    this.id = id;
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }
}

class ShoppingCart {
  /**
   * Represents a shopping cart.
   */
  constructor() {
    this.products = [];
    this.totalCost = 0;
  }

  /**
   * Adds a product to the shopping cart.
   * @param {Product} product - Product to add.
   */
  addProduct(product) {
    const existingProduct = this.products.find((p) => p.id === product.id);
    if (existingProduct) {
      existingProduct.quantity += product.quantity;
    } else {
      this.products.push(product);
    }
    this.updateTotalCost();
  }

  /**
   * Removes a product from the shopping cart.
   * @param {number} id - ID of the product to remove.
   */
  removeProduct(id) {
    this.products = this.products.filter((product) => product.id !== id);
    this.updateTotalCost();
  }

  /**
   * Updates the quantity of a product in the shopping cart.
   * @param {number} id - ID of the product to update.
   * @param {number} quantity - New quantity.
   */
  updateQuantity(id, quantity) {
    const product = this.products.find((p) => p.id === id);
    if (product) {
      product.quantity = quantity;
      if (product.quantity <= 0) {
        this.removeProduct(id);
      }
    }
    this.updateTotalCost();
  }

  /**
   * Updates the total cost of the shopping cart.
   */
  updateTotalCost() {
    this.totalCost = this.products.reduce((acc, product) => acc + product.price * product.quantity, 0);
  }

  /**
   * Clears the shopping cart.
   */
  clearCart() {
    this.products = [];
    this.totalCost = 0;
  }
}

// Example usage:
class App {
  constructor() {
    this.cart = new ShoppingCart();
  }

  renderCart() {
    console.log("Shopping Cart:");
    this.cart.products.forEach((product) => {
      console.log(`${product.name} x${product.quantity} = $${(product.price * product.quantity).toFixed(2)}`);
    });
    console.log(`Total: $${this.cart.totalCost.toFixed(2)}`);
  }

  run() {
    try {
      const reelClamp = new Product(1, "Reel Clamp", 9.99);
      const fastener = new Product(2, "Fastener", 4.99, 2);

      this.cart.addProduct(reelClamp);
      this.cart.addProduct(fastener);
      this.renderCart();

      this.cart.updateQuantity(1, 2);
      this.renderCart();

      this.cart.removeProduct(2);
      this.renderCart();

      this.cart.clearCart();
      this.renderCart();
    } catch (error) {
      console.error("Error:", error.message);
    }
  }
}

const app = new App();
app.run();
```
