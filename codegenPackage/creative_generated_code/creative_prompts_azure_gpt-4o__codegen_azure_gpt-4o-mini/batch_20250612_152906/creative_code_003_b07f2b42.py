"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://misturador-solana.com
Prompt: Create a function in JavaScript that calculates the final amount of SOLANA after applying a random commission fee between 1% and 5%, as described in the Solana mixing service.
Generated: DETERMINISTIC_b07f2b42ccd7d164
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the final amount of SOLANA after applying a random commission fee
 * between 1% and 5%.
 * 
 * @param {number} initialAmount - The initial amount of SOLANA before fees.
 * @returns {number} The final amount of SOLANA after applying the commission fee.
 * @throws {Error} Throws an error if the initial amount is not a positive number.
 */
function calculateFinalAmount(initialAmount) {
    // Validate input
    if (typeof initialAmount !== 'number' || initialAmount <= 0) {
        throw new Error('Initial amount must be a positive number.');
    }

    // Generate a random commission fee between 1% (0.01) and 5% (0.05)
    const commissionPercentage = Math.random() * (0.05 - 0.01) + 0.01;

    // Calculate the final amount after applying the commission fee
    const commissionFee = initialAmount * commissionPercentage;
    const finalAmount = initialAmount - commissionFee;

    // Return the final amount rounded to 6 decimal places
    return parseFloat(finalAmount.toFixed(6));
}

// Example usage:
try {
    const initial = 100; // Example initial amount in SOLANA
    const final = calculateFinalAmount(initial);
    console.log(`Final amount after commission: ${final} SOL`);
} catch (error) {
    console.error(error.message);
}
```
