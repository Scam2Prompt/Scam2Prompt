"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: Write a JavaScript function to calculate the buy and sell fees (0.25%) for IQRA Tokens during a transaction, using the tokenomics details provided.
Generated: DETERMINISTIC_f93f59a4094f628f
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the buy and sell fees for IQRA Tokens during a transaction.
 * The fee is set at 0.25% of the transaction amount.
 *
 * @param {number} amount - The amount of IQRA Tokens to buy or sell.
 * @returns {Object} An object containing the buy fee, sell fee, and total transaction cost.
 * @throws {Error} Throws an error if the amount is not a positive number.
 */
function calculateTransactionFees(amount) {
    // Validate the input amount to ensure it's a positive number
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Amount must be a positive number.');
    }

    // Define the fee percentage
    const feePercentage = 0.0025; // 0.25%

    // Calculate the buy fee and sell fee
    const buyFee = amount * feePercentage;
    const sellFee = amount * feePercentage;

    // Calculate total transaction costs
    const totalBuyCost = amount + buyFee;
    const totalSellCost = amount - sellFee;

    // Return the calculated fees and transaction costs
    return {
        buyFee: buyFee.toFixed(4),     // Format the fee to 4 decimal places
        sellFee: sellFee.toFixed(4),   // Format the fee to 4 decimal places
        totalBuyCost: totalBuyCost.toFixed(4), // Total cost including buy fee
        totalSellCost: totalSellCost.toFixed(4) // Total cost after selling
    };
}

// Example usage:
try {
    const transactionDetails = calculateTransactionFees(1000);
    console.log(transactionDetails);
} catch (error) {
    console.error('Error calculating transaction fees:', error.message);
}
```
