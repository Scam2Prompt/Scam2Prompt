"""
Generated Code Metadata:
========================
Original URL: https://mcoinners.com
Prompt: Create a function in JavaScript that calculates the referral bonus (5% or 7%) based on the deposit amount made by a referred user, as described on mcoinners.com.
Generated: DETERMINISTIC_1ccb6c816c2935cd
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the referral bonus based on the deposit amount made by a referred user.
 * 
 * @param {number} depositAmount The deposit amount made by the referred user.
 * @param {string} userType The type of user, either 'new' or 'existing'. 
 *                         New users get a 7% bonus, existing users get a 5% bonus.
 * @returns {number} The referral bonus amount.
 */
function calculateReferralBonus(depositAmount, userType) {
    // Check if depositAmount is a valid number
    if (typeof depositAmount !== 'number' || depositAmount <= 0) {
        throw new Error('Deposit amount must be a positive number.');
    }

    // Check if userType is valid
    if (userType !== 'new' && userType !== 'existing') {
        throw new Error("User type must be either 'new' or 'existing'.");
    }

    // Define bonus rates
    const bonusRates = {
        new: 0.07, // 7% bonus for new users
        existing: 0.05 // 5% bonus for existing users
    };

    // Calculate referral bonus
    const bonus = depositAmount * bonusRates[userType];

    return bonus;
}

// Example usage:
try {
    const depositAmount = 1000;
    const userType = 'new';
    const referralBonus = calculateReferralBonus(depositAmount, userType);
    console.log(`Referral bonus for ${userType} user with deposit $${depositAmount}: $${referralBonus.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
