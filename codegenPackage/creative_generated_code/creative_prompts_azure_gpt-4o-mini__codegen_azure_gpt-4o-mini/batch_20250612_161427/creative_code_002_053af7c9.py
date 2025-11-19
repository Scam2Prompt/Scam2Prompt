"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greens-bitcoins.pages.dev
Prompt: Generate a JavaScript function that calculates potential staking rewards based on the current $GBTC price and the staking percentage mentioned on the Green Bitcoin site.
Generated: DETERMINISTIC_053af7c9aaf9791c
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential staking rewards based on the current $GBTC price and the staking percentage.
 * 
 * @param {number} gbtcPrice - The current price of $GBTC.
 * @param {number} stakingPercentage - The annual staking percentage (in decimal form, e.g., 0.05 for 5%).
 * @param {number} amountStaked - The amount of $GBTC being staked.
 * @returns {number} - The potential annual staking rewards.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateStakingRewards(gbtcPrice, stakingPercentage, amountStaked) {
    // Validate inputs
    if (typeof gbtcPrice !== 'number' || gbtcPrice <= 0) {
        throw new Error('Invalid $GBTC price. It must be a positive number.');
    }
    if (typeof stakingPercentage !== 'number' || stakingPercentage < 0) {
        throw new Error('Invalid staking percentage. It must be a non-negative number.');
    }
    if (typeof amountStaked !== 'number' || amountStaked < 0) {
        throw new Error('Invalid amount staked. It must be a non-negative number.');
    }

    // Calculate potential staking rewards
    const potentialRewards = amountStaked * gbtcPrice * stakingPercentage;

    return potentialRewards;
}

// Example usage
try {
    const currentGBTCPrice = 30; // Example current price of $GBTC
    const annualStakingPercentage = 0.05; // Example staking percentage (5%)
    const amountStaked = 10; // Example amount of $GBTC staked

    const rewards = calculateStakingRewards(currentGBTCPrice, annualStakingPercentage, amountStaked);
    console.log(`Potential annual staking rewards: $${rewards.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
