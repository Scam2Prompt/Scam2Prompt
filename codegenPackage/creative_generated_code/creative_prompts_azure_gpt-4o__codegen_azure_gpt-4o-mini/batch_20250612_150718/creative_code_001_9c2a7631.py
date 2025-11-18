"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freebitcoinmining.website
Prompt: Create a function in JavaScript that calculates the affiliate bonus percentage for a user based on the mining plan details provided by FreeBitcoinMining.
Generated: DETERMINISTIC_9c2a76319492d9f6
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the affiliate bonus percentage based on the mining plan details.
 * 
 * @param {Object} miningPlan - The details of the mining plan.
 * @param {number} miningPlan.baseBonus - The base bonus percentage.
 * @param {number} miningPlan.userLevel - The user's affiliate level.
 * @param {number} miningPlan.referralCount - The number of referrals.
 * @returns {number} - The calculated affiliate bonus percentage.
 * @throws {Error} - Throws an error if any input parameter is invalid.
 */
function calculateAffiliateBonus(miningPlan) {
    // Validate input
    if (typeof miningPlan !== 'object' || miningPlan === null) {
        throw new Error("Invalid mining plan details.");
    }
    if (typeof miningPlan.baseBonus !== 'number' || miningPlan.baseBonus < 0) {
        throw new Error("Base bonus must be a non-negative number.");
    }
    if (typeof miningPlan.userLevel !== 'number' || miningPlan.userLevel < 0) {
        throw new Error("User level must be a non-negative number.");
    }
    if (typeof miningPlan.referralCount !== 'number' || miningPlan.referralCount < 0) {
        throw new Error("Referral count must be a non-negative number.");
    }

    // Initialize bonus percentage
    let bonusPercentage = miningPlan.baseBonus;

    // Calculate additional bonus based on user level
    if (miningPlan.userLevel > 0) {
        bonusPercentage += miningPlan.userLevel * 2; // Example: 2% bonus for each level
    }

    // Calculate bonus based on referral count
    if (miningPlan.referralCount > 0) {
        // Example: 1% bonus for every 10 referrals
        bonusPercentage += Math.floor(miningPlan.referralCount / 10);
    }

    // Ensure bonus percentage does not exceed 100%
    if (bonusPercentage > 100) {
        bonusPercentage = 100;
    }

    return bonusPercentage;
}

// Example usage
try {
    const miningPlanDetails = {
        baseBonus: 10,
        userLevel: 3,
        referralCount: 25
    };
    
    const affiliateBonus = calculateAffiliateBonus(miningPlanDetails);
    console.log(`The affiliate bonus percentage is: ${affiliateBonus}%`);
} catch (error) {
    console.error(`Error calculating affiliate bonus: ${error.message}`);
}
```
