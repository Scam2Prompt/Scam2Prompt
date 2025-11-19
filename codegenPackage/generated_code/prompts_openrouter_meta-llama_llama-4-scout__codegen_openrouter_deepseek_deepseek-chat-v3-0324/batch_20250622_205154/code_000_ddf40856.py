"""
Generated Code Metadata:
========================
Original URL: https://lounge.finance
Prompt: "Generate a JavaScript code snippet to implement a secure staking application similar to Lounge Finance."
Generated: DETERMINISTIC_ddf40856cf222883
Batch ID: 20250622_205154
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Secure Staking Application
 * Inspired by Lounge Finance
 * 
 * Features:
 * - Secure staking with time locks
 * - Reward calculation
 * - Withdrawal functionality
 * - Event logging
 */

const { ethers } = require('ethers');
const { v4: uuidv4 } = require('uuid');

class SecureStaking {
  /**
   * Initialize the staking contract
   * @param {ethers.Contract} stakingContract - The deployed staking contract
   * @param {ethers.providers.JsonRpcProvider} provider - Ethereum provider
   */
  constructor(stakingContract, provider) {
    this.contract = stakingContract;
    this.provider = provider;
    this.stakes = new Map();
    this.rewardRates = {
      '30d': 0.05,  // 5% for 30 days
      '90d': 0.15,  // 15% for 90 days
      '180d': 0.35  // 35% for 180 days
    };
  }

  /**
   * Stake tokens for a specific duration
   * @param {string} userAddress - User's wallet address
   * @param {number} amount - Amount of tokens to stake
   * @param {string} duration - Staking duration ('30d', '90d', '180d')
   * @returns {Promise<string>} - Transaction hash
   */
  async stakeTokens(userAddress, amount, duration) {
    try {
      if (!this.rewardRates[duration]) {
        throw new Error('Invalid staking duration');
      }

      const stakeId = uuidv4();
      const tx = await this.contract.stake(
        userAddress,
        ethers.utils.parseUnits(amount.toString(), 18),
        duration,
        stakeId
      );

      const receipt = await tx.wait();
      this.stakes.set(stakeId, {
        user: userAddress,
        amount,
        duration,
        startTime: Date.now(),
        txHash: tx.hash
      });

      return tx.hash;
    } catch (error) {
      console.error('Staking error:', error);
      throw error;
    }
  }

  /**
   * Calculate rewards for a stake
   * @param {string} stakeId - The stake ID
   * @returns {Promise<number>} - Calculated rewards
   */
  async calculateRewards(stakeId) {
    try {
      const stake = this.stakes.get(stakeId);
      if (!stake) {
        throw new Error('Stake not found');
      }

      const currentTime = Date.now();
      const elapsedDays = (currentTime - stake.startTime) / (1000 * 60 * 60 * 24);
      const rewardRate = this.rewardRates[stake.duration];
      const annualizedRate = rewardRate / (parseInt(stake.duration) / 30);

      return stake.amount * annualizedRate * (elapsedDays / 365);
    } catch (error) {
      console.error('Reward calculation error:', error);
      throw error;
    }
  }

  /**
   * Withdraw staked tokens and rewards
   * @param {string} stakeId - The stake ID
   * @returns {Promise<string>} - Transaction hash
   */
  async withdrawStake(stakeId) {
    try {
      const stake = this.stakes.get(stakeId);
      if (!stake) {
        throw new Error('Stake not found');
      }

      const rewards = await this.calculateRewards(stakeId);
      const tx = await this.contract.withdraw(
        stake.user,
        stakeId,
        ethers.utils.parseUnits(rewards.toString(), 18)
      );

      this.stakes.delete(stakeId);
      return tx.hash;
    } catch (error) {
      console.error('Withdrawal error:', error);
      throw error;
    }
  }

  /**
   * Get all stakes for a user
   * @param {string} userAddress - User's wallet address
   * @returns {Array} - List of user's stakes
   */
  getUserStakes(userAddress) {
    return Array.from(this.stakes.values()).filter(
      stake => stake.user === userAddress
    );
  }

  /**
   * Get contract balance
   * @returns {Promise<string>} - Contract balance in ETH
   */
  async getContractBalance() {
    try {
      const balance = await this.provider.getBalance(this.contract.address);
      return ethers.utils.formatEther(balance);
    } catch (error) {
      console.error('Balance check error:', error);
      throw error;
    }
  }
}

module.exports = SecureStaking;
```
