"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-wienerdog.pages.dev
Prompt: Create a JavaScript function that allows users to stake their $WAI tokens and calculate the potential rewards based on the current APY mentioned in the WienerAI documentation.
Generated: DETERMINISTIC_e878712e8592dcd4
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a constant for the APY (Annual Percentage Yield)
const ANNUAL_PERCENTAGE_YIELD = 0.15; // Example APY of 15%

/**
 * Function to stake WAI tokens.
 * @param {number} amount - The amount of $WAI tokens to stake.
 * @param {number} duration - The duration in days for which the tokens will be staked.
 * @throws Will throw an error if the amount is less than or equal to zero, or if the duration is less than or equal to zero.
 * @returns {object} An object containing the staked amount, duration, and potential rewards.
 */
function stakeTokens(amount, duration) {
    // Validate the input parameters
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Invalid amount. Amount must be a positive number.');
    }
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Invalid duration. Duration must be a positive number.');
    }

    // Calculate potential rewards based on the APY
    const potentialRewards = calculateRewards(amount, duration);

    // Return the staking details
    return {
        stakedAmount: amount,
        stakeDuration: duration,
        potentialRewards: potentialRewards
    };
}

/**
 * Function to calculate staking rewards.
 * @param {number} amount - The amount of $WAI tokens staked.
 * @param {number} duration - The duration in days for which the tokens are staked.
 * @returns {number} The potential rewards based on the staked amount and APY.
 */
function calculateRewards(amount, duration) {
    // Calculate the reward based on the formula for interest
    const dailyAPY = ANNUAL_PERCENTAGE_YIELD / 365; // Convert APY to daily
    const rewards = amount * dailyAPY * duration; // Calculate potential rewards
    return rewards;
}

// Example usage:
try {
    const stakeDetails = stakeTokens(1000, 30); // Stake 1000 $WAI for 30 days
    console.log('Stake Details:', stakeDetails);
} catch (error) {
    console.error('Error staking tokens:', error.message);
}
```
