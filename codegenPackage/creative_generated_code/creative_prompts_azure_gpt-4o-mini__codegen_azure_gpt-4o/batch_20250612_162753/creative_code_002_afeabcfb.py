"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Create a JavaScript function that dynamically updates a shopping cart with items such as "Cámara de Seguridad WiFi Inteligente" and "ageLOC® LumiSpa®" based on user selections, similar to the functionality on Mass Compras.
Generated: DETERMINISTIC_afeabcfbfff9d5ce
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Shopping Cart Module
 * This module handles the dynamic updates to a shopping cart based on user selections.
 */

// Shopping cart object to hold items
const shoppingCart = {
  items: [],

  /**
   * Adds an item to the shopping cart.
   * @param {string} itemName - Name of the item to add.
   * @param {number} itemPrice - Price of the item to add.
   */
  addItem(itemName, itemPrice) {
    if (!itemName || typeof itemPrice !== 'number' || itemPrice < 0) {
      console.error("Invalid itemName or itemPrice provided.");
      return;
    }

    this.items.push({ name: itemName, price: itemPrice });
    this.displayCart();
  },

  /**
   * Removes an item from the shopping cart by name.
   * @param {string} itemName - Name of the item to remove.
   */
  removeItem(itemName) {
    this.items = this.items.filter(item => item.name !== itemName);
    this.displayCart();
  },

  /**
   * Calculates the total price of items in the shopping cart.
   * @returns {number} - Total price of items.
   */
  calculateTotal() {
    return this.items.reduce((total, item) => total + item.price, 0);
  },

  /**
   * Displays the shopping cart in a user-friendly format.
   */
  displayCart() {
    console.clear();
    console.log("Your Shopping Cart:");
    if (this.items.length === 0) {
      console.log("Your cart is empty.");
    } else {
      this.items.forEach((item, index) => {
        console.log(`${index + 1}. ${item.name} - $${item.price.toFixed(2)}`);
      });
      console.log(`Total: $${this.calculateTotal().toFixed(2)}`);
    }
  }
};

/**
 * Example usage: Simulates user interactions with the shopping cart.
 */
function simulateUserActions() {
  // Adding items to the cart
  shoppingCart.addItem("Cámara de Seguridad WiFi Inteligente", 79.99);
  shoppingCart.addItem("ageLOC® LumiSpa®", 199.99);

  // Removing an item from the cart
  shoppingCart.removeItem("Cámara de Seguridad WiFi Inteligente");

  // Adding another item
  shoppingCart.addItem("Smart LED Bulb", 19.99);
}

// Simulate user actions
simulateUserActions();
```
