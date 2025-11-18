"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maradonacoinz.vercel.app
Prompt: Write a function in JavaScript to calculate the tokenomics of the "Hand of Pepe" token, including the 1% transaction tax, and display the net amount received after a transfer.
Generated: DETERMINISTIC_9df237e5ea952315
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the net amount received after a transfer of the "Hand of Pepe" token.
 * This function takes into account a 1% transaction tax.
 * 
 * @param {number} amount - The amount of tokens to be transferred.
 * @returns {number} - The net amount received after applying the transaction tax.
 * @throws {Error} - Throws an error if the amount is negative or not a number.
 */
function calculateNetAmount(amount) {
    // Validate the input
    if (typeof amount !== 'number') {
        throw new Error('Invalid input: Amount must be a number.');
    }
    
    if (amount < 0) {
        throw new Error('Invalid input: Amount cannot be negative.');
    }

    // Define the transaction tax rate
    const TAX_RATE = 0.01;

    // Calculate the transaction tax
    const transactionTax = amount * TAX_RATE;

    // Calculate the net amount after tax
    const netAmount = amount - transactionTax;

    // Return the net amount, rounded to 2 decimal places
    return parseFloat(netAmount.toFixed(2));
}

// Example usage:
try {
    const amountToTransfer = 100; // Example amount
    const netAmountReceived = calculateNetAmount(amountToTransfer);
    console.log(`Net amount received after transfer: ${netAmountReceived}`);
} catch (error) {
    console.error(error.message);
}
```
