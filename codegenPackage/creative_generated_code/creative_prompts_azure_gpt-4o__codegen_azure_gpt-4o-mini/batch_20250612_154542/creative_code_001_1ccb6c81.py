"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcoinners.com
Prompt: Create a function in JavaScript that calculates the referral bonus (5% or 7%) based on the deposit amount made by a referred user, as described on mcoinners.com.
Generated: DETERMINISTIC_1ccb6c816c2935cd
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the referral bonus based on the deposit amount.
 * 
 * Referral bonus is determined as follows:
 * - 5% for deposits up to $1,000
 * - 7% for deposits above $1,000
 *
 * @param {number} depositAmount - The deposit amount made by the referred user.
 * @returns {number} - The calculated referral bonus.
 * @throws {Error} - Throws an error if the depositAmount is not a positive number.
 */
function calculateReferralBonus(depositAmount) {
    // Validate the input to ensure it is a number and greater than 0
    if (typeof depositAmount !== 'number' || depositAmount <= 0) {
        throw new Error('Invalid deposit amount. It must be a positive number.');
    }

    let bonusPercentage;
    
    // Determine the bonus percentage based on the deposit amount
    if (depositAmount <= 1000) {
        bonusPercentage = 0.05; // 5% for deposits up to $1,000
    } else {
        bonusPercentage = 0.07; // 7% for deposits above $1,000
    }

    // Calculate and return the referral bonus
    const referralBonus = depositAmount * bonusPercentage;
    return referralBonus;
}

// Example usage:
try {
    const deposit = 1200; // Example deposit amount
    const bonus = calculateReferralBonus(deposit);
    console.log(`The referral bonus for a deposit of $${deposit} is $${bonus.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
