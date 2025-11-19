"""
Generated Code Metadata:
========================
Original URL: https://bricohogar.com
Prompt: Create a JavaScript function that calculates the total cost of items in a shopping cart, including a free shipping threshold like the one mentioned on Bricohogar (free shipping over 35€).
Generated: DETERMINISTIC_32f0574310c51b7e
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of items in a shopping cart, including free shipping for orders over a specified threshold.
 * 
 * @param {Array} cart - An array of objects representing items in the shopping cart. Each object should have:
 *                       - `price` (number): The price of the item.
 *                       - `quantity` (number): The quantity of the item.
 * @param {number} shippingCost - The cost of shipping if the free shipping threshold is not met.
 * @param {number} freeShippingThreshold - The minimum total cost required to qualify for free shipping.
 * @returns {number} - The total cost including shipping (if applicable).
 */
function calculateTotalCost(cart, shippingCost, freeShippingThreshold) {
  // Validate input
  if (!Array.isArray(cart)) {
    throw new Error("Invalid input: 'cart' must be an array.");
  }
  if (typeof shippingCost !== "number" || shippingCost < 0) {
    throw new Error("Invalid input: 'shippingCost' must be a non-negative number.");
  }
  if (typeof freeShippingThreshold !== "number" || freeShippingThreshold < 0) {
    throw new Error("Invalid input: 'freeShippingThreshold' must be a non-negative number.");
  }

  // Calculate the total cost of items in the cart
  let totalItemCost = 0;
  for (const item of cart) {
    if (typeof item.price !== "number" || item.price < 0 || typeof item.quantity !== "number" || item.quantity < 0) {
      throw new Error("Invalid item in cart: Each item must have a non-negative 'price' and 'quantity'.");
    }
    totalItemCost += item.price * item.quantity;
  }

  // Determine if free shipping applies
  const totalCost = totalItemCost >= freeShippingThreshold ? totalItemCost : totalItemCost + shippingCost;

  return totalCost;
}

// Example usage:
const shoppingCart = [
  { price: 10, quantity: 2 }, // Item 1: 10€ x 2 = 20€
  { price: 5, quantity: 3 },  // Item 2: 5€ x 3 = 15€
];
const shippingFee = 5; // 5€ shipping cost
const freeShippingLimit = 35; // Free shipping for orders over 35€

try {
  const total = calculateTotalCost(shoppingCart, shippingFee, freeShippingLimit);
  console.log(`Total cost: €${total}`); // Output: Total cost: €35
} catch (error) {
  console.error(error.message);
}
```
