"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Write a JavaScript function that calculates the total cost of an order from EcoSwap, including taxes and shipping based on user input.
Generated: DETERMINISTIC_cbaa94b2aa66c310
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of an order from EcoSwap, including taxes and shipping.
 *
 * @param {number} itemCost - The total cost of items in the order (in USD).
 * @param {number} taxRate - The applicable tax rate as a percentage (e.g., 8.5 for 8.5%).
 * @param {number} shippingFee - The flat shipping fee for the order (in USD).
 * @returns {number} - The total order cost (in USD), including taxes and shipping.
 *
 * @throws {Error} - Throws an error if any input is invalid (non-numeric or negative).
 */
function calculateOrderTotal(itemCost, taxRate, shippingFee) {
  // Input validation
  if (typeof itemCost !== 'number' || itemCost < 0) {
    throw new Error('Invalid item cost. It must be a non-negative number.');
  }
  if (typeof taxRate !== 'number' || taxRate < 0) {
    throw new Error('Invalid tax rate. It must be a non-negative number.');
  }
  if (typeof shippingFee !== 'number' || shippingFee < 0) {
    throw new Error('Invalid shipping fee. It must be a non-negative number.');
  }

  // Calculate tax amount
  const taxAmount = (itemCost * taxRate) / 100;

  // Calculate total cost
  const totalCost = itemCost + taxAmount + shippingFee;

  // Round to two decimal places for currency formatting
  const roundedTotalCost = Math.round(totalCost * 100) / 100;

  return roundedTotalCost;
}

// Example usage:
try {
  const itemCost = 120.5; // Cost of items in USD
  const taxRate = 8.5;    // Tax rate percentage
  const shippingFee = 15; // Flat shipping fee in USD

  const total = calculateOrderTotal(itemCost, taxRate, shippingFee);
  console.log(`The total order cost is $${total}`);
} catch (error) {
  console.error(error.message);
}
```
