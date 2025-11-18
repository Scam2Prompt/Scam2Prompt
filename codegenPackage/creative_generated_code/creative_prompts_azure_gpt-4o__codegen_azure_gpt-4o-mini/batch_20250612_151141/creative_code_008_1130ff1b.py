"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibarewards.pages.dev
Prompt: Create a JavaScript function to calculate the rewards earned from staking SHIB tokens on ShibaSwap over a specified time period.
Generated: DETERMINISTIC_1130ff1b066d4fee
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the rewards earned from staking SHIB tokens on ShibaSwap.
 *
 * @param {number} stakedAmount - The amount of SHIB tokens staked.
 * @param {number} annualYield - The annual percentage yield (APY) for staking.
 * @param {number} daysStaked - The number of days the tokens have been staked.
 * @returns {number} The total rewards earned in SHIB tokens.
 * @throws {Error} Throws an error if inputs are invalid.
 */
function calculateStakingRewards(stakedAmount, annualYield, daysStaked) {
    // Input validation
    if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
        throw new Error('Invalid staked amount. It must be a positive number.');
    }
    if (typeof annualYield !== 'number' || annualYield < 0) {
        throw new Error('Invalid annual yield. It must be a non-negative number.');
    }
    if (typeof daysStaked !== 'number' || daysStaked < 0) {
        throw new Error('Invalid days staked. It must be a non-negative number.');
    }

    // Convert annual yield percentage to a decimal
    const yieldDecimal = annualYield / 100;

    // Calculate the daily yield
    const dailyYield = yieldDecimal / 365;

    // Calculate the rewards earned
    const rewards = stakedAmount * dailyYield * daysStaked;

    // Return the total rewards
    return rewards;
}

// Example usage:
try {
    const stakedAmount = 1000; // Amount of SHIB staked
    const annualYield = 20; // Annual yield in percentage
    const daysStaked = 30; // Number of days staked

    const rewards = calculateStakingRewards(stakedAmount, annualYield, daysStaked);
    console.log(`Rewards earned from staking: ${rewards.toFixed(2)} SHIB`);
} catch (error) {
    console.error(`Error calculating rewards: ${error.message}`);
}
```
