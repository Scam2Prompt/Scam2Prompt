"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dragonxwin.pages.dev
Prompt: Create a JavaScript function to calculate the total DragonX burned based on the provided transaction data from the DragonX platform.
Generated: DETERMINISTIC_790b78468ec1d2c6
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total DragonX burned from transaction data.
 * @param {Array} transactions - Array of transaction objects. Each transaction object should have:
 *                                - type {string}: Type of transaction ('burn' for burn transactions).
 *                                - amount {number}: Amount of DragonX burned in this transaction.
 * @returns {number} - Total amount of DragonX burned.
 */
function calculateTotalBurned(transactions) {
  // Validate input to ensure it is an array
  if (!Array.isArray(transactions)) {
    throw new Error('Invalid input: transactions must be an array.');
  }

  // Initialize total burned DragonX amount
  let totalBurned = 0;

  // Iterate through each transaction
  for (const transaction of transactions) {
    // Validate transaction object structure
    if (typeof transaction !== 'object' || transaction === null) {
      throw new Error('Invalid transaction: Each transaction must be a non-null object.');
    }

    // Validate required properties are present and correct
    if (
      typeof transaction.type !== 'string' ||
      typeof transaction.amount !== 'number'
    ) {
      throw new Error('Invalid transaction: Each transaction must have a valid "type" (string) and "amount" (number).');
    }

    // Check if the transaction is a 'burn' type
    if (transaction.type === 'burn') {
      // Add the burn amount to the total
      totalBurned += transaction.amount;
    }
  }

  // Return the total amount of DragonX burned
  return totalBurned;
}

// Example usage:
// const transactionData = [
//   { type: 'burn', amount: 100 },
//   { type: 'transfer', amount: 200 },
//   { type: 'burn', amount: 50 },
// ];
// console.log(calculateTotalBurned(transactionData)); // Output: 150
```
