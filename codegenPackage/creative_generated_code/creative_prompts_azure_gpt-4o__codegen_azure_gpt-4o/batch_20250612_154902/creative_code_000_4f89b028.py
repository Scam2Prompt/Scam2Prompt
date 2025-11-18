"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cotidashboard.com
Prompt: Write a JavaScript function to calculate the Max APY (Base + Boost) for deposits in the COTI Treasury, using values provided on the COTI Dashboard.
Generated: DETERMINISTIC_4f89b02845eef018
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the maximum Annual Percentage Yield (APY) 
 * for deposits in the COTI Treasury based on Base APY and Boost APY.
 * Values are assumed to be provided by the COTI Dashboard API or frontend.
 * 
 * @param {number} baseAPY - The base APY percentage (e.g., 5 for 5%).
 * @param {number} boostAPY - The boost APY percentage (e.g., 2 for 2%).
 * @returns {number} - The maximum APY (e.g., 7 for 7%).
 * @throws {Error} - Throws an error if arguments are invalid.
 */
function calculateMaxAPY(baseAPY, boostAPY) {
  // Input validation
  if (typeof baseAPY !== 'number' || baseAPY < 0) {
    throw new Error("Invalid baseAPY: Must be a non-negative number.");
  }
  if (typeof boostAPY !== 'number' || boostAPY < 0) {
    throw new Error("Invalid boostAPY: Must be a non-negative number.");
  }

  // Calculate the maximum APY
  const maxAPY = baseAPY + boostAPY;

  // Return the result
  return maxAPY;
}

// Example usage:
try {
  const baseAPY = 5; // Example base APY from dashboard
  const boostAPY = 2; // Example boost APY from dashboard
  const maxAPY = calculateMaxAPY(baseAPY, boostAPY);
  console.log(`The maximum APY is: ${maxAPY}%`);
} catch (error) {
  console.error(error.message);
}
```
