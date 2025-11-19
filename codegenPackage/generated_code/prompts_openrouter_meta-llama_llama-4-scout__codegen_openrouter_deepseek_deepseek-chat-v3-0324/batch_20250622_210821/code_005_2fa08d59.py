"""
Generated Code Metadata:
========================
Original URL: https://freedumfighert.pages.dev
Prompt: Create a JavaScript function to calculate the rewards for users staking $DUM tokens in the FreeDum Fighters project, based on the provided tokenomics and reward structures.
Generated: DETERMINISTIC_2fa08d599c17f332
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates staking rewards for $DUM tokens based on the FreeDum Fighters tokenomics.
 * 
 * @param {number} stakedAmount - Amount of $DUM tokens staked
 * @param {number} stakingDurationDays - Duration of staking in days
 * @param {string} tier - User's staking tier ('bronze', 'silver', 'gold', 'platinum')
 * @param {boolean} isEarlyAdopter - Whether user is an early adopter
 * @returns {Object} Returns reward details including baseReward, bonus, and totalReward
 * @throws {Error} If input validation fails
 */
function calculateStakingRewards(stakedAmount, stakingDurationDays, tier, isEarlyAdopter) {
    // Input validation
    if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
        throw new Error('Staked amount must be a positive number');
    }
    if (typeof stakingDurationDays !== 'number' || stakingDurationDays <= 0) {
        throw new Error('Staking duration must be a positive number');
    }
    if (!['bronze', 'silver', 'gold', 'platinum'].includes(tier)) {
        throw new Error('Invalid tier. Must be one of: bronze, silver, gold, platinum');
    }
    if (typeof isEarlyAdopter !== 'boolean') {
        throw new Error('isEarlyAdopter must be a boolean value');
    }

    // Reward parameters
    const BASE_APY = 0.15; // 15% base APY
    const TIER_BONUSES = {
        bronze: 0,
        silver: 0.05,
        gold: 0.10,
        platinum: 0.20
    };
    const EARLY_ADOPTER_BONUS = 0.10;
    const MAX_STAKING_DURATION_DAYS = 365;

    // Calculate base reward (simple interest)
    const effectiveDuration = Math.min(stakingDurationDays, MAX_STAKING_DURATION_DAYS);
    const dailyRate = BASE_APY / 365;
    const baseReward = stakedAmount * dailyRate * effectiveDuration;

    // Calculate tier bonus
    const tierBonus = baseReward * TIER_BONUSES[tier];

    // Calculate early adopter bonus
    const earlyAdopterBonus = isEarlyAdopter ? baseReward * EARLY_ADOPTER_BONUS : 0;

    // Calculate total reward
    const totalReward = baseReward + tierBonus + earlyAdopterBonus;

    return {
        stakedAmount,
        stakingDurationDays: effectiveDuration,
        baseReward: parseFloat(baseReward.toFixed(6)),
        tierBonus: parseFloat(tierBonus.toFixed(6)),
        earlyAdopterBonus: parseFloat(earlyAdopterBonus.toFixed(6)),
        totalReward: parseFloat(totalReward.toFixed(6)),
        tier,
        isEarlyAdopter
    };
}

// Example usage:
// try {
//     const rewards = calculateStakingRewards(10000, 90, 'gold', true);
//     console.log(rewards);
// } catch (error) {
//     console.error('Error calculating rewards:', error.message);
// }
```
