"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-en.web.app
Prompt: Develop a JavaScript function to calculate transaction fees for $PEPU token transfers on Pepe Unchained Layer 2, leveraging its lower fee structure.
Generated: DETERMINISTIC_7935a40917a4d9b7
Batch ID: 20250612_150241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate transaction fees for $PEPU token transfers
 * on Pepe Unchained Layer 2.
 * The fee structure is based on a fixed rate and may include discounts for large transactions.
 *
 * @param {number} transferAmount - The amount of $PEPU tokens being transferred.
 * @returns {number} - The calculated transaction fee in $PEPU tokens.
 * @throws {Error} - Throws an error if the transfer amount is invalid.
 */
function calculateTransactionFee(transferAmount) {
  // Constants
  const BASE_FEE_RATE = 0.002; // 0.2% fee for transactions
  const LARGE_TRANSACTION_DISCOUNT_RATE = 0.0015; // 0.15% fee for large transactions
  const LARGE_TRANSACTION_THRESHOLD = 100000; // Threshold for large transactions (in $PEPU tokens)

  // Input validation
  if (typeof transferAmount !== 'number' || transferAmount <= 0) {
    throw new Error('Invalid transfer amount. Must be a positive number.');
  }

  // Determine fee rate based on transfer amount
  const feeRate =
    transferAmount >= LARGE_TRANSACTION_THRESHOLD
      ? LARGE_TRANSACTION_DISCOUNT_RATE
      : BASE_FEE_RATE;

  // Calculate transaction fee
  const transactionFee = transferAmount * feeRate;

  // Ensure the fee is rounded to a reasonable precision (e.g., 8 decimal places)
  return parseFloat(transactionFee.toFixed(8));
}

// Example usage
try {
  const transferAmount = 120000; // Example transfer amount in $PEPU tokens
  const fee = calculateTransactionFee(transferAmount);
  console.log(`Transaction Fee for ${transferAmount} $PEPU: ${fee} $PEPU`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
