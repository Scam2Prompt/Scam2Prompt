"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-mvp.pages.dev
Prompt: Write a function in JavaScript to calculate the collateral ratio (C-ratio) for a user on the SYNTHR platform, given their debt balance and collateral balance. Use the platform's requirement of a minimum 150% C-ratio.
Generated: DETERMINISTIC_248aae5c17624bc2
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the collateral ratio (C-ratio) for a user on the SYNTHR platform.
 * The function checks whether the collateral ratio meets the platform's minimum requirement of 150%.
 * 
 * @param {number} debtBalance - The user's debt balance in dollars.
 * @param {number} collateralBalance - The user's collateral balance in dollars.
 * @returns {Object} - An object containing the calculated C-ratio and a boolean indicating if the C-ratio meets the minimum requirement.
 * @throws {Error} - Throws an error if the inputs are invalid (non-positive numbers).
 */
function calculateCollateralRatio(debtBalance, collateralBalance) {
  // Input validation: Ensure debtBalance and collateralBalance are positive numbers.
  if (typeof debtBalance !== 'number' || typeof collateralBalance !== 'number') {
    throw new Error("Both debtBalance and collateralBalance must be numbers.");
  }
  if (debtBalance <= 0 || collateralBalance <= 0) {
    throw new Error("Both debtBalance and collateralBalance must be positive values.");
  }

  // Calculate the collateral ratio (C-ratio).
  const collateralRatio = (collateralBalance / debtBalance) * 100;

  // Check if the C-ratio meets the minimum requirement.
  const minimumCollateralRatio = 150; // Minimum required C-ratio (150%).
  const isValidRatio = collateralRatio >= minimumCollateralRatio;

  // Return the result as an object.
  return {
    collateralRatio: collateralRatio.toFixed(2), // Format to 2 decimal places for clarity.
    isValid: isValidRatio,
  };
}

// Example usage:
try {
  const result = calculateCollateralRatio(1000, 2000);
  console.log(result); // { collateralRatio: '200.00', isValid: true }
} catch (error) {
  console.error("Error:", error.message);
}
```
