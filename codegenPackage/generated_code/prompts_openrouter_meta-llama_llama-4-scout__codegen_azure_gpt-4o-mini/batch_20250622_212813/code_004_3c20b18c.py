"""
Generated Code Metadata:
========================
Original URL: https://guardian-associates.com
Prompt: "Create a function in Node.js that takes transaction data and calculates the optimal Rolling Reserve percentage for a business, considering factors discussed in the Guardian Associates' risk assessment process."
Generated: DETERMINISTIC_3c20b18c34287e2c
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the optimal Rolling Reserve percentage for a business based on transaction data.
 * 
 * @param {Array<Object>} transactions - An array of transaction objects, each containing:
 *   - {number} amount - The transaction amount.
 *   - {string} status - The status of the transaction (e.g., 'completed', 'refunded', 'chargeback').
 * @param {number} baseReservePercentage - The base reserve percentage to start calculations.
 * @returns {number} - The optimal Rolling Reserve percentage.
 * @throws {Error} - Throws an error if the input data is invalid.
 */
function calculateOptimalRollingReserve(transactions, baseReservePercentage) {
    // Validate input parameters
    if (!Array.isArray(transactions) || transactions.length === 0) {
        throw new Error('Invalid transactions data: must be a non-empty array.');
    }
    if (typeof baseReservePercentage !== 'number' || baseReservePercentage < 0 || baseReservePercentage > 100) {
        throw new Error('Invalid base reserve percentage: must be a number between 0 and 100.');
    }

    let totalAmount = 0;
    let totalChargebacks = 0;
    let totalRefunds = 0;

    // Process each transaction to calculate totals
    transactions.forEach(transaction => {
        if (typeof transaction.amount !== 'number' || transaction.amount < 0) {
            throw new Error('Invalid transaction amount: must be a non-negative number.');
        }
        totalAmount += transaction.amount;

        switch (transaction.status) {
            case 'chargeback':
                totalChargebacks += transaction.amount;
                break;
            case 'refunded':
                totalRefunds += transaction.amount;
                break;
            case 'completed':
                // No action needed for completed transactions
                break;
            default:
                throw new Error(`Invalid transaction status: ${transaction.status}`);
        }
    });

    // Calculate chargeback and refund ratios
    const chargebackRatio = totalChargebacks / totalAmount || 0;
    const refundRatio = totalRefunds / totalAmount || 0;

    // Calculate the optimal Rolling Reserve percentage
    const optimalReservePercentage = baseReservePercentage + (chargebackRatio * 100) + (refundRatio * 100);

    // Ensure the reserve percentage does not exceed 100%
    return Math.min(optimalReservePercentage, 100);
}

// Example usage
try {
    const transactions = [
        { amount: 100, status: 'completed' },
        { amount: 50, status: 'chargeback' },
        { amount: 30, status: 'refunded' },
        { amount: 200, status: 'completed' }
    ];
    const baseReservePercentage = 10;
    const optimalReserve = calculateOptimalRollingReserve(transactions, baseReservePercentage);
    console.log(`Optimal Rolling Reserve Percentage: ${optimalReserve}%`);
} catch (error) {
    console.error(`Error calculating optimal reserve: ${error.message}`);
}
```
