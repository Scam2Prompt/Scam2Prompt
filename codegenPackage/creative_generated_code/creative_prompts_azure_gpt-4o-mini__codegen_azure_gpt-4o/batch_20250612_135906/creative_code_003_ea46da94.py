"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polygon-crypto.yivesites.com
Prompt: Develop a JavaScript code to manage a shopping cart for APELBET, including features for adding and removing items.
Generated: DETERMINISTIC_ea46da9452fcc8f8
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ShoppingCart class to manage a shopping cart for APELBET.
 * Includes functionality to add, remove, and view items.
 * Implements error handling and follows best practices.
 */

class ShoppingCart {
  constructor() {
    // Initialize an empty cart
    this.cart = [];
  }

  /**
   * Add an item to the cart.
   * @param {string} itemName - Name of the item to add.
   * @param {number} quantity - Quantity of the item to add (must be > 0).
   * @param {number} price - Price of the item (must be > 0).
   */
  addItem(itemName, quantity, price) {
    // Validate inputs
    if (!itemName || typeof itemName !== 'string') {
      throw new Error('Invalid item name');
    }
    if (!quantity || typeof quantity !== 'number' || quantity <= 0) {
      throw new Error('Quantity must be a number greater than 0');
    }
    if (!price || typeof price !== 'number' || price <= 0) {
      throw new Error('Price must be a number greater than 0');
    }

    // Check if the item already exists in the cart
    const existingItem = this.cart.find((item) => item.name === itemName);
    if (existingItem) {
      // Update quantity and price if the item already exists
      existingItem.quantity += quantity;
      existingItem.price = price; // Update price to reflect the latest price
    } else {
      // Add new item to the cart
      this.cart.push({ name: itemName, quantity, price });
    }
  }

  /**
   * Remove an item from the cart by name.
   * @param {string} itemName - Name of the item to remove.
   */
  removeItem(itemName) {
    // Validate input
    if (!itemName || typeof itemName !== 'string') {
      throw new Error('Invalid item name');
    }

    // Filter out the item from the cart
    const initialLength = this.cart.length;
    this.cart = this.cart.filter((item) => item.name !== itemName);

    // Check if the item was found and removed
    if (this.cart.length === initialLength) {
      throw new Error(`Item "${itemName}" not found in the cart`);
    }
  }

  /**
   * View all items in the cart.
   * @returns {Array} - Array of items in the cart.
   */
  viewCart() {
    return this.cart.map((item) => ({
      name: item.name,
      quantity: item.quantity,
      price: item.price,
      total: item.quantity * item.price, // Calculate the total for each item
    }));
  }

  /**
   * Calculate the total cost of items in the cart.
   * @returns {number} - Total cost of items.
   */
  calculateTotal() {
    return this.cart.reduce((sum, item) => sum + item.quantity * item.price, 0);
  }
}

// Example usage:
try {
  const myCart = new ShoppingCart();

  // Add items to the cart
  myCart.addItem('Apple', 3, 1.99); // Add 3 apples at $1.99 each
  myCart.addItem('Banana', 2, 0.99); // Add 2 bananas at $0.99 each
  myCart.addItem('Apple', 2, 1.99); // Add 2 more apples

  // View the cart
  console.log('Cart Items:', myCart.viewCart());

  // Calculate total cost
  console.log('Total Cost:', myCart.calculateTotal());

  // Remove an item
  myCart.removeItem('Banana');

  // View the cart again
  console.log('Updated Cart Items:', myCart.viewCart());
} catch (error) {
  // Handle errors gracefully
  console.error('Error:', error.message);
}
```
