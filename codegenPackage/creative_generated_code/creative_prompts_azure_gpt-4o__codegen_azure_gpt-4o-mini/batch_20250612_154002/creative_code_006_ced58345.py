"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-farming.net
Prompt: Create a function in JavaScript to calculate the estimated rewards for a user based on their staked amount and the APY provided by a DeFi farming protocol.
Generated: DETERMINISTIC_ced583458cdf884e
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated rewards for a user based on the staked amount
 * and the Annual Percentage Yield (APY) provided by a DeFi farming protocol.
 *
 * @param {number} stakedAmount - The amount of tokens staked by the user.
 * @param {number} apy - The Annual Percentage Yield expressed as a decimal (e.g., 0.15 for 15%).
 * @param {number} duration - The duration in years for which the rewards are calculated.
 * @returns {number} - The estimated rewards the user would earn.
 * @throws {Error} - Throws an error if stakedAmount, apy, or duration are not valid numbers or if they are negative.
 */
function calculateEstimatedRewards(stakedAmount, apy, duration) {
    // Validate input parameters
    if (typeof stakedAmount !== 'number' || stakedAmount < 0) {
        throw new Error('Invalid staked amount. Must be a non-negative number.');
    }
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('Invalid APY. Must be a non-negative number.');
    }
    if (typeof duration !== 'number' || duration < 0) {
        throw new Error('Invalid duration. Must be a non-negative number.');
    }

    // Calculate estimated rewards
    const rewards = stakedAmount * apy * duration;

    // Return the calculated rewards
    return rewards;
}

// Example usage
try {
    const stakedAmount = 1000; // User's staked amount in tokens
    const apy = 0.15; // APY of the DeFi protocol (15%)
    const duration = 1; // Duration in years

    // Calculate estimated rewards
    const estimatedRewards = calculateEstimatedRewards(stakedAmount, apy, duration);
    console.log(`Estimated rewards: ${estimatedRewards.toFixed(2)} tokens`);
} catch (error) {
    console.error(error.message);
}
```
