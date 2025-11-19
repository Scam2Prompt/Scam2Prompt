"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cambridgesolution.com
Prompt: Write a JavaScript function that calculates the required quantities of ingredients based on the pack sizes offered by Cambridge Commodities.
Generated: DETERMINISTIC_dc7142eaaa231941
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the required quantities of ingredients based on pack sizes.
 * @param {Array<number>} packSizes - Array of available pack sizes (e.g., [5, 10, 25]).
 * @param {number} requiredAmount - Total amount of the ingredient needed.
 * @returns {Object} - An object mapping pack sizes to the number of packs needed.
 *                     Example: { 25: 3, 10: 1 }
 */
function calculateIngredientQuantities(packSizes, requiredAmount) {
  // Validate inputs
  if (!Array.isArray(packSizes) || packSizes.some(size => typeof size !== 'number' || size <= 0)) {
    throw new Error('Invalid packSizes: Must be an array of positive numbers.');
  }
  if (typeof requiredAmount !== 'number' || requiredAmount <= 0) {
    throw new Error('Invalid requiredAmount: Must be a positive number.');
  }

  // Sort pack sizes in descending order for optimal usage of larger packs first
  packSizes.sort((a, b) => b - a);

  const result = {};
  let remainingAmount = requiredAmount;

  for (const packSize of packSizes) {
    // Determine the number of packs needed for the current pack size
    const numberOfPacks = Math.floor(remainingAmount / packSize);
    if (numberOfPacks > 0) {
      result[packSize] = numberOfPacks;
      remainingAmount -= numberOfPacks * packSize;
    }
  }

  // Handle case where requiredAmount cannot be fully fulfilled
  if (remainingAmount > 0) {
    throw new Error('Cannot fulfill the required amount with the given pack sizes.');
  }

  return result;
}

// Example usage:
try {
  const packSizes = [5, 10, 25];
  const requiredAmount = 65;
  const quantities = calculateIngredientQuantities(packSizes, requiredAmount);
  console.log('Quantities needed:', quantities); // Output: { 25: 2, 10: 1, 5: 1 }
} catch (error) {
  console.error('Error:', error.message);
}
```
