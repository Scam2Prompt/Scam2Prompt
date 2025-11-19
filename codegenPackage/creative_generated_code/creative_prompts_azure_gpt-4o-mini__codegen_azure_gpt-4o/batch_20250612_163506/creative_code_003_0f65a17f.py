"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Develop a shopping cart feature in JavaScript that calculates the total price of selected furniture items, similar to the cart functionality on moveisonlinepelotasbraz.
Generated: DETERMINISTIC_0f65a17f1d37c185
Batch ID: 20250612_163506
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
 * This script calculates the total price of selected furniture items in a shopping cart.
 * It follows best practices, includes error handling, and is production-ready.
 */

// Define furniture items with their names and prices
const furnitureItems = [
  { id: 1, name: "Sofa", price: 500 },
  { id: 2, name: "Dining Table", price: 300 },
  { id: 3, name: "Chair", price: 100 },
  { id: 4, name: "Bed", price: 800 },
  { id: 5, name: "Cabinet", price: 400 }
];

// Shopping cart object to manage selected items
const shoppingCart = {
  items: [], // Stores selected furniture items

  /**
   * Adds an item to the shopping cart.
   * @param {number} itemId - ID of the furniture item to add.
   */
  addItem(itemId) {
    const item = furnitureItems.find(furniture => furniture.id === itemId);
    if (!item) {
      console.error(`Item with ID ${itemId} not found.`);
      return;
    }
    this.items.push(item);
    console.log(`${item.name} added to your shopping cart.`);
  },

  /**
   * Removes an item from the shopping cart.
   * @param {number} itemId - ID of the furniture item to remove.
   */
  removeItem(itemId) {
    const index = this.items.findIndex(item => item.id === itemId);
    if (index === -1) {
      console.error(`Item with ID ${itemId} not found in the cart.`);
      return;
    }
    const removedItem = this.items.splice(index, 1)[0];
    console.log(`${removedItem.name} removed from your shopping cart.`);
  },

  /**
   * Calculates the total price of all items in the shopping cart.
   * @returns {number} Total price of items.
   */
  calculateTotal() {
    return this.items.reduce((total, item) => total + item.price, 0);
  },

  /**
   * Prints the current items in the shopping cart along with the total price.
   */
  displayCart() {
    if (this.items.length === 0) {
      console.log("Your shopping cart is empty.");
      return;
    }
    console.log("Shopping Cart:");
    this.items.forEach(item => console.log(`- ${item.name}: $${item.price}`));
    console.log(`Total Price: $${this.calculateTotal()}`);
  }
};

// Example usage:
// Adding items to the shopping cart
shoppingCart.addItem(1); // Adds Sofa
shoppingCart.addItem(3); // Adds Chair

// Removing an item from the shopping cart
shoppingCart.removeItem(1); // Removes Sofa

// Displaying the shopping cart and total price
shoppingCart.displayCart();
```
