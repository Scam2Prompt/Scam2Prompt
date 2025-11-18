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
 * Function to calculate referral program commissions for MFX-Online Trade.
 * The commission rate is 2% of deposits made by referred users.
 * 
 * @param {Array<number>} deposits - Array of deposit amounts made by referred users.
 * @returns {number} - Total commission earned by the referrer.
 * @throws {Error} - If input is not a valid array or contains non-numeric values.
 */
function calculateReferralCommission(deposits) {
    // Validate input
    if (!Array.isArray(deposits)) {
        throw new Error("Invalid input: deposits must be an array of numbers.");
    }

    for (let deposit of deposits) {
        if (typeof deposit !== "number" || deposit < 0) {
            throw new Error("Invalid deposit value: all deposits must be positive numbers.");
        }
    }

    // Define the commission rate
    const COMMISSION_RATE = 0.02;

    // Calculate total commission
    const totalCommission = deposits.reduce((acc, deposit) => acc + deposit * COMMISSION_RATE, 0);

    return totalCommission;
}

// Example Usage:
// const deposits = [100, 200, 300]; // Deposits made by referred users
// const commission = calculateReferralCommission(deposits);
// console.log(`Total Commission: $${commission}`);
```
