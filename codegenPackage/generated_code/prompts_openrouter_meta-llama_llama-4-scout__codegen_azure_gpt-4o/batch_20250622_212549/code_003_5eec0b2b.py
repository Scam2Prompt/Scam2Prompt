"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Create a JavaScript code snippet to implement a promotions and discounts system for an e-commerce website, like the ones offered on Somos Corujas, with conditions such as "buy one get one free" or "10% off on orders above $100".
Generated: DETERMINISTIC_5eec0b2b8222e4dc
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Promotions and Discounts System for an E-commerce Website
 * This code implements a system to apply various promotions and discounts
 * such as "Buy One Get One Free" and "10% off on orders above $100".
 */

// Function to calculate the total price after applying promotions
function calculateTotal(cartItems, promotions) {
  try {
    // Validate input
    if (!Array.isArray(cartItems) || typeof promotions !== 'object') {
      throw new Error("Invalid input: cartItems must be an array and promotions must be an object.");
    }

    let total = 0;

    // Apply promotions to each item in the cart
    cartItems.forEach((item) => {
      if (!item.price || !item.quantity) {
        throw new Error("Invalid cart item: Each item must have a price and quantity.");
      }

      let itemTotal = item.price * item.quantity;

      // Check for "Buy One Get One Free" promotion
      if (promotions.bogo && promotions.bogo.includes(item.id)) {
        const freeItems = Math.floor(item.quantity / 2);
        itemTotal -= freeItems * item.price; // Subtract the price of free items
      }

      total += itemTotal;
    });

    // Apply "10% off on orders above $100" promotion
    if (promotions.discountAbove100 && total > 100) {
      total *= 0.9; // Apply 10% discount
    }

    return total.toFixed(2); // Return the total rounded to 2 decimal places
  } catch (error) {
    console.error("Error calculating total:", error.message);
    return null; // Return null in case of an error
  }
}

// Example usage
const cartItems = [
  { id: 1, name: "Product A", price: 50, quantity: 2 },
  { id: 2, name: "Product B", price: 30, quantity: 3 },
];

const promotions = {
  bogo: [1], // "Buy One Get One Free" applies to Product A (id: 1)
  discountAbove100: true, // Enable "10% off on orders above $100"
};

const totalPrice = calculateTotal(cartItems, promotions);
console.log("Total Price:", totalPrice); // Output the total price after applying promotions
```
