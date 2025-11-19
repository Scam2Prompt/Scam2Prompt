"""
Generated Code Metadata:
========================
Original URL: https://app-basemafia-com.pages.dev
Prompt: "Develop a simple staking rewards calculator in JavaScript that takes into account the $MAFIA token's staking solutions and reward mechanisms as described in the Base Mafia project."
Generated: DETERMINISTIC_c79b32f4099f28d4
Batch ID: 20250622_204946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * MafiaToken Staking Rewards Calculator
 * 
 * This calculator computes staking rewards for $MAFIA token based on the Base Mafia project's staking parameters.
 * It supports different staking durations and calculates both simple and compound rewards.
 */

class MafiaStakingCalculator {
  /**
   * @param {Object} config - Configuration object for staking parameters
   * @param {number} config.baseAPY - Base annual percentage yield (e.g., 0.15 for 15%)
   * @param {Object} config.durationMultipliers - Multipliers for different staking durations (in days)
   * @param {number} config.compoundFrequency - How often rewards are compounded (in days)
   * @param {number} config.maxStakingDuration - Maximum staking duration in days
   */
  constructor(config) {
    this.validateConfig(config);
    
    this.baseAPY = config.baseAPY;
    this.durationMultipliers = config.durationMultipliers;
    this.compoundFrequency = config.compoundFrequency;
    this.maxStakingDuration = config.maxStakingDuration;
  }

  /**
   * Validates the configuration object
   * @param {Object} config - Configuration to validate
   * @throws {Error} If configuration is invalid
   */
  validateConfig(config) {
    if (!config || typeof config !== 'object') {
      throw new Error('Invalid configuration: must be an object');
    }

    const requiredProps = ['baseAPY', 'durationMultipliers', 'compoundFrequency', 'maxStakingDuration'];
    for (const prop of requiredProps) {
      if (!(prop in config)) {
        throw new Error(`Missing required configuration property: ${prop}`);
      }
    }

    if (typeof config.baseAPY !== 'number' || config.baseAPY <= 0) {
      throw new Error('baseAPY must be a positive number');
    }

    if (typeof config.compoundFrequency !== 'number' || config.compoundFrequency <= 0) {
      throw new Error('compoundFrequency must be a positive number');
    }

    if (typeof config.maxStakingDuration !== 'number' || config.maxStakingDuration <= 0) {
      throw new Error('maxStakingDuration must be a positive number');
    }

    if (!config.durationMultipliers || typeof config.durationMultipliers !== 'object') {
      throw new Error('durationMultipliers must be an object');
    }
  }

  /**
   * Gets the multiplier for a specific staking duration
   * @param {number} duration - Staking duration in days
   * @returns {number} The duration multiplier
   */
  getDurationMultiplier(duration) {
    if (duration <= 0) {
      throw new Error('Duration must be greater than 0');
    }

    // Find the largest duration bracket that's <= the requested duration
    const sortedDurations = Object.keys(this.durationMultipliers)
      .map(Number)
      .sort((a, b) => a - b);

    let selectedMultiplier = 1; // Default multiplier
    for (const d of sortedDurations) {
      if (duration >= d) {
        selectedMultiplier = this.durationMultipliers[d];
      } else {
        break;
      }
    }

    return selectedMultiplier;
  }

  /**
   * Calculates simple staking rewards (no compounding)
   * @param {number} amount - Amount of tokens to stake
   * @param {number} duration - Staking duration in days
   * @returns {number} Total rewards earned
   */
  calculateSimpleRewards(amount, duration) {
    this.validateInputs(amount, duration);

    const effectiveAPY = this.baseAPY * this.getDurationMultiplier(duration);
    const dailyRate = effectiveAPY / 365;
    return amount * dailyRate * duration;
  }

  /**
   * Calculates compound staking rewards
   * @param {number} amount - Amount of tokens to stake
   * @param {number} duration - Staking duration in days
   * @returns {number} Total rewards earned
   */
  calculateCompoundRewards(amount, duration) {
    this.validateInputs(amount, duration);

    const effectiveAPY = this.baseAPY * this.getDurationMultiplier(duration);
    const periods = Math.floor(duration / this.compoundFrequency);
    const periodicRate = effectiveAPY * (this.compoundFrequency / 365);

    if (periods <= 0) {
      return this.calculateSimpleRewards(amount, duration);
    }

    const compoundAmount = amount * Math.pow(1 + periodicRate, periods);
    const remainingDays = duration % this.compoundFrequency;
    const remainingRewards = remainingDays > 0 
      ? this.calculateSimpleRewards(compoundAmount, remainingDays)
      : 0;

    return compoundAmount - amount + remainingRewards;
  }

  /**
   * Validates input parameters
   * @param {number} amount - Amount to stake
   * @param {number} duration - Staking duration
   * @throws {Error} If inputs are invalid
   */
  validateInputs(amount, duration) {
    if (typeof amount !== 'number' || amount <= 0) {
      throw new Error('Amount must be a positive number');
    }

    if (typeof duration !== 'number' || duration <= 0) {
      throw new Error('Duration must be a positive number');
    }

    if (duration > this.maxStakingDuration) {
      throw new Error(`Duration cannot exceed maximum staking duration of ${this.maxStakingDuration} days`);
    }
  }
}

// Example configuration for Base Mafia staking
const mafiaStakingConfig = {
  baseAPY: 0.15, // 15% base APY
  durationMultipliers: {
    30: 1.0,    // 1x for 30 days
    90: 1.2,    // 1.2x for 90 days
    180: 1.5,   // 1.5x for 180 days
    365: 2.0    // 2x for 365 days
  },
  compoundFrequency: 7, // Compounding every 7 days
  maxStakingDuration: 730 // Maximum staking duration of 2 years (730 days)
};

// Example usage:
try {
  const calculator = new MafiaStakingCalculator(mafiaStakingConfig);
  
  const stakedAmount = 10000; // 10,000 MAFIA tokens
  const stakingDuration = 90; // 90 days
  
  const simpleRewards = calculator.calculateSimpleRewards(stakedAmount, stakingDuration);
  const compoundRewards = calculator.calculateCompoundRewards(stakedAmount, stakingDuration);
  
  console.log(`Simple rewards after ${stakingDuration} days: ${simpleRewards.toFixed(2)} MAFIA`);
  console.log(`Compound rewards after ${stakingDuration} days: ${compoundRewards.toFixed(2)} MAFIA`);
} catch (error) {
  console.error('Error calculating staking rewards:', error.message);
}
```
