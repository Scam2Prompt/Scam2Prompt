"""
Generated Code Metadata:
========================
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Generate a staking rewards calculator in JavaScript that predicts the rewards for staking $EMT tokens on the EarthMeta platform, based on the provided staking calculator formula.
Generated: DETERMINISTIC_cac00f668c729964
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * EarthMeta Staking Rewards Calculator
 * 
 * Calculates the predicted rewards for staking $EMT tokens on the EarthMeta platform.
 * 
 * @author [Your Name]
 */

// Define the StakingRewardsCalculator class
class StakingRewardsCalculator {
  /**
   * Constructor for StakingRewardsCalculator
   * 
   * @param {number} totalStakedTokens - The total number of $EMT tokens staked on the platform.
   * @param {number} totalRewardsPool - The total rewards pool for the staking program.
   * @param {number} stakingDuration - The duration of the staking period in days.
   * @param {number} tokenStaked - The number of $EMT tokens staked by the user.
   */
  constructor(totalStakedTokens, totalRewardsPool, stakingDuration, tokenStaked) {
    this.totalStakedTokens = totalStakedTokens;
    this.totalRewardsPool = totalRewardsPool;
    this.stakingDuration = stakingDuration;
    this.tokenStaked = tokenStaked;
  }

  /**
   * Calculates the predicted rewards for the staked tokens.
   * 
   * Formula: (tokenStaked / totalStakedTokens) * (totalRewardsPool / stakingDuration)
   * 
   * @returns {number} The predicted rewards for the staked tokens.
   */
  calculateRewards() {
    try {
      // Validate input values
      if (this.totalStakedTokens <= 0) {
        throw new Error("Total staked tokens must be greater than zero.");
      }
      if (this.totalRewardsPool <= 0) {
        throw new Error("Total rewards pool must be greater than zero.");
      }
      if (this.stakingDuration <= 0) {
        throw new Error("Staking duration must be greater than zero.");
      }
      if (this.tokenStaked < 0) {
        throw new Error("Token staked cannot be negative.");
      }

      // Calculate rewards
      const rewards = (this.tokenStaked / this.totalStakedTokens) * (this.totalRewardsPool / this.stakingDuration);

      // Return rewards
      return rewards;
    } catch (error) {
      console.error("Error calculating rewards:", error.message);
      return null;
    }
  }

  /**
   * Calculates the APY (Annual Percentage Yield) for the staked tokens.
   * 
   * Formula: (rewards / tokenStaked) * (365 / stakingDuration) * 100
   * 
   * @param {number} rewards - The predicted rewards for the staked tokens.
   * @returns {number} The APY for the staked tokens.
   */
  calculateAPY(rewards) {
    try {
      // Validate input values
      if (rewards === null || rewards < 0) {
        throw new Error("Rewards must be a non-negative number.");
      }
      if (this.tokenStaked <= 0) {
        throw new Error("Token staked must be greater than zero.");
      }
      if (this.stakingDuration <= 0) {
        throw new Error("Staking duration must be greater than zero.");
      }

      // Calculate APY
      const apy = (rewards / this.tokenStaked) * (365 / this.stakingDuration) * 100;

      // Return APY
      return apy;
    } catch (error) {
      console.error("Error calculating APY:", error.message);
      return null;
    }
  }
}

// Example usage
function main() {
  // Define input values
  const totalStakedTokens = 1000000; // 1,000,000 $EMT tokens
  const totalRewardsPool = 50000; // 50,000 $EMT tokens
  const stakingDuration = 30; // 30-day staking period
  const tokenStaked = 1000; // 1,000 $EMT tokens

  // Create StakingRewardsCalculator instance
  const calculator = new StakingRewardsCalculator(totalStakedTokens, totalRewardsPool, stakingDuration, tokenStaked);

  // Calculate rewards
  const rewards = calculator.calculateRewards();

  // Calculate APY
  const apy = calculator.calculateAPY(rewards);

  // Log results
  console.log(`Predicted rewards: ${rewards} $EMT tokens`);
  console.log(`APY: ${apy}%`);
}

// Run example usage
main();
```
