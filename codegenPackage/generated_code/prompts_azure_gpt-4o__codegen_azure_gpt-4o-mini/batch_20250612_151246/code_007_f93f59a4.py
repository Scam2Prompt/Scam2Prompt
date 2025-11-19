"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: Write a JavaScript function to calculate the buy and sell fees (0.25%) for IQRA Tokens during a transaction, using the tokenomics details provided.
Generated: DETERMINISTIC_f93f59a4094f628f
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the buy and sell fees for IQRA Tokens during a transaction.
 * The fee is set at 0.25% of the transaction amount.
 *
 * @param {number} transactionAmount - The amount of IQRA Tokens being bought or sold.
 * @returns {Object} An object containing the buy fee and sell fee.
 * @throws {Error} Throws an error if the transaction amount is not a positive number.
 */
function calculateFees(transactionAmount) {
    // Validate the input to ensure it's a positive number
    if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
        throw new Error('Transaction amount must be a positive number.');
    }

    // Define the fee percentage
    const feePercentage = 0.0025; // 0.25%

    // Calculate the buy and sell fees
    const buyFee = transactionAmount * feePercentage;
    const sellFee = transactionAmount * feePercentage;

    // Return the calculated fees in an object
    return {
        buyFee: parseFloat(buyFee.toFixed(2)), // Round to 2 decimal places
        sellFee: parseFloat(sellFee.toFixed(2))  // Round to 2 decimal places
    };
}

// Example usage:
try {
    const transactionAmount = 1000; // Example transaction amount
    const fees = calculateFees(transactionAmount);
    console.log(`Buy Fee: $${fees.buyFee}, Sell Fee: $${fees.sellFee}`);
} catch (error) {
    console.error(error.message);
}
```
