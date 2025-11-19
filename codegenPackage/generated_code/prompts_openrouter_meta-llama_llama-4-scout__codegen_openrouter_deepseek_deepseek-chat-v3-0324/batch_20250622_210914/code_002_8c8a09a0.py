"""
Generated Code Metadata:
========================
Original URL: https://kon-8si.pages.dev
Prompt: Generate JavaScript code for a simple calculator that estimates potential rewards from the $KPN airdrop based on user eligibility and the number of tokens available.
Generated: DETERMINISTIC_8c8a09a01ea6d2a3
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * KPN Airdrop Calculator
 * Estimates potential rewards based on user eligibility and token availability.
 */

class KPNAirdropCalculator {
  /**
   * Initialize the calculator with total available tokens and eligibility criteria.
   * @param {number} totalTokens - Total KPN tokens available for airdrop
   * @param {Object} eligibilityCriteria - Criteria for user eligibility
   */
  constructor(totalTokens, eligibilityCriteria) {
    if (typeof totalTokens !== 'number' || totalTokens <= 0) {
      throw new Error('Total tokens must be a positive number');
    }

    if (!eligibilityCriteria || typeof eligibilityCriteria !== 'object') {
      throw new Error('Eligibility criteria must be an object');
    }

    this.totalTokens = totalTokens;
    this.eligibilityCriteria = eligibilityCriteria;
    this.totalEligibleUsers = 0;
    this.registeredUsers = [];
  }

  /**
   * Register a user for the airdrop calculation.
   * @param {Object} user - User object containing eligibility information
   * @param {string} user.address - User's wallet address
   * @param {boolean} user.isEligible - Whether the user meets eligibility criteria
   * @param {number} [user.weight=1] - Weight factor for distribution (default: 1)
   */
  registerUser(user) {
    if (!user || typeof user !== 'object') {
      throw new Error('User must be an object');
    }

    if (!user.address || typeof user.address !== 'string') {
      throw new Error('User must have a valid address string');
    }

    if (typeof user.isEligible !== 'boolean') {
      throw new Error('User eligibility must be a boolean');
    }

    const weight = typeof user.weight === 'number' && user.weight > 0 
      ? user.weight 
      : 1;

    this.registeredUsers.push({
      address: user.address,
      isEligible: user.isEligible,
      weight: weight
    });

    if (user.isEligible) {
      this.totalEligibleUsers += weight;
    }
  }

  /**
   * Calculate estimated reward for a specific user.
   * @param {string} address - User's wallet address
   * @returns {number} Estimated reward in KPN tokens
   */
  calculateReward(address) {
    if (!address || typeof address !== 'string') {
      throw new Error('Address must be a valid string');
    }

    const user = this.registeredUsers.find(u => u.address === address);
    if (!user) {
      throw new Error('User not registered');
    }

    if (!user.isEligible || this.totalEligibleUsers === 0) {
      return 0;
    }

    const userShare = user.weight / this.totalEligibleUsers;
    return this.totalTokens * userShare;
  }

  /**
   * Calculate estimated rewards for all registered users.
   * @returns {Object} Mapping of addresses to estimated rewards
   */
  calculateAllRewards() {
    if (this.totalEligibleUsers === 0) {
      return {};
    }

    const rewards = {};
    for (const user of this.registeredUsers) {
      if (user.isEligible) {
        const userShare = user.weight / this.totalEligibleUsers;
        rewards[user.address] = this.totalTokens * userShare;
      } else {
        rewards[user.address] = 0;
      }
    }

    return rewards;
  }

  /**
   * Get the total number of eligible users (weighted sum).
   * @returns {number} Total eligible users count
   */
  getEligibleUserCount() {
    return this.totalEligibleUsers;
  }
}

// Example usage:
/*
const calculator = new KPNAirdropCalculator(1000000, {
  minBalance: 100,
  activeSince: '2023-01-01'
});

calculator.registerUser({
  address: '0x123...',
  isEligible: true,
  weight: 1.5
});

calculator.registerUser({
  address: '0x456...',
  isEligible: true
});

calculator.registerUser({
  address: '0x789...',
  isEligible: false
});

const reward = calculator.calculateReward('0x123...');
const allRewards = calculator.calculateAllRewards();
console.log(reward, allRewards);
*/
```
