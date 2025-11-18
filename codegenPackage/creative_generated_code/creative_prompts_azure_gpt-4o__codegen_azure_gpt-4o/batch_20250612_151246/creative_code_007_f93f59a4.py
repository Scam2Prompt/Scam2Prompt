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
 * Calculate the buy and sell fees for IQRA Tokens during a transaction.
 * 
 * Tokenomics Details:
 * - Buy Fee: 0.25% of the transaction amount
 * - Sell Fee: 0.25% of the transaction amount
 * 
 * @param {number} transactionAmount - The amount of IQRA Tokens being transacted.
 * @param {string} transactionType - The type of transaction, either 'buy' or 'sell'.
 * @returns {number} The fee amount for the transaction.
 * @throws {Error} If transaction amount is not a positive number or transaction type is invalid.
 */
function calculateIQRAFees(transactionAmount, transactionType) {
    // Validate transactionAmount
    if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
        throw new Error("Transaction amount must be a positive number.");
    }

    // Validate transactionType
    if (transactionType !== 'buy' && transactionType !== 'sell') {
        throw new Error("Transaction type must be either 'buy' or 'sell'.");
    }

    // Define the fee rate (0.25%)
    const feeRate = 0.0025;

    // Calculate the fee
    const fee = transactionAmount * feeRate;

    // Return the calculated fee
    return fee;
}

// Example Usage:
try {
    const buyFee = calculateIQRAFees(1000, 'buy');  // Calculate fee for a buy transaction
    console.log(`Buy Fee: ${buyFee}`);             // Output: Buy Fee: 2.5

    const sellFee = calculateIQRAFees(2000, 'sell'); // Calculate fee for a sell transaction
    console.log(`Sell Fee: ${sellFee}`);            // Output: Sell Fee: 5
} catch (error) {
    console.error(error.message);  // Handle any errors
}
```
