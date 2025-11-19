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
 * Calculates the total DragonX burned based on transaction data.
 * 
 * @param {Array<Object>} transactions - An array of transaction objects.
 * Each transaction should have a 'type' property and a 'amount' property.
 * @param {string} transactionType - The type of transaction to consider for calculating burned DragonX.
 * @returns {number} The total amount of DragonX burned.
 * @throws {TypeError} Throws error if transactions is not an array or if transactionType is not a string.
 */
function calculateTotalDragonXBurned(transactions, transactionType) {
    // Validate input types
    if (!Array.isArray(transactions)) {
        throw new TypeError('Expected transactions to be an array.');
    }
    if (typeof transactionType !== 'string') {
        throw new TypeError('Expected transactionType to be a string.');
    }

    // Initialize total burned amount
    let totalBurned = 0;

    // Iterate over each transaction
    for (const transaction of transactions) {
        // Validate transaction structure
        if (typeof transaction !== 'object' || transaction === null) {
            console.warn('Invalid transaction format:', transaction);
            continue; // Skip invalid transaction
        }

        const { type, amount } = transaction;

        // Check if the transaction is of the specified type and amount is valid
        if (type === transactionType && typeof amount === 'number' && amount > 0) {
            totalBurned += amount;
        } else {
            console.warn(`Skipping transaction, type: ${type}, amount: ${amount}`);
        }
    }

    return totalBurned;
}

// Example usage
try {
    const transactions = [
        { type: 'burn', amount: 100 },
        { type: 'stake', amount: 50 },
        { type: 'burn', amount: 200 },
        { type: 'transfer', amount: 30 },
        { type: 'burn', amount: -50 }, // Invalid amount, should be skipped
        { type: 'burn', amount: 150 }
    ];

    const burnedAmount = calculateTotalDragonXBurned(transactions, 'burn');
    console.log(`Total DragonX burned: ${burnedAmount}`);
} catch (error) {
    console.error('Error calculating burned DragonX:', error.message);
}
```
