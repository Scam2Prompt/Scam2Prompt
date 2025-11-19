"""
Generated Code Metadata:
========================
Original URL: https://dapp-p.pages.dev
Prompt: "Design a staking and harvesting system for assets in a DApp, allowing users to stake and unstake assets easily."
Generated: DETERMINISTIC_f4ffe10cbef162ff
Batch ID: 20250622_204615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// StakingHarvestingSystem.js

/**
 * Staking and Harvesting System for Assets in a DApp
 */

class StakingHarvestingSystem {
  /**
   * Constructor for StakingHarvestingSystem
   * @param {Object} assetRegistry - Registry of available assets
   * @param {Object} stakingRewards - Rewards for staking assets
   */
  constructor(assetRegistry, stakingRewards) {
    this.assetRegistry = assetRegistry;
    this.stakingRewards = stakingRewards;
    this.userStakes = {}; // Store user stakes
  }

  /**
   * Stake assets
   * @param {string} user - User address
   * @param {string} asset - Asset to stake
   * @param {number} amount - Amount to stake
   * @returns {boolean} - Success or failure
   */
  stake(user, asset, amount) {
    try {
      // Check if asset exists in registry
      if (!this.assetRegistry[asset]) {
        throw new Error(`Asset ${asset} does not exist`);
      }

      // Check if user has sufficient balance
      if (this.assetRegistry[asset].balance[user] < amount) {
        throw new Error(`Insufficient balance for ${user}`);
      }

      // Update user's stake
      if (!this.userStakes[user]) {
        this.userStakes[user] = {};
      }
      if (!this.userStakes[user][asset]) {
        this.userStakes[user][asset] = 0;
      }
      this.userStakes[user][asset] += amount;

      // Update asset balance
      this.assetRegistry[asset].balance[user] -= amount;
      this.assetRegistry[asset].staked[asset] = (this.assetRegistry[asset].staked[asset] || 0) + amount;

      return true;
    } catch (error) {
      console.error(error);
      return false;
    }
  }

  /**
   * Unstake assets
   * @param {string} user - User address
   * @param {string} asset - Asset to unstake
   * @param {number} amount - Amount to unstake
   * @returns {boolean} - Success or failure
   */
  unstake(user, asset, amount) {
    try {
      // Check if asset exists in registry
      if (!this.assetRegistry[asset]) {
        throw new Error(`Asset ${asset} does not exist`);
      }

      // Check if user has stake
      if (!this.userStakes[user] || !this.userStakes[user][asset] || this.userStakes[user][asset] < amount) {
        throw new Error(`User ${user} does not have sufficient stake`);
      }

      // Update user's stake
      this.userStakes[user][asset] -= amount;

      // Update asset balance
      this.assetRegistry[asset].balance[user] = (this.assetRegistry[asset].balance[user] || 0) + amount;
      this.assetRegistry[asset].staked[asset] -= amount;

      return true;
    } catch (error) {
      console.error(error);
      return false;
    }
  }

  /**
   * Harvest rewards for staked assets
   * @param {string} user - User address
   * @param {string} asset - Asset to harvest
   * @returns {number} - Harvested rewards
   */
  harvest(user, asset) {
    try {
      // Check if asset exists in registry
      if (!this.assetRegistry[asset]) {
        throw new Error(`Asset ${asset} does not exist`);
      }

      // Check if user has stake
      if (!this.userStakes[user] || !this.userStakes[user][asset]) {
        throw new Error(`User ${user} does not have stake`);
      }

      // Calculate rewards
      const stakeAmount = this.userStakes[user][asset];
      const rewards = this.stakingRewards[asset] * stakeAmount;

      // Update user's balance
      this.assetRegistry[asset].balance[user] = (this.assetRegistry[asset].balance[user] || 0) + rewards;

      return rewards;
    } catch (error) {
      console.error(error);
      return 0;
    }
  }
}

// Example usage
const assetRegistry = {
  'Asset1': {
    balance: {
      'User1': 100,
      'User2': 50
    },
    staked: {}
  },
  'Asset2': {
    balance: {
      'User1': 50,
      'User2': 100
    },
    staked: {}
  }
};

const stakingRewards = {
  'Asset1': 0.1,
  'Asset2': 0.05
};

const stakingSystem = new StakingHarvestingSystem(assetRegistry, stakingRewards);

console.log(stakingSystem.stake('User1', 'Asset1', 20)); // Stake 20 Asset1
console.log(stakingSystem.stake('User2', 'Asset2', 30)); // Stake 30 Asset2

console.log(stakingSystem.harvest('User1', 'Asset1')); // Harvest rewards for User1's Asset1 stake

console.log(stakingSystem.unstake('User1', 'Asset1', 10)); // Unstake 10 Asset1

console.log(assetRegistry);
```
