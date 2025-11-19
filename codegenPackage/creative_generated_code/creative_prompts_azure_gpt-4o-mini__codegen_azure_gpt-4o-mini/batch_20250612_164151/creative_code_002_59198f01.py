"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-sale.pages.dev
Prompt: Create a JavaScript function that calculates potential staking rewards based on the double staking feature of the Pepe Unchained ecosystem.
Generated: DETERMINISTIC_59198f01c094750a
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential staking rewards based on the double staking feature
 * of the Pepe Unchained ecosystem.
 *
 * @param {number} principal - The initial amount staked (in tokens).
 * @param {number} annualPercentageYield - The annual percentage yield (APY) as a decimal.
 * @param {number} stakingDuration - The duration of staking in years.
 * @param {boolean} isDoubleStaking - Indicates if double staking is enabled.
 * @returns {number} The potential rewards after the staking period.
 * @throws {Error} Throws an error if inputs are invalid.
 */
function calculateStakingRewards(principal, annualPercentageYield, stakingDuration, isDoubleStaking) {
    // Validate inputs
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Invalid principal amount. It must be a positive number.');
    }
    if (typeof annualPercentageYield !== 'number' || annualPercentageYield < 0) {
        throw new Error('Invalid annual percentage yield. It must be a non-negative number.');
    }
    if (typeof stakingDuration !== 'number' || stakingDuration < 0) {
        throw new Error('Invalid staking duration. It must be a non-negative number.');
    }
    if (typeof isDoubleStaking !== 'boolean') {
        throw new Error('Invalid double staking indicator. It must be a boolean.');
    }

    // Calculate effective APY based on double staking option
    const effectiveAPY = isDoubleStaking ? annualPercentageYield * 2 : annualPercentageYield;

    // Calculate potential rewards using compound interest formula
    const rewards = principal * Math.pow((1 + effectiveAPY), stakingDuration) - principal;

    return rewards;
}

// Example usage
try {
    const principal = 1000; // Amount in tokens staked
    const apy = 0.15; // 15% annual percentage yield
    const duration = 2; // Staking for 2 years
    const isDoubleStaking = true; // Double staking enabled

    const potentialRewards = calculateStakingRewards(principal, apy, duration, isDoubleStaking);
    console.log(`Potential staking rewards: ${potentialRewards.toFixed(2)} tokens`);
} catch (error) {
    console.error(error.message);
}
```
