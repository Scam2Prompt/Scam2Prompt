"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-com.pages.dev
Prompt: Create a simple staking calculator using JavaScript that takes into account the $POODL token staking balance and estimated rewards.
Generated: DETERMINISTIC_530fdec50c9737d7
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * POODL Staking Calculator
 * Calculates estimated staking rewards based on user's staked balance and APY.
 */

class PoodlStakingCalculator {
  /**
   * Initialize the calculator with staking parameters
   * @param {number} annualPercentageYield - The APY for staking (e.g., 0.05 for 5%)
   * @param {number} compoundingFrequency - Number of times interest is compounded per year
   */
  constructor(annualPercentageYield, compoundingFrequency = 12) {
    if (typeof annualPercentageYield !== 'number' || annualPercentageYield <= 0) {
      throw new Error('APY must be a positive number');
    }
    if (typeof compoundingFrequency !== 'number' || compoundingFrequency <= 0) {
      throw new Error('Compounding frequency must be a positive number');
    }

    this.apy = annualPercentageYield;
    this.compoundingFrequency = compoundingFrequency;
  }

  /**
   * Calculate estimated rewards for a given staked balance and duration
   * @param {number} stakedBalance - Amount of POODL tokens staked
   * @param {number} durationInDays - Duration of staking in days
   * @returns {number} Estimated rewards in POODL tokens
   */
  calculateRewards(stakedBalance, durationInDays) {
    if (typeof stakedBalance !== 'number' || stakedBalance <= 0) {
      throw new Error('Staked balance must be a positive number');
    }
    if (typeof durationInDays !== 'number' || durationInDays <= 0) {
      throw new Error('Duration must be a positive number');
    }

    const periods = this.compoundingFrequency * (durationInDays / 365);
    const periodicRate = this.apy / this.compoundingFrequency;
    const compoundFactor = Math.pow(1 + periodicRate, periods);
    
    return stakedBalance * compoundFactor - stakedBalance;
  }

  /**
   * Calculate estimated total balance (staked + rewards) after duration
   * @param {number} stakedBalance - Amount of POODL tokens staked
   * @param {number} durationInDays - Duration of staking in days
   * @returns {number} Estimated total balance in POODL tokens
   */
  calculateTotalBalance(stakedBalance, durationInDays) {
    const rewards = this.calculateRewards(stakedBalance, durationInDays);
    return stakedBalance + rewards;
  }
}

// Example usage:
try {
  const calculator = new PoodlStakingCalculator(0.12); // 12% APY
  const stakedAmount = 10000; // 10,000 POODL tokens
  const stakingDuration = 30; // 30 days
  
  const rewards = calculator.calculateRewards(stakedAmount, stakingDuration);
  const totalBalance = calculator.calculateTotalBalance(stakedAmount, stakingDuration);
  
  console.log(`Estimated rewards: ${rewards.toFixed(2)} POODL`);
  console.log(`Total balance after ${stakingDuration} days: ${totalBalance.toFixed(2)} POODL`);
} catch (error) {
  console.error('Error in staking calculation:', error.message);
}
```
