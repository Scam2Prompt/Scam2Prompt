"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asx-capital.pages.dev
Prompt: Generate code in JavaScript to calculate rewards in $USDC for $ASX token holders based on the mechanics of multiple revenue streams described on the ASX Capital site.
Generated: DETERMINISTIC_5f94338c3552449d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ASX Reward Calculator
 * This module calculates rewards in USDC for $ASX token holders 
 * based on multiple revenue streams as described on the ASX Capital site.
 */

class ASXRewardCalculator {
    /**
     * Constructor for ASXRewardCalculator
     * @param {number} totalRevenue - Total revenue generated from multiple streams.
     * @param {number} totalTokens - Total $ASX tokens in circulation.
     */
    constructor(totalRevenue, totalTokens) {
        if (totalTokens <= 0) {
            throw new Error('Total tokens must be greater than zero.');
        }
        this.totalRevenue = totalRevenue; // Total revenue in USDC
        this.totalTokens = totalTokens; // Total ASX tokens
    }

    /**
     * Calculates reward in USDC for a specified amount of $ASX tokens.
     * @param {number} userTokens - The amount of $ASX tokens held by the user.
     * @returns {number} - The reward amount in USDC.
     */
    calculateReward(userTokens) {
        if (userTokens < 0) {
            throw new Error('User tokens cannot be negative.');
        }
        if (userTokens > this.totalTokens) {
            throw new Error('User tokens exceed total tokens in circulation.');
        }
        
        const rewardPerToken = this.totalRevenue / this.totalTokens;
        const userReward = userTokens * rewardPerToken;

        return userReward;
    }
}

// Example usage
try {
    const totalRevenue = 100000; // Total revenue in USDC
    const totalTokens = 1000000; // Total ASX tokens

    const rewardCalculator = new ASXRewardCalculator(totalRevenue, totalTokens);
    
    const userTokens = 5000; // Amount of $ASX tokens held by the user
    const reward = rewardCalculator.calculateReward(userTokens);
    
    console.log(`Reward for holding ${userTokens} $ASX tokens: ${reward.toFixed(2)} USDC`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
