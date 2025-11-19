"""
Generated Code Metadata:
========================
Original URL: https://milady-dfk.pages.dev
Prompt: Create a script in JavaScript to calculate the "Beetle Points" for users in a decentralized application, based on activity metrics and token holdings, as described in the Milady ecosystem.
Generated: DETERMINISTIC_38c028337c38f2fb
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates Beetle Points for users based on activity metrics and token holdings.
 * Implements the Beetle Points system as described in the Milady ecosystem.
 */

class BeetlePointsCalculator {
  /**
   * Initialize the calculator with configuration parameters.
   * @param {Object} config - Configuration object containing weights and parameters
   * @param {number} config.activityWeight - Weight for activity metrics (0-1)
   * @param {number} config.holdingWeight - Weight for token holdings (0-1)
   * @param {number} config.baseMultiplier - Base multiplier for points calculation
   * @param {number} config.decayFactor - Factor for decaying older activities (0-1)
   */
  constructor(config) {
    this.validateConfig(config);
    
    this.activityWeight = config.activityWeight;
    this.holdingWeight = config.holdingWeight;
    this.baseMultiplier = config.baseMultiplier;
    this.decayFactor = config.decayFactor;
  }

  /**
   * Validates the configuration object
   * @param {Object} config - Configuration to validate
   * @throws {Error} If configuration is invalid
   */
  validateConfig(config) {
    if (!config) {
      throw new Error('Configuration object is required');
    }

    const requiredParams = ['activityWeight', 'holdingWeight', 'baseMultiplier', 'decayFactor'];
    for (const param of requiredParams) {
      if (config[param] === undefined || config[param] === null) {
        throw new Error(`Missing required parameter: ${param}`);
      }
    }

    if (config.activityWeight < 0 || config.activityWeight > 1) {
      throw new Error('activityWeight must be between 0 and 1');
    }

    if (config.holdingWeight < 0 || config.holdingWeight > 1) {
      throw new Error('holdingWeight must be between 0 and 1');
    }

    if (config.activityWeight + config.holdingWeight !== 1) {
      throw new Error('activityWeight and holdingWeight must sum to 1');
    }

    if (config.baseMultiplier <= 0) {
      throw new Error('baseMultiplier must be greater than 0');
    }

    if (config.decayFactor < 0 || config.decayFactor > 1) {
      throw new Error('decayFactor must be between 0 and 1');
    }
  }

  /**
   * Calculates the activity score with time decay
   * @param {Array} activities - Array of activity objects with timestamp and value
   * @returns {number} Decay-adjusted activity score
   */
  calculateActivityScore(activities) {
    if (!Array.isArray(activities)) {
      throw new Error('Activities must be provided as an array');
    }

    const now = Date.now();
    let totalScore = 0;

    for (const activity of activities) {
      if (!activity.timestamp || !activity.value) {
        throw new Error('Activity objects must have timestamp and value properties');
      }

      const ageInDays = (now - activity.timestamp) / (1000 * 60 * 60 * 24);
      const decay = Math.pow(this.decayFactor, ageInDays);
      totalScore += activity.value * decay;
    }

    return totalScore;
  }

  /**
   * Calculates the holdings score based on token balance and staking
   * @param {number} tokenBalance - Current token balance
   * @param {number} stakedBalance - Amount of tokens staked
   * @param {number} stakingMultiplier - Multiplier for staked tokens
   * @returns {number} Holdings score
   */
  calculateHoldingsScore(tokenBalance, stakedBalance, stakingMultiplier) {
    if (tokenBalance < 0 || stakedBalance < 0) {
      throw new Error('Token balances cannot be negative');
    }

    if (stakingMultiplier < 1) {
      throw new Error('Staking multiplier must be at least 1');
    }

    return tokenBalance + (stakedBalance * stakingMultiplier);
  }

  /**
   * Normalizes a score to a 0-1 range based on the maximum possible value
   * @param {number} score - Raw score to normalize
   * @param {number} maxPossible - Maximum possible value for this score type
   * @returns {number} Normalized score (0-1)
   */
  normalizeScore(score, maxPossible) {
    if (maxPossible <= 0) {
      throw new Error('maxPossible must be greater than 0');
    }

    return Math.min(score / maxPossible, 1);
  }

  /**
   * Calculates Beetle Points for a user
   * @param {Object} userData - User data object
   * @param {Array} userData.activities - Array of user activities
   * @param {number} userData.tokenBalance - Current token balance
   * @param {number} userData.stakedBalance - Amount of tokens staked
   * @param {number} userData.stakingMultiplier - Multiplier for staked tokens
   * @param {number} maxActivityScore - Maximum possible activity score in system
   * @param {number} maxHoldingsScore - Maximum possible holdings score in system
   * @returns {number} Calculated Beetle Points
   */
  calculateBeetlePoints(userData, maxActivityScore, maxHoldingsScore) {
    if (!userData) {
      throw new Error('User data is required');
    }

    // Calculate raw scores
    const activityScore = this.calculateActivityScore(userData.activities);
    const holdingsScore = this.calculateHoldingsScore(
      userData.tokenBalance,
      userData.stakedBalance,
      userData.stakingMultiplier
    );

    // Normalize scores
    const normalizedActivity = this.normalizeScore(activityScore, maxActivityScore);
    const normalizedHoldings = this.normalizeScore(holdingsScore, maxHoldingsScore);

    // Calculate weighted score
    const weightedScore = 
      (normalizedActivity * this.activityWeight) + 
      (normalizedHoldings * this.holdingWeight);

    // Apply base multiplier
    return weightedScore * this.baseMultiplier;
  }
}

// Example usage:
/*
const config = {
  activityWeight: 0.6,
  holdingWeight: 0.4,
  baseMultiplier: 1000,
  decayFactor: 0.95
};

const calculator = new BeetlePointsCalculator(config);

const userData = {
  activities: [
    { timestamp: Date.now() - 86400000, value: 50 }, // 1 day ago
    { timestamp: Date.now() - 172800000, value: 30 } // 2 days ago
  ],
  tokenBalance: 500,
  stakedBalance: 200,
  stakingMultiplier: 1.5
};

const maxActivityScore = 100;
const maxHoldingsScore = 1000;

const beetlePoints = calculator.calculateBeetlePoints(userData, maxActivityScore, maxHoldingsScore);
console.log(`User Beetle Points: ${beetlePoints}`);
*/
```
