"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Create a JavaScript function that calculates the total cost for ordering multiple types of thermal paper rolls, as offered by Apos.
Generated: DETERMINISTIC_67d94308b6425f89
Batch ID: 20250612_164323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of ordering thermal paper rolls.
 * @param {Array} orderDetails - An array of objects representing the order.
 * Each object should have the following properties:
 * - type {String}: The type of thermal paper roll (e.g., "standard", "premium").
 * - quantity {Number}: The number of rolls ordered for this type.
 * - pricePerRoll {Number}: The price per roll for this type.
 * @returns {Number} - The total cost of the order.
 * Throws an error if input is invalid or calculation fails.
 */
function calculateTotalCost(orderDetails) {
  // Validate input
  if (!Array.isArray(orderDetails)) {
    throw new Error("Invalid input: orderDetails must be an array.");
  }

  let totalCost = 0;

  // Iterate over each order detail to calculate the total cost
  for (const item of orderDetails) {
    // Validate item structure
    if (
      typeof item.type !== "string" ||
      typeof item.quantity !== "number" ||
      typeof item.pricePerRoll !== "number"
    ) {
      throw new Error(
        "Invalid item format: Each item must have 'type' as a string, 'quantity' as a number, and 'pricePerRoll' as a number."
      );
    }

    if (item.quantity < 0 || item.pricePerRoll < 0) {
      throw new Error(
        "Invalid values: 'quantity' and 'pricePerRoll' must be non-negative numbers."
      );
    }

    // Calculate cost for the item and add it to the total
    totalCost += item.quantity * item.pricePerRoll;
  }

  return totalCost;
}

// Example usage:
try {
  const order = [
    { type: "standard", quantity: 10, pricePerRoll: 2.5 },
    { type: "premium", quantity: 5, pricePerRoll: 4.0 },
  ];
  const total = calculateTotalCost(order);
  console.log(`Total Cost: $${total.toFixed(2)}`); // Output: Total Cost: $45.00
} catch (error) {
  console.error(error.message);
}
```
