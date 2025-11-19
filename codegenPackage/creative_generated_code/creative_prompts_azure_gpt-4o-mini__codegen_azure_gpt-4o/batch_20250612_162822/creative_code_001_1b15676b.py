"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artpelbrazz.blogspot.com
Prompt: Write a JavaScript function that calculates the total cost of a shopping cart on the Art Pel website, including discounts for first-time purchases and payment via PIX.
Generated: DETERMINISTIC_1b15676b9af08ab5
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of a shopping cart on the Art Pel website.
 * Includes discounts for first-time purchases and payment via PIX.
 *
 * @param {Array} cartItems - An array of objects representing items in the cart.
 * Each item object should have the following properties:
 *    - price {number}: The price of the item.
 *    - quantity {number}: The quantity of the item purchased.
 * @param {boolean} isFirstTimeBuyer - Indicates if the user is a first-time buyer.
 * @param {boolean} isPayingViaPIX - Indicates if the user is paying via PIX.
 * @returns {number} The total cost after applying discounts.
 */
function calculateTotalCost(cartItems, isFirstTimeBuyer, isPayingViaPIX) {
  try {
    // Validate cartItems
    if (!Array.isArray(cartItems)) {
      throw new Error("cartItems must be an array.");
    }

    // Calculate the base total cost of items in the cart
    let totalCost = cartItems.reduce((total, item) => {
      // Validate item structure
      if (typeof item.price !== "number" || typeof item.quantity !== "number") {
        throw new Error("Each item in cartItems must have 'price' and 'quantity' as numbers.");
      }
      return total + item.price * item.quantity;
    }, 0);

    // Apply a 10% discount for first-time buyers
    if (isFirstTimeBuyer) {
      totalCost *= 0.9; // Reduce total cost by 10%
    }

    // Apply a 5% discount for payment via PIX
    if (isPayingViaPIX) {
      totalCost *= 0.95; // Reduce total cost by 5%
    }

    // Round to two decimal places for currency formatting
    return parseFloat(totalCost.toFixed(2));
  } catch (error) {
    console.error("Error calculating total cost:", error.message);
    return null; // Return null to indicate an error occurred
  }
}

// Example Usage
const cart = [
  { price: 100, quantity: 2 },
  { price: 50, quantity: 1 },
];
const isFirstTime = true;
const isPixPayment = true;

console.log(calculateTotalCost(cart, isFirstTime, isPixPayment)); // Output: 171
```
