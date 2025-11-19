"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Write a JavaScript function that calculates the total price of items in a shopping cart, including discounts and shipping from Baby Calçados.
Generated: DETERMINISTIC_758fab7de9052961
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total price of items in a shopping cart.
 * Includes discounts and shipping costs.
 *
 * @param {Array} cart - Array of items in the shopping cart. Each item should be an object with the following properties:
 *  - price: {number} Price of the item
 *  - quantity: {number} Quantity of the item
 *  - discount: {number} Discount percentage (optional, default is 0)
 * @param {number} shippingCost - Fixed cost for shipping.
 * @returns {number} Total price of the shopping cart (including discounts and shipping cost).
 */
function calculateTotalPrice(cart, shippingCost) {
  // Input validation
  if (!Array.isArray(cart)) {
    throw new Error("Cart must be an array.");
  }

  if (typeof shippingCost !== "number" || shippingCost < 0) {
    throw new Error("Shipping cost must be a non-negative number.");
  }

  // Calculate total price of items in the cart
  let total = 0;

  for (const item of cart) {
    // Validate item properties
    if (
      typeof item.price !== "number" ||
      typeof item.quantity !== "number" ||
      item.price < 0 ||
      item.quantity < 0
    ) {
      throw new Error("Invalid item properties in the cart.");
    }

    // Default discount to 0 if not provided
    const discount = typeof item.discount === "number" && item.discount >= 0
      ? item.discount
      : 0;

    // Calculate item price with discount
    const discountedPrice = item.price * (1 - discount / 100);

    // Add item's final price to the total
    total += discountedPrice * item.quantity;
  }

  // Add shipping cost to the total
  total += shippingCost;

  // Ensure total is rounded to two decimal places
  return parseFloat(total.toFixed(2));
}

// Example usage:
const cart = [
  { price: 100, quantity: 2, discount: 10 },
  { price: 50, quantity: 1 },
  { price: 200, quantity: 1, discount: 20 },
];
const shippingCost = 15;

console.log(calculateTotalPrice(cart, shippingCost)); // Output: 385.00
```
