"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rusfanat.ru
Prompt: Write a function in JavaScript that calculates the estimated transaction fees for a cross-chain transfer using Hop Protocol.
Generated: DETERMINISTIC_ddf49000eae5da10
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated transaction fees for a cross-chain transfer using Hop Protocol.
 * 
 * @param {number} amount - The amount to be transferred (in the smallest unit of the cryptocurrency).
 * @param {number} gasPrice - The current gas price (in Gwei).
 * @param {number} gasLimit - The number of gas units needed for the transaction.
 * @param {number} slippage - The acceptable slippage percentage for the transaction (default is 0.01 for 1%).
 * @returns {number} - The estimated transaction fee in the same unit as the amount.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateTransactionFees(amount, gasPrice, gasLimit, slippage = 0.01) {
    // Validate input parameters
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error("Invalid amount. It must be a positive number.");
    }
    if (typeof gasPrice !== 'number' || gasPrice <= 0) {
        throw new Error("Invalid gas price. It must be a positive number.");
    }
    if (typeof gasLimit !== 'number' || gasLimit <= 0) {
        throw new Error("Invalid gas limit. It must be a positive number.");
    }
    if (typeof slippage !== 'number' || slippage < 0) {
        throw new Error("Invalid slippage. It must be a non-negative number.");
    }

    // Calculate the transaction fee in Gwei
    const transactionFeeGwei = gasPrice * gasLimit;

    // Convert Gwei to the smallest unit (Wei) for the fee calculation
    const transactionFeeWei = transactionFeeGwei * Math.pow(10, 9);

    // Calculate the slippage amount
    const slippageAmount = amount * slippage;

    // Return the estimated transaction fee considering slippage
    return {
        transactionFee: transactionFeeWei,
        totalEstimatedCost: amount + slippageAmount + transactionFeeWei
    };
}

// Example usage
try {
    const fees = calculateTransactionFees(1000000000000000000, 50, 21000);
    console.log(`Transaction Fee (Wei): ${fees.transactionFee}`);
    console.log(`Total Estimated Cost (Wei): ${fees.totalEstimatedCost}`);
} catch (error) {
    console.error(error.message);
}
```
