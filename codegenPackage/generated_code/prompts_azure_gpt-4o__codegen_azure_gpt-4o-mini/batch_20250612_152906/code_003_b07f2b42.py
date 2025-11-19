"""
Generated Code Metadata:
========================
Original URL: https://misturador-solana.com
Prompt: Create a function in JavaScript that calculates the final amount of SOLANA after applying a random commission fee between 1% and 5%, as described in the Solana mixing service.
Generated: DETERMINISTIC_b07f2b42ccd7d164
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the final amount of SOLANA after applying a random commission fee
 * between 1% and 5%.
 *
 * @param {number} initialAmount - The initial amount of SOLANA before commission.
 * @returns {number} - The final amount of SOLANA after commission.
 * @throws {Error} - Throws an error if the initial amount is not a positive number.
 */
function calculateFinalAmount(initialAmount) {
    // Validate the input to ensure it's a positive number
    if (typeof initialAmount !== 'number' || initialAmount <= 0) {
        throw new Error('Initial amount must be a positive number.');
    }

    // Generate a random commission fee between 1% and 5%
    const commissionPercentage = Math.random() * (0.05 - 0.01) + 0.01;

    // Calculate the commission amount
    const commissionAmount = initialAmount * commissionPercentage;

    // Calculate the final amount after deducting the commission
    const finalAmount = initialAmount - commissionAmount;

    // Return the final amount rounded to 6 decimal places for precision
    return parseFloat(finalAmount.toFixed(6));
}

// Example usage:
try {
    const initialAmount = 100; // Example initial amount of SOLANA
    const finalAmount = calculateFinalAmount(initialAmount);
    console.log(`Final amount of SOLANA after commission: ${finalAmount}`);
} catch (error) {
    console.error(error.message);
}
```
