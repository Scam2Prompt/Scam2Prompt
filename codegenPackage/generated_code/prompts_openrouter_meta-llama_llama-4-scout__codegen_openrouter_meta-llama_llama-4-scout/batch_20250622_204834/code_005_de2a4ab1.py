"""
Generated Code Metadata:
========================
Original URL: https://sunny-3ah.pages.dev
Prompt: Create a JavaScript function to verify user eligibility for The SUNNY Awards based on their on-chain activities.
Generated: DETERMINISTIC_de2a4ab14c13c371
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Verifies user eligibility for The SUNNY Awards based on their on-chain activities.
 * 
 * @param {Object} userActivities - User's on-chain activities.
 * @param {number} userActivities.totalTransactions - Total transactions made by the user.
 * @param {number} userActivities.totalAssets - Total assets held by the user.
 * @param {number} userActivities.stakingDuration - Total staking duration in days.
 * @returns {boolean} True if the user is eligible, false otherwise.
 */
function verifyEligibility(userActivities) {
    try {
        // Define the eligibility criteria
        const eligibilityCriteria = {
            minTransactions: 10,
            minAssets: 1000,
            minStakingDuration: 30 // in days
        };

        // Check if userActivities is valid
        if (typeof userActivities !== 'object' || userActivities === null) {
            throw new Error('Invalid user activities');
        }

        // Check if required properties exist
        const requiredProperties = ['totalTransactions', 'totalAssets', 'stakingDuration'];
        if (!requiredProperties.every(prop => prop in userActivities)) {
            throw new Error('User activities must contain totalTransactions, totalAssets, and stakingDuration');
        }

        // Check eligibility criteria
        const isEligible =
            userActivities.totalTransactions >= eligibilityCriteria.minTransactions &&
            userActivities.totalAssets >= eligibilityCriteria.minAssets &&
            userActivities.stakingDuration >= eligibilityCriteria.minStakingDuration;

        return isEligible;
    } catch (error) {
        console.error('Error verifying eligibility:', error.message);
        return false;
    }
}

/**
 * Example usage:
 */
function main() {
    const userActivities = {
        totalTransactions: 15,
        totalAssets: 1500,
        stakingDuration: 60 // in days
    };

    const isEligible = verifyEligibility(userActivities);
    console.log(`User is ${isEligible ? '' : 'not '}eligible for The SUNNY Awards.`);
}

main();
```
