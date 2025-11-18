"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Write a function in JavaScript to calculate the cost for multiple campers attending the L-Zero basketball camp, factoring in discounts for group registrations.
Generated: DETERMINISTIC_5ad6fceb8f367a4b
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the cost for multiple campers attending the L-Zero basketball camp.
 * Discounts are applied for group registrations.
 * 
 * @param {number} numCampers - The number of campers registering.
 * @param {number} baseCostPerCamper - The base cost per camper.
 * @returns {number} - The total cost after applying group discounts.
 * 
 * Discounts:
 * - 5% off for groups of 5-9 campers
 * - 10% off for groups of 10-19 campers
 * - 15% off for groups of 20 or more campers
 */
function calculateCampCost(numCampers, baseCostPerCamper) {
  // Validate input parameters
  if (typeof numCampers !== 'number' || typeof baseCostPerCamper !== 'number') {
    throw new Error('Invalid input: numCampers and baseCostPerCamper must be numbers');
  }

  if (numCampers <= 0 || baseCostPerCamper <= 0) {
    throw new Error('Invalid input: numCampers and baseCostPerCamper must be positive numbers');
  }

  // Determine the discount rate based on the number of campers
  let discountRate = 0;
  if (numCampers >= 5 && numCampers <= 9) {
    discountRate = 0.05; // 5% discount
  } else if (numCampers >= 10 && numCampers <= 19) {
    discountRate = 0.10; // 10% discount
  } else if (numCampers >= 20) {
    discountRate = 0.15; // 15% discount
  }

  // Calculate total cost before discount
  const totalCostBeforeDiscount = numCampers * baseCostPerCamper;

  // Apply discount
  const discountAmount = totalCostBeforeDiscount * discountRate;
  const totalCostAfterDiscount = totalCostBeforeDiscount - discountAmount;

  // Return the final total cost
  return totalCostAfterDiscount;
}

// Example usage
try {
  const totalCost = calculateCampCost(10, 200); // 10 campers, each costing $200
  console.log(`The total camp cost is: $${totalCost.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
