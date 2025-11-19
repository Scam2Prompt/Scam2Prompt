"""
Generated Code Metadata:
========================
Original URL: https://ultimateexperttrade24.com
Prompt: "Write a function in JavaScript to calculate referral bonuses for investment plans, such as the Silver Plan with a 15.5% referral bonus."
Generated: DETERMINISTIC_196e910fc6d34f8c
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates referral bonuses for investment plans based on the referred amount and plan details.
 * 
 * @param {number} referredAmount - The amount invested by the referred person.
 * @param {string} planName - The name of the investment plan (e.g., "Silver Plan").
 * @param {Object} planDetails - An object containing plan details, including referral bonuses.
 * @returns {number} The calculated referral bonus.
 * @throws {Error} If referredAmount is not a positive number or planName is not found.
 */
function calculateReferralBonus(referredAmount, planName, planDetails) {
    // Validate input parameters
    if (typeof referredAmount !== 'number' || referredAmount <= 0) {
        throw new Error('referredAmount must be a positive number');
    }

    if (!planName || typeof planName !== 'string') {
        throw new Error('planName must be a non-empty string');
    }

    if (!planDetails || typeof planDetails !== 'object') {
        throw new Error('planDetails must be an object');
    }

    // Normalize plan name for case-insensitive comparison
    const normalizedPlanName = planName.trim().toLowerCase();

    // Find the plan in planDetails
    const plan = Object.entries(planDetails).find(([name]) => 
        name.toLowerCase() === normalizedPlanName
    );

    if (!plan) {
        throw new Error(`Plan '${planName}' not found in planDetails`);
    }

    const [, bonusPercentage] = plan;

    // Validate bonus percentage
    if (typeof bonusPercentage !== 'number' || bonusPercentage < 0) {
        throw new Error('bonusPercentage must be a non-negative number');
    }

    // Calculate and return the referral bonus
    const referralBonus = referredAmount * (bonusPercentage / 100);
    return parseFloat(referralBonus.toFixed(2)); // Round to 2 decimal places
}

// Example plan details (can be extended with more plans)
const investmentPlans = {
    'Silver Plan': 15.5,
    'Gold Plan': 20.0,
    'Platinum Plan': 25.0
};

// Example usage:
// try {
//     const bonus = calculateReferralBonus(1000, 'Silver Plan', investmentPlans);
//     console.log(`Referral bonus: $${bonus}`);
// } catch (error) {
//     console.error('Error calculating referral bonus:', error.message);
// }
```
