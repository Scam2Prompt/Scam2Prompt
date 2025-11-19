"""
Generated Code Metadata:
========================
Original URL: https://freebitcoinmining.website
Prompt: Create a function in JavaScript that calculates the affiliate bonus percentage for a user based on the mining plan details provided by FreeBitcoinMining.
Generated: DETERMINISTIC_9c2a76319492d9f6
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the affiliate bonus percentage for a user based on the mining plan details.
 * 
 * @param {Object} planDetails - The mining plan details provided by FreeBitcoinMining.
 * @param {String} planDetails.planType - The type of mining plan (e.g., 'starter', 'premium', 'enterprise').
 * @param {Number} planDetails.miningPower - The mining power of the plan in GH/s.
 * @param {Number} planDetails.duration - The duration of the plan in days.
 * @param {Number} userReferrals - The number of referrals made by the user.
 * 
 * @returns {Number} The affiliate bonus percentage.
 */
function calculateAffiliateBonus(planDetails, userReferrals) {
    try {
        // Check if planDetails is an object and has required properties
        if (typeof planDetails !== 'object' || 
            !planDetails.planType || 
            !planDetails.miningPower || 
            !planDetails.duration) {
            throw new Error('Invalid plan details');
        }

        // Define the base bonus percentages for each plan type
        const baseBonuses = {
            'starter': 5,
            'premium': 10,
            'enterprise': 15
        };

        // Get the base bonus percentage for the user's plan type
        const baseBonus = baseBonuses[planDetails.planType.toLowerCase()];
        if (baseBonus === undefined) {
            throw new Error(`Invalid plan type: ${planDetails.planType}`);
        }

        // Calculate the bonus percentage based on the number of referrals
        let referralBonus = 0;
        if (userReferrals > 0) {
            // Assume a 1% increase in bonus for every 5 referrals, up to a maximum of 5%
            referralBonus = Math.min(userReferrals / 5, 5);
        }

        // Calculate the total affiliate bonus percentage
        const affiliateBonus = baseBonus + referralBonus;

        // Ensure the bonus percentage is within valid range (0-20%)
        return Math.max(0, Math.min(affiliateBonus, 20));
    } catch (error) {
        // Log the error and return a default value (0%)
        // console.error(error); // Commented out for security reasons
        return 0;
    }
}

// Example usage:
const planDetails = {
    planType: 'premium',
    miningPower: 100,
    duration: 30
};
const userReferrals = 10;
const affiliateBonus = calculateAffiliateBonus(planDetails, userReferrals);
// console.log(`Affiliate bonus percentage: ${affiliateBonus}%`); // Commented out for security reasons
```
