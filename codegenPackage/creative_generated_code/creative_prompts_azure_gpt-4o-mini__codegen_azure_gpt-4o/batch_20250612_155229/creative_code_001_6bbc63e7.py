"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banktoken.pages.dev
Prompt: Write a JavaScript function to calculate the holding dividend tax for $Bank token holders based on a 2.95% rate and a minimum holding of 88W Bank tokens.
Generated: DETERMINISTIC_6bbc63e7efe373a9
Batch ID: 20250612_155229
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the holding dividend tax for $Bank token holders.
 *
 * @param {number} holdingAmount - The number of $Bank tokens held by the user.
 * @returns {string} - The calculated dividend tax in USD or an error message if minimum holding is not met.
 */
function calculateDividendTax(holdingAmount) {
  // Constants
  const TAX_RATE = 0.0295; // 2.95% dividend tax rate
  const MINIMUM_HOLDING = 88; // Minimum tokens required to qualify for the tax

  // Input validation
  if (typeof holdingAmount !== 'number' || holdingAmount < 0) {
    return "Invalid input: 'holdingAmount' should be a positive number.";
  }

  // Check if user meets the minimum holding requirement
  if (holdingAmount < MINIMUM_HOLDING) {
    return `Holding amount (${holdingAmount}W) does not meet the minimum requirement of ${MINIMUM_HOLDING}W Bank tokens.`;
  }

  // Calculate dividend tax
  const dividendTax = holdingAmount * TAX_RATE;

  // Return the result rounded to two decimal places
  return `The dividend tax for holding ${holdingAmount}W Bank tokens is $${dividendTax.toFixed(2)} USD.`;
}

// Example usage
console.log(calculateDividendTax(100)); // Replace 100 with any holding amount for testing
```
