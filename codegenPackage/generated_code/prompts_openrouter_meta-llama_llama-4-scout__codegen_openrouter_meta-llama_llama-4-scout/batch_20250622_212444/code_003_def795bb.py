"""
Generated Code Metadata:
========================
Original URL: https://solana-mixer.org
Prompt: Generate a code snippet in JavaScript to calculate the processing cost for mixing a certain amount of SOL, taking into account the 2% fee for amounts above 15 SOL and the 3% fee for amounts below 15 SOL.
Generated: DETERMINISTIC_def795bbe21a7fe2
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the processing cost for mixing a certain amount of SOL.
 * 
 * @param {number} amount - The amount of SOL to mix.
 * @returns {object} An object containing the total cost and the fee applied.
 */
function calculateProcessingCost(amount) {
    // Check if the amount is a valid number
    if (typeof amount !== 'number' || isNaN(amount)) {
        throw new Error('Invalid amount. Please enter a valid number.');
    }

    // Check if the amount is below 0
    if (amount < 0) {
        throw new Error('Invalid amount. Please enter a non-negative number.');
    }

    let fee = 0;
    let totalCost = 0;

    // Apply 2% fee for amounts above 15 SOL
    if (amount > 15) {
        fee = amount * 0.02;
        totalCost = amount + fee;
    } 
    // Apply 3% fee for amounts below or equal to 15 SOL
    else {
        fee = amount * 0.03;
        totalCost = amount + fee;
    }

    return {
        totalCost: totalCost,
        fee: fee
    };
}

// Example usage:
try {
    const amount = 10; // SOL
    const result = calculateProcessingCost(amount);
    console.log(`For ${amount} SOL, the total cost is ${result.totalCost} SOL and the fee is ${result.fee} SOL.`);
} catch (error) {
    console.error(error.message);
}
```
