"""
Generated Code Metadata:
========================
Original URL: https://misturador-solana.com
Prompt: Generate a code snippet in JavaScript to calculate the total cost of a SOLANA transaction using the Misturador Solana service, including a random fee between 1% and 5%.
Generated: DETERMINISTIC_b4373bb5237892fe
Batch ID: 20250622_210423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a SOLANA transaction using the Misturador Solana service,
 * including a random fee between 1% and 5%.
 * 
 * @param {number} transactionAmount The amount of the transaction in SOLANA.
 * @returns {object} An object containing the transaction amount, fee, and total cost.
 */

function calculateTransactionCost(transactionAmount) {
    // Check if transaction amount is a positive number
    if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
        throw new Error('Transaction amount must be a positive number');
    }

    // Generate a random fee between 1% and 5%
    const minFee = 0.01; // 1%
    const maxFee = 0.05; // 5%
    const fee = Math.random() * (maxFee - minFee) + minFee;

    // Calculate the transaction fee
    const transactionFee = transactionAmount * fee;

    // Calculate the total cost
    const totalCost = transactionAmount + transactionFee;

    // Return the transaction details
    return {
        transactionAmount,
        fee: `${(fee * 100).toFixed(2)}%`,
        transactionFee: transactionFee.toFixed(2),
        totalCost: totalCost.toFixed(2),
    };
}

// Example usage
try {
    const transactionAmount = 10.0;
    const transactionDetails = calculateTransactionCost(transactionAmount);
    console.log(`Transaction Amount: ${transactionDetails.transactionAmount} SOLANA`);
    console.log(`Fee: ${transactionDetails.fee}`);
    console.log(`Transaction Fee: ${transactionDetails.transactionFee} SOLANA`);
    console.log(`Total Cost: ${transactionDetails.totalCost} SOLANA`);
} catch (error) {
    console.error(error.message);
}
```
