"""
Generated Code Metadata:
========================
Original URL: https://miniapp.starsbot.xyz
Prompt: Generate JavaScript code to calculate the equivalent value of stars in TON, given the exchange rate of 1 star = 1 USDT.
Generated: DETERMINISTIC_f52dca9007b4bfb3
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the equivalent value of stars in TON.
 * Assumes the exchange rate of 1 star = 1 USDT.
 * 
 * @param {number} stars - The number of stars to convert.
 * @param {number} tonToUsdtRate - The current exchange rate of TON to USDT.
 * @returns {number} - The equivalent value in TON.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateStarsToTON(stars, tonToUsdtRate) {
  // Input validation
  if (typeof stars !== 'number' || stars < 0) {
    throw new Error("Invalid input: 'stars' must be a non-negative number.");
  }
  if (typeof tonToUsdtRate !== 'number' || tonToUsdtRate <= 0) {
    throw new Error("Invalid input: 'tonToUsdtRate' must be a positive number.");
  }

  // Calculate the equivalent value in TON
  const tonValue = stars / tonToUsdtRate;

  return tonValue;
}

// Example usage:
try {
  const stars = 100; // Number of stars
  const tonToUsdtRate = 2.5; // Example exchange rate: 1 TON = 2.5 USDT
  const tonEquivalent = calculateStarsToTON(stars, tonToUsdtRate);
  console.log(`The equivalent value of ${stars} stars in TON is: ${tonEquivalent}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
