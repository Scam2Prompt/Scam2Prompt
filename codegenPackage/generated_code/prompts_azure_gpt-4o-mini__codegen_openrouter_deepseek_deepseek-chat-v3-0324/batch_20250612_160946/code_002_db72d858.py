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
 * Calculates the transaction tax for buying Super Trump Coin based on tokenomics.
 * 
 * @param {number} amount - The amount of Super Trump Coin being purchased.
 * @param {object} taxRates - Object containing the different tax rates.
 * @param {number} taxRates.buyTax - Tax rate for buying (in percentage).
 * @param {number} taxRates.sellTax - Tax rate for selling (in percentage).
 * @param {number} taxRates.transferTax - Tax rate for transferring (in percentage).
 * @param {string} transactionType - Type of transaction ('buy', 'sell', or 'transfer').
 * @returns {object} An object containing the tax amount and the net amount after tax.
 * @throws {Error} If input validation fails.
 */
function calculateSuperTrumpCoinTax(amount, taxRates, transactionType) {
    // Input validation
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Amount must be a positive number');
    }
    
    if (!taxRates || typeof taxRates !== 'object') {
        throw new Error('Tax rates must be provided as an object');
    }
    
    const requiredTaxFields = ['buyTax', 'sellTax', 'transferTax'];
    for (const field of requiredTaxFields) {
        if (typeof taxRates[field] !== 'number' || taxRates[field] < 0) {
            throw new Error(`Invalid tax rate for ${field}`);
        }
    }
    
    const validTransactionTypes = ['buy', 'sell', 'transfer'];
    if (!validTransactionTypes.includes(transactionType)) {
        throw new Error('Transaction type must be "buy", "sell", or "transfer"');
    }
    
    // Calculate tax based on transaction type
    let taxRate;
    switch (transactionType) {
        case 'buy':
            taxRate = taxRates.buyTax;
            break;
        case 'sell':
            taxRate = taxRates.sellTax;
            break;
        case 'transfer':
            taxRate = taxRates.transferTax;
            break;
    }
    
    const taxAmount = amount * (taxRate / 100);
    const netAmount = amount - taxAmount;
    
    return {
        originalAmount: amount,
        taxRate: taxRate,
        taxAmount: taxAmount,
        netAmount: netAmount
    };
}

// Example usage:
// const taxRates = {
//     buyTax: 5,
//     sellTax: 10,
//     transferTax: 2
// };
// const result = calculateSuperTrumpCoinTax(1000, taxRates, 'buy');
// console.log(result);
```
