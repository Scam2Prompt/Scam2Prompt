"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Generate a JavaScript code to implement a shopping cart functionality for a website like Jurunense Home Center."
Generated: DETERMINISTIC_47428d3b7a01e1b5
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Shopping Cart Implementation for a Website

// Class representing a single item in the shopping cart
class CartItem {
  constructor(id, name, price, quantity = 1) {
    this.id = id; // Unique identifier for the item
    this.name = name; // Name of the item
    this.price = price; // Price of the item
    this.quantity = quantity; // Quantity of the item
  }

  // Calculate the total price for this item
  getTotalPrice() {
    return this.price * this.quantity;
  }
}

// Class representing the shopping cart
class ShoppingCart {
  constructor() {
    this.items = []; // Array to store CartItem objects
  }

  // Add an item to the cart
  addItem(id, name, price, quantity = 1) {
    const existingItem = this.items.find((item) => item.id === id);
    if (existingItem) {
      // If the item already exists, update its quantity
      existingItem.quantity += quantity;
    } else {
      // Otherwise, add a new item to the cart
      const newItem = new CartItem(id, name, price, quantity);
      this.items.push(newItem);
    }
  }

  // Remove an item from the cart by its ID
  removeItem(id) {
    this.items = this.items.filter((item) => item.id !== id);
  }

  // Update the quantity of an item in the cart
  updateItemQuantity(id, quantity) {
    const item = this.items.find((item) => item.id === id);
    if (item) {
      if (quantity <= 0) {
        // If quantity is zero or less, remove the item
        this.removeItem(id);
      } else {
        // Otherwise, update the item's quantity
        item.quantity = quantity;
      }
    } else {
      console.error(`Item with ID ${id} not found in the cart.`);
    }
  }

  // Calculate the total cost of all items in the cart
  getTotalCost() {
    return this.items.reduce((total, item) => total + item.getTotalPrice(), 0);
  }

  // Display the contents of the cart
  displayCart() {
    if (this.items.length === 0) {
      console.log("Your cart is empty.");
    } else {
      console.log("Shopping Cart:");
      this.items.forEach((item) => {
        console.log(
          `- ${item.name} (ID: ${item.id}): $${item.price} x ${item.quantity} = $${item.getTotalPrice()}`
        );
      });
      console.log(`Total Cost: $${this.getTotalCost()}`);
    }
  }
}

// Example usage
try {
  const cart = new ShoppingCart();

  // Adding items to the cart
  cart.addItem(1, "Hammer", 15.99, 2);
  cart.addItem(2, "Screwdriver", 7.49, 1);
  cart.addItem(3, "Drill", 89.99, 1);

  // Displaying the cart
  cart.displayCart();

  // Updating item quantity
  cart.updateItemQuantity(1, 3);

  // Removing an item
  cart.removeItem(2);

  // Displaying the updated cart
  cart.displayCart();
} catch (error) {
  console.error("An error occurred while managing the shopping cart:", error);
}
```
