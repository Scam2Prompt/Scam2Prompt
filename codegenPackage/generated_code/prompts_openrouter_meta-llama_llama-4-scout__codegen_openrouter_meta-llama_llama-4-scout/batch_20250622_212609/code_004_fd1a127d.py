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
// shoppingCart.js

/**
 * Represents an electronic component.
 */
class Component {
  /**
   * Creates a new Component.
   * @param {string} id - Unique identifier.
   * @param {string} name - Component name.
   * @param {number} price - Component price.
   * @param {number} quantity - Component quantity.
   */
  constructor(id, name, price, quantity) {
    this.id = id;
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }
}

/**
 * Represents a shopping cart.
 */
class ShoppingCart {
  /**
   * Creates a new ShoppingCart.
   */
  constructor() {
    this.items = [];
  }

  /**
   * Adds a component to the cart.
   * @param {Component} component - Component to add.
   * @param {number} quantity - Quantity to add.
   */
  addItem(component, quantity) {
    if (quantity <= 0) {
      throw new Error('Quantity must be greater than 0');
    }

    const existingItem = this.items.find(item => item.component.id === component.id);
    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      this.items.push({ component, quantity });
    }
  }

  /**
   * Removes a component from the cart.
   * @param {string} componentId - ID of the component to remove.
   * @param {number} quantity - Quantity to remove.
   */
  removeItem(componentId, quantity) {
    if (quantity <= 0) {
      throw new Error('Quantity must be greater than 0');
    }

    const existingItem = this.items.find(item => item.component.id === componentId);
    if (existingItem) {
      if (existingItem.quantity <= quantity) {
        this.items = this.items.filter(item => item.component.id !== componentId);
      } else {
        existingItem.quantity -= quantity;
      }
    } else {
      throw new Error(`Component ${componentId} not found in cart`);
    }
  }

  /**
   * Updates the quantity of a component in the cart.
   * @param {string} componentId - ID of the component to update.
   * @param {number} quantity - New quantity.
   */
  updateQuantity(componentId, quantity) {
    if (quantity <= 0) {
      throw new Error('Quantity must be greater than 0');
    }

    const existingItem = this.items.find(item => item.component.id === componentId);
    if (existingItem) {
      existingItem.quantity = quantity;
    } else {
      throw new Error(`Component ${componentId} not found in cart`);
    }
  }

  /**
   * Calculates the total cost of the items in the cart.
   * @returns {number} Total cost.
   */
  calculateTotal() {
    return this.items.reduce((total, item) => total + item.component.price * item.quantity, 0);
  }

  /**
   * Clears the cart.
   */
  clearCart() {
    this.items = [];
  }
}

/**
 * Represents an order.
 */
class Order {
  /**
   * Creates a new Order.
   * @param {string} id - Unique identifier.
   * @param {ShoppingCart} cart - Shopping cart.
   */
  constructor(id, cart) {
    this.id = id;
    this.cart = cart;
    this.status = 'pending';
  }

  /**
   * Updates the order status.
   * @param {string} status - New status.
   */
  updateStatus(status) {
    this.status = status;
  }
}

// Example usage:
function main() {
  try {
    // Create components
    const component1 = new Component('1', 'Resistor', 1.99, 100);
    const component2 = new Component('2', 'Capacitor', 2.99, 50);

    // Create shopping cart
    const cart = new ShoppingCart();
    cart.addItem(component1, 2);
    cart.addItem(component2, 3);

    // Calculate total cost
    console.log(`Total cost: $${cart.calculateTotal().toFixed(2)}`);

    // Create order
    const order = new Order('ORD-1', cart);
    console.log(`Order ID: ${order.id}`);
    console.log(`Order status: ${order.status}`);

    // Update order status
    order.updateStatus('shipped');
    console.log(`Order status: ${order.status}`);

    // Clear cart
    cart.clearCart();
    console.log(`Cart items: ${cart.items.length}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
