"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Write JavaScript code to enable a shopping cart feature for an e-commerce site like "Mass Compras," including functionality for adding items like "Cámara de Seguridad WiFi Inteligente" and calculating the total price.
Generated: DETERMINISTIC_5105d65695099471
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Shopping cart implementation for an e-commerce site

// Represents the item structure
class Item {
  constructor(name, price, quantity = 1) {
    this.name = name; // Name of the item
    this.price = price; // Price of the item
    this.quantity = quantity; // Quantity of the item
  }

  // Calculate the total price for this item (price * quantity)
  getTotalPrice() {
    return this.price * this.quantity;
  }
}

// Shopping Cart Class
class ShoppingCart {
  constructor() {
    this.items = []; // Array to store items in the cart
  }

  // Add a new item to the cart
  addItem(name, price, quantity = 1) {
    try {
      if (!name || typeof name !== "string") {
        throw new Error("Item name must be a valid string.");
      }
      if (isNaN(price) || price < 0) {
        throw new Error("Item price must be a valid positive number.");
      }
      if (!Number.isInteger(quantity) || quantity <= 0) {
        throw new Error("Item quantity must be a valid positive integer.");
      }

      // Check if the item already exists in the cart
      const existingItem = this.items.find((item) => item.name === name);
      if (existingItem) {
        // If the item exists, update its quantity
        existingItem.quantity += quantity;
      } else {
        // Otherwise, add a new item to the cart
        const item = new Item(name, price, quantity);
        this.items.push(item);
      }
    } catch (error) {
      console.error("Error adding item:", error.message);
    }
  }

  // Calculate the total price of all items in the cart
  calculateTotalPrice() {
    return this.items.reduce((total, item) => total + item.getTotalPrice(), 0);
  }

  // Display the contents of the cart
  displayCart() {
    if (this.items.length === 0) {
      console.log("Your cart is empty.");
      return;
    }

    console.log("Shopping Cart:");
    this.items.forEach((item, index) => {
      console.log(
        `${index + 1}. ${item.name} - $${item.price.toFixed(
          2
        )} x ${item.quantity} = $${item.getTotalPrice().toFixed(2)}`
      );
    });
    console.log(`Total Price: $${this.calculateTotalPrice().toFixed(2)}`);
  }

  // Remove an item from the cart by name
  removeItem(name) {
    try {
      const itemIndex = this.items.findIndex((item) => item.name === name);
      if (itemIndex === -1) {
        throw new Error(`Item "${name}" not found in the cart.`);
      }
      this.items.splice(itemIndex, 1);
    } catch (error) {
      console.error("Error removing item:", error.message);
    }
  }

  // Clear all items from the cart
  clearCart() {
    this.items = [];
    console.log("Cart has been cleared.");
  }
}

// Example Usage
const cart = new ShoppingCart();

// Add items to the cart
cart.addItem("Cámara de Seguridad WiFi Inteligente", 59.99, 2);
cart.addItem("Auriculares Bluetooth", 29.99, 1);

// Display the cart
cart.displayCart();

// Remove an item
cart.removeItem("Auriculares Bluetooth");

// Display the cart again
cart.displayCart();

// Calculate total price
console.log(`Final Total: $${cart.calculateTotalPrice().toFixed(2)}`);

// Clear the cart
cart.clearCart();

// Display the cart after clearing
cart.displayCart();
```
