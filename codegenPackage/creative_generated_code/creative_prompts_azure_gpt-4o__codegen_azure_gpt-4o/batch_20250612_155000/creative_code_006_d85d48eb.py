"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntes.me
Prompt: Create a JavaScript function to calculate rewards for Ethereum 2.0 staking based on validator performance metrics.
Generated: DETERMINISTIC_d85d48ebc31832dc
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates Ethereum 2.0 staking rewards based on validator performance metrics.
 * 
 * @param {number} balance - The validator's balance in ETH.
 * @param {number} effectiveBalance - The validator's effective balance capped at 32 ETH.
 * @param {number} baseRewardFactor - The base reward factor determined by network conditions.
 * @param {number} validatorPerformance - A performance metric (0 to 1) representing the validator's effectiveness.
 * @returns {number} The calculated rewards in ETH.
 * @throws Will throw an error if any of the inputs are invalid or out of range.
 */
function calculateStakingRewards(balance, effectiveBalance, baseRewardFactor, validatorPerformance) {
    // Input validation
    if (typeof balance !== 'number' || balance <= 0) {
        throw new Error("Invalid balance: Must be a positive number.");
    }
    if (typeof effectiveBalance !== 'number' || effectiveBalance <= 0 || effectiveBalance > 32) {
        throw new Error("Invalid effective balance: Must be a positive number and capped at 32 ETH.");
    }
    if (typeof baseRewardFactor !== 'number' || baseRewardFactor <= 0) {
        throw new Error("Invalid base reward factor: Must be a positive number.");
    }
    if (typeof validatorPerformance !== 'number' || validatorPerformance < 0 || validatorPerformance > 1) {
        throw new Error("Invalid validator performance: Must be a number between 0 and 1.");
    }

    // Constants (Ethereum-specific values)
    const baseRewardDenominator = 64; // Protocol-defined constant
    const inactivityPenaltyQuotient = 2 ** 24; // Used for performance penalties

    // Calculate the base reward for the validator
    const baseReward = (effectiveBalance * baseRewardFactor) / baseRewardDenominator;

    // Adjust reward based on validator performance
    const adjustedReward = baseReward * validatorPerformance;

    // Apply inactivity penalty if performance is poor
    const penalty = validatorPerformance < 0.5 
        ? baseReward / inactivityPenaltyQuotient 
        : 0;

    // Final reward calculation
    const totalReward = adjustedReward - penalty;

    // Ensure rewards are not negative
    return Math.max(totalReward, 0);
}

// Example usage:
try {
    const balance = 32; // Validator's total balance in ETH
    const effectiveBalance = 32; // Validator's effective balance capped at 32 ETH
    const baseRewardFactor = 10000; // Network-specific base reward factor
    const validatorPerformance = 0.95; // Validator's performance metric (95% effectiveness)

    const rewards = calculateStakingRewards(balance, effectiveBalance, baseRewardFactor, validatorPerformance);
    console.log(`Calculated Rewards: ${rewards.toFixed(4)} ETH`);
} catch (error) {
    console.error(`Error calculating rewards: ${error.message}`);
}
```
