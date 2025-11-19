"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Write a JavaScript function that calculates the number of JESSE tokens a user can buy based on their BASE investment during the presale.
Generated: DETERMINISTIC_c029f744da5df3b9
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the number of JESSE tokens a user can buy during presale.
 * @param {number} baseInvestment - The amount of BASE currency the user invests.
 * @param {number} tokenPrice - The price of one JESSE token in BASE currency.
 * @returns {number} - The number of JESSE tokens the user can purchase.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateJesseTokens(baseInvestment, tokenPrice) {
  // Validate inputs
  if (typeof baseInvestment !== 'number' || baseInvestment <= 0) {
    throw new Error('Invalid baseInvestment: Must be a positive number.');
  }
  if (typeof tokenPrice !== 'number' || tokenPrice <= 0) {
    throw new Error('Invalid tokenPrice: Must be a positive number.');
  }

  // Calculate the number of JESSE tokens the user can purchase
  const tokens = baseInvestment / tokenPrice;

  // Ensure we return a valid number
  if (!Number.isFinite(tokens)) {
    throw new Error('Calculation error: Result is not a valid number.');
  }

  return tokens;
}

// Example usage:
try {
  const baseInvestment = 1000; // Amount of BASE currency user invests
  const tokenPrice = 10; // Price of one JESSE token in BASE currency
  const jesseTokens = calculateJesseTokens(baseInvestment, tokenPrice);
  console.log(`You can purchase ${jesseTokens} JESSE tokens.`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
