"""
Generated Code Metadata:
========================
Original URL: https://ton-coin-mixer.com
Prompt: Develop a simple fee calculator in JavaScript for a TONCOIN mixing service, taking into account a fixed fee of 0.001 TONCOIN and a variable fee of less than 2% on the remaining amount.
Generated: DETERMINISTIC_b23bbf4817adfdc5
Batch ID: 20250622_210423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TONCOIN Mixing Service Fee Calculator
 * 
 * Calculates the total fee for mixing TONCOIN, consisting of:
 * - A fixed fee: 0.001 TONCOIN
 * - A variable fee: less than 2% of the remaining amount after fixed fee
 * 
 * @param {number} amount - The amount of TONCOIN to be mixed
 * @returns {object} An object containing:
 *   - fixedFee: The fixed fee amount
 *   - variableFee: The variable fee amount
 *   - totalFee: The sum of fixed and variable fees
 *   - amountAfterFees: The remaining amount after all fees
 * @throws {Error} If input is invalid (non-number, negative, or insufficient amount)
 */
function calculateMixingFees(amount) {
    // Validate input
    if (typeof amount !== 'number' || isNaN(amount)) {
        throw new Error('Invalid input: amount must be a number');
    }
    
    if (amount <= 0) {
        throw new Error('Invalid input: amount must be positive');
    }

    const FIXED_FEE = 0.001; // Fixed fee in TONCOIN
    const MAX_VARIABLE_FEE_PERCENT = 2; // Maximum variable fee percentage

    // Check if amount is sufficient to cover fixed fee
    if (amount <= FIXED_FEE) {
        throw new Error(`Insufficient amount: must be greater than fixed fee (${FIXED_FEE} TON)`);
    }

    // Calculate variable fee (random between 0% and 2% of remaining amount)
    const remainingAfterFixed = amount - FIXED_FEE;
    const variableFeePercent = Math.random() * MAX_VARIABLE_FEE_PERCENT;
    const variableFee = remainingAfterFixed * (variableFeePercent / 100);

    // Calculate total fees and remaining amount
    const totalFee = FIXED_FEE + variableFee;
    const amountAfterFees = amount - totalFee;

    // Return results with precise decimal places
    return {
        fixedFee: parseFloat(FIXED_FEE.toFixed(6)),
        variableFee: parseFloat(variableFee.toFixed(6)),
        variableFeePercent: parseFloat(variableFeePercent.toFixed(2)),
        totalFee: parseFloat(totalFee.toFixed(6)),
        amountAfterFees: parseFloat(amountAfterFees.toFixed(6))
    };
}

// Example usage with error handling
try {
    const amount = 1.5; // Example amount in TONCOIN
    const fees = calculateMixingFees(amount);
    console.log('Fee Calculation Results:');
    console.log(`Input Amount: ${amount} TON`);
    console.log(`Fixed Fee: ${fees.fixedFee} TON`);
    console.log(`Variable Fee: ${fees.variableFee} TON (${fees.variableFeePercent}%)`);
    console.log(`Total Fee: ${fees.totalFee} TON`);
    console.log(`Amount After Fees: ${fees.amountAfterFees} TON`);
} catch (error) {
    console.error('Error calculating fees:', error.message);
}
```
