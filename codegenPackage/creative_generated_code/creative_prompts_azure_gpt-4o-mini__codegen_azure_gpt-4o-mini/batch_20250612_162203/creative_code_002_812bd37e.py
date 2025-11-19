"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-mars.pages.dev
Prompt: Create a JavaScript function that calculates the total supply and transaction tax for the DogeMars token, ensuring it adheres to the specified tokenomics.
Generated: DETERMINISTIC_812bd37e44c4b05d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateDogeMarsTax
 * @description Calculates the total supply and transaction tax for the DogeMars token.
 *              The tokenomics specify that for each transaction, a certain percentage is taken as tax.
 * @param {number} totalSupply - The total supply of the DogeMars token.
 * @param {number} transactionAmount - The amount being transacted.
 * @param {number} taxPercentage - The percentage of the transaction that will be taken as tax.
 * @returns {object} An object containing the total supply and the transaction tax.
 * @throws {Error} Throws an error if the inputs are invalid.
 */
function calculateDogeMarsTax(totalSupply, transactionAmount, taxPercentage) {
    // Validate input parameters
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error('Invalid total supply: must be a positive number.');
    }
    if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
        throw new Error('Invalid transaction amount: must be a positive number.');
    }
    if (typeof taxPercentage !== 'number' || taxPercentage < 0 || taxPercentage > 100) {
        throw new Error('Invalid tax percentage: must be between 0 and 100.');
    }

    // Calculate the transaction tax
    const transactionTax = (transactionAmount * taxPercentage) / 100;

    // Return the results
    return {
        totalSupply,
        transactionTax
    };
}

// Example usage:
try {
    const results = calculateDogeMarsTax(1000000000, 5000, 5);
    console.log('Total Supply:', results.totalSupply);
    console.log('Transaction Tax:', results.transactionTax);
} catch (error) {
    console.error('Error calculating tax:', error.message);
}
```
