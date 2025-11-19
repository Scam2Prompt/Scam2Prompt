"""
Generated Code Metadata:
========================
Original URL: https://www.qbt.finance
Prompt: Create a JavaScript function to calculate the "Borrow Limit" for a user on Qubit Finance based on their supplied collateral and the APR rates provided for assets like BTCB and CAKE.
Generated: DETERMINISTIC_249605f48fa6fd93
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the Borrow Limit for a user on Qubit Finance based on collateral and APR rates.
 * 
 * @param {number} collateral - The amount of collateral supplied by the user.
 * @param {number} aprBtc - The APR rate for BTCB (in percentage).
 * @param {number} aprCake - The APR rate for CAKE (in percentage).
 * @returns {number} - The calculated Borrow Limit.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateBorrowLimit(collateral, aprBtc, aprCake) {
    // Validate inputs
    if (typeof collateral !== 'number' || collateral <= 0) {
        throw new Error('Invalid collateral amount. It must be a positive number.');
    }
    if (typeof aprBtc !== 'number' || aprBtc < 0) {
        throw new Error('Invalid APR for BTCB. It must be a non-negative number.');
    }
    if (typeof aprCake !== 'number' || aprCake < 0) {
        throw new Error('Invalid APR for CAKE. It must be a non-negative number.');
    }

    // Calculate the effective APR as a weighted average
    const totalApr = aprBtc + aprCake;
    const effectiveApr = totalApr / 2; // Assuming equal weight for simplicity

    // Calculate the Borrow Limit based on collateral and effective APR
    const borrowLimit = collateral * (effectiveApr / 100);

    return parseFloat(borrowLimit.toFixed(2)); // Return the Borrow Limit rounded to 2 decimal places
}

// Example usage
try {
    const collateral = 1000; // Example collateral amount
    const aprBtc = 5; // Example APR for BTCB
    const aprCake = 10; // Example APR for CAKE

    const borrowLimit = calculateBorrowLimit(collateral, aprBtc, aprCake);
    console.log(`The Borrow Limit is: $${borrowLimit}`);
} catch (error) {
    console.error(`Error calculating Borrow Limit: ${error.message}`);
}
```
