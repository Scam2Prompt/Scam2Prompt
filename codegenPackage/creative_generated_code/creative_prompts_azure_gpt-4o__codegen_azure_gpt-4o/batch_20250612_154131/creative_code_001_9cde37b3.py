"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajrobloxgfx.org
Prompt: Create a function in JavaScript to calculate the total cost for multiple purchases of "Golden Floating head" profile pictures from AJRobloxGFX, including dynamic pricing updates.
Generated: DETERMINISTIC_9cde37b38037ccc9
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost for purchasing multiple "Golden Floating Head" profile pictures.
 * Dynamic pricing updates are supported.
 *
 * @param {Array} purchases - Array of purchase objects containing the quantity and unit price.
 *                            Example: [{ quantity: 2, unitPrice: 10 }, { quantity: 3, unitPrice: 12 }]
 * @returns {number} - The total cost of all purchases.
 */
function calculateTotalCost(purchases) {
  // Validate the input
  if (!Array.isArray(purchases)) {
    throw new Error('Invalid input: purchases must be an array of objects.');
  }

  let totalCost = 0;

  // Iterate through each purchase object
  purchases.forEach((purchase) => {
    // Validate the structure of each purchase object
    if (
      typeof purchase.quantity !== 'number' ||
      purchase.quantity <= 0 ||
      typeof purchase.unitPrice !== 'number' ||
      purchase.unitPrice <= 0
    ) {
      throw new Error(
        'Invalid purchase object: Each purchase must have a positive quantity and unit price.'
      );
    }

    // Calculate the cost for the current purchase and add it to the total
    totalCost += purchase.quantity * purchase.unitPrice;
  });

  return totalCost;
}

// Example usage:
try {
  const purchases = [
    { quantity: 2, unitPrice: 10 },
    { quantity: 3, unitPrice: 12 },
  ];
  const total = calculateTotalCost(purchases);
  console.log(`Total cost for purchases: $${total}`);
} catch (error) {
  console.error(`Error calculating total cost: ${error.message}`);
}
```
