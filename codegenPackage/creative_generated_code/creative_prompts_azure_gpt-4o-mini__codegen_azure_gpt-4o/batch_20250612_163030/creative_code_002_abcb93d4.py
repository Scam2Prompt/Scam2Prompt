"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Create a JavaScript function that calculates the total price of items in a cart, including discounts for products like "hulajnogi" and "rowerki biegowe."
Generated: DETERMINISTIC_abcb93d4db662df7
Batch ID: 20250612_163030
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
 * Discounts are applied to specific product types: "hulajnogi" and "rowerki biegowe".
 *
 * @param {Array} cart - Array of objects representing items in the cart.
 * Each object should have the following properties:
 *   - name {string}: Name of the product.
 *   - price {number}: Price of the product (per unit).
 *   - quantity {number}: Number of units of the product.
 *
 * @returns {number} Total price of the cart after applying discounts.
 */
function calculateTotalPrice(cart) {
  // Validate input
  if (!Array.isArray(cart)) {
    throw new Error("Invalid input: cart must be an array.");
  }

  // Define discount percentages for specific product types
  const DISCOUNTS = {
    hulajnogi: 10, // 10% discount
    rowerki_biegowe: 15 // 15% discount
  };

  let totalPrice = 0;

  // Iterate through the cart items
  for (const item of cart) {
    // Validate item structure
    if (
      typeof item !== "object" ||
      typeof item.name !== "string" ||
      typeof item.price !== "number" ||
      typeof item.quantity !== "number"
    ) {
      throw new Error("Invalid item format in cart.");
    }

    // Calculate base price for the item
    let itemTotal = item.price * item.quantity;

    // Apply discount if applicable
    if (DISCOUNTS[item.name]) {
      const discountPercentage = DISCOUNTS[item.name];
      const discountAmount = (itemTotal * discountPercentage) / 100;
      itemTotal -= discountAmount;
    }

    // Accumulate the total price
    totalPrice += itemTotal;
  }

  return totalPrice;
}

// Example usage:
const cart = [
  { name: "hulajnogi", price: 200, quantity: 2 },
  { name: "rowerki_biegowe", price: 150, quantity: 1 },
  { name: "kaski", price: 50, quantity: 3 }
];

try {
  const total = calculateTotalPrice(cart);
  console.log("Total Price:", total); // Expected output: Total Price: 580
} catch (error) {
  console.error("Error:", error.message);
}
```
