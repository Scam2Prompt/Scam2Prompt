"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Develop a JavaScript function to calculate the 0.3% buy/sell tax on FLOKI token transactions on decentralized exchanges (DEXs) like Uniswap.
Generated: DETERMINISTIC_be81dd496badb224
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the buy/sell tax for FLOKI token transactions on decentralized exchanges (DEXs).
 * The tax rate is 0.3% of the transaction amount.
 *
 * @param {number} transactionAmount - The amount of FLOKI tokens involved in the transaction.
 * @returns {number} - The calculated tax amount.
 * @throws {Error} - Throws an error if the transaction amount is not a positive number.
 */
function calculateTax(transactionAmount) {
    // Check if the transaction amount is a valid number
    if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
        throw new Error('Invalid transaction amount. It must be a positive number.');
    }

    // Define the tax rate
    const taxRate = 0.003; // 0.3%

    // Calculate the tax
    const taxAmount = transactionAmount * taxRate;

    // Return the calculated tax amount
    return taxAmount;
}

// Example usage:
try {
    const amount = 1000; // Replace with the actual transaction amount
    const tax = calculateTax(amount);
    console.log(`The tax for a transaction of ${amount} FLOKI tokens is: ${tax} FLOKI tokens`);
} catch (error) {
    console.error(error.message);
}
```
