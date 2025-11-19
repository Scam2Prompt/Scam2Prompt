"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babywif-io.pages.dev
Prompt: Create a JavaScript function to calculate the transaction fees for buying Baby WIF tokens, considering the 5% tax distribution for liquidity, marketing, and development.
Generated: DETERMINISTIC_81555c94e5ecdee8
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the transaction fees for buying Baby WIF tokens.
 * The total fee is split into three categories: liquidity, marketing, and development.
 * Each category receives an equal share of the total transaction fee.
 *
 * @param {number} transactionAmount - The amount of Baby WIF tokens being purchased.
 * @returns {Object} An object containing the fees for liquidity, marketing, and development.
 * @throws {Error} Throws an error if the transaction amount is negative or not a number.
 */
function calculateTransactionFees(transactionAmount) {
    // Validate input
    if (typeof transactionAmount !== 'number') {
        throw new Error('Transaction amount must be a number.');
    }
    if (transactionAmount < 0) {
        throw new Error('Transaction amount cannot be negative.');
    }

    // Define the total tax rate
    const taxRate = 0.05; // 5% tax
    const totalTax = transactionAmount * taxRate;

    // Calculate fees for each category (liquidity, marketing, development)
    const liquidityFee = totalTax / 3; // Equal split
    const marketingFee = totalTax / 3; // Equal split
    const developmentFee = totalTax / 3; // Equal split

    // Return the calculated fees in an object
    return {
        liquidityFee: parseFloat(liquidityFee.toFixed(2)), // Round to two decimal places
        marketingFee: parseFloat(marketingFee.toFixed(2)), // Round to two decimal places
        developmentFee: parseFloat(developmentFee.toFixed(2)), // Round to two decimal places
    };
}

// Example usage
try {
    const fees = calculateTransactionFees(100);
    console.log('Transaction Fees:', fees);
} catch (error) {
    console.error('Error calculating transaction fees:', error.message);
}
```
