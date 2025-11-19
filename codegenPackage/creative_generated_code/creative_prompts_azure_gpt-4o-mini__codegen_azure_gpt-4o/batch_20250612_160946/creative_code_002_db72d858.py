"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supertrumpcoin-io.pages.dev
Prompt: Create a JavaScript function that calculates the transaction tax for buying Super Trump Coin based on the provided tokenomics details.
Generated: DETERMINISTIC_db72d858f4919632
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the transaction tax for buying Super Trump Coin.
 * Tokenomics details:
 * - Buy tax: 5% of the transaction amount.
 * - Additional fees: A fixed fee of $2 applies to every transaction.
 * - Minimum transaction amount: $10 (transactions below this amount are invalid).
 * 
 * @param {number} transactionAmount - The amount (in USD) used to buy Super Trump Coin.
 * @returns {number} - The total transaction tax (including additional fees).
 * @throws {Error} - Throws an error if transactionAmount is invalid or below the minimum threshold.
 */
function calculateTransactionTax(transactionAmount) {
  // Constants based on tokenomics details
  const BUY_TAX_RATE = 0.05; // 5% buy tax
  const FIXED_FEE = 2; // Additional fixed fee
  const MIN_TRANSACTION_AMOUNT = 10; // Minimum transaction amount

  // Validate input
  if (typeof transactionAmount !== 'number' || isNaN(transactionAmount) || transactionAmount <= 0) {
    throw new Error('Invalid transaction amount. Please provide a positive numeric value.');
  }

  if (transactionAmount < MIN_TRANSACTION_AMOUNT) {
    throw new Error(
      `Transaction amount must be at least $${MIN_TRANSACTION_AMOUNT}.`
    );
  }

  // Calculate percentage-based buy tax
  const buyTax = transactionAmount * BUY_TAX_RATE;

  // Add the fixed fee to the tax
  const totalTax = buyTax + FIXED_FEE;

  // Return the total transaction tax rounded to two decimal places
  return parseFloat(totalTax.toFixed(2));
}

// Example usage:
try {
  const transactionAmount = 50; // Example transaction amount in USD
  const transactionTax = calculateTransactionTax(transactionAmount);
  console.log(`Transaction tax for $${transactionAmount}: $${transactionTax}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
