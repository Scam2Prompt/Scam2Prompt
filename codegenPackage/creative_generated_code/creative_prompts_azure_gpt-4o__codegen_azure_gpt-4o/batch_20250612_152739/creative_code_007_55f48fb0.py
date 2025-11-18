"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Write JavaScript code to implement a dynamic shopping cart system for TiburonFishingReels.com, allowing users to add items like reel clamps and fasteners while updating the total cost in real-time.
Generated: DETERMINISTIC_55f48fb097d1f425
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// shoppingCart.js

// A Shopping Cart class to encapsulate functionality
class ShoppingCart {
  constructor() {
    this.items = []; // Array to store items in the cart
    this.totalCost = 0; // Total cost of all items
  }

  /**
   * Adds an item to the shopping cart.
   * @param {string} name - Name of the item (e.g., "Reel Clamp").
   * @param {number} price - Price of the item.
   * @param {number} quantity - Quantity of the item.
   */
  addItem(name, price, quantity = 1) {
    if (!name || price < 0 || quantity <= 0) {
      throw new Error("Invalid input for adding an item.");
    }

    // Check if the item already exists in the cart
    const existingItem = this.items.find((item) => item.name === name);

    if (existingItem) {
      // Update quantity and total price of the existing item
      existingItem.quantity += quantity;
      existingItem.totalPrice = existingItem.quantity * existingItem.price;
    } else {
      // Add the new item to the cart
      this.items.push({
        name,
        price,
        quantity,
        totalPrice: price * quantity,
      });
    }

    // Update the total cost of the cart
    this.updateTotalCost();
  }

  /**
   * Removes an item from the shopping cart.
   * @param {string} name - Name of the item to remove.
   */
  removeItem(name) {
    // Filter out the item by name
    this.items = this.items.filter((item) => item.name !== name);
    // Update the total cost of the cart
    this.updateTotalCost();
  }

  /**
   * Updates the total cost of the shopping cart.
   */
  updateTotalCost() {
    this.totalCost = this.items.reduce((sum, item) => sum + item.totalPrice, 0);
  }

  /**
   * Displays the contents of the shopping cart.
   * @returns {string} A string representation of the cart contents.
   */
  displayCart() {
    if (this.items.length === 0) {
      return "Your shopping cart is empty.";
    }

    let cartContents = "Shopping Cart:\n";
    this.items.forEach((item) => {
      cartContents += `${item.name} - $${item.price} x ${item.quantity} = $${item.totalPrice}\n`;
    });
    cartContents += `Total Cost: $${this.totalCost}`;
    return cartContents;
  }

  /**
   * Clears all items from the shopping cart.
   */
  clearCart() {
    this.items = [];
    this.totalCost = 0;
  }
}

// Usage Example (Frontend Integration)
document.addEventListener("DOMContentLoaded", () => {
  const cart = new ShoppingCart(); // Initialize the shopping cart
  const cartDisplay = document.getElementById("cart-display");
  const addItemForm = document.getElementById("add-item-form");

  // Function to update the cart display
  function updateCartDisplay() {
    cartDisplay.textContent = cart.displayCart();
  }

  // Handle item addition form submission
  addItemForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = e.target.elements["item-name"].value;
    const price = parseFloat(e.target.elements["item-price"].value);
    const quantity = parseInt(e.target.elements["item-quantity"].value, 10);

    try {
      cart.addItem(name, price, quantity);
      updateCartDisplay();
    } catch (error) {
      alert(error.message);
    }

    // Reset the form fields
    addItemForm.reset();
  });

  // Attach functionality to clear cart button
  document.getElementById("clear-cart-btn").addEventListener("click", () => {
    cart.clearCart();
    updateCartDisplay();
  });

  // Initial display state
  updateCartDisplay();
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tiburon Fishing Reels - Shopping Cart</title>
  <script src="shoppingCart.js" defer></script>
</head>
<body>
  <h1>Tiburon Fishing Reels Shopping Cart</h1>

  <form id="add-item-form">
    <label>
      Item Name:
      <input type="text" name="item-name" required>
    </label>
    <label>
      Item Price:
      <input type="number" name="item-price" step="0.01" required>
    </label>
    <label>
      Quantity:
      <input type="number" name="item-quantity" min="1" required>
    </label>
    <button type="submit">Add Item</button>
  </form>

  <button id="clear-cart-btn">Clear Cart</button>

  <div id="cart-display" style="margin-top: 20px; white-space: pre-wrap;"></div>
</body>
</html>
```
