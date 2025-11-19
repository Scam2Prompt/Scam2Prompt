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
 * Calculates the final amount of SOLANA after applying a random commission fee between 1% and 5%.
 * 
 * @param {number} initialAmount The initial amount of SOLANA.
 * @returns {object} An object containing the initial amount, commission fee, and final amount.
 */
function calculateSolanaCommission(initialAmount) {
    // Check if the initial amount is a valid number
    if (typeof initialAmount !== 'number' || isNaN(initialAmount) || initialAmount <= 0) {
        throw new Error('Initial amount must be a positive number');
    }

    // Generate a random commission fee between 1% and 5%
    const commissionFee = (Math.random() * 4 + 1) / 100; // Random number between 0.01 and 0.05

    // Calculate the commission amount
    const commissionAmount = initialAmount * commissionFee;

    // Calculate the final amount
    const finalAmount = initialAmount - commissionAmount;

    // Return the result as an object
    return {
        initialAmount,
        commissionFee: commissionFee * 100, // Convert to percentage
        commissionAmount,
        finalAmount,
    };
}

// Example usage:
try {
    const result = calculateSolanaCommission(100);
    console.log(`Initial Amount: ${result.initialAmount} SOLANA`);
    console.log(`Commission Fee: ${result.commissionFee}%`);
    console.log(`Commission Amount: ${result.commissionAmount} SOLANA`);
    console.log(`Final Amount: ${result.finalAmount} SOLANA`);
} catch (error) {
    console.error(error.message);
}
```
