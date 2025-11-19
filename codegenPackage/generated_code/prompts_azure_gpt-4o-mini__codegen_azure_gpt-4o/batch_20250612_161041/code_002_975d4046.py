"""
Generated Code Metadata:
========================
Original URL: https://btcbulltoken.pages.dev
Prompt: Create a JavaScript function that calculates the potential rewards from holding $BTCBULL tokens based on the token burn milestones outlined on the BTC Bull Token website.
Generated: DETERMINISTIC_975d404627301ebc
Batch ID: 20250612_161041
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate potential rewards from holding $BTCBULL tokens
 * based on token burn milestones.
 *
 * @param {number} userTokens - The number of $BTCBULL tokens the user holds.
 * @param {number} totalSupply - The total supply of $BTCBULL tokens.
 * @param {Array<Object>} burnMilestones - Array of burn milestones, each containing:
 *   - {number} milestonePercentage: Percentage of tokens burned at this milestone.
 *   - {number} rewardPool: Total reward pool allocated for this milestone.
 * @returns {number} - The potential rewards for the user.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateBTCBullRewards(userTokens, totalSupply, burnMilestones) {
  // Input validation
  if (typeof userTokens !== 'number' || userTokens <= 0) {
    throw new Error("Invalid input: 'userTokens' must be a positive number.");
  }
  if (typeof totalSupply !== 'number' || totalSupply <= 0) {
    throw new Error("Invalid input: 'totalSupply' must be a positive number.");
  }
  if (!Array.isArray(burnMilestones) || burnMilestones.length === 0) {
    throw new Error("Invalid input: 'burnMilestones' must be a non-empty array.");
  }

  let totalRewards = 0;

  // Iterate through each burn milestone
  for (const milestone of burnMilestones) {
    const { milestonePercentage, rewardPool } = milestone;

    // Validate milestone structure
    if (
      typeof milestonePercentage !== 'number' ||
      milestonePercentage <= 0 ||
      milestonePercentage > 100
    ) {
      throw new Error(
        "Invalid milestone: 'milestonePercentage' must be a number between 0 and 100."
      );
    }
    if (typeof rewardPool !== 'number' || rewardPool <= 0) {
      throw new Error(
        "Invalid milestone: 'rewardPool' must be a positive number."
      );
    }

    // Calculate the number of tokens burned at this milestone
    const tokensBurned = (milestonePercentage / 100) * totalSupply;

    // Calculate the user's share of the reward pool
    const userShare = userTokens / (totalSupply - tokensBurned);
    const userReward = userShare * rewardPool;

    // Accumulate rewards
    totalRewards += userReward;
  }

  return totalRewards;
}

// Example usage:
try {
  const userTokens = 1000; // User holds 1000 $BTCBULL tokens
  const totalSupply = 1000000; // Total supply of $BTCBULL tokens
  const burnMilestones = [
    { milestonePercentage: 10, rewardPool: 50000 },
    { milestonePercentage: 20, rewardPool: 100000 },
    { milestonePercentage: 30, rewardPool: 150000 },
  ];

  const rewards = calculateBTCBullRewards(userTokens, totalSupply, burnMilestones);
  console.log(`Potential rewards: $${rewards.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
