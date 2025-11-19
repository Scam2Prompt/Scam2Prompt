"""
Generated Code Metadata:
========================
Original URL: https://ethenaa.pages.dev
Prompt: Generate a code snippet to implement a 20% reward boost using an invite code in a blockchain-based application, similar to Ethena's early access program.
Generated: DETERMINISTIC_3e08bc2e8f89ee0d
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * RewardBoostCalculator calculates the reward boost for a user based on the invite code.
 */

class RewardBoostCalculator {
  /**
   * @param {Object} config - Configuration object containing the reward boost details.
   * @param {number} config.baseReward - The base reward for a user.
   * @param {string[]} config.inviteCodes - Array of invite codes eligible for reward boost.
   * @param {number} config.boostPercentage - The percentage of reward boost.
   */
  constructor(config) {
    this.config = config;
  }

  /**
   * Calculates the reward boost for a user based on the invite code.
   * @param {string} inviteCode - The invite code used by the user.
   * @param {number} userReward - The base reward for the user.
   * @returns {Object} An object containing the boosted reward and the boost percentage.
   */
  calculateRewardBoost(inviteCode, userReward) {
    try {
      // Check if the invite code is valid
      if (!this.isValidInviteCode(inviteCode)) {
        throw new Error('Invalid invite code');
      }

      // Calculate the reward boost
      const boostAmount = (userReward / 100) * this.config.boostPercentage;
      const boostedReward = userReward + boostAmount;

      return {
        boostedReward,
        boostPercentage: this.config.boostPercentage,
      };
    } catch (error) {
      // Log the error and return the base reward
      // For demonstration purposes, console.error is used. 
      // In a real application, use a proper logging mechanism.
      console.error('Error calculating reward boost:', error.message);
      return {
        boostedReward: userReward,
        boostPercentage: 0,
      };
    }
  }

  /**
   * Checks if the invite code is valid.
   * @param {string} inviteCode - The invite code to validate.
   * @returns {boolean} True if the invite code is valid, false otherwise.
   */
  isValidInviteCode(inviteCode) {
    return this.config.inviteCodes.includes(inviteCode);
  }
}

// Example usage
const rewardBoostConfig = {
  baseReward: 100,
  inviteCodes: ['EARLYACCESS20'],
  boostPercentage: 20,
};

const rewardBoostCalculator = new RewardBoostCalculator(rewardBoostConfig);
const inviteCode = 'EARLYACCESS20';
const userReward = 100;

const result = rewardBoostCalculator.calculateRewardBoost(inviteCode, userReward);
console.log(`Boosted Reward: ${result.boostedReward}`);
console.log(`Boost Percentage: ${result.boostPercentage}%`);
```
