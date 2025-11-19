"""
Generated Code Metadata:
========================
Original URL: https://teeny-activity-colossal.on-fleek.app
Prompt: Develop a JavaScript function that dynamically updates the shopping cart for a comic series, ensuring it reflects the purchase of items like "Top G Volume 3.1."
Generated: DETERMINISTIC_c8646d54d4d06ff2
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to dynamically update the shopping cart for a comic series.
 * @param {Array} cart - The current shopping cart array.
 * @param {Object} item - The item to be added or updated in the cart.
 * @param {number} quantity - The quantity of the item to be added.
 * @returns {Array} - The updated shopping cart array.
 */
function updateShoppingCart(cart, item, quantity) {
  // Validate inputs
  if (!Array.isArray(cart)) {
    throw new Error("Invalid cart: Cart must be an array.");
  }
  if (typeof item !== "object" || item === null || !item.name || !item.price) {
    throw new Error("Invalid item: Item must be an object with 'name' and 'price' properties.");
  }
  if (typeof quantity !== "number" || quantity <= 0) {
    throw new Error("Invalid quantity: Quantity must be a positive number.");
  }

  // Check if the item already exists in the cart
  const existingItemIndex = cart.findIndex(cartItem => cartItem.name === item.name);

  if (existingItemIndex !== -1) {
    // Update the quantity if the item already exists
    cart[existingItemIndex].quantity += quantity;
  } else {
    // Add the new item to the cart
    cart.push({
      name: item.name,
      price: item.price,
      quantity: quantity
    });
  }

  return cart;
}

// Example usage:
try {
  let shoppingCart = [];
  const comicItem = { name: "Top G Volume 3.1", price: 15.99 };

  shoppingCart = updateShoppingCart(shoppingCart, comicItem, 2);
  console.log("Updated Cart:", shoppingCart);

  shoppingCart = updateShoppingCart(shoppingCart, comicItem, 1);
  console.log("Updated Cart:", shoppingCart);
} catch (error) {
  console.error("Error updating shopping cart:", error.message);
}
```
