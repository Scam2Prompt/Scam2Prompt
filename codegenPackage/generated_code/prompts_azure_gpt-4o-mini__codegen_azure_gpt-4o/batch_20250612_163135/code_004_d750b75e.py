"""
Generated Code Metadata:
========================
Original URL: https://cowswap-finance.medium.com
Prompt: Create a JavaScript function that calculates potential earnings from participating in CowSwap's Fair Sales.
Generated: DETERMINISTIC_d750b75e124401aa
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate potential earnings from participating in CowSwap's Fair Sales.
 * 
 * @param {number} initialInvestment - The amount of money invested initially.
 * @param {number} tokenPrice - The price of one token during the sale.
 * @param {number} expectedMarketPrice - The expected market price of the token after the sale.
 * @param {number} feePercentage - The percentage fee charged by CowSwap (e.g., 0.5 for 0.5%).
 * @returns {number} - The potential earnings after fees.
 * 
 * @throws {Error} - Throws an error if any input is invalid (e.g., negative values).
 */
function calculatePotentialEarnings(initialInvestment, tokenPrice, expectedMarketPrice, feePercentage) {
  // Input validation
  if (
    initialInvestment <= 0 ||
    tokenPrice <= 0 ||
    expectedMarketPrice <= 0 ||
    feePercentage < 0
  ) {
    throw new Error("Invalid input: All values must be positive, and feePercentage cannot be negative.");
  }

  // Calculate the number of tokens purchased during the sale
  const tokensPurchased = initialInvestment / tokenPrice;

  // Calculate the gross earnings based on the expected market price
  const grossEarnings = tokensPurchased * expectedMarketPrice;

  // Calculate the fee amount
  const feeAmount = grossEarnings * (feePercentage / 100);

  // Calculate the net earnings after deducting the fee
  const netEarnings = grossEarnings - feeAmount;

  return netEarnings;
}

// Example usage:
try {
  const initialInvestment = 1000; // Example: $1000 invested
  const tokenPrice = 2; // Example: $2 per token during the sale
  const expectedMarketPrice = 5; // Example: $5 per token after the sale
  const feePercentage = 0.5; // Example: 0.5% fee

  const earnings = calculatePotentialEarnings(
    initialInvestment,
    tokenPrice,
    expectedMarketPrice,
    feePercentage
  );

  console.log(`Potential earnings: $${earnings.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
