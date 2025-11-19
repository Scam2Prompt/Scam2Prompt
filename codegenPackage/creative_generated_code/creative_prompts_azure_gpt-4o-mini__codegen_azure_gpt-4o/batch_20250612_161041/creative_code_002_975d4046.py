"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcbulltoken.pages.dev
Prompt: Create a JavaScript function that calculates the potential rewards from holding $BTCBULL tokens based on the token burn milestones outlined on the BTC Bull Token website.
Generated: DETERMINISTIC_975d404627301ebc
Batch ID: 20250612_161041
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential rewards for holding $BTCBULL tokens based on token burn milestones.
 *
 * @param {number} userTokens - The number of $BTCBULL tokens held by the user.
 * @param {Array<Object>} burnMilestones - An array of objects representing burn milestones. 
 *                                          Each object contains:
 *                                          - `burnAmount`: Total tokens burned at the milestone.
 *                                          - `rewardRatio`: Reward ratio for the milestone (e.g., 0.01 for 1%).
 * @returns {number} - The potential rewards for the user, calculated in tokens.
 */
function calculateBTCBullRewards(userTokens, burnMilestones) {
  // Input validation
  if (!Array.isArray(burnMilestones)) {
    throw new Error('Invalid input: burnMilestones must be an array.');
  }
  
  if (typeof userTokens !== 'number' || userTokens <= 0) {
    throw new Error('Invalid input: userTokens must be a positive number.');
  }

  let potentialRewards = 0;

  // Iterate through each burn milestone and calculate rewards
  burnMilestones.forEach((milestone) => {
    if (
      typeof milestone.burnAmount !== 'number' ||
      milestone.burnAmount <= 0 ||
      typeof milestone.rewardRatio !== 'number' ||
      milestone.rewardRatio < 0
    ) {
      throw new Error('Invalid milestone object: burnAmount and rewardRatio must be valid numbers.');
    }

    // Calculate rewards for the current milestone
    const milestoneReward = milestone.rewardRatio * userTokens;
    potentialRewards += milestoneReward;
  });

  return potentialRewards;
}

// Example usage:
const burnMilestones = [
  { burnAmount: 100000, rewardRatio: 0.01 }, // 1% reward
  { burnAmount: 500000, rewardRatio: 0.02 }, // 2% reward
  { burnAmount: 1000000, rewardRatio: 0.03 }, // 3% reward
];

const userTokens = 1000;

try {
  const rewards = calculateBTCBullRewards(userTokens, burnMilestones);
  console.log(`Potential Rewards: ${rewards} BTCBULL tokens`);
} catch (error) {
  console.error(error.message);
}
```
