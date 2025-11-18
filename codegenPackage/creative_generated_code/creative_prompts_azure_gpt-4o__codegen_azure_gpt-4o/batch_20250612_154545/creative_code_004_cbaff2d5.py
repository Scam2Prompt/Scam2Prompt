"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Write JavaScript code to implement a shopping cart system for AirstyleArt, including features like "Add to Cart," "Quick View," and "Continue Shopping."
Generated: DETERMINISTIC_cbaff2d549a17fa2
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Shopping Cart System for AirstyleArt

// Create an IIFE (Immediately Invoked Function Expression) to encapsulate the Shopping Cart System
const ShoppingCartSystem = (() => {
  // Private variables for cart data
  let cart = [];
  let inventory = [
    { id: 1, name: "Abstract Painting", price: 120.0, stock: 5 },
    { id: 2, name: "Nature Canvas", price: 95.0, stock: 10 },
    { id: 3, name: "Modern Sculpture", price: 350.0, stock: 2 },
  ];

  // Utility function to find an item in the cart
  const findCartItem = (id) => cart.find((item) => item.id === id);

  // Utility function to find an item in the inventory
  const findInventoryItem = (id) => inventory.find((item) => item.id === id);

  // Add item to the cart
  const addToCart = (id, quantity = 1) => {
    const inventoryItem = findInventoryItem(id);

    if (!inventoryItem) {
      console.error(`Item with ID ${id} not found in inventory.`);
      return;
    }

    if (inventoryItem.stock < quantity) {
      console.error(`Insufficient stock for ${inventoryItem.name}. Available: ${inventoryItem.stock}`);
      return;
    }

    const cartItem = findCartItem(id);
    if (cartItem) {
      // Update quantity if item is already in the cart
      cartItem.quantity += quantity;
    } else {
      // Add new item to the cart
      cart.push({ id: inventoryItem.id, name: inventoryItem.name, price: inventoryItem.price, quantity });
    }

    // Update inventory stock
    inventoryItem.stock -= quantity;

    console.log(`Added ${quantity}x "${inventoryItem.name}" to the cart.`);
  };

  // View item details (Quick View)
  const quickView = (id) => {
    const inventoryItem = findInventoryItem(id);
    if (!inventoryItem) {
      console.error(`Item with ID ${id} not found.`);
      return;
    }

    console.log(`Quick View for "${inventoryItem.name}":`);
    console.log(`Price: $${inventoryItem.price.toFixed(2)}`);
    console.log(`Stock: ${inventoryItem.stock}`);
  };

  // Continue shopping - Display inventory
  const continueShopping = () => {
    console.log("Available items:");
    inventory.forEach((item) => {
      console.log(
        `ID: ${item.id}, Name: ${item.name}, Price: $${item.price.toFixed(2)}, Stock: ${item.stock}`
      );
    });
  };

  // View cart contents
  const viewCart = () => {
    if (cart.length === 0) {
      console.log("Your cart is empty.");
      return;
    }
    console.log("Your Cart:");
    cart.forEach((item) => {
      console.log(
        `ID: ${item.id}, Name: ${item.name}, Price: $${item.price.toFixed(
          2
        )}, Quantity: ${item.quantity}, Subtotal: $${(item.price * item.quantity).toFixed(2)}`
      );
    });
  };

  // Export public methods
  return {
    addToCart,
    quickView,
    continueShopping,
    viewCart,
  };
})();

// Example usage:

// Show available inventory
ShoppingCartSystem.continueShopping();

// Quick View of an item
ShoppingCartSystem.quickView(1);

// Add items to the cart
ShoppingCartSystem.addToCart(1, 2);
ShoppingCartSystem.addToCart(2, 3);
ShoppingCartSystem.addToCart(3, 1);

// View cart contents
ShoppingCartSystem.viewCart();

// Continue shopping (show remaining inventory)
ShoppingCartSystem.continueShopping();
```
