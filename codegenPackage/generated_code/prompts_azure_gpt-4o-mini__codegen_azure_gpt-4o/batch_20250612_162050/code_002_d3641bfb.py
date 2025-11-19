"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Create a JavaScript function that calculates the cost of cleaning services based on user input, inspired by the pricing structure of Maid in Heaven's cleaning plans.
Generated: DETERMINISTIC_d3641bfb0d5e7e95
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost of cleaning services based on user input.
 * Pricing structure:
 * - Base rate: $50 per visit
 * - Additional charges:
 *   - $20 per extra room
 *   - $15 for deep cleaning
 *   - $10 for eco-friendly cleaning supplies
 * - Discounts:
 *   - 10% off for weekly plans
 *   - 5% off for bi-weekly plans
 * 
 * @param {number} numRooms - Number of rooms to clean (minimum 1).
 * @param {boolean} deepCleaning - Whether deep cleaning is requested.
 * @param {boolean} ecoSupplies - Whether eco-friendly supplies are requested.
 * @param {string} frequency - Cleaning frequency: "weekly", "bi-weekly", or "one-time".
 * @returns {number} - The total cost of the cleaning service.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateCleaningCost(numRooms, deepCleaning, ecoSupplies, frequency) {
  // Validate input
  if (typeof numRooms !== 'number' || numRooms < 1) {
    throw new Error("Invalid number of rooms. Must be a number greater than or equal to 1.");
  }
  if (typeof deepCleaning !== 'boolean') {
    throw new Error("Invalid value for deepCleaning. Must be a boolean.");
  }
  if (typeof ecoSupplies !== 'boolean') {
    throw new Error("Invalid value for ecoSupplies. Must be a boolean.");
  }
  if (!['weekly', 'bi-weekly', 'one-time'].includes(frequency)) {
    throw new Error("Invalid frequency. Must be 'weekly', 'bi-weekly', or 'one-time'.");
  }

  // Base rate
  const baseRate = 50;

  // Additional charges
  const extraRoomCharge = 20 * (numRooms - 1); // $20 per extra room
  const deepCleaningCharge = deepCleaning ? 15 : 0; // $15 for deep cleaning
  const ecoSuppliesCharge = ecoSupplies ? 10 : 0; // $10 for eco-friendly supplies

  // Calculate total before discounts
  let totalCost = baseRate + extraRoomCharge + deepCleaningCharge + ecoSuppliesCharge;

  // Apply discounts based on frequency
  if (frequency === 'weekly') {
    totalCost *= 0.9; // 10% discount
  } else if (frequency === 'bi-weekly') {
    totalCost *= 0.95; // 5% discount
  }

  // Round to two decimal places for currency formatting
  return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
  const cost = calculateCleaningCost(3, true, false, 'weekly');
  console.log(`The total cleaning cost is: $${cost}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
