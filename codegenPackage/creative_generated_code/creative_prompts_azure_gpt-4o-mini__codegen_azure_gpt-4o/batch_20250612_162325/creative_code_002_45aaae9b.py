"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepelovesinu.pages.dev
Prompt: Generate a JavaScript function that calculates the total amount of PLINU tokens received when purchasing with USDT, including the 10% bonus.
Generated: DETERMINISTIC_45aaae9b7e63f7b5
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total amount of PLINU tokens received, including a 10% bonus.
 * @param {number} usdtAmount - The amount of USDT used for purchasing PLINU tokens.
 * @param {number} plinuPrice - The price of 1 PLINU token in USDT.
 * @returns {number} The total amount of PLINU tokens received, including the bonus.
 * @throws {Error} Throws an error if inputs are invalid or zero/negative.
 */
function calculatePlinuTokens(usdtAmount, plinuPrice) {
  // Validate input parameters
  if (typeof usdtAmount !== 'number' || typeof plinuPrice !== 'number') {
    throw new Error('Invalid input: usdtAmount and plinuPrice must be numbers.');
  }
  if (usdtAmount <= 0 || plinuPrice <= 0) {
    throw new Error('Invalid input: usdtAmount and plinuPrice must be greater than zero.');
  }

  // Calculate the base PLINU tokens received
  const basePlinuTokens = usdtAmount / plinuPrice;

  // Apply the 10% bonus
  const bonusPlinuTokens = basePlinuTokens * 0.10;

  // Calculate the total PLINU tokens received
  const totalPlinuTokens = basePlinuTokens + bonusPlinuTokens;

  // Return the total PLINU tokens
  return totalPlinuTokens;
}

// Example usage:
// const usdtAmount = 100; // Amount in USDT
// const plinuPrice = 2;   // Price of 1 PLINU token in USDT
// console.log(calculatePlinuTokens(usdtAmount, plinuPrice)); // Output: 55
```
