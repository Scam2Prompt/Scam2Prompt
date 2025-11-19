"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: Write a JavaScript function that calculates the total price of items in a cart, specifically for the Hoorainz collection of bracelets, considering both regular and sale prices.
Generated: DETERMINISTIC_94467cd3ee293b05
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the total price of items in a cart for the Hoorainz collection of bracelets.
 * It considers both regular and sale prices.
 * 
 * @param {Array} cart - Array of cart items. Each item is an object with the following properties:
 *   - name {string}: Name of the item.
 *   - collection {string}: Collection name (e.g., "Hoorainz").
 *   - regularPrice {number}: Regular price of the item.
 *   - salePrice {number|null}: Sale price of the item (null if not on sale).
 *   - quantity {number}: Quantity of the item in the cart.
 * 
 * @returns {number} - Total price of all Hoorainz bracelets in the cart.
 */
function calculateHoorainzTotal(cart) {
  // Validate input
  if (!Array.isArray(cart)) {
    throw new Error("Invalid input: cart must be an array.");
  }

  let totalPrice = 0;

  // Iterate through the cart items
  for (const item of cart) {
    // Validate item structure
    if (
      typeof item.name !== "string" ||
      typeof item.collection !== "string" ||
      typeof item.regularPrice !== "number" ||
      (item.salePrice !== null && typeof item.salePrice !== "number") ||
      typeof item.quantity !== "number"
    ) {
      throw new Error("Invalid item structure in cart.");
    }

    // Check if the item belongs to the Hoorainz collection
    if (item.collection === "Hoorainz") {
      // Use sale price if available, otherwise use regular price
      const pricePerItem = item.salePrice !== null ? item.salePrice : item.regularPrice;

      // Add the total price for this item to the overall total
      totalPrice += pricePerItem * item.quantity;
    }
  }

  return totalPrice;
}

// Example usage:
const cart = [
  { name: "Bracelet A", collection: "Hoorainz", regularPrice: 50, salePrice: 40, quantity: 2 },
  { name: "Bracelet B", collection: "Hoorainz", regularPrice: 30, salePrice: null, quantity: 1 },
  { name: "Necklace C", collection: "OtherCollection", regularPrice: 100, salePrice: 80, quantity: 1 },
];

try {
  const total = calculateHoorainzTotal(cart);
  console.log(`Total price for Hoorainz collection: $${total}`);
} catch (error) {
  console.error(error.message);
}
```
