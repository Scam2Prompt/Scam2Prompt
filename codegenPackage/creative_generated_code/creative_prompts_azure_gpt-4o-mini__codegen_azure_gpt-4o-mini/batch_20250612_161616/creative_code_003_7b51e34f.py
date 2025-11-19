"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogemarsclaim.pages.dev
Prompt: Develop a JavaScript function that calculates the total supply and transaction tax for DogeMars ($MARS) based on the tokenomics described on the DogeMars webpage.
Generated: DETERMINISTIC_7b51e34f97d99e40
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total supply and transaction tax for DogeMars ($MARS).
 * 
 * @param {number} totalSupply - The total supply of $MARS tokens.
 * @param {number} transactionAmount - The amount of $MARS being transacted.
 * @param {number} transactionTaxRate - The tax rate applied to each transaction (in percentage).
 * @returns {Object} - An object containing total supply and total transaction tax.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateDogeMarsTokenomics(totalSupply, transactionAmount, transactionTaxRate) {
    // Validate input parameters
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error('Invalid total supply: must be a positive number.');
    }
    if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
        throw new Error('Invalid transaction amount: must be a positive number.');
    }
    if (typeof transactionTaxRate !== 'number' || transactionTaxRate < 0) {
        throw new Error('Invalid transaction tax rate: must be a non-negative number.');
    }

    // Calculate the total transaction tax
    const transactionTax = (transactionAmount * transactionTaxRate) / 100;

    // Return an object containing the total supply and transaction tax
    return {
        totalSupply: totalSupply,
        transactionTax: parseFloat(transactionTax.toFixed(2)) // Round to two decimal places
    };
}

// Example usage:
try {
    const tokenomics = calculateDogeMarsTokenomics(1000000000, 500, 5);
    console.log(`Total Supply: $${tokenomics.totalSupply}, Transaction Tax: $${tokenomics.transactionTax}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
