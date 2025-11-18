"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfxhk.com
Prompt: Create a function in JavaScript to calculate referral program commissions for MFX-Online Trade, where the commission rate is 2% of deposits made by referred users.
Generated: DETERMINISTIC_b4f7b6c24d90b5d1
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total commission earned from referred user deposits.
 * 
 * @param {Array<number>} deposits - An array of deposit amounts made by referred users.
 * @returns {number} - The total commission earned, calculated at a rate of 2%.
 * @throws {Error} - Throws an error if the deposits array is not an array or contains non-numeric values.
 */
function calculateReferralCommission(deposits) {
    // Validate input
    if (!Array.isArray(deposits)) {
        throw new Error("Invalid input: deposits should be an array.");
    }

    let totalCommission = 0;
    const commissionRate = 0.02; // 2% commission rate

    // Iterate over each deposit to calculate total commission
    for (let i = 0; i < deposits.length; i++) {
        const deposit = deposits[i];

        // Validate deposit to ensure it is a positive number
        if (typeof deposit !== 'number' || deposit < 0) {
            throw new Error(`Invalid deposit at index ${i}: must be a positive number.`);
        }

        totalCommission += deposit * commissionRate; // Calculate commission for this deposit
    }

    return totalCommission; // Return the total commission earned
}

// Example usage:
try {
    const userDeposits = [1000, 2000, 1500]; // Example deposits from referred users
    const commission = calculateReferralCommission(userDeposits);
    console.log(`Total commission earned: $${commission.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating commission: ${error.message}`);
}
```
