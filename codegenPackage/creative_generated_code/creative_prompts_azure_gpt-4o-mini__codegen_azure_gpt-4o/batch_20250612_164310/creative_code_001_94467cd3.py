"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoorainz.com
Prompt: Write a JavaScript function that calculates the total price of items in a cart, specifically for the Hoorainz collection of bracelets, considering both regular and sale prices.
Generated: DETERMINISTIC_94467cd3ee293b05
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total price of items in the cart for the Hoorainz collection of bracelets.
 * Handles both regular and sale prices.
 *
 * @param {Array<Object>} cart - Array of cart items. Each item must have:
 *                               - name: Name of the product
 *                               - collection: Name of the collection
 *                               - quantity: Number of items
 *                               - price: Regular price of the item
 *                               - salePrice: Sale price of the item (optional)
 * @returns {number} - Total price of Hoorainz bracelets in the cart.
 */
function calculateTotalPrice(cart) {
  // Validate the input is an array
  if (!Array.isArray(cart)) {
    throw new Error("The cart must be an array.");
  }

  // Initialize total price to 0
  let totalPrice = 0;

  // Loop through each item in the cart
  for (const item of cart) {
    // Validate item structure and required fields
    if (
      typeof item !== 'object' ||
      !item.name ||
      !item.collection ||
      typeof item.quantity !== 'number' ||
      typeof item.price !== 'number'
    ) {
      throw new Error("Invalid item structure in cart.");
    }

    // Check if the item belongs to the Hoorainz collection
    if (item.collection === "Hoorainz") {
      // Use salePrice if it exists and is valid, otherwise use regular price
      const applicablePrice =
        typeof item.salePrice === 'number' && item.salePrice < item.price
          ? item.salePrice
          : item.price;

      // Add the item's total price to the totalPrice
      totalPrice += applicablePrice * item.quantity;
    }
  }

  // Return the calculated total price
  return totalPrice;
}

// Example usage:
const cart = [
  { name: "Bracelet A", collection: "Hoorainz", quantity: 2, price: 50, salePrice: 40 },
  { name: "Bracelet B", collection: "Hoorainz", quantity: 1, price: 70 },
  { name: "Bracelet C", collection: "OtherCollection", quantity: 3, price: 30, salePrice: 25 },
];

try {
  const total = calculateTotalPrice(cart);
  console.log("Total price:", total); // Output: 130
} catch (error) {
  console.error("Error calculating total price:", error.message);
}
```
