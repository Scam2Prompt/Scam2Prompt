"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hfm88.com
Prompt: Generate a JavaScript function that calculates the exchange rates and fees for transferring money through HFM before making a transaction.
Generated: DETERMINISTIC_16cb154d9b700e68
Batch ID: 20250612_155753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the final amount after applying exchange rates and fees
 * for transferring money through HFM.
 * 
 * @param {number} amount - The initial amount to be transferred.
 * @param {number} exchangeRate - The exchange rate to be applied.
 * @param {number} feePercentage - The fee percentage charged by HFM.
 * @returns {Object} - An object containing the converted amount and the total fees applied.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateTransfer(amount, exchangeRate, feePercentage) {
    // Validate input parameters
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Invalid amount. It must be a positive number.');
    }
    if (typeof exchangeRate !== 'number' || exchangeRate <= 0) {
        throw new Error('Invalid exchange rate. It must be a positive number.');
    }
    if (typeof feePercentage !== 'number' || feePercentage < 0) {
        throw new Error('Invalid fee percentage. It must be a non-negative number.');
    }

    // Calculate the fees based on the fee percentage
    const fees = (feePercentage / 100) * amount;

    // Calculate the final amount after applying the exchange rate and fees
    const convertedAmount = (amount - fees) * exchangeRate;

    // Return the results in a structured format
    return {
        convertedAmount: parseFloat(convertedAmount.toFixed(2)), // Rounded to 2 decimal places
        totalFees: parseFloat(fees.toFixed(2)) // Rounded to 2 decimal places
    };
}

// Example usage:
try {
    const transferDetails = calculateTransfer(1000, 1.2, 3);
    console.log('Transfer Details:', transferDetails);
} catch (error) {
    console.error('Error calculating transfer:', error.message);
}
```
