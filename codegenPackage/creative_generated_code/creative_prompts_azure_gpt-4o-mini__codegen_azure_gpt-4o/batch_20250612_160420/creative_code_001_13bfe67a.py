"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.host
Prompt: Write a JavaScript function that calculates the total price of a custom gift basket from Agoda, including items like spa gift baskets and essential oils.
Generated: DETERMINISTIC_13bfe67a60a10d5f
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total price of a custom gift basket.
 * @param {Array} items - Array of objects representing items in the basket. Each object should have 'name', 'price', and 'quantity'.
 * @returns {number} - The total price of the gift basket.
 * @throws {Error} - Throws an error if the input structure is invalid or a price/quantity is negative.
 */
function calculateGiftBasketTotal(items) {
  // Validate input
  if (!Array.isArray(items)) {
    throw new Error("Invalid input: items should be an array.");
  }

  let totalPrice = 0;

  for (const item of items) {
    // Validate item structure
    if (
      typeof item !== "object" ||
      typeof item.name !== "string" ||
      typeof item.price !== "number" ||
      typeof item.quantity !== "number"
    ) {
      throw new Error(
        "Invalid item structure: each item should have 'name', 'price', and 'quantity'."
      );
    }

    // Validate price and quantity
    if (item.price < 0 || item.quantity < 0) {
      throw new Error(
        `Invalid values for item '${item.name}': price and quantity must be non-negative.`
      );
    }

    // Calculate total for the current item
    totalPrice += item.price * item.quantity;
  }

  return totalPrice;
}

// Example usage:
// Define a custom gift basket with items
const giftBasket = [
  { name: "Spa Gift Basket", price: 50, quantity: 2 },
  { name: "Essential Oils", price: 15, quantity: 3 },
  { name: "Chocolate Box", price: 25, quantity: 1 },
];

try {
  const total = calculateGiftBasketTotal(giftBasket);
  console.log(`Total price of the gift basket: $${total}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
