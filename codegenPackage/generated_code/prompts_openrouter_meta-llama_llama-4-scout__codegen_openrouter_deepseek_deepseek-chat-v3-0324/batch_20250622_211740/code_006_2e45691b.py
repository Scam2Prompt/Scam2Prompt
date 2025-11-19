"""
Generated Code Metadata:
========================
Original URL: https://vatanbet.info
Prompt: Write a JavaScript function to implement a cashback system, like BaxBet's cashback feature, for users' losses, with a dynamic rewards calculation.
Generated: DETERMINISTIC_2e45691b2a45f31b
Batch ID: 20250622_211740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cashback System Implementation
 * 
 * This function calculates cashback rewards for users based on their losses,
 * with dynamic rewards calculation similar to BaxBet's cashback feature.
 * 
 * @param {Object} user - User object containing necessary details
 * @param {number} user.totalLosses - Total losses incurred by the user
 * @param {number} user.bettingActivity - User's betting activity level (1-10)
 * @param {number} user.loyaltyTier - User's loyalty tier (1-5)
 * @param {Object} config - Configuration for cashback calculation
 * @param {number} config.baseRate - Base cashback rate (percentage)
 * @param {number} config.maxRate - Maximum cashback rate (percentage)
 * @param {number} config.activityWeight - Weight for betting activity in calculation
 * @param {number} config.loyaltyWeight - Weight for loyalty tier in calculation
 * @returns {Object} Result containing cashback amount and details
 * @throws {Error} If input validation fails
 */
function calculateCashback(user, config) {
    // Input validation
    if (!user || typeof user !== 'object') {
        throw new Error('Invalid user object');
    }
    
    const requiredUserFields = ['totalLosses', 'bettingActivity', 'loyaltyTier'];
    for (const field of requiredUserFields) {
        if (typeof user[field] !== 'number' || user[field] < 0) {
            throw new Error(`Invalid user.${field} value`);
        }
    }

    if (!config || typeof config !== 'object') {
        throw new Error('Invalid config object');
    }

    const requiredConfigFields = ['baseRate', 'maxRate', 'activityWeight', 'loyaltyWeight'];
    for (const field of requiredConfigFields) {
        if (typeof config[field] !== 'number' || config[field] < 0) {
            throw new Error(`Invalid config.${field} value`);
        }
    }

    // Normalize user activity and loyalty to 0-1 range
    const normalizedActivity = Math.min(Math.max(user.bettingActivity, 1), 10) / 10;
    const normalizedLoyalty = Math.min(Math.max(user.loyaltyTier, 1), 5) / 5;

    // Calculate dynamic cashback rate
    const activityComponent = config.activityWeight * normalizedActivity;
    const loyaltyComponent = config.loyaltyWeight * normalizedLoyalty;
    const dynamicRate = config.baseRate + activityComponent + loyaltyComponent;

    // Ensure rate doesn't exceed maximum
    const finalRate = Math.min(dynamicRate, config.maxRate);

    // Calculate cashback amount
    const cashbackAmount = user.totalLosses * (finalRate / 100);

    return {
        success: true,
        cashbackAmount: parseFloat(cashbackAmount.toFixed(2)),
        cashbackRate: parseFloat(finalRate.toFixed(2)),
        currency: 'USD', // Can be parameterized if needed
        details: {
            baseRate: config.baseRate,
            activityContribution: activityComponent,
            loyaltyContribution: loyaltyComponent,
            normalizedActivity,
            normalizedLoyalty
        }
    };
}

// Example configuration
const defaultConfig = {
    baseRate: 5,        // 5% base cashback
    maxRate: 15,        // Maximum 15% cashback
    activityWeight: 3,  // Weight for betting activity
    loyaltyWeight: 7    // Weight for loyalty tier
};

// Example usage:
// const user = {
//     totalLosses: 1000,
//     bettingActivity: 8,
//     loyaltyTier: 3
// };
// const result = calculateCashback(user, defaultConfig);
```
