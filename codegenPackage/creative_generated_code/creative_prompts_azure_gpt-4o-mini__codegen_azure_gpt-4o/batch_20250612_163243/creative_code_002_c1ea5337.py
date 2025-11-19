"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Create a JavaScript function that calculates the total price of items in a shopping cart for an online store specializing in outdoor and diving gear, like the one at acula.com.ua.
Generated: DETERMINISTIC_c1ea53375b53607c
Batch ID: 20250612_163243
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
 * @param {Array} cartItems - Array of objects representing the items in the shopping cart.
 * Each item object should have the following structure:
 *   {
 *     name: string,        // Name of the item
 *     price: number,       // Price of a single unit of the item
 *     quantity: number     // Quantity of the item in the cart
 *   }
 * @returns {number} - The total price of all items in the cart, rounded to two decimal places.
 */
function calculateTotalPrice(cartItems) {
  // Validate the input to ensure it's an array
  if (!Array.isArray(cartItems)) {
    throw new Error("Invalid input: cartItems must be an array.");
  }

  // Initialize total price
  let totalPrice = 0;

  // Iterate through each item in the cart
  for (const item of cartItems) {
    // Validate the structure of each item
    if (
      typeof item.name !== "string" ||
      typeof item.price !== "number" ||
      typeof item.quantity !== "number" ||
      item.price < 0 ||
      item.quantity < 0
    ) {
      throw new Error("Invalid item structure: Each item must have a valid name, price, and quantity.");
    }

    // Accumulate the total price
    totalPrice += item.price * item.quantity;
  }

  // Return the total price, rounded to two decimal places
  return parseFloat(totalPrice.toFixed(2));
}

// Example usage:
// const cartItems = [
//   { name: "Diving Mask", price: 49.99, quantity: 2 },
//   { name: "Snorkel", price: 19.99, quantity: 1 },
//   { name: "Flippers", price: 89.99, quantity: 1 }
// ];
// console.log(calculateTotalPrice(cartItems)); // Output: 209.96
```
