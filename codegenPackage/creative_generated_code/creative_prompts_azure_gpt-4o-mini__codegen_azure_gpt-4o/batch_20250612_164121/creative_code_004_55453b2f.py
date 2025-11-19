"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beltsmania.com
Prompt: Illustrate how to implement a shopping cart feature in JavaScript that allows users to add custom championship belts from Belts Mania to their cart and proceed to checkout.
Generated: DETERMINISTIC_55453b2f16f3c032
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Shopping Cart Feature for "Belts Mania"

// Define the shopping cart as an object
const ShoppingCart = {
  items: [], // Array to hold items in the cart

  // Method to add a custom championship belt to the cart
  addItem: function (beltName, price, quantity) {
    if (!beltName || price <= 0 || quantity <= 0) {
      console.error("Invalid item data. Please provide valid belt name, price, and quantity.");
      return;
    }

    const existingItemIndex = this.items.findIndex(item => item.beltName === beltName);

    if (existingItemIndex !== -1) {
      // If the item already exists in the cart, update its quantity
      this.items[existingItemIndex].quantity += quantity;
    } else {
      // Add new item to the cart
      this.items.push({ beltName, price, quantity });
    }

    console.log(`${beltName} added to the cart.`);
  },

  // Method to remove an item from the cart
  removeItem: function (beltName) {
    const updatedItems = this.items.filter(item => item.beltName !== beltName);

    if (updatedItems.length === this.items.length) {
      console.warn(`Item "${beltName}" not found in the cart.`);
      return;
    }

    this.items = updatedItems;
    console.log(`${beltName} removed from the cart.`);
  },

  // Method to calculate the total price of items in the cart
  calculateTotal: function () {
    return this.items.reduce((total, item) => {
      return total + item.price * item.quantity;
    }, 0);
  },

  // Method to display the cart contents
  displayCart: function () {
    if (this.items.length === 0) {
      console.log("Your cart is empty.");
      return;
    }

    console.log("Shopping Cart:");
    this.items.forEach(item => {
      console.log(`- ${item.beltName} | $${item.price} | Quantity: ${item.quantity}`);
    });
    console.log(`Total: $${this.calculateTotal()}`);
  },

  // Method to proceed to checkout
  checkout: function () {
    if (this.items.length === 0) {
      console.warn("Your cart is empty. Add items before proceeding to checkout.");
      return;
    }

    const totalAmount = this.calculateTotal();
    console.log(`Proceeding to checkout...`);
    console.log(`Total Amount: $${totalAmount}`);
    console.log("Thank you for shopping at Belts Mania!");
    this.items = []; // Clear the cart after checkout
  }
};

// Example usage
ShoppingCart.addItem("World Championship Belt", 299.99, 1);
ShoppingCart.addItem("Tag Team Championship Belt", 199.99, 2);
ShoppingCart.displayCart();
ShoppingCart.removeItem("Tag Team Championship Belt");
ShoppingCart.displayCart();
ShoppingCart.checkout();
ShoppingCart.displayCart(); // Cart should now be empty
```
