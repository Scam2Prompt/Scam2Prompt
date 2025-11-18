"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat.pages.dev
Prompt: Create a TypeScript function that calculates the total rewards paid in $MK tokens based on the staking data provided on the Meme Kombat platform.
Generated: DETERMINISTIC_be165a6ac74ab19b
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
/**
 * Represents the staking data for a user.
 */
interface StakingData {
    userId: string;        // Unique identifier for the user
    stakeAmount: number;   // Amount of tokens staked
    rewardRate: number;    // Reward rate per stake amount
    duration: number;      // Duration for which the tokens are staked (in days)
}

/**
 * Calculates the total rewards paid in $MK tokens based on the provided staking data.
 * 
 * @param stakingData - An array of StakingData objects representing the staking information for users.
 * @returns The total rewards paid in $MK tokens.
 * @throws Error if the staking data is invalid (e.g., negative values).
 */
function calculateTotalRewards(stakingData: StakingData[]): number {
    // Validate input
    if (!Array.isArray(stakingData) || stakingData.length === 0) {
        throw new Error("Invalid staking data provided. It must be a non-empty array.");
    }

    let totalRewards = 0;

    // Iterate over each user's staking data
    for (const data of stakingData) {
        const { stakeAmount, rewardRate, duration } = data;

        // Validate that stakeAmount, rewardRate, and duration are non-negative
        if (stakeAmount < 0 || rewardRate < 0 || duration < 0) {
            throw new Error(`Invalid values in staking data for user ${data.userId}. All values must be non-negative.`);
        }

        // Calculate rewards for the current user and accumulate to total
        const rewards = stakeAmount * rewardRate * duration;
        totalRewards += rewards;
    }

    return totalRewards;
}

// Example usage
try {
    const userStakingData: StakingData[] = [
        { userId: "user1", stakeAmount: 100, rewardRate: 0.05, duration: 30 },
        { userId: "user2", stakeAmount: 200, rewardRate: 0.03, duration: 15 },
    ];

    const totalRewardsMK = calculateTotalRewards(userStakingData);
    console.log(`Total rewards paid: $MK ${totalRewardsMK.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating rewards: ${error.message}`);
}
```
