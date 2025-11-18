"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Write a JavaScript function to dynamically update a shopping cart for products such as "Car Mounts" and "Holder Accessories," as described on the Volport website.
Generated: DETERMINISTIC_3d97567b0dad8e86
Batch ID: 20250612_153225
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
 * Provides functionality to dynamically update a shopping cart.
 */

/**
 * Updates the shopping cart with the specified product and quantity.
 * Adds new items if they don't exist or updates the quantity if they do.
 *
 * @param {string} productName - The name of the product (e.g., "Car Mounts", "Holder Accessories").
 * @param {number} quantity - The quantity to add (must be a positive integer).
 * @param {Object[]} cart - The current shopping cart array (e.g., [{ product: "Car Mounts", quantity: 2 }]).
 * @returns {Object[]} Updated shopping cart.
 */
function updateCart(productName, quantity, cart) {
  // Input validation
  if (typeof productName !== 'string' || productName.trim() === '') {
    throw new Error('Invalid product name. It must be a non-empty string.');
  }
  if (typeof quantity !== 'number' || quantity <= 0 || !Number.isInteger(quantity)) {
    throw new Error('Invalid quantity. It must be a positive integer.');
  }
  if (!Array.isArray(cart)) {
    throw new Error('Invalid cart. Cart must be an array.');
  }

  // Normalize product name (case-insensitive comparison)
  const normalizedProductName = productName.trim().toLowerCase();

  // Check if the product already exists in the cart
  const existingProductIndex = cart.findIndex(
    (item) => item.product.trim().toLowerCase() === normalizedProductName
  );

  if (existingProductIndex !== -1) {
    // Update quantity for the existing product
    cart[existingProductIndex].quantity += quantity;
  } else {
    // Add new product to the cart
    cart.push({ product: productName.trim(), quantity });
  }

  return cart;
}

/**
 * Example Usage
 */
try {
  let shoppingCart = [
    { product: 'Car Mounts', quantity: 2 },
    { product: 'Holder Accessories', quantity: 1 },
  ];

  shoppingCart = updateCart('Car Mounts', 3, shoppingCart);
  shoppingCart = updateCart('New Product', 1, shoppingCart);

  console.log('Updated Shopping Cart:', shoppingCart);
} catch (error) {
  console.error('Error:', error.message);
}
```
