"""
Generated Code Metadata:
========================
Original URL: https://taniphones.com
Prompt: Develop a shopping cart system in JavaScript that mimics the "Shto ne Shporte" (Add to Cart) feature described on TaniPhone.com.
Generated: DETERMINISTIC_7f80b8cfc9455fcd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// shoppingCart.js

/**
 * Represents a product in the shopping cart.
 */
class Product {
  /**
   * Creates a new Product instance.
   * @param {number} id - Unique product ID.
   * @param {string} name - Product name.
   * @param {number} price - Product price.
   */
  constructor(id, name, price) {
    this.id = id;
    this.name = name;
    this.price = price;
  }
}

/**
 * Represents a shopping cart.
 */
class ShoppingCart {
  /**
   * Creates a new ShoppingCart instance.
   */
  constructor() {
    this.items = [];
  }

  /**
   * Adds a product to the shopping cart.
   * @param {Product} product - Product to add.
   * @throws {Error} If product is not provided or is invalid.
   */
  addToCart(product) {
    if (!product || !(product instanceof Product)) {
      throw new Error('Invalid product provided');
    }
    this.items.push(product);
  }

  /**
   * Removes a product from the shopping cart.
   * @param {number} productId - ID of the product to remove.
   * @throws {Error} If product ID is not provided or is invalid.
   */
  removeFromCart(productId) {
    if (typeof productId !== 'number' || productId <= 0) {
      throw new Error('Invalid product ID provided');
    }
    this.items = this.items.filter((item) => item.id !== productId);
  }

  /**
   * Updates the quantity of a product in the shopping cart.
   * @param {number} productId - ID of the product to update.
   * @param {number} quantity - New quantity of the product.
   * @throws {Error} If product ID or quantity is not provided or is invalid.
   */
  updateQuantity(productId, quantity) {
    if (typeof productId !== 'number' || productId <= 0) {
      throw new Error('Invalid product ID provided');
    }
    if (typeof quantity !== 'number' || quantity <= 0) {
      throw new Error('Invalid quantity provided');
    }
    const index = this.items.findIndex((item) => item.id === productId);
    if (index >= 0) {
      // For simplicity, we assume quantity is not actually stored,
      // and the product can be added multiple times instead.
      for (let i = 0; i < quantity - 1; i++) {
        this.addToCart(this.items.find((item) => item.id === productId));
      }
    }
  }

  /**
   * Calculates the total cost of products in the shopping cart.
   * @returns {number} Total cost.
   */
  calculateTotal() {
    return this.items.reduce((total, item) => total + item.price, 0);
  }

  /**
   * Displays the shopping cart contents.
   */
  displayCart() {
    console.log('Shopping Cart:');
    this.items.forEach((item) => {
      console.log(`${item.name} - ${item.price}`);
    });
    console.log(`Total: ${this.calculateTotal()}`);
  }
}

// Example usage:
function main() {
  const cart = new ShoppingCart();

  const product1 = new Product(1, 'iPhone', 999);
  const product2 = new Product(2, 'iPad', 799);

  try {
    cart.addToCart(product1);
    cart.addToCart(product2);
    cart.displayCart();

    cart.updateQuantity(1, 2);
    cart.displayCart();

    cart.removeFromCart(2);
    cart.displayCart();
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
