"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://florerialima.com
Prompt: Develop a JavaScript function to calculate the total cost of a floral order, including discounts for bulk purchases, based on the products listed on a floral website.
Generated: DETERMINISTIC_ab587089b7792a37
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of a floral order, including bulk discounts.
 * @param {Array} orderItems - Array of objects representing items in the order. Each item should have:
 *   - {string} name: Name of the product
 *   - {number} price: Price per unit of the product
 *   - {number} quantity: Number of units ordered
 * @returns {number} - Total cost of the order after applying discounts
 */
function calculateFloralOrderTotal(orderItems) {
  // Validate input
  if (!Array.isArray(orderItems)) {
    throw new Error("Invalid input: orderItems must be an array.");
  }

  let totalCost = 0;

  // Iterate through each item in the order
  for (const item of orderItems) {
    // Validate item structure
    if (
      typeof item.name !== "string" ||
      typeof item.price !== "number" ||
      typeof item.quantity !== "number"
    ) {
      throw new Error("Invalid item structure. Each item must have name, price, and quantity.");
    }

    // Calculate cost for the current item
    let itemTotal = item.price * item.quantity;

    // Apply bulk discount
    // Example: 10% discount for quantities >= 10, 20% discount for quantities >= 20
    if (item.quantity >= 20) {
      itemTotal *= 0.8; // 20% discount
    } else if (item.quantity >= 10) {
      itemTotal *= 0.9; // 10% discount
    }

    // Add to the total cost
    totalCost += itemTotal;
  }

  // Return the total cost rounded to two decimal places
  return parseFloat(totalCost.toFixed(2));
}

// Example usage
const exampleOrder = [
  { name: "Roses", price: 2.5, quantity: 15 },
  { name: "Tulips", price: 1.8, quantity: 25 },
  { name: "Lilies", price: 3.0, quantity: 5 },
];

try {
  const totalCost = calculateFloralOrderTotal(exampleOrder);
  console.log(`Total Cost: $${totalCost}`);
} catch (error) {
  console.error(error.message);
}
```
