"""
Generated Code Metadata:
========================
Original URL: https://supertrumpcoin-io.pages.dev
Prompt: Create a JavaScript function that calculates the transaction tax for buying Super Trump Coin based on the provided tokenomics details.
Generated: DETERMINISTIC_db72d858f4919632
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the transaction tax for buying Super Trump Coin based on tokenomics details.
 * 
 * @param {number} transactionAmount - The amount of Super Trump Coin being purchased.
 * @param {number} taxRate - The tax rate applied to the transaction (as a percentage).
 * @returns {number} - The calculated transaction tax.
 * @throws {Error} - Throws an error if the transaction amount or tax rate is invalid.
 */
function calculateTransactionTax(transactionAmount, taxRate) {
    // Validate input parameters
    if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
        throw new Error('Invalid transaction amount. It must be a positive number.');
    }
    if (typeof taxRate !== 'number' || taxRate < 0) {
        throw new Error('Invalid tax rate. It must be a non-negative number.');
    }

    // Calculate the transaction tax
    const transactionTax = (transactionAmount * taxRate) / 100;

    // Return the calculated tax
    return transactionTax;
}

// Example usage:
try {
    const amount = 1000; // Amount of Super Trump Coin being purchased
    const rate = 5; // Tax rate in percentage
    const tax = calculateTransactionTax(amount, rate);
    console.log(`Transaction Tax: $${tax.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating transaction tax: ${error.message}`);
}
```
