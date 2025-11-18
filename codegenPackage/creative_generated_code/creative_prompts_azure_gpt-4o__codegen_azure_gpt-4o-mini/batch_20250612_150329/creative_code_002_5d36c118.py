"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lounge.finance
Prompt: Generate a JavaScript function to calculate estimated staking rewards based on the parameters provided by Lounge Finance.
Generated: DETERMINISTIC_5d36c11820d4099b
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates estimated staking rewards based on the provided parameters.
 * 
 * @param {number} stakeAmount - The amount of tokens staked.
 * @param {number} annualYield - The annual yield percentage (in decimal form).
 * @param {number} stakingDuration - The duration of staking in years.
 * @returns {number} - The estimated staking rewards.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateStakingRewards(stakeAmount, annualYield, stakingDuration) {
    // Validate input values
    if (typeof stakeAmount !== 'number' || stakeAmount <= 0) {
        throw new Error('Invalid stake amount. It must be a positive number.');
    }
    if (typeof annualYield !== 'number' || annualYield < 0) {
        throw new Error('Invalid annual yield. It must be a non-negative number.');
    }
    if (typeof stakingDuration !== 'number' || stakingDuration <= 0) {
        throw new Error('Invalid staking duration. It must be a positive number.');
    }

    // Calculate the estimated rewards
    const estimatedRewards = stakeAmount * annualYield * stakingDuration;

    // Return the calculated estimated rewards
    return estimatedRewards;
}

// Example usage (uncomment to run):
// try {
//     const rewards = calculateStakingRewards(1000, 0.05, 1);
//     console.log(`Estimated Staking Rewards: $${rewards.toFixed(2)}`);
// } catch (error) {
//     console.error(error.message);
// }
```
