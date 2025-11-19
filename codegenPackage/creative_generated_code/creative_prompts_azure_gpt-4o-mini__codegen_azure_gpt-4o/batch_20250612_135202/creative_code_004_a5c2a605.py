"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Create a JavaScript function to calculate the total amount raised in USDT for a presale event, referencing the BOI Coin presale model.
Generated: DETERMINISTIC_a5c2a60554fa9ded
Batch ID: 20250612_135202
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total amount raised in USDT during a presale event.
 * 
 * @param {Array<Object>} contributions - Array of contribution objects.
 *        Each object should have the structure: { contributor: string, amountUSDT: number }
 * @returns {number} - Total amount raised in USDT.
 * @throws {Error} - Throws an error if contributions data is invalid.
 */
function calculateTotalRaisedUSDT(contributions) {
  // Validate the input
  if (!Array.isArray(contributions)) {
    throw new Error("Invalid input: contributions must be an array.");
  }

  let totalRaised = 0;

  for (const contribution of contributions) {
    // Validate each contribution object
    if (
      typeof contribution !== "object" ||
      !contribution.hasOwnProperty("amountUSDT") ||
      typeof contribution.amountUSDT !== "number"
    ) {
      throw new Error("Invalid contribution data. Each contribution must be an object with a numeric 'amountUSDT' property.");
    }

    // Accumulate the total
    totalRaised += contribution.amountUSDT;
  }

  return totalRaised;
}

// Example usage:
// const presaleContributions = [
//   { contributor: "Alice", amountUSDT: 100 },
//   { contributor: "Bob", amountUSDT: 200 },
//   { contributor: "Charlie", amountUSDT: 50 }
// ];

// console.log(calculateTotalRaisedUSDT(presaleContributions)); // Output: 350

// Note: Be sure to validate the input data structure before calling the function.
```
