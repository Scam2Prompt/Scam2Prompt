"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-ethereum.com
Prompt: Generate a JavaScript function that utilizes ES6 template literals, referencing the usage examples provided on the Ethereum webpage.
Generated: DETERMINISTIC_702575e661a7423a
Batch ID: 20250612_135940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Generates a formatted Ethereum transaction summary using ES6 template literals.
 *
 * @param {string} from - The address of the sender.
 * @param {string} to - The address of the recipient.
 * @param {number} amount - The amount of Ether being transferred (in ETH).
 * @param {number} gasFee - The gas fee associated with the transaction (in Gwei).
 * @param {string} txHash - The transaction hash identifier.
 * @returns {string} A formatted string summarizing the transaction.
 *
 * Example usage:
 * const summary = generateTransactionSummary(
 *   '0xSenderAddress',
 *   '0xRecipientAddress',
 *   2.5,
 *   21,
 *   '0xTxHashExample'
 * );
 * console.log(summary);
 */
function generateTransactionSummary(from, to, amount, gasFee, txHash) {
  // Input validation
  if (!from || !to || !txHash || typeof amount !== 'number' || typeof gasFee !== 'number') {
    throw new Error('Invalid input: Ensure all parameters are correctly provided.');
  }

  // Generate a formatted transaction summary
  const summary = `
    Ethereum Transaction Summary:
    -----------------------------
    From Address: ${from}
    To Address: ${to}
    Amount Transferred: ${amount} ETH
    Gas Fee: ${gasFee} Gwei
    Transaction Hash: ${txHash}
    -----------------------------
  `;

  return summary.trim(); // Remove any extra whitespace from the formatted string
}

// Example usage:
// const summary = generateTransactionSummary(
//   '0xSenderAddress',
//   '0xRecipientAddress',
//   2.5,
//   21,
//   '0xTxHashExample'
// );
// console.log(summary);
```
