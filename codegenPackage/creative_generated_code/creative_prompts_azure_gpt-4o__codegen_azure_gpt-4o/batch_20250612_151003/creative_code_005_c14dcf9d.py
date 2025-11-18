"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-bananagun-io.pages.dev
Prompt: Create a TypeScript function that combines Solana and EVM rewards to calculate total $BANANA and USD values, following the Bananagun reward calculation methodology.
Generated: DETERMINISTIC_c14dcf9dc0191fbf
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
/**
 * Calculate total $BANANA and USD values from Solana and EVM rewards.
 * This function uses the Bananagun reward calculation methodology.
 */

type Reward = {
  bananaAmount: number; // Amount of $BANANA tokens
  usdValue: number; // USD value of the reward
};

type RewardsInput = {
  solanaRewards: Reward[]; // Array of Solana rewards
  evmRewards: Reward[]; // Array of EVM rewards
};

type RewardTotals = {
  totalBanana: number; // Total $BANANA tokens
  totalUsd: number; // Total USD value
};

/**
 * Combines Solana and EVM rewards to calculate total $BANANA and USD values.
 *
 * @param {RewardsInput} rewardsInput - The rewards for Solana and EVM.
 * @returns {RewardTotals} An object containing total $BANANA and total USD values.
 */
function calculateTotalRewards(rewardsInput: RewardsInput): RewardTotals {
  try {
    // Validate input
    if (!rewardsInput || !rewardsInput.solanaRewards || !rewardsInput.evmRewards) {
      throw new Error("Invalid input: rewardsInput must contain solanaRewards and evmRewards arrays.");
    }

    // Helper function to calculate totals for a given array of rewards
    const calculateTotals = (rewards: Reward[]): RewardTotals => {
      return rewards.reduce(
        (totals, reward) => {
          // Accumulate $BANANA tokens and USD values
          totals.totalBanana += reward.bananaAmount;
          totals.totalUsd += reward.usdValue;
          return totals;
        },
        { totalBanana: 0, totalUsd: 0 } // Initial totals
      );
    };

    // Calculate totals for Solana and EVM rewards
    const solanaTotals = calculateTotals(rewardsInput.solanaRewards);
    const evmTotals = calculateTotals(rewardsInput.evmRewards);

    // Combine totals for final result
    const finalTotals: RewardTotals = {
      totalBanana: solanaTotals.totalBanana + evmTotals.totalBanana,
      totalUsd: solanaTotals.totalUsd + evmTotals.totalUsd,
    };

    return finalTotals;
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error("Error calculating total rewards:", error.message);
    throw error; // Re-throw the error for higher-level handling
  }
}

export { Reward, RewardsInput, RewardTotals, calculateTotalRewards };
```
