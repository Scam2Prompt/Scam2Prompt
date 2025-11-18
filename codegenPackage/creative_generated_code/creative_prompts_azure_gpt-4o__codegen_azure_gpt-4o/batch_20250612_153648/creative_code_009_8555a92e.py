"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9ias90dia90sdi9asidasdk.pages.dev
Prompt: Write a JavaScript function to calculate affiliate fees earned from cross-chain swaps executed through THORChain. Include logic for specifying custom fee percentages.
Generated: DETERMINISTIC_8555a92e846b9e4a
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the affiliate fees earned from cross-chain swaps executed through THORChain.
 * 
 * @param {number} swapAmount - The total amount of the swap in the base currency.
 * @param {number} feePercentage - Custom fee percentage set by the affiliate (e.g., 0.01 for 1%).
 * 
 * @returns {number} The affiliate fee earned from the swap.
 * @throws {Error} Throws an error if input is invalid (non-numeric or negative values).
 */
function calculateAffiliateFees(swapAmount, feePercentage) {
  // Input validation
  if (typeof swapAmount !== 'number' || typeof feePercentage !== 'number') {
    throw new Error('Invalid input: swapAmount and feePercentage must be numeric values.');
  }

  if (swapAmount < 0 || feePercentage < 0) {
    throw new Error('Invalid input: swapAmount and feePercentage cannot be negative.');
  }

  // Calculate the fee
  const affiliateFee = swapAmount * feePercentage;

  // Ensure the fee is rounded to two decimal places for monetary accuracy
  return parseFloat(affiliateFee.toFixed(2));
}

// Example usage
try {
  const swapAmount = 1000; // Example swap amount
  const feePercentage = 0.015; // Example fee percentage (1.5%)
  const feesEarned = calculateAffiliateFees(swapAmount, feePercentage);
  console.log(`Affiliate fees earned: $${feesEarned}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
