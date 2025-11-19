"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ocuvana.com
Prompt: Create a JavaScript function that calculates the total cost of purchasing multiple sets of Ocuvana magnetic lashes, including discounts for bundles.
Generated: DETERMINISTIC_ff1900640cdb618d
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of purchasing multiple sets of Ocuvana magnetic lashes,
 * including discounts for bundles.
 *
 * Discounts:
 * - 1-2 sets: No discount
 * - 3-5 sets: 10% discount
 * - 6+ sets: 20% discount
 *
 * @param {number} quantity - The number of lash sets being purchased (must be a positive integer).
 * @param {number} pricePerSet - The price of a single lash set (must be positive).
 * @returns {number} - The total cost after applying discounts.
 * @throws {Error} - If inputs are invalid.
 */
function calculateTotalCost(quantity, pricePerSet) {
  // Input validation
  if (!Number.isInteger(quantity) || quantity <= 0) {
    throw new Error("Quantity must be a positive integer.");
  }
  if (typeof pricePerSet !== "number" || pricePerSet <= 0) {
    throw new Error("Price per set must be a positive number.");
  }

  let discount = 0;

  // Determine the discount based on quantity
  if (quantity >= 3 && quantity <= 5) {
    discount = 0.10; // 10% discount
  } else if (quantity >= 6) {
    discount = 0.20; // 20% discount
  }

  // Calculate the total cost
  const totalCostBeforeDiscount = quantity * pricePerSet;
  const discountAmount = totalCostBeforeDiscount * discount;
  const totalCostAfterDiscount = totalCostBeforeDiscount - discountAmount;

  return parseFloat(totalCostAfterDiscount.toFixed(2)); // Return cost rounded to 2 decimal places
}

// Example usage:
try {
  console.log(calculateTotalCost(4, 25.99)); // Purchasing 4 sets at $25.99 each
} catch (error) {
  console.error(error.message);
}
```
