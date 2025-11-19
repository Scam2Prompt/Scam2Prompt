"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write a JavaScript function to create a shopping cart system for an e-commerce website selling electronic components, with features like cart tracking and order management.
Generated: DETERMINISTIC_fd1a127d8b9a41c7
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Shopping Cart System for an E-commerce Website
 * Features:
 * - Add items to the cart
 * - Remove items from the cart
 * - View cart contents
 * - Calculate total price
 * - Place an order
 */

// Shopping Cart Class
class ShoppingCart {
  constructor() {
    this.cart = []; // Array to store cart items
  }

  /**
   * Add an item to the cart
   * @param {string} itemName - Name of the item
   * @param {number} price - Price of the item
   * @param {number} quantity - Quantity of the item
   */
  addItem(itemName, price, quantity = 1) {
    if (!itemName || price <= 0 || quantity <= 0) {
      throw new Error("Invalid item details provided.");
    }

    // Check if the item already exists in the cart
    const existingItem = this.cart.find((item) => item.name === itemName);
    if (existingItem) {
      existingItem.quantity += quantity; // Update quantity if item exists
    } else {
      this.cart.push({ name: itemName, price, quantity }); // Add new item
    }
  }

  /**
   * Remove an item from the cart
   * @param {string} itemName - Name of the item to remove
   */
  removeItem(itemName) {
    const itemIndex = this.cart.findIndex((item) => item.name === itemName);
    if (itemIndex === -1) {
      throw new Error("Item not found in the cart.");
    }
    this.cart.splice(itemIndex, 1); // Remove item from the cart
  }

  /**
   * View the contents of the cart
   * @returns {Array} - Array of cart items
   */
  viewCart() {
    return this.cart.map((item) => ({
      name: item.name,
      price: item.price,
      quantity: item.quantity,
      total: item.price * item.quantity,
    }));
  }

  /**
   * Calculate the total price of items in the cart
   * @returns {number} - Total price
   */
  calculateTotal() {
    return this.cart.reduce((total, item) => total + item.price * item.quantity, 0);
  }

  /**
   * Place an order
   * @returns {Object} - Order summary
   */
  placeOrder() {
    if (this.cart.length === 0) {
      throw new Error("Cannot place an order with an empty cart.");
    }

    const orderSummary = {
      items: this.viewCart(),
      totalPrice: this.calculateTotal(),
      orderDate: new Date().toISOString(),
    };

    // Clear the cart after placing the order
    this.cart = [];
    return orderSummary;
  }
}

// Example Usage
try {
  const cart = new ShoppingCart();

  // Add items to the cart
  cart.addItem("Resistor", 0.5, 10);
  cart.addItem("Capacitor", 1.2, 5);
  cart.addItem("Microcontroller", 15.0, 1);

  // View cart contents
  console.log("Cart Contents:", cart.viewCart());

  // Calculate total price
  console.log("Total Price:", cart.calculateTotal());

  // Remove an item
  cart.removeItem("Capacitor");

  // Place an order
  const order = cart.placeOrder();
  console.log("Order Summary:", order);
} catch (error) {
  console.error("Error:", error.message);
}
```
