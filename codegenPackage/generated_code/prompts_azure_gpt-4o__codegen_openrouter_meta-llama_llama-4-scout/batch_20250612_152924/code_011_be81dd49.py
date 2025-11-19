"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Develop a JavaScript function to calculate the 0.3% buy/sell tax on FLOKI token transactions on decentralized exchanges (DEXs) like Uniswap.
Generated: DETERMINISTIC_be81dd496badb224
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the 0.3% buy/sell tax on FLOKI token transactions.
 * 
 * @param {number} transactionAmount - The amount of FLOKI tokens being transacted.
 * @returns {number} The calculated tax amount.
 */
function calculateFlokiTax(transactionAmount) {
    // Check if transaction amount is a valid number
    if (typeof transactionAmount !== 'number' || isNaN(transactionAmount)) {
        throw new Error('Transaction amount must be a valid number');
    }

    // Check if transaction amount is non-negative
    if (transactionAmount < 0) {
        throw new Error('Transaction amount cannot be negative');
    }

    // Define the tax rate as a constant
    const TAX_RATE = 0.003; // 0.3%

    // Calculate the tax amount
    const taxAmount = transactionAmount * TAX_RATE;

    return taxAmount;
}

/**
 * Calculates the total transaction cost including tax.
 * 
 * @param {number} transactionAmount - The amount of FLOKI tokens being transacted.
 * @returns {object} An object containing the transaction amount, tax amount, and total transaction cost.
 */
function calculateTotalTransactionCost(transactionAmount) {
    try {
        const taxAmount = calculateFlokiTax(transactionAmount);
        const totalTransactionCost = transactionAmount + taxAmount;

        return {
            transactionAmount,
            taxAmount,
            totalTransactionCost
        };
    } catch (error) {
        throw new Error(`Failed to calculate total transaction cost: ${error.message}`);
    }
}

// Example usage:
function main() {
    const transactionAmount = 1000; // Example transaction amount
    try {
        const result = calculateTotalTransactionCost(transactionAmount);
        console.log(`Transaction Amount: ${result.transactionAmount}`);
        console.log(`Tax Amount: ${result.taxAmount}`);
        console.log(`Total Transaction Cost: ${result.totalTransactionCost}`);
    } catch (error) {
        console.error(error.message);
    }
}

main();
```
