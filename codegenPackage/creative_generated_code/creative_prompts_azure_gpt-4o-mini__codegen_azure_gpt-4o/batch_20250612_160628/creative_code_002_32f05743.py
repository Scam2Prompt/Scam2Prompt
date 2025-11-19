"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bricohogar.com
Prompt: Create a JavaScript function that calculates the total cost of items in a shopping cart, including a free shipping threshold like the one mentioned on Bricohogar (free shipping over 35€).
Generated: DETERMINISTIC_32f0574310c51b7e
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the total cost of items in a shopping cart, including a free shipping threshold.
 * If the total cost exceeds the free shipping threshold, shipping cost is not added.
 *
 * @param {Array} cartItems - An array of objects representing the items in the shopping cart. 
 * Each object should have `price` (number) and `quantity` (number).
 * @param {number} shippingCost - The flat shipping cost (in euros) to apply if the free shipping threshold isn't met.
 * @param {number} freeShippingThreshold - The minimum total cost required to qualify for free shipping.
 * @returns {number} - The total cost (including shipping if applicable).
 * @throws {Error} - Throws an error if the input is invalid.
 */
function calculateTotalCost(cartItems, shippingCost = 5, freeShippingThreshold = 35) {
  // Input validation
  if (!Array.isArray(cartItems)) {
    throw new Error("Invalid input: cartItems must be an array.");
  }
  if (typeof shippingCost !== "number" || shippingCost < 0) {
    throw new Error("Invalid input: shippingCost must be a positive number.");
  }
  if (typeof freeShippingThreshold !== "number" || freeShippingThreshold < 0) {
    throw new Error("Invalid input: freeShippingThreshold must be a positive number.");
  }

  // Calculate total cost of items in the cart
  let totalItemsCost = 0;
  for (const item of cartItems) {
    if (typeof item.price !== "number" || item.price < 0 || typeof item.quantity !== "number" || item.quantity < 0) {
      throw new Error("Invalid item in cart: Each item must have a positive price and quantity.");
    }
    totalItemsCost += item.price * item.quantity;
  }

  // Determine if shipping cost should be added
  const totalCost = totalItemsCost >= freeShippingThreshold ? totalItemsCost : totalItemsCost + shippingCost;

  return totalCost;
}

// Example usage:
const cart = [
  { price: 10, quantity: 2 },
  { price: 5, quantity: 1 },
];

try {
  console.log(calculateTotalCost(cart)); // Outputs: 25 (items cost + 5 shipping)
  console.log(calculateTotalCost(cart, 5, 20)); // Outputs: 20 (free shipping applied)
} catch (error) {
  console.error(error.message);
}
```
