"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: Create a JavaScript function that calculates potential savings on car insurance based on user input, inspired by the money-saving tips on recuperacionjc.com.
Generated: DETERMINISTIC_d4bb337d5946325c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate potential savings on car insurance based on user input.
 * Inspired by money-saving tips on recuperacionjc.com.
 *
 * @param {number} currentPremium - The current annual insurance premium paid by the user.
 * @param {number} discountRate - The percentage discount the user expects to achieve (e.g., 10 for 10%).
 * @param {number} additionalSavings - Additional savings in dollars (e.g., bundling policies, safe driving discounts).
 * @returns {object} - An object containing the calculated savings and the new premium amount.
 */
function calculateInsuranceSavings(currentPremium, discountRate, additionalSavings) {
  // Input validation
  if (typeof currentPremium !== 'number' || currentPremium <= 0) {
    throw new Error("Invalid input: 'currentPremium' must be a positive number.");
  }
  if (typeof discountRate !== 'number' || discountRate < 0 || discountRate > 100) {
    throw new Error("Invalid input: 'discountRate' must be a number between 0 and 100.");
  }
  if (typeof additionalSavings !== 'number' || additionalSavings < 0) {
    throw new Error("Invalid input: 'additionalSavings' must be a non-negative number.");
  }

  // Calculate savings from discount rate
  const discountSavings = (currentPremium * discountRate) / 100;

  // Calculate total savings
  const totalSavings = discountSavings + additionalSavings;

  // Calculate new premium after savings
  const newPremium = currentPremium - totalSavings;

  // Ensure new premium is not negative
  const adjustedNewPremium = Math.max(newPremium, 0);

  // Return the results as an object
  return {
    totalSavings: totalSavings.toFixed(2), // Rounded to 2 decimal places
    newPremium: adjustedNewPremium.toFixed(2) // Rounded to 2 decimal places
  };
}

// Example usage:
try {
  const result = calculateInsuranceSavings(1200, 15, 50);
  console.log("Potential Savings:", result.totalSavings);
  console.log("New Premium:", result.newPremium);
} catch (error) {
  console.error("Error:", error.message);
}
```
