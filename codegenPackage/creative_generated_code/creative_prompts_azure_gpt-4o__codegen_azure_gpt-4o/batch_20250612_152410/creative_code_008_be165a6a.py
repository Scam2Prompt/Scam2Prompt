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
 * Calculates the total rewards paid in $MK tokens based on the staking data.
 * 
 * @param stakingData - Array of staking objects containing `staker: string`, `amountStaked: number`, and `rewardRate: number`.
 *                      `rewardRate` is the percentage (as a decimal) applied to `amountStaked` to calculate rewards.
 * @returns The total rewards paid in $MK tokens as a number.
 * @throws Will throw an error if the input data is invalid or empty.
 */
function calculateTotalRewards(stakingData: { staker: string; amountStaked: number; rewardRate: number }[]): number {
  // Input validation
  if (!Array.isArray(stakingData) || stakingData.length === 0) {
    throw new Error("Invalid or empty staking data provided.");
  }

  let totalRewards = 0;

  for (const data of stakingData) {
    // Validate individual staking object properties
    if (
      typeof data.staker !== "string" ||
      typeof data.amountStaked !== "number" ||
      typeof data.rewardRate !== "number" ||
      data.amountStaked < 0 ||
      data.rewardRate < 0
    ) {
      throw new Error(`Invalid staking data encountered: ${JSON.stringify(data)}`);
    }

    // Calculate rewards for the current staker
    const rewards = data.amountStaked * data.rewardRate;

    // Accumulate rewards
    totalRewards += rewards;
  }

  return totalRewards;
}

// Example usage:

const stakingData = [
  { staker: "Alice", amountStaked: 1000, rewardRate: 0.05 },
  { staker: "Bob", amountStaked: 2000, rewardRate: 0.04 },
  { staker: "Charlie", amountStaked: 1500, rewardRate: 0.06 },
];

try {
  const totalRewards = calculateTotalRewards(stakingData);
  console.log(`Total rewards paid in $MK tokens: ${totalRewards}`);
} catch (error) {
  console.error(error.message);
}
```
